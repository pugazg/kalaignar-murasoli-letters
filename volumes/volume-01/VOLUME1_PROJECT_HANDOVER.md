# Volume 1 — Project Handover

## Repository

`pugazg/kalaignar-murasoli-letters`

Work on `main`.

Active canonical tree: `volumes/volume-01/`.

Legacy preserved tree: `volumes/volume-1/`.

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
17. `volumes/volume-01/translations/en/alignment/README.md`
18. `volumes/volume-01/translations/en/alignment/PROGRESS.md`
19. `volumes/volume-01/translations/en/alignment/ALIGNMENT_MANIFEST.csv`
20. existing `volumes/volume-01/translations/en/alignment/ALIGNMENT_*.md` reports

Then inspect current GitHub `main`. Repository state is authoritative over stale SHAs or older status paragraphs. If bilingual-alignment work exists beyond the recorded boundary, continue it instead of duplicating it.

## Completed Tamil gates — do not restart

- canonical Tamil migration: **401 / 401 PDF pages**
- letters: **110 / 110** (`0001–0110`)
- full-volume structural audit: **PASS**
- second visual/textual-fidelity verification: **PASS — PDF 001–401 / 401**
- second-pass corrections: **159 canonical pages / 274 spans**
- PDF 401 is a non-letter back cover
- legacy bilingual records remain **110 / 110** under `volumes/volume-1/`

Do not restart Tamil migration, structural audit or the completed full-volume fidelity pass.

## Completed English source-check gate — do not restart

Canonical English migration/source checking is complete:

- **0001–0110 / 110** canonical records migrated
- **110 / 110** source-checked
- each canonical record contains the complete canonical Tamil witness
- all records remain `source-checked`, not `verified`

Important retained source controls include complete Kamaraj material in 0002; **Runner Cup** in 0010; restored PDF-099 material in 0019; source date **28-12-1968** in 0028; unexpanded **C. P. C.** in 0036; printed `சென்னை. / 10.10.1972` in 0048; source figure **6908** in 0054; undated 0063; verbatim printed English judicial quotation in 0070; actual PDF-392 heading and unreconstructed opaque wording in 0109; and the full 1949 quotation through PDF 400 in 0110.

## Active gate — bilingual alignment

Completed batches:

- **0001–0010** — PDF **024–066** — PASS — 0 English prose corrections
- **0011–0020** — PDF **067–104** — PASS after 1 English prose correction
- **0021–0030** — PDF **105–135** — PASS — 0 English prose corrections
- **0031–0040** — PDF **136–177** — PASS — 0 English prose corrections
- **0041–0050** — PDF **178–213** — PASS after 1 English prose correction
- **0051–0060** — PDF **214–249** — PASS after 2 English prose/quotation corrections
- **0061–0070** — PDF **250–276** — PASS — 0 English prose/quotation corrections
- **0071–0080** — PDF **277–297** — PASS — 0 English prose/quotation corrections

Current totals:

- alignment-reviewed and PASS: **80 / 110**
- completed alignment range: **0001–0080**
- cumulative alignment-driven English prose/quotation corrections: **4**
- verified: **0 / 110**
- editorially reviewed: **0 / 110**

Authoritative alignment records:

- `translations/en/alignment/ALIGNMENT_0001_0010.md`
- `translations/en/alignment/ALIGNMENT_0011_0020.md`
- `translations/en/alignment/ALIGNMENT_0021_0030.md`
- `translations/en/alignment/ALIGNMENT_0031_0040.md`
- `translations/en/alignment/ALIGNMENT_0041_0050.md`
- `translations/en/alignment/ALIGNMENT_0051_0060.md`
- `translations/en/alignment/ALIGNMENT_0061_0070.md`
- `translations/en/alignment/ALIGNMENT_0071_0080.md`
- `translations/en/alignment/ALIGNMENT_MANIFEST.csv`
- `translations/en/alignment/PROGRESS.md`
- `BILINGUAL_ALIGNMENT_HANDOVER.md`

### Alignment corrections made — do not revert

- **0014:** Tamil contains separate statements about political swagger and armed violence. The aligned English preserves that distinction.
- **0043:** Tamil `ஒன்று மட்டும் மறவாதே` means **“Do not forget this one thing.”** The canonical English has been corrected from the earlier opposite imperative.
- **0058:** the opening worker-centred verse has been restored to Tamil source sequence.
- **0059:** R. M. Veerappan's inset-letter `அன்புள்ள,` is restored as **“With affection,”** before his signature.

The **0061–0070** and **0071–0080** batches required no English content correction. Do not rewrite their canonical translation files merely to change source-check-era frontmatter.

## Alignment bookkeeping convention

Dedicated alignment reports plus `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. When a reviewed record requires no content correction, canonical translation files are not rewritten solely to churn source-check-era frontmatter. When a demonstrable correspondence error exists, the English prose/quotation itself is corrected.

This bookkeeping convention does **not** promote aligned records to `verified` or release-ready status.

## Exact next activity

Proceed with bilingual alignment for canonical English letters **0081–0090**, source PDF / printed pages **298–325**.

For each record:

1. compare English directly against the complete canonical Tamil witness and canonical chapter/page evidence where needed;
2. check substantive coverage, thought order, paragraph/verse/quotation correspondence, names, dates, figures, lists, metaphors, rhetorical questions, repetition, political terminology, attribution and closing integrity;
3. preserve Kalaignar's voice, directness, rhetorical force, imagery and movement vocabulary;
4. retain `Udanpirappē` under the established project convention;
5. do not modernise, normalise, reconstruct or infer unsupported Tamil;
6. correct only demonstrable English/Tamil correspondence errors;
7. create `translations/en/alignment/ALIGNMENT_0081_0090.md`;
8. append 0081–0090 to `translations/en/alignment/ALIGNMENT_MANIFEST.csv`;
9. advance alignment progress to **90 / 110** only after all ten records pass;
10. update the alignment handover and continuation prompt to the next exact boundary.

Consult `translations/en/SOURCE_CHECK_0081_0090.md` for source controls: Rajamannar Committee / **8,226-word** state-autonomy report in 0081; Pongal analogy in 0082; campaign-headline and cadre rhetoric in 0083; budget and journey imagery in 0084; rose/internal-election image in 0085; May Day labour history in 0086; railway-strike Centre/State asymmetry in 0087; birthday-fund redirection in 0088; lamp/pearls/balance-needle imagery in 0089; and Tamil–Malayali violence/cyclone/Kamaraj material in 0090.

## Gates still blocked

Do **not** begin yet:

- volume-level editorial consistency review;
- final translation manifest;
- final release report;
- final release declaration.

Those begin only after bilingual alignment reaches **110 / 110**.