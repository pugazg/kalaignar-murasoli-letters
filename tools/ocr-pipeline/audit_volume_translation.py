#!/usr/bin/env python3
"""Audit a completed bilingual volume translation against its source manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


TAMIL_SECTION = re.compile(
    r"^## (?:Source-Corrected Tamil|Original Tamil[^\n]*)\s*$", re.MULTILINE
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", type=int, required=True)
    parser.add_argument("--translations-root", type=Path, default=Path("translations"))
    parser.add_argument("--expected-count", type=int)
    parser.add_argument("--verified-titles", type=Path)
    args = parser.parse_args()

    volume_dir = args.translations_root / f"vol{args.volume}"
    manifest_path = volume_dir / "translation_manifest.csv"
    rows = list(csv.DictReader(manifest_path.open(encoding="utf-8")))
    errors: list[str] = []
    file_results: list[dict[str, object]] = []
    expected_files: set[Path] = set()
    reading_titles: dict[str, str] = {}
    verified_titles: dict[str, str] = {}
    if args.verified_titles:
        with args.verified_titles.open(encoding="utf-8", newline="") as handle:
            verified_titles = {
                f"{int(item['number']):04d}": item["final_title"]
                for item in csv.DictReader(handle)
            }

    for position, row in enumerate(rows, 1):
        chapter_id = row["chapter_id"]
        source = Path(row["source_file"])
        translation = Path(row["translation_file"])
        expected_files.add(translation.resolve())
        result: dict[str, object] = {"order": position, "chapter_id": chapter_id}

        if int(row["order"]) != position:
            errors.append(f"{chapter_id}: manifest order is not contiguous")
        if row["status"] != "translated":
            errors.append(f"{chapter_id}: status is {row['status']}")
        if not source.exists() or not translation.exists():
            errors.append(f"{chapter_id}: source or translation file is missing")
            continue

        actual_hash = sha256(source)
        if actual_hash != row["source_sha256"]:
            errors.append(f"{chapter_id}: canonical source hash changed")

        text = translation.read_text(encoding="utf-8")
        lines = text.splitlines()
        english_title = lines[0] if lines else ""
        section = TAMIL_SECTION.search(text)
        tamil_part = text[section.end() :] if section else ""
        number = str(int(row["letter_number"]))
        tamil_title_match = re.search(
            rf"^#{{1,3}}\s+{re.escape(number)}\.\s+(.+)$", tamil_part, re.MULTILINE
        )
        reading_title = tamil_title_match.group(1).strip() if tamil_title_match else ""
        reading_titles[row["letter_number"]] = reading_title
        checks = {
            "source_hash_matches": actual_hash == row["source_sha256"],
            "english_section_count": text.count("## English Translation"),
            "tamil_section_count": len(TAMIL_SECTION.findall(text)),
            "translator_note_count": text.count("## Translator's Note"),
            "has_udanpirappe": "Udanpirappē" in text,
            "source_uses_udanpirappe": "உடன்பிறப்ப" in source.read_text(encoding="utf-8"),
            "tamil_reading_title": reading_title,
            "english_title": english_title,
        }
        result.update(checks)
        if checks["english_section_count"] != 1:
            errors.append(f"{chapter_id}: English section count is not one")
        if checks["tamil_section_count"] != 1:
            errors.append(f"{chapter_id}: Tamil section count is not one")
        if checks["translator_note_count"] != 1:
            errors.append(f"{chapter_id}: translator note count is not one")
        if not english_title.startswith(f"# {number}. "):
            errors.append(f"{chapter_id}: English Markdown title missing or malformed")
        if checks["source_uses_udanpirappe"] and not checks["has_udanpirappe"]:
            errors.append(f"{chapter_id}: source uses உடன்பிறப்பே but translation lacks Udanpirappē")
        if not reading_title:
            errors.append(f"{chapter_id}: source-checked Tamil reading title missing")
        if verified_titles and reading_title != verified_titles.get(row["letter_number"]):
            errors.append(f"{chapter_id}: Tamil reading title differs from verified visual title")
        file_results.append(result)

    actual_files = {p.resolve() for p in volume_dir.glob(f"m{args.volume}-l*.en.md")}
    drafts = sorted(str(p) for p in volume_dir.glob("*.draft.md"))
    contents = volume_dir / "contents.en.md"
    contents_text = contents.read_text(encoding="utf-8") if contents.exists() else ""
    contents_numbers = re.findall(r"^\|\s*(\d{4})\s*\|", contents_text, re.MULTILINE)
    contents_rows = re.findall(r"^\|\s*(\d{4})\s*\|\s*(.*?)\s*\|", contents_text, re.MULTILINE)
    contents_titles = dict(contents_rows)
    manifest_numbers = [row["letter_number"] for row in rows]

    if args.expected_count is not None and len(rows) != args.expected_count:
        errors.append(
            f"manifest contains {len(rows)} records, expected {args.expected_count}"
        )
    if actual_files != expected_files:
        errors.append("bilingual file set does not exactly match manifest")
    if drafts:
        errors.append("draft files remain")
    if not contents.exists():
        errors.append("translated contents file is missing")
    if contents_numbers != manifest_numbers:
        errors.append("contents letter order does not exactly match manifest")
    for number in manifest_numbers:
        if contents_titles.get(number) != reading_titles.get(number):
            errors.append(f"m{args.volume}-l{number}: contents title differs from Tamil reading title")

    ledger_path = volume_dir / "translation_progress.json"
    if not ledger_path.exists():
        errors.append("translation progress ledger is missing")
    else:
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        completed_ids = [item["chapter_id"] for item in ledger.get("completed", [])]
        manifest_ids = [row["chapter_id"] for row in rows]
        if completed_ids != manifest_ids:
            errors.append("progress ledger order does not exactly match manifest")
        if ledger.get("next_chapter_id") is not None:
            errors.append("progress ledger still has a next chapter")
        if ledger.get("raw_ocr_modified") is not False:
            errors.append("progress ledger does not affirm raw OCR preservation")
        if ledger.get("source_spine_modified") is not False:
            errors.append("progress ledger does not affirm source-spine preservation")

    report = {
        "volume": args.volume,
        "passed": not errors,
        "manifest_records": len(rows),
        "translated_files": len(actual_files),
        "pending_records": sum(row["status"] != "translated" for row in rows),
        "contents_entries": len(contents_numbers),
        "draft_files": drafts,
        "errors": errors,
        "files": file_results,
    }
    report_path = volume_dir / "translation_audit.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "files"}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
