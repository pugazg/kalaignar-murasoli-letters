#!/usr/bin/env python3
"""Apply source-confirmed OCR rules to an existing frozen chapter structure."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import shutil
from pathlib import Path


def load_correction_module():
    path = Path(__file__).with_name("apply_source_confirmed_ocr_corrections.py")
    spec = importlib.util.spec_from_file_location("source_confirmed_corrections", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def fingerprint(index: dict) -> str:
    spine = [{"id": c["id"], "number": c["number"], "title": c["title"],
              "sourcePages": c["sourcePages"]} for c in index["chapters"]]
    return hashlib.sha256(json.dumps(spine, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volume", type=int, required=True)
    parser.add_argument("--source-root", type=Path,
                        default=Path("v6_source_verification/v6_4/publication_text_layer"))
    parser.add_argument("--output-root", type=Path,
                        default=Path("v6_source_verification/v6_7_pretranslation"))
    parser.add_argument("--rules", type=Path, default=Path("config/kalaignar_ocr_autocorrection_rules.json"))
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    correction = load_correction_module()
    rules = json.loads(args.rules.read_text(encoding="utf-8"))["rules"]
    source = args.source_root / f"vol{args.volume}"
    output = args.output_root / f"vol{args.volume}"
    if output.exists():
        if not args.force:
            raise SystemExit(f"Output exists: {output}\nUse --force to rebuild the isolated layer.")
        shutil.rmtree(output)
    shutil.copytree(source, output)

    source_index = json.loads((source / "chapters-index.json").read_text(encoding="utf-8"))
    audit = []
    changed_chapters = set()
    for item in source_index["chapters"]:
        folder = output / "chapters" / item["folder"]
        json_path = folder / "chapter.json"
        data = json.loads(json_path.read_text(encoding="utf-8"))
        fields = [("title", data.get("title", {}).get("ta") or ""),
                  ("salutation", data.get("salutation") or "")]
        fields.extend(
            (f"paragraph:{i}", value or "")
            for i, value in enumerate(data.get("paragraphs", []))
        )
        corrected_values = {}
        for field, value in fields:
            corrected, changes = correction.apply_rules(value, rules)
            corrected_values[field] = corrected
            for change in changes:
                audit.append({"chapter_id": item["id"], "field": field, **change})
                changed_chapters.add(item["id"])
        data["title"]["ta"] = corrected_values["title"]
        data["salutation"] = corrected_values["salutation"]
        data["paragraphs"] = [corrected_values[f"paragraph:{i}"] for i in range(len(data.get("paragraphs", [])))]
        data["sourceConfirmedCorrectionStage"] = {
            "rules": str(args.rules),
            "changes": sum(int(r["occurrences"]) for r in audit if r["chapter_id"] == item["id"]),
            "source_layer": str(source),
        }
        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        md_path = folder / "chapter.md"
        blocks = md_path.read_text(encoding="utf-8").split("\n\n")
        md_path.write_text("\n\n".join(correction.apply_rules(block, rules)[0] for block in blocks), encoding="utf-8")

    fields = ["chapter_id", "field", "rule_id", "before", "after", "occurrences", "confidence", "scope"]
    with (args.output_root / f"vol{args.volume}_correction_audit.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(audit)

    output_index = json.loads((output / "chapters-index.json").read_text(encoding="utf-8"))
    result = {
        "volume": args.volume,
        "chapters": len(source_index["chapters"]),
        "changed_chapters": len(changed_chapters),
        "corrections": sum(int(r["occurrences"]) for r in audit),
        "source_spine_fingerprint": fingerprint(source_index),
        "output_spine_fingerprint": fingerprint(output_index),
        "structural_regression_passed": fingerprint(source_index) == fingerprint(output_index),
        "source_layer_modified": False,
    }
    (args.output_root / f"vol{args.volume}_validation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
