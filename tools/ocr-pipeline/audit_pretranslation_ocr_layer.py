#!/usr/bin/env python3
"""Audit an isolated chapter layer for unresolved pre-translation OCR anomalies."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
from collections import Counter
from pathlib import Path


REVIEW_CLASSES = {
    "isolated_latin_fragment_in_tamil_context",
    "mixed_script_token",
    "unexpected_unicode_character",
    "malformed_tamil_combining_sequence",
    "probable_tamil_ocr_confusion",
    "punctuation_or_symbol_junk",
    "broken_word_boundary",
    "probable_missing_space",
    "probable_spurious_space",
    "metadata_date_missing_with_visible_signoff_date",
    "repeated_or_duplicated_ocr_fragment",
    "very_low_tamil_ratio_line",
}


def write_csv(path: Path, rows: list[dict]):
    fields = list(rows[0]) if rows else ["anomaly_id", "chapter_id", "status"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volume", type=int, required=True)
    parser.add_argument("--layer-root", type=Path, default=Path("v6_source_verification/v6_7_pretranslation"))
    parser.add_argument("--anomalies", type=Path, default=Path("v6_source_verification/v6_3/ocr_anomaly_manifest.csv"))
    parser.add_argument("--rules", type=Path, default=Path("config/kalaignar_ocr_autocorrection_rules.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or Path(f"analysis/vol{args.volume}_pretranslation_ocr_audit")
    output.mkdir(parents=True, exist_ok=True)

    layer = args.layer_root / f"vol{args.volume}"
    index = json.loads((layer / "chapters-index.json").read_text(encoding="utf-8"))
    texts, dates = {}, {}
    for item in index["chapters"]:
        path = layer / "chapters" / item["folder"] / "chapter.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        texts[item["id"]] = "\n".join([data.get("title", {}).get("ta", ""), data.get("salutation", ""), *data.get("paragraphs", [])])
        dates[item["id"]] = data.get("date")

    rules = json.loads(args.rules.read_text(encoding="utf-8"))["rules"]
    correction_path = Path(__file__).with_name("apply_source_confirmed_ocr_corrections.py")
    spec = importlib.util.spec_from_file_location("source_confirmed_corrections", correction_path)
    correction_module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(correction_module)
    correction_map = {r["ocr"]: r["corrected"] for r in rules}
    anomalies = [r for r in csv.DictReader(args.anomalies.open(encoding="utf-8"))
                 if r["volume"] == str(args.volume) and r["anomaly_class"] in REVIEW_CLASSES]
    rows = []
    for row in anomalies:
        cid, fragment = row["chapter_id"], row["fragment"]
        text = texts.get(cid, "")
        survives = bool(fragment and fragment in text)
        corrected = correction_map.get(fragment, "")
        corrected_present = bool(corrected and corrected in text)
        if row["anomaly_class"] == "metadata_date_missing_with_visible_signoff_date" and dates.get(cid):
            status = "resolved_metadata_date_present"
        elif not survives and corrected_present:
            status = "resolved_by_source_confirmed_rule"
        elif survives:
            status = "survives_requires_review"
        else:
            status = "not_present_in_current_layer"
        rows.append({**row, "current_layer_status": status,
                     "rule_corrected_form": corrected, "current_metadata_date": dates.get(cid) or ""})

    write_csv(output / "anomaly_reconciliation.csv", rows)
    unresolved = [r for r in rows if r["current_layer_status"] == "survives_requires_review"]
    write_csv(output / "unresolved_pretranslation_queue.csv", unresolved)

    # Exact source-confirmed OCR forms that still survive are useful regressions,
    # but remain review signals because source context can differ.
    residuals = []
    for rule in rules:
        for cid, text in texts.items():
            if rule["type"] in {"exact_token", "context_token"}:
                count = sum(token == rule["ocr"] for token in correction_module.TOKEN_RE.findall(text))
            else:
                count = text.count(rule["ocr"])
            if count:
                residuals.append({"chapter_id": cid, "rule_id": rule["id"], "ocr_form": rule["ocr"],
                                  "corrected_form": rule["corrected"], "occurrences": count,
                                  "status": "source_check_before_translation"})
    write_csv(output / "known_pattern_residuals.csv", residuals)

    summary = {
        "volume": args.volume,
        "chapters": len(index["chapters"]),
        "review_class_records": len(rows),
        "status_counts": dict(Counter(r["current_layer_status"] for r in rows)),
        "unresolved_by_class": dict(Counter(r["anomaly_class"] for r in unresolved)),
        "chapters_with_unresolved": len({r["chapter_id"] for r in unresolved}),
        "known_pattern_residual_records": len(residuals),
        "translation_started": False,
    }
    (output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = [f"# Volume {args.volume} Pre-Translation OCR Audit", "",
              f"- Chapters audited: {summary['chapters']}",
              f"- Review-class anomaly records reconciled: {summary['review_class_records']}",
              f"- Chapters with surviving review signals: {summary['chapters_with_unresolved']}",
              f"- Known source-confirmed OCR pattern residuals: {summary['known_pattern_residual_records']}",
              "", "## Status", ""]
    report.extend(f"- `{key}`: {value}" for key, value in summary["status_counts"].items())
    report += ["", "## Surviving Signals by Class", ""]
    report.extend(f"- `{key}`: {value}" for key, value in summary["unresolved_by_class"].items())
    report += ["", "These are review signals, not automatically proven errors. Genuine English and valid Tamil morphology must be preserved. Translation has not started.", ""]
    (output / "report.md").write_text("\n".join(report), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
