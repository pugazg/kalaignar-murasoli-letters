# Volume 1 — Bilingual Alignment Workspace

This directory records the dedicated English ↔ canonical-Tamil bilingual-alignment gate for Volume 1.

## Authority and scope

The controlling order remains:

1. supplied `Vol1.pdf` scan;
2. verified canonical Tamil under `volumes/volume-01/pages/` and `chapters/`;
3. canonical English under `volumes/volume-01/translations/en/letters/`;
4. alignment reports and tracking records in this directory.

The canonical English migration/source-check gate is already complete at **110 / 110**. Bilingual alignment is a separate meaning-level review. It checks argument sequence, substantive coverage, paragraph and quotation correspondence, names, dates, figures, lists, metaphors, rhetorical questions, repetition, political terminology, attribution and source anomalies.

Only demonstrable correspondence errors are corrected at this gate. Stylistic rewriting is deferred to the later editorial-consistency gate.

## Batch cadence

Volume 1 uses the established **10-letter regular cadence** for this review and proceeds consecutively.

Completed alignment batches:

- **0001–0010** — PASS — 0 English prose corrections
- **0011–0020** — PASS after 1 English prose correction
- **0021–0030** — PASS — 0 English prose corrections

Exact next batch: **0031–0040**.

## Status recording

The alignment reports and `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. Canonical translation files are not rewritten solely to churn source-check-era frontmatter when no content change is required. Their existing source-check metadata may therefore remain unchanged while the dedicated alignment ledger records the completed meaning-level review.

When a demonstrable correspondence error exists, the English prose itself is corrected. Through 0030, one such correction has been required, in **0014**, where two consecutive Tamil statements had been compressed into one English sentence. The aligned text preserves the source distinction between political swagger that does not befit politics and the separately stronger condemnation of raising a gun or drawing a knife.

No English prose correction was required in the 0021–0030 batch.

This bookkeeping convention does **not** promote any record to `verified` or release-ready status.

## Current status

- Source-checked: **110 / 110**
- Alignment-reviewed and PASS: **30 / 110**
- Completed alignment range: **0001–0030**
- English prose corrections required by alignment so far: **1**
- Verified: **0 / 110**
- Editorially reviewed: **0 / 110**

Completed reports:

- [`ALIGNMENT_0001_0010.md`](ALIGNMENT_0001_0010.md)
- [`ALIGNMENT_0011_0020.md`](ALIGNMENT_0011_0020.md)
- [`ALIGNMENT_0021_0030.md`](ALIGNMENT_0021_0030.md)

Tracking records:

- [`ALIGNMENT_MANIFEST.csv`](ALIGNMENT_MANIFEST.csv)
- [`PROGRESS.md`](PROGRESS.md)

## Exact next activity

Align canonical English letters **0031–0040** against their complete canonical Tamil witnesses. Correct only demonstrable correspondence errors, create `ALIGNMENT_0031_0040.md`, append record-level results to the manifest, and advance progress to **40 / 110** only after all ten records pass.

Volume-level editorial consistency, final manifest, release report and release declaration remain blocked until bilingual alignment reaches **110 / 110**.