# Volume 1 — Next Chat Prompt

Copy the prompt below into a new window.

---

Continue the **Kalaignar Murasoli Letters — Volume 1 canonical English migration** directly in:

`pugazg/kalaignar-murasoli-letters`

Work on `main`.

Active canonical tree:

`volumes/volume-01/`

Legacy preserved tree:

`volumes/volume-1/`

The supplied `Vol1.pdf` scan remains the controlling source for this edition.

## MANDATORY STARTUP

Before making any repository change, read these files completely:

1. `VOLUME_PROCESSING_GUIDE.md`
2. `TRANSCRIPTION_GUIDE.md`
3. `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
4. `FUTURE_VOLUME_WORK_GUIDELINES.md`
5. root `PROJECT_HANDOVER.md`
6. `volumes/volume-01/VOLUME1_MIGRATION_GUIDELINES.md`
7. `volumes/volume-01/VOLUME1_PROJECT_HANDOVER.md`
8. `volumes/volume-01/README.md`
9. `volumes/volume-01/PROGRESS.md`
10. `volumes/volume-01/AUDIT.md`
11. `volumes/volume-01/metadata.yml`
12. `volumes/volume-01/chapters/README.md`
13. existing `volumes/volume-01/translations/en/SOURCE_CHECK_*.md` reports

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or historical status paragraphs. Confirm whether any work beyond the recorded boundary has already been committed; if so, continue it and do not duplicate or overwrite it.

## COMPLETED WORK — DO NOT RESTART

Tamil Volume 1 is complete:

- canonical Tamil migration: **401 / 401 PDF pages**
- letters: **110 / 110**
- structural audit: **PASS**
- second visual/textual-fidelity verification: **PASS — 401 / 401**
- legacy bilingual records preserved: **110 / 110**

Do not restart Tamil migration, structural audit or full-volume fidelity verification.

Canonical English source-check migration is complete through **0090 / 110**. The closed ten-letter batch **0081–0090** is documented in `volumes/volume-01/translations/en/SOURCE_CHECK_0081_0090.md`.

## EXACT NEXT ACTIVITY

Migrate and source-check **letters 0091–0100**:

- 0091 — `நமது விழாக்கள்!` — PDF 326–327
- 0092 — `பயணம் தொடரட்டும்!` — PDF 328–329
- 0093 — `பிறந்த நாள் விழாவும் மறந்த சில விவரங்களும்!` — PDF 330–334
- 0094 — `நேரமும் நினைப்பும்!` — PDF 335–338
- 0095 — `‘மாம்பழ மங்கை!’` — PDF 339–342
- 0096 — `அதே தேதிகள்!` — PDF 343–344
- 0097 — `இன்றே தயாராகு!` — PDF 345–346
- 0098 — `உயர்த்திடுவோம் தோள்!` — PDF 347–350
- 0099 — `வழி மேல் விழி...` — PDF 351–353
- 0100 — `அழைக்கிறேன் - வா! அன்பே வா!` — PDF 354–358

Use corresponding legacy English records under `volumes/volume-1/translations/en/letters/` only as reusable drafts/evidence. The verified canonical Tamil and controlling scan are authoritative.

For every letter, source-check for omissions, mistranslations, OCR-derived errors, title/date errors, altered metaphors, rhetorical flattening and political-language drift. Preserve Kalaignar's language, thought order, repetition, imagery and movement vocabulary. Retain `Udanpirappē` under the established project convention. Include the full canonical Tamil witness.

At this gate use:

- `translation_status: source-checked`
- `quality_controls.source_checked: true`
- `quality_controls.full_tamil_included: true`
- `quality_controls.bilingual_alignment_checked: false`
- `quality_controls.editorial_consistency_checked: false`

Do not mark any record `verified` yet.

## BATCH CLOSURE AFTER 0100

Only after all canonical English records **0091–0100** are confirmed present and source-checked:

1. create `volumes/volume-01/translations/en/SOURCE_CHECK_0091_0100.md`;
2. update progress to **100 / 110** canonical English records/source-checked;
3. synchronise Volume 1 tracking and root status where current conventions require it;
4. verify all ten files have `full_tamil_included: true` and later-gate flags remain false;
5. commit coherent changes directly to `main`.

## DO NOT START YET

Do not begin:

- letters 0101 onward until the 0091–0100 batch is properly closed;
- bilingual alignment;
- volume-level editorial consistency review;
- final translation manifest/release report;
- final release declaration.

Those later gates remain blocked until the canonical English source-check migration reaches **110 / 110**.

Proceed directly with the work; do not merely describe what should be done.
