#!/usr/bin/env python3
"""Build Volume 1 chapters from source-verified page starts, not OCR numbers."""

from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from pathlib import Path

ZERO_WIDTH = re.compile(r"[\u200b\u200c\u200d\ufeff]")
BARE_PAGE = re.compile(r"^\s*[0-9௦-௯|Il\[\]]{1,5}\s*$")
HEADER = re.compile(r"^\s*(?:\d+\s*)?(?:தலைவர்\s+கலைஞர்|கலைஞரின்\s+கடிதங்கள்)(?:\s*\d+)?\s*$")
DATE = re.compile(r"\b(\d{1,2})\s*[./-]\s*(\d{1,2})\s*[./-]\s*(\d{2,4})\b")


def clean(value: str) -> str:
    return unicodedata.normalize("NFC", ZERO_WIDTH.sub("", value)).strip()


def page_paragraphs(data: dict) -> list[str]:
    result = []
    for paragraph in data.get("paragraphs", []):
        lines = []
        for raw in paragraph.splitlines():
            line = clean(raw)
            if not line or BARE_PAGE.fullmatch(line) or HEADER.fullmatch(line):
                continue
            lines.append(line)
        if lines:
            result.append("\n".join(lines))
    return result


def terminal_date(paragraphs: list[str]) -> str | None:
    tail = "\n".join(paragraphs[-8:])
    matches = list(DATE.finditer(tail))
    if not matches:
        return None
    day, month, year = map(int, matches[-1].groups())
    if year < 100:
        year += 1900
    if 1 <= day <= 31 and 1 <= month <= 12 and 1960 <= year <= 2020:
        return f"{year:04d}-{month:02d}-{day:02d}"
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", type=int, default=1)
    parser.add_argument("--pages-dir", type=Path, required=True)
    parser.add_argument("--starts", type=Path, default=Path(__file__).with_name("volume1_source_starts.csv"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--last-page", type=int, default=401)
    args = parser.parse_args()

    starts = []
    with args.starts.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            starts.append((int(row["number"]), int(row["source_page"])))
    if [number for number, _ in starts] != list(range(1, 111)):
        raise SystemExit("Start manifest must contain letters 1 through 110 exactly once")
    if any(a[1] >= b[1] for a, b in zip(starts, starts[1:])):
        raise SystemExit("Source starts must be strictly increasing")

    pages = {}
    for path in args.pages_dir.glob(f"m{args.volume}-p*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        pages[int(data["page"])] = data
    expected = set(range(starts[0][1], args.last_page + 1))
    missing = sorted(expected - set(pages))
    if missing:
        raise SystemExit(f"Missing source OCR page JSON: {missing}")

    args.output.mkdir(parents=True, exist_ok=True)
    index = []
    ownership = {}
    for position, (number, first) in enumerate(starts):
        last = starts[position + 1][1] - 1 if position + 1 < len(starts) else args.last_page
        page_ids = [f"m{args.volume}-p{page:04d}" for page in range(first, last + 1)]
        paragraphs = []
        for page in range(first, last + 1):
            ownership.setdefault(page, []).append(number)
            paragraphs.extend(page_paragraphs(pages[page]))

        # Remove the printed number/title and salutation from the body only
        # when they are separate leading OCR paragraphs. Raw page JSON remains
        # untouched and is always the provenance layer.
        title_ocr = paragraphs[0] if paragraphs else f"{number}."
        body = list(paragraphs)
        if body and re.match(rf"^\s*{number}\s*[.,]", body[0]):
            body.pop(0)
        salutation = None
        if body and len(body[0]) <= 80 and re.search(r"(?:நண்பா|உடன்பிறப்பே|தம்பி|தோழா)", body[0]):
            salutation = body.pop(0)

        chapter_id = f"m{args.volume}-l{number:04d}"
        folder = args.output / chapter_id
        folder.mkdir(parents=True, exist_ok=True)
        chapter = {
            "id": chapter_id,
            "collection": "murasoli-letter",
            "volume": args.volume,
            "number": number,
            "date": terminal_date(paragraphs),
            "title": {"ta": re.sub(rf"^\s*{number}\s*[.,]\s*", "", title_ocr), "en": f"Letter {number}"},
            "salutation": salutation,
            "pages": page_ids,
            "paragraphs": body,
            "ocrStatus": "raw_ocr_source_spine",
            "boundaryEvidence": "source_verified_contents_and_visual_start_page",
        }
        (folder / "chapter.json").write_text(json.dumps(chapter, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        heading = f"# {number}. {chapter['title']['ta']}"
        md = [heading]
        if salutation:
            md.append(salutation)
        md.extend(body)
        (folder / "chapter.md").write_text("\n\n".join(md).rstrip() + "\n", encoding="utf-8")
        index.append({"id": chapter_id, "number": number, "date": chapter["date"], "title": chapter["title"], "sourcePages": page_ids, "folder": chapter_id})

    duplicates = {str(page): owners for page, owners in ownership.items() if len(owners) != 1}
    unassigned = sorted(expected - set(ownership))
    report = {
        "volume": args.volume,
        "status": "source_spine_candidate_pending_title_verification",
        "chapterCount": len(index),
        "bodyPageRange": [starts[0][1], args.last_page],
        "assignedBodyPages": len(ownership),
        "unassignedBodyPages": unassigned,
        "duplicatePageAssignments": duplicates,
        "chapterOrderOk": [row["number"] for row in index] == list(range(1, 111)),
        "rawOcrModified": False,
    }
    (args.output / "chapters-index.json").write_text(json.dumps({"collection": "murasoli-chapters", "volume": args.volume, "chapterCount": len(index), "chapters": index}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output / "source_spine_audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if len(index) != 110 or unassigned or duplicates or not report["chapterOrderOk"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
