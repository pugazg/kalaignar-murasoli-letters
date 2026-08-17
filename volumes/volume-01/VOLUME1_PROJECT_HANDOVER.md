# Volume 1 — Project Handover

## Repository

`pugazg/kalaignar-murasoli-letters`

Work on `main`.

## Active work

Canonical migration/release preparation of **Murasoli Letters — Volume 1** under:

`volumes/volume-01/`

Legacy preserved tree:

`volumes/volume-1/`

The legacy tree contains 110 bilingual records and remains preserved as migration evidence. Do not rewrite it.

## Controlling source

The supplied **`Vol1.pdf` scan** is authoritative for this edition.

- SHA-256: `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`
- size: 244,892,260 bytes
- PDF pages: 401
- publisher-stated printed pages: 400
- edition: first edition, 2022
- publisher: Seethai Pathippagam
- usable searchable text layer: none

Do not commit the PDF.

## Mandatory startup in a new window

Before making any repository change, read completely:

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
13. all existing `volumes/volume-01/translations/en/SOURCE_CHECK_*.md` reports

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or older status paragraphs.

## Completed Tamil gates — do not restart

Volume 1 Tamil work is complete:

- canonical Tamil migration: **401 / 401 PDF pages**
- letters: **110 / 110** (`0001–0110`)
- full-volume structural audit: **PASS**
- second visual/textual-fidelity verification: **PASS — PDF 001–401 / 401**
- second-pass corrections: **159 canonical pages / 274 spans**
- PDF 401 is a non-letter back cover
- legacy bilingual records remain **110 / 110** under `volumes/volume-1/`

Do not restart Tamil migration, structural audit, or the completed full-volume fidelity pass.

## Active English migration gate

Canonical English migration is now the active gate.

Previously completed and source-checked canonical English range:

- **0001–0070 / 110**

In the current session, canonical English records **0071–0075** were additionally created/source-checked on `main`:

- 0071 — `காலக் கருவூலம்!` / *A Treasury of Time!* — PDF 277–278
- 0072 — `ஒன்று சொல்க!` / *Tell Them One Thing!* — PDF 279–280
- 0073 — `புன்னகையும் பெருமூச்சும்!` / *A Smile and a Sigh!* — PDF 281–282
- 0074 — `குறள் மறவோம்!` / *Let Us Not Forget the Kural!* — PDF 283–284
- 0075 — `உன் எதிரே!` / *Before You!* — PDF 285–286

These records use the verified canonical Tamil and preserved legacy English as migration evidence. They retain Kalaignar's thought order, rhetoric and political language and include the Tamil witness in the canonical bilingual record.

At this handover boundary, **0076–0080 have not yet been canonically migrated**. A batch-level `SOURCE_CHECK_0071_0080.md` has also not yet been created, and `PROGRESS.md` still records the prior completed batch boundary of 0070. The next window must finish 0076–0080 and only then close/synchronise the 0071–0080 batch.

## Exact next activity

Continue canonical English migration with **letters 0076–0080**:

- 0076 — `தட்டிக் கேட்கலாமா?` — PDF 287–288
- 0077 — `பெரியாரின் வெற்றி!` — PDF 289–290
- 0078 — `நம்மை வென்றாரா?` — PDF 291–292
- 0079 — `இருபதாயிரம் பாடி வீடுகள்!` — PDF 293–295
- 0080 — `கொள்கை மலர்கள்` — PDF 296–297

For each record:

1. treat verified canonical Tamil pages/chapters and the controlling scan as authoritative;
2. use the corresponding legacy `volumes/volume-1/translations/en/letters/m1-l00xx.en.md` only as a reusable draft/evidence;
3. source-check for omissions, mistranslations, OCR-derived errors, title/date errors, rhetorical flattening and altered political terminology;
4. preserve Kalaignar's voice, thought order, repetition, metaphors and movement vocabulary;
5. retain `Udanpirappē` where established by the project convention;
6. include the full canonical Tamil witness in the bilingual canonical record;
7. mark `translation_status: source-checked` and `quality_controls.source_checked: true` only after the check;
8. leave `bilingual_alignment_checked: false` and `editorial_consistency_checked: false` at this gate.

After 0076–0080 are complete:

- create `volumes/volume-01/translations/en/SOURCE_CHECK_0071_0080.md` covering the full ten-letter batch;
- update `PROGRESS.md` from 70 to **80 / 110** only after all ten records are confirmed present/source-checked;
- update `AUDIT.md`, Volume 1 `README.md`, translation indexes/manifests if the established previous batches require them, and root status only where the repository's current conventions require it;
- inspect current `main` before every write so concurrent work is not overwritten;
- commit coherent changes directly to `main`.

## Important source notes in this batch

- 0071 contains an English medicine ingredient list and mixed Tamil-English forms; preserve source-supported forms.
- 0072 contains Bharathidasan verse; preserve source-controlled verse structure and rhetoric.
- 0074 closes with a Thirukkural; preserve the Tamil couplet and translate for meaning without replacing the source witness.
- 0076 is built around the three-sons / Sixth Finance Commission analogy.
- 0077 and 0078 are consecutive reflections on Periyar; do not flatten their distinct arguments.
- 0079 uses `பாடி வீடுகள்` as a martial metaphor for branch organisations/camps; preserve the governing metaphor rather than neutralising it.
- 0080 uses the closing `கொள்கை மலர்கள்` / flowers-of-principle image.

## Gates still blocked

Do **not** begin yet:

- bilingual alignment;
- volume-level editorial consistency review;
- final translation manifest/release report;
- final release declaration.

Those begin only after all **110 / 110** canonical English records have completed the source-check migration gate.
