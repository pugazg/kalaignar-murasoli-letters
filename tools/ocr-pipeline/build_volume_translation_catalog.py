#!/usr/bin/env python3
"""Build a translation manifest and bilingual contents from a frozen chapter spine."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


TAMIL_SECTION = re.compile(
    r"^## (?:Source-Corrected Tamil|Original Tamil[^\n]*)\s*$", re.MULTILINE
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reading_title(text: str, number: int) -> str:
    match = TAMIL_SECTION.search(text)
    if not match:
        raise ValueError("Tamil reading section missing")
    tail = text[match.end() :]
    title = re.search(rf"^#{{1,3}}\s+{number}\.\s+(.+)$", tail, re.MULTILINE)
    if not title:
        raise ValueError("Tamil reading title missing")
    return title.group(1).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", type=int, required=True)
    parser.add_argument("--spine", type=Path, required=True)
    parser.add_argument("--translations-root", type=Path, default=Path("translations"))
    parser.add_argument("--verified-titles", type=Path)
    args = parser.parse_args()

    volume_dir = args.translations_root / f"vol{args.volume}"
    verified = {}
    if args.verified_titles:
        with args.verified_titles.open(encoding="utf-8", newline="") as handle:
            verified = {row["chapter_id"]: row for row in csv.DictReader(handle)}
    chapters = []
    for chapter_file in args.spine.glob("m*-l*/chapter.json"):
        chapter = json.loads(chapter_file.read_text(encoding="utf-8"))
        chapters.append((int(chapter["number"]), chapter_file.resolve(), chapter))
    chapters.sort(key=lambda item: item[0])

    manifest_rows = []
    contents_rows = []
    for order, (number, source_file, chapter) in enumerate(chapters, 1):
        chapter_id = chapter["id"]
        translation = (volume_dir / f"{chapter_id}.en.md").resolve()
        text = translation.read_text(encoding="utf-8")
        english_heading = text.splitlines()[0]
        prefix = f"# {number}. "
        if not english_heading.startswith(prefix):
            raise ValueError(f"{chapter_id}: malformed English heading")
        english_title = english_heading[len(prefix) :].strip()
        tamil_title = reading_title(text, number)
        pages = chapter.get("pages", [])
        verified_row = verified.get(chapter_id, {})
        source_date = verified_row.get("contents_date") or chapter.get("date") or ""
        manifest_rows.append(
            {
                "order": order,
                "chapter_id": chapter_id,
                "letter_number": f"{number:04d}",
                "source_file": str(source_file),
                "source_sha256": sha256(source_file),
                "translation_file": str(translation),
                "status": "translated",
                "date": source_date,
                "source_pages": ";".join(pages),
            }
        )
        contents_rows.append(
            (f"{number:04d}", tamil_title, english_title, source_date, pages)
        )

    manifest = volume_dir / "translation_manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=manifest_rows[0].keys())
        writer.writeheader()
        writer.writerows(manifest_rows)

    lines = [
        "# Volume 1 Contents / தொகுதி 1 உள்ளடக்கம்",
        "",
        "This contents list follows the frozen, source-verified 110-letter order. Tamil titles are taken from each source-corrected reading copy; English titles match the bilingual chapter files.",
        "",
        "| No. | Source-Verified Tamil Title | English Translation | Date | Source Pages |",
        "|---:|---|---|---|---|",
    ]
    for number, tamil, english, date, pages in contents_rows:
        page_numbers = ", ".join(str(int(page.rsplit("p", 1)[1])) for page in pages)
        lines.append(f"| {number} | {tamil} | {english} | {date} | {page_numbers} |")
    (volume_dir / "contents.en.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"manifest_records": len(manifest_rows), "contents_entries": len(contents_rows)}))


if __name__ == "__main__":
    main()
