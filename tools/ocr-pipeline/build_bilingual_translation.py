#!/usr/bin/env python3
"""Combine a separate English translation with its unchanged Tamil source."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


NOTE = """## Translator's Note

This translation is intended to carry Kalaignar's voice into clear, contemporary English rather than recast the letter as literary or academic prose. It preserves the source's argument, political directness, rhetorical questions, repetition, irony, factual detail, and paragraph order. Names, dates, figures, quotations, and intentional English expressions are retained. Where Tamil idiom cannot be reproduced literally without sounding unnatural, the English follows its sense and rhetorical force without adding claims absent from the source. The original Tamil is reproduced in full below the translation and remains the authoritative text.

`Udanpirappē` is retained in Tamil transliteration rather than flattened into “brother,” “sister,” or “comrade.” Literally evoking “one born alongside me,” Kalaignar uses it as a distinctive address of shared identity, equality, affection, and solidarity within the movement.
"""


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--translation", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()

    before = digest(args.source)
    english = args.translation.read_text(encoding="utf-8").strip()
    tamil = args.source.read_text(encoding="utf-8").strip()
    english_lines = english.splitlines()
    title = english_lines[0]
    english_body = "\n".join(english_lines[1:]).strip()

    combined = (
        f"{title}\n\n{NOTE.strip()}\n\n"
        "## English Translation\n\n"
        f"{english_body}\n\n"
        "---\n\n"
        "## Original Tamil\n\n"
        f"{tamil}\n"
    )
    args.translation.write_text(combined, encoding="utf-8")
    after = digest(args.source)
    if before != after:
        raise SystemExit("Source Tamil changed unexpectedly")
    print(f"bilingual translation written: {args.translation}")
    print(f"source Tamil unchanged: sha256 {after}")


if __name__ == "__main__":
    main()
