# Volume 1 — Project Handover

## Repository

`pugazg/kalaignar-murasoli-letters`

Work on `main`.

Active canonical tree:

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
8. `volumes/volume-01/BILINGUAL_ALIGNMENT_HANDOVER.md`
9. `volumes/volume-01/README.md`
10. `volumes/volume-01/PROGRESS.md`
11. `volumes/volume-01/AUDIT.md`
12. `volumes/volume-01/metadata.yml`
13. `volumes/volume-01/chapters/README.md`
14. all `volumes/volume-01/translations/en/SOURCE_CHECK_*.md` reports
15. `volumes/volume-01/translations/en/README.md`
16. `volumes/volume-01/translations/en/PROGRESS.md`
17. `volumes/volume-01/translations/en/alignment/PROGRESS.md`
18. `volumes/volume-01/translations/en/alignment/ALIGNMENT_MANIFEST.csv`
19. existing `volumes/volume-01/translations/en/alignment/ALIGNMENT_*.md` reports

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or older status paragraphs. If bilingual-alignment work exists beyond the recorded boundary, continue it instead of duplicating it.

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

## Completed English source-check gate — do not restart

Canonical English migration/source checking is complete:

- **0001–0110 / 110** canonical records migrated
- **110 / 110** source-checked
- each canonical record contains the complete canonical Tamil witness
- all records remain `source-checked`, not `verified`
- volume-level editorial consistency and final release work remain later gates

The final source-check batch **0101–0110** is closed in `volumes/volume-01/translations/en/SOURCE_CHECK_0101_0110.md`. Earlier source-check reports remain authoritative evidence for their respective batches.

Important retained source controls include:

- 0002 complete Kamaraj Deepavali quotation from PDF 030;
- 0010 scan-supported **Runner Cup** (`ரன்னர்`), not stale legacy `Rainer`;
- 0018 deliberate source censorship preserved without reconstruction;
- 0019 scan-visible PDF-099 material restored, including Anna's `ரத்தத்தின் ரத்தம் / சதையின் சதை` reply and Morarji Desai's Hindi statement;
- 0028 source-printed date **28-12-1968** retained over conflicting legacy metadata;
- 0036 `சி. பி. சி.` / `C. P. C.` left unexpanded;
- 0048 printed `சென்னை. / 10.10.1972` retained without inferred composition date;
- 0063 left undated because the source prints no date;
- 0070 printed English judicial quotation retained verbatim;
- 0109 actual PDF-392 heading `அவள் ஒரு தொடர்கதை!` controls over the contents variant, and opaque `நமப்பார்வதி பதேக்கள்!` remains unreconstructed;
- 0110 preserves the full 1949 *கயிற்றில் தொங்கிய கணபதி* quotation and closes on PDF 400 with `(01-12-1974)`.

## Active gate — bilingual alignment

Bilingual alignment is **in progress**.

Completed batches:

- **0001–0010** — PDF **024–066** — PASS — 0 English prose corrections
- **0011–0020** — PDF **067–104** — PASS after 1 English prose correction

Current totals:

- alignment-reviewed and PASS: **20 / 110**
- completed alignment range: **0001–0020**
- cumulative alignment-driven English prose corrections: **1**
- verified: **0 / 110**
- editorially reviewed: **0 / 110**

Authoritative alignment records:

- `volumes/volume-01/translations/en/alignment/ALIGNMENT_0001_0010.md`
- `volumes/volume-01/translations/en/alignment/ALIGNMENT_0011_0020.md`
- `volumes/volume-01/translations/en/alignment/ALIGNMENT_MANIFEST.csv`
- `volumes/volume-01/translations/en/alignment/PROGRESS.md`
- `volumes/volume-01/BILINGUAL_ALIGNMENT_HANDOVER.md`

### Alignment correction made in 0014

Tamil contains two consecutive but distinct statements:

1. `முண்டா தட்டுதல்-மீசை முறுக்குதல்-அரசியலுக்கு ஏற்றதல்ல!`
2. `துப்பாக்கி தூக்குதல்-கத்தி எடுத்தல்-காட்டு மிராண்டிகள் கூட கடைப்பிடிக்க அஞ்ச வேண்டிய அரசியல் முறையாகும்!`

The earlier English compressed both into one sentence and extended the stronger armed-violence condemnation to the preceding swagger imagery. The aligned English now preserves the distinction:

- slapping one's thighs / twirling one's moustache — these do not befit politics;
- raising a gun / drawing a knife — these are separately condemned as political methods even savages should fear to adopt.

No other demonstrable English/Tamil correspondence error was found in 0011–0020.

## Alignment bookkeeping convention

Dedicated alignment reports plus `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. When a reviewed record requires no content correction, canonical translation files are not rewritten solely to churn source-check-era frontmatter. When a demonstrable correspondence error exists, the English prose is corrected, as in 0014.

This bookkeeping convention does **not** promote aligned records to `verified` or release-ready status.

## Exact next activity

Proceed with bilingual alignment for canonical English letters **0021–0030**.

For each record:

1. compare English directly against the complete canonical Tamil witness and canonical chapter/page evidence where needed;
2. check substantive coverage, thought order, paragraph/quotation correspondence, names, dates, figures, lists, metaphors, rhetorical questions, repetition, political terminology, attribution and closing integrity;
3. preserve Kalaignar's voice, directness, rhetorical force, imagery and movement vocabulary;
4. retain `Udanpirappē` under the established project convention;
5. do not modernise, normalise, reconstruct or infer unsupported Tamil;
6. correct only demonstrable English/Tamil correspondence errors;
7. create `translations/en/alignment/ALIGNMENT_0021_0030.md`;
8. append 0021–0030 to `translations/en/alignment/ALIGNMENT_MANIFEST.csv`;
9. advance alignment progress to **30 / 110** only after all ten records pass;
10. update the alignment handover and continuation prompt to the next exact boundary.

## Gates still blocked

Do **not** begin yet:

- volume-level editorial consistency review;
- final translation manifest;
- final release report;
- final release declaration.

Those begin only after bilingual alignment reaches **110 / 110**.