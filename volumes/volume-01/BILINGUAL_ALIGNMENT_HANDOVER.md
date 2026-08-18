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

Four regular alignment batches are complete:

- **0001–0010** — PDF **024–066** — PASS — 0 English prose corrections
- **0011–0020** — PDF **067–104** — PASS after 1 English prose correction
- **0021–0030** — PDF **105–135** — PASS — 0 English prose corrections
- **0031–0040** — PDF **136–177** — PASS — 0 English prose corrections

Current gate totals:

- alignment-reviewed and PASS: **40 / 110**
- completed range: **0001–0040**
- cumulative alignment-driven English prose corrections: **1**
- verified: **0 / 110**
- editorially reviewed: **0 / 110**

Reports:

- `translations/en/alignment/ALIGNMENT_0001_0010.md`
- `translations/en/alignment/ALIGNMENT_0011_0020.md`
- `translations/en/alignment/ALIGNMENT_0021_0030.md`
- `translations/en/alignment/ALIGNMENT_0031_0040.md`
- ledger: `translations/en/alignment/ALIGNMENT_MANIFEST.csv`
- progress: `translations/en/alignment/PROGRESS.md`

The review compares every English translation with its complete canonical Tamil witness and checks argument sequence, coverage, paragraph/quotation correspondence, names, dates, figures, metaphors, rhetorical questions, repetition, political terminology, attribution and closing integrity.

## Important alignment findings so far

The first batch reconfirmed two earlier source controls:

- 0002 carries the complete Kamaraj Deepavali quotation, including the source-restored clause from PDF 030;
- 0010 uses **Runner Cup**, following PDF 063 `“ரன்னர்” கோப்பை`, not stale legacy `Rainer`.

The second batch required one meaning-level English correction:

- **0014:** the prior English merged Tamil's separate statements on aggressive political swagger and armed violence. The corrected English now preserves the source distinction: slapping one's thighs/twirling one's moustache does not befit politics; raising a gun/drawing a knife is separately condemned as a method even savages should fear to adopt.

The third batch, **0021–0030**, required no English prose correction. It reconfirmed the Tamil Nadu renaming chronology, anti-retaliation instruction, Venmani source/date controls, non-causation caveat and Nijalingappa/Haryana/Mysore satire.

The fourth batch, **0031–0040**, also required no English prose correction. Important controls reconfirmed include:

- 0031 — extended *The Hindu* eyewitness quotation and tiger/goat-disguise satire;
- 0032 — language-issue chronology and Kamaraj/Subramaniam argument;
- 0033 — direct address to Anna, anti-Hindi history and medium-of-instruction argument;
- 0034 — **Eleven Lakhs** memory and Anna's warning that only self-destruction can defeat the movement;
- 0035 — `கடமை, கண்ணியம், கட்டுப்பாடு`, six-item Anna list and final stay-awake appeal;
- 0036 — source initials `சி. பி. சி.` / **C. P. C.** retained without speculative expansion;
- 0037 — scan-supported title `தூங்குவோமா?`, Rajamannar Committee and state-autonomy argument;
- 0038 — parliamentary/righteous-struggle/Gandhian/Anna methods and final membership-enrolment directive;
- 0039 — Coimbatore General Council/state-autonomy programme and source imagery;
- 0040 — P. Kannan chronology, quoted 2 April letter, dramatic works and closing Tirukkural.

## Alignment metadata convention for this gate

Dedicated alignment reports plus `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. Canonical translation records are not rewritten solely for frontmatter churn when no content change is required. Their source-check-era alignment metadata may therefore remain unchanged while the ledger records `bilingual_alignment_checked=true` for reviewed records.

When a demonstrable correspondence correction is required, the English prose itself is corrected, as in 0014. This convention does not promote any record to `verified` or release-ready status.

## Exact next activity

Proceed with bilingual alignment for **0041–0050**, source PDF **178–213**.

For each record:

1. compare English directly against the complete canonical Tamil witness;
2. check substantive coverage, sequence, paragraph/quotation correspondence, names, dates, figures, lists, metaphors, rhetorical questions, repetition, political terminology and attribution;
3. correct only demonstrable English/Tamil correspondence errors;
4. preserve `Udanpirappē` and established movement vocabulary;
5. record PASS/corrections in `translations/en/alignment/ALIGNMENT_0041_0050.md`;
6. append rows to `translations/en/alignment/ALIGNMENT_MANIFEST.csv`;
7. update `translations/en/alignment/PROGRESS.md` to **50 / 110** only after all ten records pass.

Important source controls for the next batch are documented in `translations/en/SOURCE_CHECK_0041_0050.md`, including the Beggars' Rehabilitation Fund appeal in 0041, anti-violence sequence in 0042–0043, Indira Congress accusation list in 0044, Madurai conference material in 0045–0046, `நாடு + அகம் = நாடகம்` in 0047, printed `சென்னை. / 10.10.1972` in 0048, Anna's 1961 reply in 0049 and *Navasakthi* chronology/figures in 0050.

## Still blocked

Do not begin yet:

- volume-level editorial consistency review;
- final translation manifest;
- release report;
- final release declaration.

These remain blocked until bilingual alignment reaches **110 / 110**.