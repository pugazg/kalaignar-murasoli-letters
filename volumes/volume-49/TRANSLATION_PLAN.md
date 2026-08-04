# English Translation Plan — Kalaignar's Murasoli Letters

## Objective

Create a clear, faithful English translation that carries Kalaignar's argument, political judgement, irony, direct address, evidence and emotional emphasis into English without turning the letters into literary adaptations.

The translation must help an English reader understand **what Kalaignar is thinking, why he cites particular facts, how he builds his case, and where he uses sarcasm or rhetorical questions**.

## Translation principles

1. **Thought before ornament** — preserve the sequence of Kalaignar's reasoning. Do not beautify, dramatise or rewrite for elegance.
2. **No summarising** — every substantive statement, list, quotation and rhetorical question must be translated.
3. **Direct but natural English** — avoid word-for-word Tamil syntax when it obscures meaning, but do not add interpretation that is absent from the source.
4. **Preserve the political voice** — retain criticism, irony, repetition, exclamation, accusation, contrast and direct questions.
5. **Preserve quoted voices** — newspaper reports, interviews and speeches remain visibly quoted. Colloquial speech may become natural spoken English, but its claims and tone must not be softened.
6. **Preserve names and institutions** — use established English forms where clear; otherwise transliterate. Party abbreviations such as DMK and AIADMK are retained.
7. **Preserve Indian public-language units** — `lakh` and `crore` are retained. A glossary explains them once.
8. **Do not silently correct the source** — source anomalies, unusual spellings and dates remain documented. Translation may clarify meaning in a note but must not replace the archival Tamil.
9. **Minimal notes** — notes are used only for an untranslatable term, source anomaly, historical institutional name or ambiguity that affects meaning.
10. **Traceability** — every translation records the source PDF range and links to the canonical Tamil page files.

## Recurrent terms

- `உடன்பிறப்பே` is retained as **Udanpirappē**. It is Kalaignar's distinctive movement address, combining kinship and political fellowship; no single English word carries the full sense.
- `அன்புள்ள, மு.க.` is rendered **With affection, M.K.**
- `கழகம்`, when it clearly refers to the DMK, is rendered **the DMK** or **the movement**, according to context; it is not mechanically translated as “organisation”.
- `ஆட்சி` is rendered **government**, **rule** or **regime** according to the force of the sentence.

## File structure

```text
volumes/volume-49/translations/en/
  README.md
  PROGRESS.md
  GLOSSARY.md
  letters/
    3764-what-was-left-out-of-the-list-of-achievements.md
    ...
```

Each letter file contains:

- Tamil and English titles
- date and source page range
- links to canonical Tamil pages
- complete English translation
- only necessary translator's notes
- review status

## Workflow

### Phase 1 — Pilot and style lock

Translate letters 3764–3766 individually. Review title style, `Udanpirappē`, quotations, party terminology, rhetorical questions and notes. Freeze the style guide after the pilot.

### Phase 2 — Main translation

Translate in batches of five letters, while keeping one file per letter. Each batch receives:

- source-completeness check
- paragraph and quotation check
- names, dates and figures check
- title and closing check
- glossary update

### Phase 3 — Bilingual alignment QA

For every letter, compare the Tamil and English paragraph sequence and verify that no list item, quotation, number or rhetorical question was omitted.

### Phase 4 — English editorial review

Improve clarity only where the English is awkward. No change may alter political meaning, intensity, responsibility, uncertainty or attribution.

### Phase 5 — Volume release

Generate a complete Volume 49 English index, translation manifest and review report. The Tamil transcription remains the canonical source.

## Status labels

- `draft-translated` — full translation exists; not yet independently reviewed
- `source-checked` — checked against all canonical Tamil pages
- `reviewed` — meaning, tone, quotations and English readability checked
- `verified` — final bilingual alignment completed
