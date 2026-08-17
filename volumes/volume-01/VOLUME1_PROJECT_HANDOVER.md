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

Canonical English migration/source checking is now complete through:

- **0001–0080 / 110**

The ten-letter batch **0071–0080** is closed and documented in:

`volumes/volume-01/translations/en/SOURCE_CHECK_0071_0080.md`

All canonical English records through 0080 are `source-checked`, not `verified`. They include the full canonical Tamil witness. Bilingual alignment and editorial consistency remain later gates.

The completed 0071–0080 batch includes:

- 0071 — `காலக் கருவூலம்!` — PDF 277–278
- 0072 — `ஒன்று சொல்க!` — PDF 279–280
- 0073 — `புன்னகையும் பெருமூச்சும்!` — PDF 281–282
- 0074 — `குறள் மறவோம்!` — PDF 283–284
- 0075 — `உன் எதிரே!` — PDF 285–286
- 0076 — `தட்டிக் கேட்கலாமா?` — PDF 287–288
- 0077 — `பெரியாரின் வெற்றி!` — PDF 289–290
- 0078 — `நம்மை வென்றாரா?` — PDF 291–292
- 0079 — `இருபதாயிரம் பாடி வீடுகள்!` — PDF 293–295
- 0080 — `கொள்கை மலர்கள்` — PDF 296–297

Important semantic/source decisions in the just-closed batch:

- 0076 retains the three-sons analogy and Sixth Finance Commission argument.
- 0077 retains the mother/child analogy and the distinction between Periyar's objective and method.
- 0078 retains the self-critical caste turn and the question whether Periyar has truly won over those who profess agreement.
- 0079 retains `பாடி வீடுகள்` as a martial camps metaphor rather than neutralising it into administrative offices; PDF 294 controls `அறை கூவல்`, `நியாய நெஞ்சும்` and `வலிப்பு நோய் ஆவான்...`.
- 0080 retains the `கொள்கை மலர்கள்` / victory-garland image for Anna; PDF 297 controls `தன்னலமற்ற-கண்ணயராத`.

## Exact next activity

Continue canonical English migration/source checking with **letters 0081–0090**:

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

For each record:

1. treat the verified canonical Tamil pages/chapters and controlling scan as authoritative;
2. use the corresponding legacy `volumes/volume-1/translations/en/letters/m1-l00xx.en.md` only as reusable draft/evidence;
3. source-check for omissions, mistranslations, OCR-derived errors, title/date errors, rhetorical flattening, altered metaphors and political-language drift;
4. preserve Kalaignar's voice, thought order, repetition, metaphors and movement vocabulary;
5. retain `Udanpirappē` where established by project convention;
6. include the full canonical Tamil witness;
7. use `translation_status: source-checked`, `quality_controls.source_checked: true`, `quality_controls.full_tamil_included: true`;
8. leave `bilingual_alignment_checked: false` and `editorial_consistency_checked: false`.

After 0081–0090 are complete, create `SOURCE_CHECK_0081_0090.md`, update tracking to **90 / 110**, and identify 0091–0100 as the next source-check batch.

## Gates still blocked

Do **not** begin yet:

- bilingual alignment;
- volume-level editorial consistency review;
- final translation manifest/release report;
- final release declaration.

Those begin only after all **110 / 110** canonical English records have completed the source-check migration gate.
