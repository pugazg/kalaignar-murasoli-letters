#!/usr/bin/env python3
"""Compare Volume 53 OCR stages against the corrected Tamil translation copies."""

from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


WORD_RE = re.compile(r"[\u0B80-\u0BFF]+|[A-Za-z]+(?:[-'][A-Za-z]+)*|\d+(?:[./-]\d+)*|[^\s]", re.UNICODE)
TAMIL_RE = re.compile(r"[\u0B80-\u0BFF]")
LATIN_RE = re.compile(r"[A-Za-z]")
ZERO_WIDTH = {"\u200b", "\u200c", "\u200d", "\u2060", "\ufeff"}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_csv(path: Path, rows: list[dict], fields: list[str] | None = None):
    if not fields:
        fields = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def normalize(text: str, *, collapse: bool = True) -> str:
    text = unicodedata.normalize("NFC", text)
    text = "".join(ch for ch in text if ch not in ZERO_WIDTH and unicodedata.category(ch) != "Cf")
    text = text.replace("\u00a0", " ")
    if collapse:
        text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_page_paragraphs(data: dict) -> list[str]:
    out = []
    for paragraph in data.get("paragraphs", []):
        value = normalize(paragraph)
        if not value or value == "தலைவர் கலைஞர்" or re.fullmatch(r"\d{1,4}", value):
            continue
        out.append(value)
    return out


def chapter_text_from_pages(text_dir: Path, pages: list[str]) -> str:
    paragraphs = []
    for page_id in pages:
        path = text_dir / f"{page_id}.json"
        if path.exists():
            paragraphs.extend(clean_page_paragraphs(read_json(path)))
    return normalize("\n".join(paragraphs))


def chapter_text(data: dict) -> str:
    title = data.get("title", {}).get("ta", "")
    number = data.get("number", "")
    parts = [f"{number}. {title}" if title else "", data.get("salutation", "")]
    parts.extend(data.get("paragraphs", []))
    return normalize("\n".join(x for x in parts if x))


