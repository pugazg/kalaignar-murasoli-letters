# Volume 1 — Next Chat Prompt

Copy the prompt below into a new window.

---

Continue the **Kalaignar Murasoli Letters — Volume 1 canonical English review** directly in:

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
13. all `volumes/volume-01/translations/en/SOURCE_CHECK_*.md` reports
14. `volumes/volume-01/translations/en/README.md`
15. `volumes/volume-01/translations/en/PROGRESS.md`

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or historical status paragraphs. If bilingual-alignment work has already been started beyond the recorded boundary, continue it rather than duplicating or overwriting it.

## COMPLETED WORK — DO NOT RESTART

Tamil Volume 1 is complete:

- canonical Tamil migration: **401 / 401 PDF pages**
- letters: **110 / 110**
- structural audit: **PASS**
- second visual/textual-fidelity verification: **PASS — 401 / 401**
- legacy bilingual records preserved: **110 / 110**

Canonical English migration/source checking is also complete:

- canonical English records: **110 / 110**
- source-checked records: **110 / 110**
- completed canonical range: **0001–0110**
- final source-check report: `volumes/volume-01/translations/en/SOURCE_CHECK_0101_0110.md`

Do not restart Tamil migration, structural audit, full-volume fidelity verification or English source-check migration.

All canonical English records remain `source-checked`, not final/release-ready. They include the full canonical Tamil witness. At source-check closure their later-gate flags remain:

- `quality_controls.bilingual_alignment_checked: false`
- `quality_controls.editorial_consistency_checked: false`

## EXACT NEXT ACTIVITY — BILINGUAL ALIGNMENT

Begin the dedicated **bilingual alignment review** across canonical English letters **0001–0110**.

For each canonical record:

1. compare the English translation directly with the complete `Original Tamil — மூலத் தமிழ்` witness and the canonical chapter/page evidence where necessary;
2. verify sentence/paragraph correspondence, omissions, additions, quotation boundaries, figures, names, dates, metaphors, rhetorical questions, political terminology and repeated language;
3. preserve Kalaignar's thought order, rhetorical force, imagery and movement vocabulary;
4. retain `Udanpirappē` under the established project convention;
5. do not modernise, normalise, reconstruct or infer unsupported Tamil;
6. correct only demonstrable English/Tamil correspondence errors;
7. after a record passes, set `quality_controls.bilingual_alignment_checked: true`;
8. keep `quality_controls.editorial_consistency_checked: false` until the later volume-level editorial-consistency gate.

Do not treat a source-checked record as automatically bilingual-aligned. Record the alignment work according to the established repository workflow and update progress only for records actually checked.

## GATES STILL BLOCKED

Do not begin yet:

- volume-level editorial consistency review;
- final translation manifest;
- final release report;
- final release declaration.

Those remain later gates after bilingual alignment is complete.

Proceed directly with the bilingual-alignment work; do not merely describe what should be done.