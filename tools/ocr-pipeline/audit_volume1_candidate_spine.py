#!/usr/bin/env python3
"""Strict structural audit for the Volume 1 candidate chapter spine."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def page_number(page_id: str) -> int:
    return int(page_id.rsplit("p", 1)[-1])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--chapters",
        type=Path,
        default=Path("processed/vol1/ocr/04_candidate_spine"),
    )
    parser.add_argument("--first-body-page", type=int, default=24)
    parser.add_argument("--last-body-page", type=int, default=401)
    args = parser.parse_args()

    index_path = args.chapters / "chapters-index.json"
    if not index_path.exists():
        raise SystemExit(f"Candidate spine index not found: {index_path}")
    index = json.loads(index_path.read_text(encoding="utf-8"))
    chapters = index.get("chapters", [])

    numbers = [row.get("number") for row in chapters if row.get("number") is not None]
    # The printed contents spans 1-110. Earlier planning incorrectly assumed
    # 100 chapters, which made valid letters 101-110 look unexpected.
    expected_numbers = set(range(1, 111))
    actual_numbers = set(numbers)
    duplicate_numbers = sorted(number for number, count in Counter(numbers).items() if count > 1)
    missing_numbers = sorted(expected_numbers - actual_numbers)
    unexpected_numbers = sorted(actual_numbers - expected_numbers)

    page_owners: dict[int, list[str]] = {}
    for row in chapters:
        for page_id in row.get("sourcePages", []):
            page = page_number(page_id)
            if args.first_body_page <= page <= args.last_body_page:
                page_owners.setdefault(page, []).append(row["id"])

    expected_pages = set(range(args.first_body_page, args.last_body_page + 1))
    assigned_pages = set(page_owners)
    unassigned_pages = sorted(expected_pages - assigned_pages)
    duplicate_pages = {
        str(page): owners for page, owners in sorted(page_owners.items()) if len(owners) > 1
    }

    ordered_numbers = [row.get("number") for row in chapters if row.get("number") is not None]
    order_ok = ordered_numbers == sorted(ordered_numbers)
    passed = (
        len(chapters) == 110
        and not missing_numbers
        and not unexpected_numbers
        and not duplicate_numbers
        and not unassigned_pages
        and not duplicate_pages
        and order_ok
    )
    report = {
        "volume": 1,
        "status": "candidate_only_not_frozen",
        "passed_strict_structure": passed,
        "expected_chapters": 110,
        "actual_chapters": len(chapters),
        "missing_letter_numbers": missing_numbers,
        "unexpected_letter_numbers": unexpected_numbers,
        "duplicate_letter_numbers": duplicate_numbers,
        "body_page_range": [args.first_body_page, args.last_body_page],
        "assigned_body_pages": len(assigned_pages),
        "unassigned_body_pages": unassigned_pages,
        "duplicate_page_assignments": duplicate_pages,
        "chapter_order_ok": order_ok,
        "freeze_allowed": False,
        "freeze_note": "Visual source reconciliation and complete contents verification are still required.",
    }
    output = args.chapters / "candidate_spine_audit.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if passed else 2)


if __name__ == "__main__":
    main()
