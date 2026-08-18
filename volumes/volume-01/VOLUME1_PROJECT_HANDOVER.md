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

- **0001–0090 / 110**

The ten-letter batch **0081–0090** is closed and documented in:

`volumes/volume-01/translations/en/SOURCE_CHECK_0081_0090.md`

All canonical English records through 0090 are `source-checked`, not `verified`. They include the full canonical Tamil witness. Bilingual alignment and editorial consistency remain later gates.

The completed 0081–0090 batch includes:

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

Important semantic/source decisions in the just-closed batch:

- 0081 retains the Rajamannar / Sezhiyan–Maran sequence, 8,226-word report and banyan-seed metaphor for state autonomy.
- 0082 retains the Pongal stove/pot metaphor and the shield / bow-and-arrow warning; PDF 301 controls `“நல்லவர்”(?)களுக்கும்`.
- 0083 retains the campaign-headline sequence, repeated `ஊழல்` rhetoric and cadre-as-`படைக்கருவி` martial image.
- 0084 retains the budget argument and the flour/sweet, rain-cloud, sun and storm-boat images; `திருவள்ளுவர் ஆலயம்` is rendered directly as a Thiruvalluvar shrine.
- 0085 retains the internal-election principle that the contest is not ideological conflict and every movement flower remains a rose.
- 0086 retains the Chicago/May Day history, labour measures, `சமதர்ம சங்கீதம்` satire and rights/friendship pledge.
- 0087 retains the railway-strike negotiation argument, Centre/State authority contrast and proposed no-victimisation settlement.
- 0088 retains the anti-extravagance birthday request, three funds, `கழகக் குரல்` and poor-person's-smile sequence.
- 0089 retains the earthen-lamp, equal-pearls, balance-needle and `சிந்தாமல் சிதறாமல்` images.
- 0090 retains the birthday-affection / `கட்டுமரம்` sequence, explicit anti-violence position, *அலைஓசை* passage and Kamaraj “cool breeze” satire; PDF 325 controls `காமராசரின்`.

## Exact next activity

Continue canonical English migration/source checking with **letters 0091–0100**:

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

Use the corresponding legacy `volumes/volume-1/translations/en/letters/m1-l00xx.en.md` only as reusable draft/evidence. The verified canonical Tamil pages/chapters and controlling scan remain authoritative.

For each record:

1. source-check for omissions, mistranslations, OCR-derived errors, title/date errors, rhetorical flattening, altered metaphors and political-language drift;
2. preserve Kalaignar's voice, thought order, repetition, metaphors and movement vocabulary;
3. retain `Udanpirappē` where established by project convention;
4. include the full canonical Tamil witness;
5. use `translation_status: source-checked`, `quality_controls.source_checked: true`, `quality_controls.full_tamil_included: true`;
6. leave `bilingual_alignment_checked: false` and `editorial_consistency_checked: false`.

After 0091–0100 are complete, create `SOURCE_CHECK_0091_0100.md`, update tracking to **100 / 110**, and identify 0101–0110 as the final source-check batch.

## Gates still blocked

Do **not** begin yet:

- bilingual alignment;
- volume-level editorial consistency review;
- final translation manifest/release report;
- final release declaration.

Those begin only after all **110 / 110** canonical English records have completed the source-check migration gate.
