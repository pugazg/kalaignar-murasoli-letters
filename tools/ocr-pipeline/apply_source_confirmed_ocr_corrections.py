#!/usr/bin/env python3
"""Apply conservative source-confirmed OCR corrections to page JSON files.

Raw OCR is never modified. The tool copies each page JSON to a separate output
stage, changes paragraph text only, and preserves OCR lines as evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


TOKEN_RE = re.compile(r"[\u0B80-\u0BFF]+|[A-Za-z]+(?:[-'][A-Za-z]+)*|\d+(?:[./-]\d+)*|[^\s]", re.UNICODE)
ZERO_WIDTH = {"\u200b", "\u200c", "\u200d", "\u2060", "\ufeff"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    return "".join(ch for ch in text if ch not in ZERO_WIDTH and unicodedata.category(ch) != "Cf")


def replace_exact_token(text: str, old: str, new: str) -> tuple[str, int]:
    pieces, cursor, count = [], 0, 0
    for match in TOKEN_RE.finditer(text):
        pieces.append(text[cursor:match.start()])
        token = match.group(0)
        if token == old:
            pieces.append(new)
            count += 1
        else:
            pieces.append(token)
        cursor = match.end()
    pieces.append(text[cursor:])
    return "".join(pieces), count


def context_satisfied(text: str, rule: dict) -> bool:
    return all(term in text for term in rule.get("required_context", []))


def apply_rules(text: str, rules: list[dict]) -> tuple[str, list[dict]]:
    changes = []
    current = normalize_text(text)
    for rule in rules:
        if rule["type"].startswith("context_") and not context_satisfied(current, rule):
            continue
        before = current
        if rule["type"] in {"exact_token", "context_token"}:
            current, count = replace_exact_token(current, rule["ocr"], rule["corrected"])
        elif rule["type"] == "context_span":
            count = current.count(rule["ocr"])
            if count == 1:
                current = current.replace(rule["ocr"], rule["corrected"], 1)
            elif count > 1:
                count = 0
        else:
            raise ValueError(f"Unsupported rule type: {rule['type']}")
        if count:
            changes.append({"rule_id": rule["id"], "before": rule["ocr"],
                            "after": rule["corrected"], "occurrences": count,
                            "confidence": rule["confidence"], "scope": rule["scope"]})
        assert current == before or count > 0
    return current, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volume", type=int, help="Infer standard input/output paths for this volume")
    parser.add_argument("--processed-root", type=Path,
                        default=Path("processed"))
    parser.add_argument("--input", type=Path, help="Directory containing page JSON files")
    parser.add_argument("--output", type=Path, help="Separate output text directory; required unless --dry-run")
    parser.add_argument("--rules", type=Path, default=Path("config/kalaignar_ocr_autocorrection_rules.json"))
    parser.add_argument("--audit", type=Path)
    parser.add_argument("--review-queue", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Rebuild outputs whose source hash has not changed")
    args = parser.parse_args()
    if args.volume:
        stage_root = args.processed_root / f"vol{args.volume}/ocr/01b_source_confirmed"
        args.input = args.input or args.processed_root / f"vol{args.volume}/ocr/01_ocr_v2_full/text"
        if not args.dry_run:
            args.output = args.output or stage_root / "text"
        args.audit = args.audit or stage_root / ("dry_run_audit.csv" if args.dry_run else "correction_audit.csv")
        args.review_queue = args.review_queue or stage_root / ("dry_run_review_queue.csv" if args.dry_run else "review_queue.csv")
    if not args.input:
        parser.error("provide --volume or --input")
    args.audit = args.audit or Path("ocr_autocorrection_audit.csv")
    args.review_queue = args.review_queue or Path("ocr_autocorrection_review_queue.csv")
    if not args.dry_run and not args.output:
        parser.error("--output is required unless --dry-run is used")
    if args.output and args.input.resolve() == args.output.resolve():
        parser.error("Input and output must be different; raw OCR cannot be overwritten")

    rule_data = json.loads(args.rules.read_text(encoding="utf-8"))
    rules = rule_data["rules"]
    rule_hash = sha256(args.rules)
    audit_rows, review_rows = [], []
    existing_audit_rows = list(csv.DictReader(args.audit.open(encoding="utf-8"))) if args.audit.exists() else []
    existing_review_rows = list(csv.DictReader(args.review_queue.open(encoding="utf-8"))) if args.review_queue.exists() else []
    rebuilt_page_ids = set()
    counts = Counter()
    pages = sorted(args.input.glob("*.json"))
    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)

    for source in pages:
        source_hash = sha256(source)
        target = args.output / source.name if args.output else None
        if target and target.exists() and not args.force:
            existing = json.loads(target.read_text(encoding="utf-8"))
            stage = existing.get("sourceConfirmedCorrectionStage", {})
            if stage.get("source_sha256") == source_hash and stage.get("rules_sha256") == rule_hash:
                counts["resumed"] += 1
                continue

        data = json.loads(source.read_text(encoding="utf-8"))
        rebuilt_page_ids.add(data.get("id", source.stem))
        page_changes = []
        new_paragraphs = []
        for paragraph_index, paragraph in enumerate(data.get("paragraphs", [])):
            corrected, changes = apply_rules(paragraph, rules)
            new_paragraphs.append(corrected)
            for change in changes:
                audit_rows.append({"page_id": data.get("id", source.stem), "paragraph_index": paragraph_index,
                                   **change, "source_file": str(source)})
            page_changes.extend(changes)

            # Flag context-dependent OCR strings that remain because their context gate failed.
            for rule in rules:
                if rule["type"].startswith("context_") and rule["ocr"] in corrected and not context_satisfied(corrected, rule):
                    review_rows.append({"page_id": data.get("id", source.stem), "paragraph_index": paragraph_index,
                                        "rule_id": rule["id"], "suspicious_text": rule["ocr"],
                                        "reason": "context_gate_not_satisfied", "paragraph": corrected})

        data["paragraphs"] = new_paragraphs
        data["sourceConfirmedCorrectionStage"] = {
            "script": "apply_source_confirmed_ocr_corrections.py",
            "source_sha256": source_hash,
            "rules_sha256": rule_hash,
            "changes_applied": sum(c["occurrences"] for c in page_changes),
            "rules_triggered": sorted({c["rule_id"] for c in page_changes}),
            "ocr_lines_preserved": True,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        counts["pages"] += 1
        counts["changes"] += data["sourceConfirmedCorrectionStage"]["changes_applied"]
        if page_changes:
            counts["pages_changed"] += 1
        if target and not args.dry_run:
            target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    audit_rows = [r for r in existing_audit_rows if r.get("page_id") not in rebuilt_page_ids] + audit_rows
    review_rows = [r for r in existing_review_rows if r.get("page_id") not in rebuilt_page_ids] + review_rows
    fields = ["page_id", "paragraph_index", "rule_id", "before", "after", "occurrences", "confidence", "scope", "source_file"]
    args.audit.parent.mkdir(parents=True, exist_ok=True)
    with args.audit.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(audit_rows)
    with args.review_queue.open("w", encoding="utf-8", newline="") as handle:
        fields2 = ["page_id", "paragraph_index", "rule_id", "suspicious_text", "reason", "paragraph"]
        writer = csv.DictWriter(handle, fieldnames=fields2); writer.writeheader(); writer.writerows(review_rows)

    summary = {"input_pages": len(pages), "processed_pages": counts["pages"], "resumed_pages": counts["resumed"],
               "pages_changed": counts["pages_changed"], "corrections_applied": counts["changes"],
               "audit_total_corrections": sum(int(r.get("occurrences", 0)) for r in audit_rows),
               "review_items": len(review_rows), "dry_run": args.dry_run, "rules": len(rules),
               "raw_ocr_modified": False}
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
