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

Current totals:

- alignment-reviewed and PASS: **50 / 110**
- completed alignment range: **0001–0050**
- cumulative alignment-driven English prose corrections: **2**
- verified: **0 / 110**
- editorially reviewed: **0 / 110**

Authoritative alignment records:

- `translations/en/alignment/ALIGNMENT_0001_0010.md`
- `translations/en/alignment/ALIGNMENT_0011_0020.md`
- `translations/en/alignment/ALIGNMENT_0021_0030.md`
- `translations/en/alignment/ALIGNMENT_0031_0040.md`
- `translations/en/alignment/ALIGNMENT_0041_0050.md`
- `translations/en/alignment/ALIGNMENT_MANIFEST.csv`
- `translations/en/alignment/PROGRESS.md`
- `BILINGUAL_ALIGNMENT_HANDOVER.md`

### Alignment corrections made

**0014:** Tamil contains separate statements about political swagger and armed violence. The aligned English preserves that distinction and must not be collapsed again.

**0043:** Tamil closing `ஒன்று மட்டும் மறவாதே` means **“Do not forget this one thing.”** The earlier English said **“Forget only this one thing,”** reversing the imperative. The canonical English has been corrected to **“Do not forget this one thing:”**. Do not revert it.

### Fifth alignment batch — 0041–0050

All ten records passed after the single 0043 correction. Important controls reconfirmed include:

- 0041 — Beggars' Rehabilitation Fund and birthday appeal;
- 0042–0043 — anti-violence sequence, July 15 and Anna's `கத்தியைத் தீட்டாதே! புத்தியைத் தீட்டு!`;
- 0044 — Gospel epigraph, complete Indira Congress accusation list, Fernandes and `கொங்கணவா?`;
- 0045–0046 — Madurai conference and state-autonomy imagery, Race Course chronology and hundred-flag campaign;
- 0047 — `நாடு + அகம் = நாடகம்`, *Silappathikaram*, health/longevity passage and proverb reversal;
- 0048 — MGR/1972 Executive Committee episode, **25 of 33**, and printed `சென்னை. / 10.10.1972` without inferred replacement date;
- 0049 — Anna's full 1961 reply and `நெஞ்சகம் / அன்பகம் / அறிவகம்` wordplay;
- 0050 — *Navasakthi* chronology, collection figures and elephant-pit image.

## Alignment bookkeeping convention

Dedicated alignment reports plus `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. When a reviewed record requires no content correction, canonical translation files are not rewritten solely to churn source-check-era frontmatter. When a demonstrable correspondence error exists, the English prose is corrected.

This bookkeeping convention does **not** promote aligned records to `verified` or release-ready status.

## Exact next activity

Proceed with bilingual alignment for canonical English letters **0051–0060**, source PDF / printed pages **214–249**.

For each record:

1. compare English directly against the complete canonical Tamil witness and canonical chapter/page evidence where needed;
2. check substantive coverage, thought order, paragraph/quotation correspondence, names, dates, figures, lists, metaphors, rhetorical questions, repetition, political terminology, attribution and closing integrity;
3. preserve Kalaignar's voice, directness, rhetorical force, imagery and movement vocabulary;
4. retain `Udanpirappē` under the established project convention;
5. do not modernise, normalise, reconstruct or infer unsupported Tamil;
6. correct only demonstrable English/Tamil correspondence errors;
7. create `translations/en/alignment/ALIGNMENT_0051_0060.md`;
8. append 0051–0060 to `translations/en/alignment/ALIGNMENT_MANIFEST.csv`;
9. advance alignment progress to **60 / 110** only after all ten records pass;
10. update the alignment handover and continuation prompt to the next exact boundary.

Consult `translations/en/SOURCE_CHECK_0051_0060.md` for source controls: earthen-lamp/Anna quotation in 0051; memorial/state-autonomy/anti-Hindi material in 0052; Dindigul by-election in 0053; source figure **6908** in 0054; `அரிதாரம்` argument in 0055; Assembly figures **166 / 152** and Rajaji precedent in 0056; Rickshaw Fund appeal in 0057; source date **29-05-1973** in 0058; R. M. Veerappan inset letter in 0059; and the 31 May 1973 plane-crash chronology in 0060.

## Gates still blocked

Do **not** begin yet:

- volume-level editorial consistency review;
- final translation manifest;
- final release report;
- final release declaration.

Those begin only after bilingual alignment reaches **110 / 110**.