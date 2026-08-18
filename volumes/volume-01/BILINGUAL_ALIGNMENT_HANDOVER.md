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

The first regular alignment batch is complete:

- letters: **0001–0010**
- source span: **PDF 024–066**
- result: **PASS**
- alignment-reviewed: **10 / 110**
- English prose corrections required: **0**
- report: `translations/en/alignment/ALIGNMENT_0001_0010.md`
- ledger: `translations/en/alignment/ALIGNMENT_MANIFEST.csv`

The review directly compared every English translation with its complete canonical Tamil witness and checked argument sequence, coverage, paragraph/quotation correspondence, names, dates, figures, metaphors, rhetorical questions, repetition, political terminology, attribution and closing integrity.

The first batch reconfirmed two important earlier source controls:

- 0002 carries the complete Kamaraj Deepavali quotation, including the source-restored clause from PDF 030;
- 0010 uses **Runner Cup**, following PDF 063 `“ரன்னர்” கோப்பை`, not stale legacy `Rainer`.

No demonstrable correspondence error was found in 0001–0010, so no translation prose was rewritten.

## Alignment metadata convention for this gate

Dedicated alignment reports plus `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. When an alignment batch requires no content change, canonical translation records are not rewritten solely for frontmatter churn. Their existing source-check metadata may therefore remain unchanged while the alignment ledger records `bilingual_alignment_checked=true` for reviewed records.

This convention is explicit and auditable; it does not promote records to `verified` or release-ready status.

## Exact next activity

Proceed with bilingual alignment for **0011–0020**.

For each record:

1. compare English directly against the complete canonical Tamil witness;
2. check substantive coverage, sequence, paragraph/quotation correspondence, names, dates, figures, lists, metaphors, rhetorical questions, repetition, political terminology and attribution;
3. correct only demonstrable English/Tamil correspondence errors;
4. preserve `Udanpirappē` and established movement vocabulary;
5. record PASS/corrections in `translations/en/alignment/ALIGNMENT_0011_0020.md`;
6. append rows to `translations/en/alignment/ALIGNMENT_MANIFEST.csv`;
7. update `translations/en/alignment/PROGRESS.md` to **20 / 110** only after all ten records pass.

## Still blocked

Do not begin yet:

- volume-level editorial consistency review;
- final translation manifest;
- release report;
- final release declaration.

These remain blocked until bilingual alignment reaches **110 / 110**.