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

Volume 1 uses the established **10-letter regular cadence** for this review. Alignment begins with **0001–0010**, then proceeds consecutively.

## Status recording

The alignment reports and `ALIGNMENT_MANIFEST.csv` are the authoritative gate ledger. Because the first batch required **no English prose correction**, its canonical translation files are intentionally not rewritten solely to churn frontmatter metadata. Their existing source-check metadata therefore remains unchanged for now; the dedicated alignment ledger records the completed meaning-level review. A later metadata-synchronisation pass can promote frontmatter consistently after the alignment gate, without conflating content correction with bookkeeping.

This does **not** promote any record to `verified` or release-ready status.

## Current status

- Source-checked: **110 / 110**
- Alignment-reviewed and PASS: **10 / 110**
- Completed alignment range: **0001–0010**
- English prose corrections required by alignment so far: **0**
- Verified: **0 / 110**
- Editorially reviewed: **0 / 110**

Completed report:

- [`ALIGNMENT_0001_0010.md`](ALIGNMENT_0001_0010.md)

Exact next batch: **0011–0020**.

Volume-level editorial consistency, final manifest, release report and release declaration remain blocked until bilingual alignment is complete.