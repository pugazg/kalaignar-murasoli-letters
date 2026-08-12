#!/usr/bin/env python3
"""Prepare or refresh a resumable chapter translation manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", type=int, required=True)
    parser.add_argument("--source-root", type=Path, default=Path("v6_source_verification/v6_4/publication_text_layer"))
    parser.add_argument("--output-root", type=Path, default=Path("translations"))
    args = parser.parse_args()

    source = args.source_root / f"vol{args.volume}"
    output = args.output_root / f"vol{args.volume}"
    output.mkdir(parents=True, exist_ok=True)
    index = json.loads((source / "chapters-index.json").read_text(encoding="utf-8"))
    rows = []
    for order, item in enumerate(index["chapters"], 1):
        chapter = source / "chapters" / item["folder"] / "chapter.md"
        target = output / f"{item['id']}.en.md"
        rows.append({
            "order": order,
            "chapter_id": item["id"],
            "letter_number": item.get("number", ""),
            "tamil_title": item["title"]["ta"],
            "source_file": str(chapter),
            "source_sha256": sha256(chapter),
            "translation_file": str(target),
            "status": "translated" if target.exists() else "pending",
        })
    with (output / "translation_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    summary = {"volume": args.volume, "chapters": len(rows), "translated": sum(x["status"] == "translated" for x in rows),
               "pending": sum(x["status"] == "pending" for x in rows), "source_layer": str(source)}
    (output / "translation_status.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
