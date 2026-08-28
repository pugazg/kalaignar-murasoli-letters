# Volume 45 English Translation Plan

## Objective

Create a clear, faithful English translation of Volume 45 that preserves Kalaignar's thought order, political judgement, evidence, irony, direct address, repetition, rhetorical questions and emotional emphasis without turning the letters into literary or academic rewrites.

The audited canonical Tamil is the translation source. The controlling scan remains the ultimate textual authority.

## Tamil QA prerequisite

Both Tamil gates are complete and durable for Volume 45:

- full-volume Tamil structural audit: **PASS**;
- second full-volume direct visual/textual-fidelity verification: **PASS — PDF 001–402 / 402**.

Because every canonical page has already been directly compared against the controlling scan, translation batches use that audited canonical Tamil. If translation work exposes a possible Tamil discrepancy, stop on that point and re-check the scan before changing either layer.

## Mandatory translator’s note and bilingual order

Every translated letter must place the following note immediately below the English title, before source metadata or the translated body:

> **Translator’s note**
>
> This translation is intended to carry Kalaignar's voice into clear, contemporary English rather than recast the letter as literary or academic prose. It preserves the source's argument, political directness, rhetorical questions, repetition, irony, factual detail, and paragraph order. Names, dates, figures, quotations, and intentional English expressions are retained. Where Tamil idiom cannot be reproduced literally without sounding unnatural, the English follows its sense and rhetorical force without adding claims absent from the source. The original Tamil is reproduced in full below the translation and remains the authoritative text. `Udanpirappē` is retained in Tamil transliteration rather than flattened into “brother,” “sister,” or “comrade.” Literally evoking “one born alongside me,” Kalaignar uses it as a distinctive address of shared identity, equality, affection, and solidarity within the movement.

Each letter follows this order:

1. YAML source/translation metadata;
2. English title;
3. standard translator’s note;
4. Tamil chapter link, canonical PDF range and date;
5. complete English translation;
6. letter-specific notes only where necessary;
7. **Original Tamil — மூலத் தமிழ்**, reproduced in full from the audited canonical page files in physical page order.

The Tamil section is never a summary or selected extract.

## Translation principles

1. **Thought before ornament** — preserve the sequence of Kalaignar's reasoning.
2. **No summarising** — translate every substantive claim, heading, list, quotation, figure and rhetorical question.
3. **Direct but natural English** — avoid opaque word-for-word syntax without adding interpretation.
4. **Preserve political force** — criticism, praise, irony, accusation, repetition and direct questions remain visible.
5. **Preserve quoted voices and attribution** — newspaper reports, speeches and cited statements remain clearly attributed.
6. **Preserve names, institutions, dates and figures** — no historical correction from outside knowledge.
7. **Retain Indian public-language units** — `lakh` and `crore` are retained.
8. **Do not silently repair source anomalies** — the Tamil remains source-exact; English may use a minimal note where an anomaly affects comprehension.
9. **Minimal notes** — explanatory notes are added only when needed for an institutional term, source anomaly, ambiguity or untranslatable expression.
10. **Traceability** — every translation links to its chapter record and canonical Tamil PDF range.

## Recurrent terms

The working terminology is maintained in [`translations/en/GLOSSARY.md`](translations/en/GLOSSARY.md). Core locked forms include `Udanpirappē`, `With affection, M.K.`, DMK / AIADMK, and `lakh` / `crore`. A glossary entry never overrides wording or an anomaly visible in the audited source.

## File structure

```text
volumes/volume-45/
  TRANSLATION_PLAN.md
  translations/en/
    README.md
    PROGRESS.md
    GLOSSARY.md
    PILOT_REVIEW_3537_3539.md
    DRAFT_SOURCE_CHECK_3540_3544.md
    DRAFT_SOURCE_CHECK_3545_3549.md
    DRAFT_SOURCE_CHECK_3550_3554.md
    DRAFT_SOURCE_CHECK_3555_3559.md
    letters/
      3537-....md
      ...
```

## Workflow

### Phase 1 — Pilot and style lock — COMPLETE

Pilot letters: **3537–3539**, audited canonical PDF **024–049**. Result: **3 / 3 source-checked; PASS — STYLE LOCKED**.

### Phase 2 — Main translation — IN PROGRESS

Post-pilot drafting cadence: **five complete consecutive source letters per normal drafting iteration**, one bilingual Markdown file per letter.

Completed normal drafting iterations:

- **3540–3544 / PDF 050–088** — **5 / 5 source-checked; PASS**.
- **3545–3549 / PDF 089–122** — **5 / 5 source-checked; PASS**.
- **3550–3554 / PDF 123–154** — **5 / 5 source-checked; PASS**.
- **3555–3559 / PDF 155–180** — **5 / 5 source-checked; PASS**.

Current cumulative drafting state: **3537–3559 / 23 of 55 source-checked**, audited canonical PDF **024–180**.

**Exact next drafting batch: Letters 3560–3564 / PDF 181–217.**

Each drafting batch receives source-completeness/canonical-page coverage, paragraph/heading coverage, names/dates/figures/units, quotation/rhetorical-question, title/closing, glossary and progress/handover checks.

### Phase 3 — Bilingual alignment QA

After draft translation, compare each English record directly against the authoritative audited Tamil. Correct omission, addition or semantic drift before marking a letter verified.

### Phase 4 — English editorial consistency review

Perform a separate volume-level consistency pass only after bilingual alignment. Improve English readability without changing political meaning, intensity, responsibility, uncertainty or attribution.

### Phase 5 — Volume release

Prepare the complete English index, translation manifest, editorial review and final release report. Tamil remains canonical.

## Status labels

- `draft-translated` — a complete English draft exists;
- `source-checked` — the English has been checked for coverage against all audited canonical Tamil pages for that letter;
- `reviewed` — English meaning, tone and readability have passed editorial review;
- `verified` — final bilingual alignment is complete.

Letters **3537–3559** are currently **source-checked** drafts. They are not yet final bilingual-alignment/release records.
