#!/usr/bin/env python3
"""Audit the isolated Volume 1 random-page bilingual sample."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "samples" / "vol1_random_10"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    with (SAMPLE / "sample_manifest.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    results = []
    errors = []
    for row in rows:
        page_id = row["page_id"]
        image = SAMPLE / row["source_image"]
        raw_ocr = SAMPLE / row["ocr_text"]
        bilingual = SAMPLE / "corrected" / f"{page_id}.bilingual.md"
        text = bilingual.read_text(encoding="utf-8") if bilingual.exists() else ""
        is_contents = row["page_type"] == "contents"
        english_ok = "English translation" in text if is_contents else "## English Translation" in text
        tamil_ok = "Source-verified Tamil title" in text if is_contents else "## Source-Corrected Tamil" in text
        checks = {
            "page_id": page_id,
            "page_type": row["page_type"],
            "image_exists": image.is_file(),
            "raw_ocr_exists": raw_ocr.is_file(),
            "bilingual_exists": bilingual.is_file(),
            "source_note_present": "## Source Note" in text,
            "english_present": english_ok,
            "tamil_present": tamil_ok,
            "em_dash_absent": "—" not in text,
            "source_image_sha256": sha256(image) if image.is_file() else None,
            "raw_ocr_sha256": sha256(raw_ocr) if raw_ocr.is_file() else None,
            "bilingual_sha256": sha256(bilingual) if bilingual.is_file() else None,
            "tamil_character_count": len(re.findall(r"[\u0B80-\u0BFF]", text)),
        }
        failed = [key for key, value in checks.items() if key.endswith(("_exists", "_present", "_absent")) and not value]
        if failed:
            errors.append({"page_id": page_id, "failed_checks": failed})
        results.append(checks)

    contents_entries = {}
    for page_id in ("page_0019", "page_0021"):
        text = (SAMPLE / "corrected" / f"{page_id}.bilingual.md").read_text(encoding="utf-8")
        contents_entries[page_id] = len(re.findall(r"^\|\s*\d+\s*\|", text, re.MULTILINE))

    payload = {
        "passed": not errors,
        "sample_pages": len(rows),
        "contents_pages": sum(row["page_type"] == "contents" for row in rows),
        "letter_pages": sum(row["page_type"] == "letter" for row in rows),
        "bilingual_files": sum((SAMPLE / "corrected" / f"{row['page_id']}.bilingual.md").is_file() for row in rows),
        "contents_entries_translated": contents_entries,
        "errors": errors,
        "pages": results,
    }
    output = SAMPLE / "sample_audit.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in payload if key != "pages"}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if payload["passed"] else 1)


if __name__ == "__main__":
    main()
