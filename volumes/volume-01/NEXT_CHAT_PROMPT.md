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

Canonical English source-check migration is complete through **0080 / 110**. The closed ten-letter batch **0071–0080** is documented in `volumes/volume-01/translations/en/SOURCE_CHECK_0071_0080.md`.

## EXACT NEXT ACTIVITY

Migrate and source-check **letters 0081–0090**:

- 0081 — `தெள்ளிய ஆலின் சிறு பழத்தொரு விதை!` — PDF 298–300
- 0082 — `பொங்கல் உறுதி!` — PDF 301
- 0083 — `காண வருகிறேன் உன்னை!` — PDF 302–304
- 0084 — `‘தொய்வு இல்லை! தொடர்க பயணம்!’` — PDF 305–307
- 0085 — `“எல்லா மலர்களும் ரோஜா மலர்களே!”` — PDF 308–309
- 0086 — `மே தின வாழ்த்து!` — PDF 310–312
- 0087 — `‘நமது நிலை’!` — PDF 313–315
- 0088 — `என் பிறந்த நாளில்...!` — PDF 316–318
- 0089 — `“மறவாதே!”` — PDF 319–321
- 0090 — `கோடையிலே...!` — PDF 322–325

Use corresponding legacy English records under `volumes/volume-1/translations/en/letters/` only as reusable drafts/evidence. The verified canonical Tamil and controlling scan are authoritative.

For every letter, source-check for omissions, mistranslations, OCR-derived errors, title/date errors, altered metaphors, rhetorical flattening and political-language drift. Preserve Kalaignar's language, thought order, repetition, imagery and movement vocabulary. Retain `Udanpirappē` under the established project convention. Include the full canonical Tamil witness.

At this gate use:

- `translation_status: source-checked`
- `quality_controls.source_checked: true`
- `quality_controls.full_tamil_included: true`
- `quality_controls.bilingual_alignment_checked: false`
- `quality_controls.editorial_consistency_checked: false`

Do not mark any record `verified` yet.

## BATCH CLOSURE AFTER 0090

Only after all canonical English records **0081–0090** are confirmed present and source-checked:

1. create `volumes/volume-01/translations/en/SOURCE_CHECK_0081_0090.md`;
2. update progress to **90 / 110** canonical English records/source-checked;
3. synchronise Volume 1 tracking and root status where current conventions require it;
4. verify all ten files have `full_tamil_included: true` and later-gate flags remain false;
5. commit coherent changes directly to `main`.

## DO NOT START YET

Do not begin:

- letters 0091 onward until the 0081–0090 batch is properly closed;
- bilingual alignment;
- volume-level editorial consistency review;
- final translation manifest/release report;
- final release declaration.

Those later gates remain blocked until the canonical English source-check migration reaches **110 / 110**.

Proceed directly with the work; do not merely describe what should be done.
