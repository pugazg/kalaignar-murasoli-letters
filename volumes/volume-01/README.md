# தொகுதி 1 — canonical migration

**நூல்:** கலைஞரின் கடிதங்கள் — தொகுதி 1  
**அட்டைப் காலவரம்பு:** 22.10.1968 முதல் 01.12.1974 வரை  
**முதல் பதிப்பு:** 2022  
**பதிப்பகம்:** சீதை பதிப்பகம்  
**PDF:** 401 பக்கங்கள்; நூலில் குறிப்பிடப்பட்ட அச்சுப் பக்கங்கள்: 400

## Migration status

Volume 1 was previously processed by a different workflow under [`../volume-1/`](../volume-1/). That legacy corpus contains 110 bilingual records and audit material. It is preserved unchanged while the canonical later-volume structure and source-checked English records are built here.

The supplied `Vol1.pdf` is the controlling source for this migration. Existing Tamil reading copies and English translations are reusable evidence/drafts, but they do not override the scan or the verified canonical Tamil.

## Volume 1 batch override

For **Volume 1 alone**, regular migration/review iterations use **10 complete consecutive letters per iteration**. This volume-specific instruction supersedes the repository's normal five-letter cadence for Volume 1 work only. A documented final residue may be smaller.

A previous user-approved iteration used an expanded scope of **20 complete consecutive letters — 0057 through 0076**. That was a one-time exception; regular Volume 1 work returned to the ten-letter cadence afterward.

## Current canonical state

- Canonical PDF coverage: **001–401 / 401 — first-pass complete**.
- Mandatory first batch: **complete — PDF 001–025**.
- Interrupted letter 0001 completion: **complete — PDF 026–027**.
- Initial five-letter batch completed before the Volume 1 override: **0002–0006 / PDF 028–047**.
- First Volume 1 ten-letter batch: **complete — 0007–0016 / PDF 048–089**.
- Second Volume 1 ten-letter batch: **complete — 0017–0026 / PDF 090–126**.
- Third Volume 1 ten-letter batch: **complete — 0027–0036 / PDF 127–160**.
- Fourth Volume 1 ten-letter batch: **complete — 0037–0046 / PDF 161–199**.
- Fifth Volume 1 ten-letter batch: **complete — 0047–0056 / PDF 200–235**.
- User-approved expanded 20-letter batch: **complete — 0057–0076 / PDF 236–288**.
- Sixth regular Volume 1 ten-letter batch: **complete — 0077–0086 / PDF 289–312**.
- Seventh regular Volume 1 ten-letter batch: **complete — 0087–0096 / PDF 313–344**.
- Eighth regular Volume 1 ten-letter batch: **complete — 0097–0106 / PDF 345–383**.
- Final documented residue: **complete — 0107–0110 / PDF 384–400**.
- Back cover / non-letter tail: **complete — PDF 401**.
- Front matter/preface: PDF **001–017** first-pass reviewed.
- Printed contents: PDF **018–023**, all **110 printed entries** transcribed.
- Canonically complete letters: **0001–0110 (110 / 110)**.
- Partial canonical letter: **none**.
- Source pagination note: PDF 039 prints **38**, while PDF 040 prints **40**; text is continuous, so printed number 39 is treated as a source pagination anomaly, not missing content.
- Actual heading variants are preserved where they differ from contents entries, including letters 0008, 0012, 0024 and 0109. For 0109, the contents prints `அவள் ஒரு தொடற்கதை!`, while PDF 392 actually heads the letter `அவள் ஒரு தொடர்கதை!`.
- Batch-specific source observations for 0097–0106 are recorded in [`BATCH_0097_0106_AUDIT.md`](BATCH_0097_0106_AUDIT.md), and the final 0107–0110 residue / source ending is recorded in [`BATCH_0107_0110_AUDIT.md`](BATCH_0107_0110_AUDIT.md); earlier migration observations remain in [`AUDIT.md`](AUDIT.md).
- Letter 0063 has **no date printed in the source**; no date is inferred.
- Letters 0107–0110 are complete on PDF **384–400**. Letter 0110 closes on PDF 400 with `(01-12-1974)`; PDF 401 is a non-letter colour back cover / publisher advertisement.
- Full-volume Tamil structural audit: **complete — PASS**. See [`FULL_VOLUME_STRUCTURAL_AUDIT.md`](FULL_VOLUME_STRUCTURAL_AUDIT.md). The audit confirmed 401/401 page records, 110/110 chapter records, continuous letter coverage PDF 024–400, and no structural gaps or overlaps.
- Full-volume second visual/textual-fidelity verification: **complete — PASS, PDF 001–401 / 401**. See [`FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md).
- Cumulative second-pass corrections: **159 canonical pages / 274 scan-proven spans**.
- Final letter-text range [`376–400`](translations/en/TEXTUAL_FIDELITY_AUDIT_376_400.md) required corrections on **5 pages / 5 spans**, restoring the scan-bold opening salutations for letters 0106–0110 on PDFs 380, 384, 388, 392 and 396. The non-letter [`PDF 401`](translations/en/TEXTUAL_FIDELITY_AUDIT_401.md) back cover required no canonical correction.
- Letters **0001–0110** have complete second-pass source-page coverage.
- Canonical English migration/source check: **0001–0110 / 110 complete and source-checked**. See [`translations/en/PROGRESS.md`](translations/en/PROGRESS.md) and [`translations/en/SOURCE_CHECK_0101_0110.md`](translations/en/SOURCE_CHECK_0101_0110.md).
- Bilingual alignment: **in progress — 0001–0020 / 20 reviewed and PASS**. See [`translations/en/alignment/PROGRESS.md`](translations/en/alignment/PROGRESS.md) and [`BILINGUAL_ALIGNMENT_HANDOVER.md`](BILINGUAL_ALIGNMENT_HANDOVER.md).
- Alignment-driven English prose corrections: **1**, in letter 0014. The correction restores the source distinction between political swagger that does not befit politics and the separately stronger condemnation of armed violence.
- Canonical English records remain **source-checked, not verified**. Volume-level editorial consistency review and final release work remain later gates.

## Source identity

- Source file: `Vol1.pdf`
- SHA-256: `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`
- Size: `244892260` bytes
- PDF pages: `401`
- Searchable text layer: none usable; scan images control transcription.

## Legacy provenance

The earlier work is intentionally not deleted or silently rewritten. See:

- [`../volume-1/MIGRATION_AUDIT.md`](../volume-1/MIGRATION_AUDIT.md)
- [`../volume-1/audits/`](../volume-1/audits/)
- [`../volume-1/translations/en/`](../volume-1/translations/en/)

## Exact next task

Continue the dedicated bilingual-alignment review with canonical English letters **0021–0030**. Compare each English record directly with its complete canonical Tamil witness, correct only demonstrable correspondence/alignment errors, create `translations/en/alignment/ALIGNMENT_0021_0030.md`, append record-level results to the alignment manifest, and advance alignment progress to **30 / 110** only after all ten records pass.

Keep volume-level editorial consistency, final translation manifest, release report and release declaration blocked until bilingual alignment reaches **110 / 110**.