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

- Canonical PDF coverage: **001–401 / 401 — complete**.
- Printed contents: PDF **018–023**, all **110 printed entries** transcribed.
- Canonically complete letters: **0001–0110 (110 / 110)**.
- Partial canonical letter: **none**.
- Canonical letter coverage: PDF **024–400**; PDF **401** is non-letter back cover / publisher advertisement.
- Source pagination note: PDF 039 prints **38**, while PDF 040 prints **40**; text is continuous, so printed number 39 is treated as a source pagination anomaly, not missing content.
- Actual heading variants are preserved where they differ from contents entries, including letters 0008, 0012, 0024 and 0109. For 0109, the contents prints `அவள் ஒரு தொடற்கதை!`, while PDF 392 actually heads the letter `அவள் ஒரு தொடர்கதை!`.
- Letter 0063 has **no date printed in the source**; no date is inferred.
- Full-volume Tamil structural audit: **complete — PASS**. See [`FULL_VOLUME_STRUCTURAL_AUDIT.md`](FULL_VOLUME_STRUCTURAL_AUDIT.md).
- Full-volume second visual/textual-fidelity verification: **complete — PASS, PDF 001–401 / 401**. See [`FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md).
- Cumulative second-pass corrections: **159 canonical pages / 274 scan-proven spans**.
- Letters **0001–0110** have complete second-pass source-page coverage.
- Canonical English migration/source check: **0001–0110 / 110 complete and source-checked**. See [`translations/en/PROGRESS.md`](translations/en/PROGRESS.md).
- Bilingual alignment: **in progress — 0001–0080 / 80 reviewed and PASS**. See [`translations/en/alignment/PROGRESS.md`](translations/en/alignment/PROGRESS.md) and [`BILINGUAL_ALIGNMENT_HANDOVER.md`](BILINGUAL_ALIGNMENT_HANDOVER.md).
- Alignment-driven English prose/quotation corrections: **4**, in letters **0014, 0043, 0058 and 0059**.
- Alignment batch **0071–0080**: **PASS with no English prose/quotation correction required**. Controls including the Time Capsule wordplay, source-ordered Bharathidasan verse, Corporation allegory, closing Kural, fundraising sequence, Sixth Finance Commission structure, Periyar victory/self-critique, `பாடி வீடுகள்` and `கொள்கை மலர்கள்` imagery were reconfirmed.
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

Continue the dedicated bilingual-alignment review with canonical English letters **0081–0090**, source PDF / printed pages **298–325**. Compare each English record directly with its complete canonical Tamil witness, correct only demonstrable correspondence/alignment errors, create `translations/en/alignment/ALIGNMENT_0081_0090.md`, append record-level results to the alignment manifest, and advance alignment progress to **90 / 110** only after all ten records pass.

Keep volume-level editorial consistency, final translation manifest, release report and release declaration blocked until bilingual alignment reaches **110 / 110**.