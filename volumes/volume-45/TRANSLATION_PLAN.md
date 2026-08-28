# Volume 45 English Translation Plan

## Objective

Create a clear, faithful English translation of Volume 45 that preserves Kalaignar's thought order, political judgement, evidence, irony, direct address, repetition, rhetorical questions and emotional emphasis without turning the letters into literary or academic rewrites.

The audited canonical Tamil is the translation source. The controlling scan remains the ultimate textual authority.

## Tamil QA prerequisite

Both Tamil gates are complete and durable for Volume 45:

- full-volume Tamil structural audit: **PASS**;
- second full-volume direct visual/textual-fidelity verification: **PASS — PDF 001–402 / 402**.

The completed second-pass audit is recorded in [`FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md). Because every canonical page has already been directly compared against the controlling scan, translation batches use that audited canonical Tamil. If translation work exposes a possible Tamil discrepancy, stop on that point and re-check the scan before changing either layer.

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
7. **Retain Indian public-language units** — `lakh` and `crore` are retained and explained in the glossary.
8. **Do not silently repair source anomalies** — the Tamil remains source-exact; English may use a minimal note where an anomaly affects comprehension.
9. **Minimal notes** — explanatory notes are added only when needed for an institutional term, source anomaly, ambiguity or untranslatable expression.
10. **Traceability** — every translation links to its chapter record and canonical Tamil PDF range.

## Recurrent terms locked for Volume 45

- `உடன்பிறப்பே` → **Udanpirappē**.
- `அன்புள்ள, மு.க.` → **With affection, M.K.**
- `திராவிட முன்னேற்றக் கழகம் / தி.மு.க.` → **Dravida Munnetra Kazhagam (DMK)** / **DMK**.
- `அனைத்திந்திய அண்ணா திராவிட முன்னேற்றக் கழகம் / அ.தி.மு.க.` → **All India Anna Dravida Munnetra Kazhagam (AIADMK)** / **AIADMK**.
- `கழகம்` → **the DMK** or **the movement**, according to context.
- `லட்சம்` / `கோடி` → **lakh** / **crore**.
- `ஊரக வளர்ச்சி மற்றும் ஊராட்சித் துறை` → **Rural Development and Panchayat Raj Department**.
- `மக்கள் நல்வாழ்வு மற்றும் குடும்ப நலத்துறை` → **Health and Family Welfare Department**.
- Scheme names that function as proper names may be retained in transliteration on first use with a concise English identification where useful.

The working glossary is maintained at [`translations/en/GLOSSARY.md`](translations/en/GLOSSARY.md).

## File structure

```text
volumes/volume-45/
  TRANSLATION_PLAN.md
  translations/en/
    README.md
    PROGRESS.md
    GLOSSARY.md
    PILOT_REVIEW_3537_3539.md
    letters/
      3537-rural-development-and-panchayat-raj-five-year-achievements-2.md
      3538-rural-development-and-panchayat-raj-five-year-achievements-3.md
      3539-health-and-family-welfare-five-year-achievements-1.md
      ...
```

## Workflow

### Phase 1 — Pilot and style lock

Pilot letters: **3537–3539**, covering audited canonical PDF **024–049**.

The pilot tests:

- title treatment, including numbered/continuation titles;
- `Udanpirappē` and the `With affection, M.K.` closing;
- government-department and scheme terminology;
- dense statistics, lists and monetary figures;
- source headings and parenthetical continuation markers;
- minimal explanatory notes;
- full-Tamil reproduction in every bilingual file.

The pilot is complete in the same initialization checkpoint as this plan. Its review is recorded in [`translations/en/PILOT_REVIEW_3537_3539.md`](translations/en/PILOT_REVIEW_3537_3539.md). The style is therefore **LOCKED** for the main drafting phase, subject only to source-specific glossary additions or scan-proven corrections.

### Phase 2 — Main translation

After the three-letter pilot, translate **five complete consecutive letters per atomic drafting iteration**, keeping one bilingual Markdown file per letter.

The exact next drafting batch is **Letters 3540–3544**.

Each batch receives:

- source-completeness / canonical-page coverage check;
- paragraph and heading coverage check;
- names, dates, figures and units check;
- quotation and rhetorical-question check;
- title, continuation marker and closing check;
- glossary update where required;
- progress/handover update.

### Phase 3 — Bilingual alignment QA

After draft translation, compare each English record directly against the authoritative audited Tamil. Check semantic coverage, paragraph order, headings, names, dates, figures, quotations, lists, rhetoric, repetitions and closing. Correct omission, addition or semantic drift before marking a letter verified.

### Phase 4 — English editorial consistency review

Perform a separate volume-level consistency pass only after bilingual alignment. Improve English readability without changing political meaning, intensity, responsibility, uncertainty or attribution.

### Phase 5 — Volume release

Prepare the complete English index, translation manifest, editorial review and final release report. Tamil remains canonical.

## Status labels

- `draft-translated` — a complete English draft exists;
- `source-checked` — the English has been checked for coverage against all audited canonical Tamil pages for that letter;
- `reviewed` — English meaning, tone and readability have passed editorial review;
- `verified` — final bilingual alignment is complete.

The initial pilot letters 3537–3539 are committed as **source-checked** drafts. They are not yet final bilingual-alignment/release records.
