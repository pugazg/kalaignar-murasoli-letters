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

Canonical English source-check migration was complete through **0070 / 110** before the latest session.

The latest session additionally created/source-checked canonical English records **0071–0075**. Treat those as completed unless current `main` proves otherwise. Do not redo them.

`PROGRESS.md` may still show 0070 because the ten-letter 0071–0080 batch has not yet been closed. `SOURCE_CHECK_0071_0080.md` does not yet exist at the handover boundary.

## EXACT NEXT ACTIVITY

Complete the remaining half of the current English batch: **letters 0076–0080**.

- 0076 — `தட்டிக் கேட்கலாமா?` — PDF 287–288
- 0077 — `பெரியாரின் வெற்றி!` — PDF 289–290
- 0078 — `நம்மை வென்றாரா?` — PDF 291–292
- 0079 — `இருபதாயிரம் பாடி வீடுகள்!` — PDF 293–295
- 0080 — `கொள்கை மலர்கள்` — PDF 296–297

Use the corresponding legacy English records under:

`volumes/volume-1/translations/en/letters/`

only as reusable drafts/evidence. The verified canonical Tamil and controlling scan are authoritative.

For every letter, source-check the English against the canonical Tamil for omissions, mistranslations, OCR-derived errors, title/date errors, altered metaphors, rhetorical flattening and political-language drift. Preserve Kalaignar's language, thought order, repetition, imagery and movement vocabulary. Retain `Udanpirappē` under the established project convention. Include the full canonical Tamil witness in each canonical bilingual record.

At this gate use:

- `translation_status: source-checked`
- `quality_controls.source_checked: true`
- `quality_controls.full_tamil_included: true`
- `quality_controls.bilingual_alignment_checked: false`
- `quality_controls.editorial_consistency_checked: false`

Do not mark any record `verified` yet.

Important semantic cautions:

- 0076: retain the three-sons analogy and its Sixth Finance Commission argument.
- 0077: retain Kalaignar's mother/child analogy and the distinction between Periyar's objective and methods.
- 0078: retain the self-critical turn — the question is whether Periyar has truly won over those who profess agreement while caste remains embedded in everyday conduct.
- 0079: `பாடி வீடுகள்` is a governing martial metaphor for the movement's branch organisations/camps; do not neutralise it into merely administrative offices.
- 0080: preserve the closing image of office-bearers as `கொள்கை மலர்கள்`, gathered into a victory garland for Anna.

## BATCH CLOSURE AFTER 0080

Only after all canonical English records **0071–0080** are confirmed present and source-checked:

1. create `volumes/volume-01/translations/en/SOURCE_CHECK_0071_0080.md`;
2. update `PROGRESS.md` to **80 / 110** canonical English records/source-checked;
3. synchronise `AUDIT.md`, Volume 1 `README.md`, translation indexes/manifests and root status where current repository conventions require it;
4. verify all ten files 0071–0080 have `full_tamil_included: true` and the later-gate flags remain false;
5. commit coherent changes directly to `main`.

## DO NOT START YET

Do not begin:

- letters 0081 onward until the 0071–0080 batch is properly closed;
- bilingual alignment;
- volume-level editorial consistency review;
- final translation manifest/release report;
- final release declaration.

Those later gates remain blocked until the canonical English source-check migration reaches **110 / 110**.

Proceed directly with the work; do not merely describe what should be done.
