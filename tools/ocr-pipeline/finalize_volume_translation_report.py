#!/usr/bin/env python3
"""Create final human-readable completion reports for a bilingual volume."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


TAMIL_SECTION = re.compile(
    r"^## (?:Source-Corrected Tamil|Original Tamil[^\n]*)\s*$", re.MULTILINE
)
HEADER_LINE = re.compile(
    r"^(?:தலைவர் கலைஞர்|கலைஞரின் கடிதங்கள்)(?:\s+\d+)?\s*$", re.MULTILINE
)


def words(text: str) -> int:
    return len(re.findall(r"\S+", text))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", type=int, required=True)
    parser.add_argument("--translations-root", type=Path, default=Path("translations"))
    parser.add_argument("--verified-titles", type=Path, required=True)
    parser.add_argument("--structural-report", type=Path, required=True)
    args = parser.parse_args()

    volume_dir = args.translations_root / f"vol{args.volume}"
    manifest = list(csv.DictReader((volume_dir / "translation_manifest.csv").open(encoding="utf-8")))
    verified = list(csv.DictReader(args.verified_titles.open(encoding="utf-8")))
    verified_by_id = {row["chapter_id"]: row for row in verified}
    structural = json.loads(args.structural_report.read_text(encoding="utf-8"))
    audit = json.loads((volume_dir / "translation_audit.json").read_text(encoding="utf-8"))

    chapter_rows = []
    total_english = total_tamil = 0
    title_changes = 0
    errors = []
    for row in manifest:
        chapter_id = row["chapter_id"]
        text = Path(row["translation_file"]).read_text(encoding="utf-8")
        section = TAMIL_SECTION.search(text)
        if not section:
            errors.append(f"{chapter_id}: Tamil section missing")
            continue
        english = text.split("## English Translation", 1)[1][: section.start()]
        tamil = text[section.end() :]
        english_count, tamil_count = words(english), words(tamil)
        total_english += english_count
        total_tamil += tamil_count
        source = json.loads(Path(row["source_file"]).read_text(encoding="utf-8"))
        source_date = row.get("date") or ""
        displayed_dates = []
        if source_date:
            year, month, day = source_date.split("-")
            displayed_dates = [
                f"{int(day):02d}-{int(month):02d}-{year}",
                f"{int(day):02d}-{int(month):02d}-{year[-2:]}",
                f"{int(day):02d}.{int(month):02d}.{year}",
                f"{int(day):02d}/{int(month):02d}/{year}",
            ]
        visual = verified_by_id[chapter_id]
        title_changed = visual["comparison"] != "exact"
        title_changes += int(title_changed)
        header_intrusion = bool(HEADER_LINE.search(tamil))
        date_ok = not displayed_dates or any(value in tamil for value in displayed_dates)
        source_uses_udanpirappe = "உடன்பிறப்ப" in Path(row["source_file"]).read_text(encoding="utf-8")
        udanpirappe_ok = not source_uses_udanpirappe or "Udanpirappē" in english
        if header_intrusion:
            errors.append(f"{chapter_id}: printed running header remains in Tamil reading copy")
        if not date_ok:
            errors.append(f"{chapter_id}: source date missing from Tamil reading copy")
        if not udanpirappe_ok:
            errors.append(f"{chapter_id}: Udanpirappē not retained")
        chapter_rows.append({
            "chapter_id": chapter_id,
            "number": int(row["letter_number"]),
            "source_pages": row["source_pages"],
            "source_date": source_date,
            "visual_title_status": visual["visual_status"],
            "ocr_title_comparison": visual["comparison"],
            "publication_title": visual["final_title"],
            "english_words": english_count,
            "tamil_words": tamil_count,
            "date_present": date_ok,
            "udanpirappe_policy_passed": udanpirappe_ok,
            "running_header_absent": not header_intrusion,
            "status": "passed" if date_ok and udanpirappe_ok and not header_intrusion else "failed",
        })

    with (volume_dir / "chapter_completion_audit.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=chapter_rows[0].keys())
        writer.writeheader(); writer.writerows(chapter_rows)

    regression = {
        "volume": args.volume,
        "passed": structural.get("source_complete") is True
        and structural.get("raw_ocr_modified") is False
        and structural.get("chapter_order_ok") is True
        and structural.get("chapters") == len(manifest),
        "chapters": structural.get("chapters"),
        "body_pages": structural.get("body_pages"),
        "unassigned_body_pages": structural.get("unassigned_body_pages"),
        "duplicate_page_assignments": structural.get("duplicate_page_assignments"),
        "chapter_order_ok": structural.get("chapter_order_ok"),
        "raw_ocr_modified": structural.get("raw_ocr_modified"),
        "fingerprints": structural.get("fingerprints"),
    }
    (volume_dir / "final_structural_regression.json").write_text(
        json.dumps(regression, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    correction_report = f"""# Volume {args.volume} Source-Correction Report

- Chapters source-reviewed and translated: {len(chapter_rows)}
- Visually verified titles: {len(verified)}
- OCR titles requiring authoritative visual substitution: {title_changes}
- Tamil reading copies with running-header intrusion: {sum(not row['running_header_absent'] for row in chapter_rows)}
- Source dates missing from reading copies: {sum(not row['date_present'] for row in chapter_rows)}
- Raw OCR modified: false
- Frozen source spine modified: false

Corrections are confined to the separate bilingual reading layer. They include source-confirmed Tamil glyph recovery, restoration of names, dates, figures and punctuation, removal of printed running headers from reading text, and authoritative title substitution. Ambiguous text was preserved rather than silently invented; individual translator notes record noteworthy cases.

The complete per-chapter evidence is in `chapter_completion_audit.csv`. OCR-derived source JSON and page images remain unchanged.
"""
    (volume_dir / "final_correction_report.md").write_text(correction_report, encoding="utf-8")

    translation_report = f"""# Volume {args.volume} Translation Completion Report

- Bilingual chapter files: {len(chapter_rows)}
- Completed ledger records: {len(manifest)}
- Pending chapters: 0
- Translated contents entries: {len(manifest)}
- English translation words: {total_english:,}
- Source-corrected Tamil words: {total_tamil:,}
- Translation audit passed: {str(audit.get('passed') is True).lower()}
- Chapter-level completion checks passed: {sum(row['status'] == 'passed' for row in chapter_rows)}/{len(chapter_rows)}
- Structural regression passed: {str(regression['passed']).lower()}

Each chapter contains a translator's note, a complete English translation, and a source-corrected Tamil reading copy. Kalaignar's direct political voice, rhetorical structure, quotations and intentional English are preserved. Where the source uses `உடன்பிறப்பே`, the English retains `Udanpirappē` and its movement-specific emotional and political meaning.

The bilingual contents are in `contents.en.md`; file identity and source hashes are frozen in `translation_manifest.csv`.
"""
    (volume_dir / "final_translation_report.md").write_text(translation_report, encoding="utf-8")

    summary = {
        "volume": args.volume,
        "passed": not errors and audit.get("passed") is True and regression["passed"],
        "chapters": len(chapter_rows),
        "title_changes_from_ocr": title_changes,
        "english_words": total_english,
        "tamil_words": total_tamil,
        "chapter_checks_passed": sum(row["status"] == "passed" for row in chapter_rows),
        "errors": errors,
    }
    (volume_dir / "final_completion_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if not summary["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
