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

Canonical English source-check migration is complete through **0100 / 110**. The closed ten-letter batch **0091–0100** is documented in `volumes/volume-01/translations/en/SOURCE_CHECK_0091_0100.md`.

## EXACT NEXT ACTIVITY

Migrate and source-check the **final Volume 1 source-check batch, letters 0101–0110**:

- 0101 — `உயிரே! உடன்பிறப்பே! வா! வா!` — PDF 359–360
- 0102 — `என் காணிக்கை!` — PDF 361–364
- 0103 — `பார், பார்-இதோ பார்! இந்தியா பார்!` — PDF 365–368
- 0104 — `‘கல்கி’யின் கண்ணோட்டம்!` — PDF 369–373
- 0105 — `‘கல்கி’யின் கண்ணோட்டம் (2)` — PDF 374–379
- 0106 — `‘கல்கி’யின் கண்ணோட்டம்(3)` — PDF 380–383
- 0107 — `வாழ்க-உன் புன்னகை!` — PDF 384–387
- 0108 — `வாண வேடிக்கை!` — PDF 388–391
- 0109 — `அவள் ஒரு தொடர்கதை!` — PDF 392–395
- 0110 — `கயிற்றில் தொங்கிய கணபதி!` — PDF 396–400

Use corresponding legacy English records under `volumes/volume-1/translations/en/letters/` only as reusable drafts/evidence. The verified canonical Tamil and controlling scan are authoritative.

For every letter, source-check for omissions, mistranslations, OCR-derived errors, title/date errors, altered metaphors, rhetorical flattening and political-language drift. Preserve Kalaignar's language, thought order, repetition, imagery and movement vocabulary. Retain `Udanpirappē` under the established project convention. Include the full canonical Tamil witness.

At this gate use:

- `translation_status: source-checked`
- `quality_controls.source_checked: true`
- `quality_controls.full_tamil_included: true`
- `quality_controls.bilingual_alignment_checked: false`
- `quality_controls.editorial_consistency_checked: false`

Do not mark any record `verified` yet.

## BATCH CLOSURE AFTER 0110

Only after all canonical English records **0101–0110** are confirmed present and source-checked:

1. create `volumes/volume-01/translations/en/SOURCE_CHECK_0101_0110.md`;
2. update source-check migration to **110 / 110**;
3. synchronise Volume 1 tracking and root status where current conventions require it;
4. verify all ten files have `full_tamil_included: true` and later-gate flags remain false;
5. close the source-check migration gate;
6. only then identify **bilingual alignment** as the next gate.

## DO NOT START YET

Do not begin, until the final source-check batch is closed:

- bilingual alignment;
- volume-level editorial consistency review;
- final translation manifest/release report;
- final release declaration.

Proceed directly with the work; do not merely describe what should be done.