def translation_tamil(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "## Original Tamil" not in text:
        return ""
    text = text.split("## Original Tamil", 1)[1]
    lines = []
    for line in text.splitlines():
        line = re.sub(r"^#{1,6}\s+", "", line.strip())
        if line:
            lines.append(line)
    return normalize("\n".join(lines))


def tokens(text: str) -> list[str]:
    return WORD_RE.findall(normalize(text))


def stage_metrics(before: str, after: str) -> dict:
    a, b = tokens(before), tokens(after)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    equal = sum(i2 - i1 for tag, i1, i2, _, _ in sm.get_opcodes() if tag == "equal")
    inserted = sum(j2 - j1 for tag, _, _, j1, j2 in sm.get_opcodes() if tag == "insert")
    deleted = sum(i2 - i1 for tag, i1, i2, _, _ in sm.get_opcodes() if tag == "delete")
    replaced_before = sum(i2 - i1 for tag, i1, i2, _, _ in sm.get_opcodes() if tag == "replace")
    replaced_after = sum(j2 - j1 for tag, _, _, j1, j2 in sm.get_opcodes() if tag == "replace")
    return {
        "before_tokens": len(a), "after_tokens": len(b), "equal_tokens": equal,
        "inserted_tokens": inserted, "deleted_tokens": deleted,
        "replaced_before_tokens": replaced_before, "replaced_after_tokens": replaced_after,
        "token_similarity": round(sm.ratio(), 6),
    }


def script_type(value: str) -> str:
    tamil = bool(TAMIL_RE.search(value)); latin = bool(LATIN_RE.search(value))
    if tamil and latin: return "mixed"
    if tamil: return "tamil"
    if latin: return "latin"
    if any(ch.isdigit() for ch in value): return "numeric"
    return "symbol"


def classify_change(old: str, new: str) -> str:
    if normalize(old) == normalize(new): return "unicode_or_whitespace_normalization"
    so, sn = script_type(old), script_type(new)
    if so in {"latin", "mixed"} and sn == "tamil": return "latin_hallucination_to_tamil"
    if so == "tamil" and sn == "tamil": return "tamil_glyph_or_word_corruption"
    if so == "numeric" or sn == "numeric": return "numeric_or_date_corruption"
    if so == "symbol" or sn == "symbol": return "punctuation_or_symbol_corruption"
    return "other_replacement"


def edit_distance(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def char_ops(old: str, new: str):
    a, b = list(old), list(new)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal": continue
        left, right = "".join(a[i1:i2]), "".join(b[j1:j2])
        yield tag, left or "∅", right or "∅"


def extract_changes(chapter_id: str, stage: str, before: str, after: str) -> list[dict]:
    a, b = tokens(before), tokens(after)
    rows = []
    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal": continue
        old_tokens, new_tokens = a[i1:i2], b[j1:j2]
        if tag == "replace" and len(old_tokens) == len(new_tokens):
            pairs = zip(old_tokens, new_tokens)
        else:
            pairs = [(" ".join(old_tokens), " ".join(new_tokens))]
        for old, new in pairs:
            rows.append({
                "chapter_id": chapter_id, "stage_transition": stage, "operation": tag,
                "before": old, "after": new, "before_script": script_type(old),
                "after_script": script_type(new), "change_class": classify_change(old, new),
                "edit_distance": edit_distance(old, new) if len(old) < 100 and len(new) < 100 else "",
                "before_token_index": i1, "after_token_index": j1,
            })
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--volume", type=int, default=53)
    parser.add_argument("--processed-root", type=Path, default=Path("processed"))
    parser.add_argument("--output", type=Path, default=Path("analysis/vol53_ocr_stage_comparison"))
    args = parser.parse_args()
    volume = args.volume
    out = args.output
    out.mkdir(parents=True, exist_ok=True)

    raw_dir = args.processed_root / f"vol{volume}/ocr/01_ocr_v2_full/text"
    corrected_dir = args.processed_root / f"vol{volume}/ocr/03_corrected_v4/text"
    v64 = Path(f"v6_source_verification/v6_4/publication_text_layer/vol{volume}")
    index = read_json(v64 / "chapters-index.json")["chapters"]
    translations = Path(f"translations/vol{volume}")

    chapter_rows, change_rows = [], []
    texts = {}
    for item in index:
        cid = item["id"]
        chapter_path = v64 / "chapters" / item["folder"] / "chapter.json"
        raw = chapter_text_from_pages(raw_dir, item["sourcePages"])
        corrected = chapter_text_from_pages(corrected_dir, item["sourcePages"])
        publication = chapter_text(read_json(chapter_path))
        translated = translation_tamil(translations / f"{cid}.en.md")
        texts[cid] = {"raw": raw, "corrected": corrected, "publication": publication, "translation": translated}
        row = {"chapter_id": cid, "number": item["number"], "pages": len(item["sourcePages"])}
        for label, before, after in [
            ("raw_to_dictionary", raw, corrected),
            ("dictionary_to_v6_4", corrected, publication),
            ("v6_4_to_translation", publication, translated),
            ("raw_to_translation", raw, translated),
        ]:
            metrics = stage_metrics(before, after)
            row.update({f"{label}_{key}": value for key, value in metrics.items()})
            change_rows.extend(extract_changes(cid, label, before, after))
        chapter_rows.append(row)

    write_csv(out / "chapter_stage_comparison.csv", chapter_rows)
    write_csv(out / "token_change_manifest.csv", change_rows)

    correction_changes = [r for r in change_rows if r["stage_transition"] == "v6_4_to_translation"]
    pair_counts = Counter((r["before"], r["after"], r["change_class"]) for r in correction_changes if r["operation"] == "replace")
    pair_rows = [{"before": a, "after": b, "change_class": c, "occurrences": n,
                  "edit_distance": edit_distance(a, b) if len(a) < 100 and len(b) < 100 else ""}
                 for (a, b, c), n in pair_counts.most_common()]
    write_csv(out / "corrected_span_patterns.csv", pair_rows)

    confusions = Counter()
    examples = defaultdict(list)
    for row in correction_changes:
        if row["operation"] != "replace" or len(row["before"].split()) != 1 or len(row["after"].split()) != 1:
            continue
        for op, old, new in char_ops(row["before"], row["after"]):
            key = (op, old, new)
            confusions[key] += 1
            if len(examples[key]) < 5:
                examples[key].append(f"{row['chapter_id']}:{row['before']}→{row['after']}")
    confusion_rows = [{"operation": op, "ocr_sequence": old, "source_sequence": new,
                       "occurrences": count, "examples": " | ".join(examples[(op, old, new)])}
                      for (op, old, new), count in confusions.most_common()]
    write_csv(out / "character_confusion_patterns.csv", confusion_rows)

    # A frequently source-corrected OCR token that still survives in a translation
    # copy is strong evidence that the translation layer is not yet a complete gold set.
    residual_rows = []
    recurring_pairs = [(a, b, c, n) for (a, b, c), n in pair_counts.items()
                       if n >= 2 and len(a) >= 3 and len(b) >= 3 and " " not in a
                       and a != b and script_type(a) == script_type(b) == "tamil"]
    for cid, stage_texts in texts.items():
        final_tokens = Counter(tokens(stage_texts["translation"]))
        for old, new, change_class, learned_count in recurring_pairs:
            if final_tokens[old]:
                residual_rows.append({
                    "chapter_id": cid, "surviving_ocr_token": old,
                    "source_corrected_form_seen_elsewhere": new,
                    "surviving_occurrences": final_tokens[old],
                    "source_confirmed_pair_occurrences": learned_count,
                    "change_class": change_class,
                    "status": "requires_source_check_not_auto_replace",
                })
    write_csv(out / "learned_pattern_residuals.csv", residual_rows)

    experiment_path = Path("v6_source_verification/v6_4/targeted_reocr_experiment_manifest.csv")
    experiments = list(csv.DictReader(experiment_path.open(encoding="utf-8")))
    reocr_rows = []
    for row in experiments:
        source = normalize(row.get("source_visible_reading", ""))
        variants = [normalize(row.get(name, "")) for name in (
            "ocr_variant_A_mild_psm6", "ocr_variant_B_mild_psm7", "ocr_variant_C_threshold_psm7")]
        reocr_rows.append({
            "experiment_id": row["experiment_id"], "chapter_id": row["chapter_id"],
            "page_id": row["page_id"], "selection_class": row["selection_class"],
            "original_ocr": row["original_ocr"], "source_visible_reading": source,
            "variant_a": variants[0], "variant_b": variants[1], "variant_c": variants[2],
            "any_exact_source_recovery": bool(source and source in variants),
            "manifest_correct_any": row.get("correct_source_form_in_any_variant", ""),
            "variants_converge": row.get("ocr_variants_converge", ""),
            "chapter_text_replaced": row.get("chapter_text_replaced", ""),
            "recommended_method": row.get("recommended_recovery_method", ""),
        })
    write_csv(out / "targeted_reocr_comparison.csv", reocr_rows)

    stage_summary = {}
    for stage in ("raw_to_dictionary", "dictionary_to_v6_4", "v6_4_to_translation", "raw_to_translation"):
        rows = [r for r in change_rows if r["stage_transition"] == stage]
        stage_summary[stage] = {
            "change_records": len(rows),
            "chapters_changed": len({r["chapter_id"] for r in rows}),
            "classes": dict(Counter(r["change_class"] for r in rows).most_common()),
            "operations": dict(Counter(r["operation"] for r in rows).most_common()),
        }
    residual_markers = []
    suspicious_patterns = [r"\b[A-Za-z]{2,}\b", r"[௧௨௩௪௫௬௭௮௯]", r"[\u200b\u200c\u200d\ufeff]"]
    for cid, stage_texts in texts.items():
        final = stage_texts["translation"]
        for pattern in suspicious_patterns:
            for match in re.finditer(pattern, final):
                residual_markers.append({"chapter_id": cid, "pattern": pattern, "match": match.group(0),
                                         "context": final[max(0, match.start()-50):match.end()+50]})
    write_csv(out / "translation_residual_suspicion.csv", residual_markers)

    page_fix_counts = Counter()
    dictionary_fixes_applied = 0
    for path in corrected_dir.glob("*.json"):
        correction = read_json(path).get("correctionStage", {})
        fixes = int(correction.get("fixesApplied", 0))
        page_fix_counts[str(fixes)] += 1
        dictionary_fixes_applied += fixes
    manifest_reocr_recoveries = sum(str(r.get("manifest_correct_any", "")).lower() == "true" for r in reocr_rows)
    summary = {
        "volume": volume, "chapters": len(index),
        "stage_summary": stage_summary,
        "targeted_reocr": {
            "experiments": len(reocr_rows),
            "strict_full_field_equality_recovery": sum(bool(r["any_exact_source_recovery"]) for r in reocr_rows),
            "manifest_source_form_recovered_in_any_variant": manifest_reocr_recoveries,
            "chapter_text_replaced": sum(str(r["chapter_text_replaced"]).lower() in {"yes", "true", "1"} for r in reocr_rows),
        },
        "dictionary_stage": {
            "page_fixes_applied": dictionary_fixes_applied,
            "page_fix_distribution": dict(page_fix_counts),
        },
        "learned_pattern_residual_records": len(residual_rows),
        "translation_residual_suspicion_records": len(residual_markers),
        "input_fingerprints": {
            "chapter_index_sha256": hashlib.sha256((v64 / "chapters-index.json").read_bytes()).hexdigest(),
            "translation_manifest_sha256": hashlib.sha256((translations / "translation_manifest.csv").read_bytes()).hexdigest(),
        },
    }
    (out / "comparison_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    top_confusions = confusion_rows[:20]
    report = [
        f"# Volume {volume} OCR Stage Corruption Analysis", "",
        "## Scope", "",
        f"All {len(index)} source-complete chapters were compared across raw page OCR, v4 dictionary correction, the v6.4 publication layer, and the corrected Tamil reading copy embedded in each translation file. Targeted re-OCR is reported separately because it covered only selected crops and did not constitute a full-corpus text stage.", "",
        "## Stage Results", "",
    ]
    for stage, data in stage_summary.items():
        report.append(f"- `{stage}`: {data['change_records']} aligned change records across {data['chapters_changed']} chapters; classes: {data['classes']}.")
    report += ["", "## Targeted Re-OCR", "",
               f"- Experiments: {summary['targeted_reocr']['experiments']}",
               f"- Source form reported as recovered in at least one variant by the v6.4 experiment manifest: {summary['targeted_reocr']['manifest_source_form_recovered_in_any_variant']}",
               f"- Strict equality between the complete stored source-reading field and a complete OCR variant: {summary['targeted_reocr']['strict_full_field_equality_recovery']} (not the experiment's substring/region recovery metric)",
               f"- Chapter-text replacements made by the experiment: {summary['targeted_reocr']['chapter_text_replaced']}", "",
               "## Most Frequent Character/Subsequence Changes in Translation Corrections", "",
               "| OCR sequence | Corrected sequence | Operation | Count |", "|---|---|---:|---:|"]
    for row in top_confusions:
        report.append(f"| `{row['ocr_sequence']}` | `{row['source_sequence']}` | {row['operation']} | {row['occurrences']} |")
    report += ["", "## Interpretation", "",
        "1. The dictionary stage primarily removes Unicode formatting artifacts and applies a small set of curated changes. It cannot repair a malformed token when the OCR output is absent from the trusted lexicon, has several plausible neighbours, or has been hallucinated as Latin text.",
        "2. Tamil glyph errors are contextual and many-to-many. The same visible glyph may become different Unicode sequences, while valid case endings and sandhi resemble one-edit OCR errors. Global edit-distance replacement is therefore unsafe.",
        "3. Word-boundary damage is common: OCR inserts or removes spaces inside inflected words and across line endings. Token dictionaries cannot recover these reliably without line and sentence context.",
        "4. Latin hallucinations arise where Tamil glyph clusters are interpreted as short Roman strings. Genuine English in the letters means script detection is a review signal, not a deletion rule.",
        "5. Targeted re-OCR occasionally recovers the source form but the stored variants do not converge consistently. It is useful as supporting evidence, not as an automatic authority.",
        "6. The translation Tamil copies contain many source-guided repairs, but the residual-suspicion file must still be reviewed before treating them as a fully source-verified gold corpus. Intentional English will appear in that audit.", "",
        f"Recurring source-corrected OCR forms still survive in {len(residual_rows)} chapter/token records in the translation layer. These are evidence for source checking, not permission for global replacement.", "",
        "## Outputs", "",
        "- `chapter_stage_comparison.csv`: chapter-level token metrics.",
        "- `token_change_manifest.csv`: aligned changes for every stage transition.",
        "- `corrected_span_patterns.csv`: recurring v6.4-to-translation span corrections.",
        "- `character_confusion_patterns.csv`: character/subsequence confusion counts.",
        "- `targeted_reocr_comparison.csv`: the 29 stored re-OCR experiments.",
        "- `translation_residual_suspicion.csv`: possible residual Latin, Tamil-number, and control-character signals.",
        "- `learned_pattern_residuals.csv`: recurring corrected OCR forms that still survive in a translation Tamil copy.",
    ]
    (out / "ocr_corruption_pattern_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
