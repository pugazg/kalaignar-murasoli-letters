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

Six regular alignment batches are complete:

- **0001–0010** — PDF **024–066** — PASS — 0 English prose corrections
- **0011–0020** — PDF **067–104** — PASS after 1 English prose correction
- **0021–0030** — PDF **105–135** — PASS — 0 English prose corrections
- **0031–0040** — PDF **136–177** — PASS — 0 English prose corrections
- **0041–0050** — PDF **178–213** — PASS after 1 English prose correction
- **0051–0060** — PDF **214–249** — PASS after 2 English prose/quotation corrections

Current gate totals:

- alignment-reviewed and PASS: **60 / 110**
- completed range: **0001–0060**
- cumulative alignment-driven English prose/quotation corrections: **4**
- verified: **0 / 110**
- editorially reviewed: **0 / 110**

Reports:

- `translations/en/alignment/ALIGNMENT_0001_0010.md`
- `translations/en/alignment/ALIGNMENT_0011_0020.md`
- `translations/en/alignment/ALIGNMENT_0021_0030.md`
- `translations/en/alignment/ALIGNMENT_0031_0040.md`
- `translations/en/alignment/ALIGNMENT_0041_0050.md`
- `translations/en/alignment/ALIGNMENT_0051_0060.md`
- ledger: `translations/en/alignment/ALIGNMENT_MANIFEST.csv`
- progress: `translations/en/alignment/PROGRESS.md`

The review compares every English translation with its complete canonical Tamil witness and checks argument sequence, substantive coverage, paragraph/verse/quotation correspondence, names, dates, figures, metaphors, rhetorical questions, repetition, political terminology, attribution and closing integrity.

## Alignment corrections so far

- **0014:** restored Tamil's distinction between political swagger and the separately stronger condemnation of armed violence.
- **0043:** corrected the reversed imperative `Forget only this one thing` to **`Do not forget this one thing`**, following `ஒன்று மட்டும் மறவாதே`.
- **0058:** restored the Tamil sequence of the opening worker-centred verse. The English now begins with the little village/embanked fields and canal imagery before the `நிறையுழைப்புத் தோள்கள்` / shoulders-of-labour image, rather than moving that image to the front.
- **0059:** restored the omitted `அன்புள்ள,` in R. M. Veerappan's inset letter as **`With affection,`** before `Veerappan.`.

The **0051–0060** batch otherwise required no English prose change. Important controls reconfirmed include:

- 0051 — earthen-lamp journey, Muthu/mother passage, Anna's reform-without-humiliation quotation and Nanjil Manoharan line;
- 0052 — Anna memorial, state-autonomy/anti-Hindi material, pledge and Kattabomman/Ettappan close;
- 0053 — Dindigul by-election, candidate histories, welfare arguments and rhythmic closing exhortation;
- 0054 — A. C. George satire and source figure **6908**;
- 0055 — Mujibur Rahman/Awami League, Banka/Kerala comparisons and `அரிதாரம்` image;
- 0056 — **166 / 152**, Rajaji/Aruppukkottai precedent and political-civility appeal;
- 0057 — fiftieth-birthday Rickshaw Fund appeal;
- 0058 — source date **29-05-1973** and restored verse sequence;
- 0059 — R. M. Veerappan inset letter dated **22 April 1972**, now with complete source-supported sign-off;
- 0060 — 31 May 1973 plane-crash chronology, Mohan Kumaramangalam/Gurnam Singh/Baladhandayutham memories and source close **02-06-1973**.

## Alignment metadata convention

Dedicated alignment reports plus `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. Canonical translation records are not rewritten solely for frontmatter churn when no content change is required. When a demonstrable correspondence error exists, the English prose/quotation itself is corrected.

This convention does not promote any record to `verified` or release-ready status.

## Exact next activity

Proceed with bilingual alignment for **0061–0070**, source PDF / printed pages **250–276**.

For each record:

1. compare English directly against the complete canonical Tamil witness;
2. check substantive coverage, sequence, paragraph/verse/quotation correspondence, names, dates, figures, lists, metaphors, rhetorical questions, repetition, political terminology and attribution;
3. correct only demonstrable English/Tamil correspondence errors;
4. preserve `Udanpirappē` and established movement vocabulary;
5. record PASS/corrections in `translations/en/alignment/ALIGNMENT_0061_0070.md`;
6. append rows to `translations/en/alignment/ALIGNMENT_MANIFEST.csv`;
7. update `translations/en/alignment/PROGRESS.md` to **70 / 110** only after all ten records pass.

Consult `translations/en/SOURCE_CHECK_0061_0070.md` before review. Important source controls include letter 0063 remaining undated, scan-controlled Bharathidasan forms in 0068, PDF 274 `இலாக்காக்களில்` in 0069, and the printed English judicial quotation in 0070 reproduced verbatim.

## Still blocked

Do not begin yet:

- volume-level editorial consistency review;
- final translation manifest;
- release report;
- final release declaration.

These remain blocked until bilingual alignment reaches **110 / 110**.