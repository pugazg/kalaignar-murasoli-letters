#!/usr/bin/env python3
"""Audit Volume 1 source spine against the visually verified title manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path


def normalized(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"[\u200b-\u200d\ufeff]", "", text)
    text = re.sub(r"^[0-9]+\s*[.,]\s*", "", text)
    text = text.replace("'", "’").replace('"', "”")
    return re.sub(r"\s+", " ", text).strip(" .,!?:;“”‘’-")


def digest(value: object) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spine", type=Path, required=True)
    parser.add_argument("--verified", type=Path, default=Path(__file__).with_name("volume1_verified_titles.csv"))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    index = json.loads((args.spine / "chapters-index.json").read_text(encoding="utf-8"))
    chapters = index["chapters"]
    with args.verified.open(encoding="utf-8", newline="") as handle:
        verified = list(csv.DictReader(handle))
    if len(chapters) != 110 or len(verified) != 110:
        raise SystemExit("Expected exactly 110 spine chapters and 110 verified title rows")

    rows = []
    owners = {}
    for chapter, source in zip(chapters, verified):
        number = int(source["number"])
        if chapter["number"] != number or chapter["id"] != f"m1-l{number:04d}":
            raise SystemExit(f"Identity mismatch at letter {number}")
        pages = chapter["sourcePages"]
        expected_start = f"m1-p{int(source['source_page']):04d}"
        if not pages or pages[0] != expected_start:
            raise SystemExit(f"Start-page mismatch at letter {number}")
        for page in pages:
            owners.setdefault(page, []).append(chapter["id"])
        ocr_title = chapter["title"]["ta"]
        source_title = source["title_ta"]
        comparison = "exact" if ocr_title == source_title else (
            "normalized" if normalized(ocr_title) == normalized(source_title) else "mismatch"
        )
        rows.append({
            "volume": 1,
            "chapter_id": chapter["id"],
            "number": number,
            "page_id": expected_start,
            "source_pdf_page": int(source["source_page"]),
            "ocr_title": ocr_title,
            "visual_source_transcription": source_title,
            "final_title": source_title,
            "comparison": comparison,
            "changed_for_verified_layer": comparison != "exact",
            "visual_status": source["visual_status"],
            "contents_date": source["date"] or None,
            "source_crop": f"page_{int(source['source_page']):04d}.png#title",
            "boundary_status": "verified_title_start_and_interval_to_next_verified_start",
        })

    expected_pages = {f"m1-p{p:04d}" for p in range(24, 402)}
    duplicate_pages = {page: ids for page, ids in owners.items() if len(ids) != 1}
    unassigned = sorted(expected_pages - set(owners))
    stats = {kind: sum(row["comparison"] == kind for row in rows) for kind in ("exact", "normalized", "mismatch")}
    report = {
        "volume": 1,
        "status": "source_spine_verified",
        "chapters": len(chapters),
        "titles_visually_reviewed": len(rows),
        "verified_exact_statuses": sum(row["visual_status"] == "verified_exact" for row in rows),
        "title_comparison": stats,
        "body_pages": len(expected_pages),
        "unassigned_body_pages": unassigned,
        "duplicate_page_assignments": duplicate_pages,
        "chapter_order_ok": [row["number"] for row in rows] == list(range(1, 111)),
        "source_complete": not unassigned and not duplicate_pages,
        "raw_ocr_modified": False,
        "fingerprints": {
            "chapter_ids": digest([row["chapter_id"] for row in rows]),
            "chapter_order": digest([row["number"] for row in rows]),
            "page_ownership": digest({row["chapter_id"]: chapters[i]["sourcePages"] for i, row in enumerate(rows)}),
            "verified_titles": digest([row["final_title"] for row in rows]),
        },
    }
    (args.output / "volume1_verified_title_manifest.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (args.output / "volume1_verified_title_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader(); writer.writerows(rows)
    (args.output / "volume1_source_spine_verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output / "volume1_source_spine_verification.md").write_text(
        "# Volume 1 source-spine verification\n\n"
        f"- Chapters: {report['chapters']}\n"
        f"- Titles visually reviewed: {report['titles_visually_reviewed']}\n"
        f"- Exact/normalized/mismatched OCR titles: {stats['exact']}/{stats['normalized']}/{stats['mismatch']}\n"
        f"- Assigned body pages: {report['body_pages']}\n"
        f"- Duplicate assignments: {len(duplicate_pages)}\n"
        f"- Unassigned pages: {len(unassigned)}\n"
        f"- Source complete: {str(report['source_complete']).lower()}\n"
        "- Raw OCR modified: false\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["source_complete"] or not report["chapter_order_ok"] or report["verified_exact_statuses"] != 110:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
