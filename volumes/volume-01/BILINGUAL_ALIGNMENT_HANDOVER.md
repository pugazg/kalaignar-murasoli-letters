# Volume 1 — Bilingual Alignment Handover

## Repository

`pugazg/kalaignar-murasoli-letters` — work on `main`.

Active canonical tree: `volumes/volume-01/`.

Legacy tree `volumes/volume-1/` remains preserved and must not be rewritten.

## Completed gates — do not restart

- Canonical Tamil migration: **401 / 401 PDF pages**
- Canonical letters: **110 / 110**
- Full-volume Tamil structural audit: **PASS**
- Full visual/textual-fidelity verification: **PASS — PDF 001–401 / 401**
- Canonical English migration/source check: **110 / 110**

## Active gate — bilingual alignment

Three regular alignment batches are complete:

- **0001–0010** — PDF **024–066** — PASS — 0 English prose corrections
- **0011–0020** — PDF **067–104** — PASS after 1 English prose correction
- **0021–0030** — PDF **105–135** — PASS — 0 English prose corrections

Current gate totals:

- alignment-reviewed and PASS: **30 / 110**
- completed range: **0001–0030**
- cumulative alignment-driven English prose corrections: **1**
- verified: **0 / 110**
- editorially reviewed: **0 / 110**

Reports:

- `translations/en/alignment/ALIGNMENT_0001_0010.md`
- `translations/en/alignment/ALIGNMENT_0011_0020.md`
- `translations/en/alignment/ALIGNMENT_0021_0030.md`
- ledger: `translations/en/alignment/ALIGNMENT_MANIFEST.csv`
- progress: `translations/en/alignment/PROGRESS.md`

The review directly compares every English translation with its complete canonical Tamil witness and checks argument sequence, coverage, paragraph/quotation correspondence, names, dates, figures, metaphors, rhetorical questions, repetition, political terminology, attribution and closing integrity.

## Important alignment findings so far

The first batch reconfirmed two earlier source controls:

- 0002 carries the complete Kamaraj Deepavali quotation, including the source-restored clause from PDF 030;
- 0010 uses **Runner Cup**, following PDF 063 `“ரன்னர்” கோப்பை`, not stale legacy `Rainer`.

The second batch required one meaning-level English correction:

- **0014:** the prior English merged Tamil's separate statements on aggressive political swagger and armed violence. The corrected English now preserves the source distinction: slapping one's thighs/twirling one's moustache does not befit politics; raising a gun/drawing a knife is separately condemned as a method even savages should fear to adopt.

The source-check restoration in 0019 remains intact, including Anna's `ரத்தத்தின் ரத்தம் / சதையின் சதை` reply and Morarji Desai's Hindi statement from PDF 099.

The third batch required **no English prose correction**. Important controls reconfirmed include:

- 0021 — the complete 1960–1967 `தமிழ் நாடு` renaming chronology, legislative quotations, literary examples and closing `நெருஞ்சி முள்` image;
- 0027 — the explicit ethical turn that wrongdoing is not answered by wrongdoing;
- 0028 — source figure **43**, **13** arrests, Gopalakrishna Naidu context and the source-printed date **28-12-1968**;
- 0029 — Kalaignar observes the timing of the two Hindi-news reports but does **not** assert causation with certainty;
- 0030 — Nijalingappa/Haryana/Mysore reports and the ruined-hall/bats satire remain in source order.

## Alignment metadata convention for this gate

Dedicated alignment reports plus `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. Canonical translation records are not rewritten solely for frontmatter churn when no content change is required. Their source-check-era alignment metadata may therefore remain unchanged while the ledger records `bilingual_alignment_checked=true` for reviewed records.

When a demonstrable correspondence correction is required, the English prose itself is corrected, as in 0014. This convention does not promote any record to `verified` or release-ready status.

## Exact next activity

Proceed with bilingual alignment for **0031–0040**.

For each record:

1. compare English directly against the complete canonical Tamil witness;
2. check substantive coverage, sequence, paragraph/quotation correspondence, names, dates, figures, lists, metaphors, rhetorical questions, repetition, political terminology and attribution;
3. correct only demonstrable English/Tamil correspondence errors;
4. preserve `Udanpirappē` and established movement vocabulary;
5. record PASS/corrections in `translations/en/alignment/ALIGNMENT_0031_0040.md`;
6. append rows to `translations/en/alignment/ALIGNMENT_MANIFEST.csv`;
7. update `translations/en/alignment/PROGRESS.md` to **40 / 110** only after all ten records pass.

Important source controls for the next batch are already documented in `translations/en/SOURCE_CHECK_0031_0040.md`, including `சி. பி. சி.` / `C. P. C.` left unexpanded in 0036, the scan title `தூங்குவோமா?` in 0037, the membership directive in 0038, General Council programme in 0039 and P. Kannan quotation/Tirukkural in 0040.

## Still blocked

Do not begin yet:

- volume-level editorial consistency review;
- final translation manifest;
- release report;
- final release declaration.

These remain blocked until bilingual alignment reaches **110 / 110**.