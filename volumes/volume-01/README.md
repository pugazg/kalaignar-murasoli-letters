# தொகுதி 1 — canonical migration

**நூல்:** கலைஞரின் கடிதங்கள் — தொகுதி 1  
**அட்டைப் காலவரம்பு:** 22.10.1968 முதல் 01.12.1974 வரை  
**முதல் பதிப்பு:** 2022  
**பதிப்பகம்:** சீதை பதிப்பகம்  
**PDF:** 401 பக்கங்கள்; நூலில் குறிப்பிடப்பட்ட அச்சுப் பக்கங்கள்: 400

## Migration status

Volume 1 was previously processed under [`../volume-1/`](../volume-1/). That legacy corpus contains 110 bilingual records and remains preserved unchanged as migration evidence. The supplied `Vol1.pdf` is the controlling source; verified canonical Tamil outranks legacy Tamil/English drafts.

## Volume 1 batch override

Regular Volume 1 migration/review iterations use **10 complete consecutive letters**. A previous user-approved 20-letter iteration for 0057–0076 was a one-time exception.

## Current canonical state

- Canonical PDF coverage: **001–401 / 401 — complete**.
- Printed contents: **110 / 110** entries.
- Canonically complete letters: **0001–0110 (110 / 110)**.
- Letter coverage: PDF **024–400**; PDF **401** is a non-letter back cover / publisher advertisement.
- Printed pagination skips number **39** between PDF 039 and PDF 040 while text remains continuous.
- Letter 0063 has no printed date and remains undated.
- Contents/heading variants remain source-literal, including 0109 contents `அவள் ஒரு தொடற்கதை!` versus actual PDF-392 heading `அவள் ஒரு தொடர்கதை!`.
- Full-volume Tamil structural audit: **PASS**.
- Full-volume second visual/textual-fidelity verification: **PASS — PDF 001–401 / 401**.
- Cumulative second-pass corrections: **159 canonical pages / 274 scan-proven spans**.
- Canonical English migration/source check: **0001–0110 / 110 complete and source-checked**.
- Bilingual alignment: **COMPLETE — 0001–0110 / 110 reviewed and PASS**.
- Alignment-driven English prose/quotation corrections: **4**, in 0014, 0043, 0058 and 0059.
- Final alignment batch **0101–0110**: **PASS with no English prose/quotation correction required**.
- Canonical English records remain **source-checked, not verified**. Volume-level editorial consistency is the next gate; release artifacts remain later.

## Source identity

- Source file: `Vol1.pdf`
- SHA-256: `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`
- Size: `244892260` bytes
- PDF pages: `401`
- Searchable text layer: none usable; scan images control transcription.

## Legacy provenance

See [`../volume-1/MIGRATION_AUDIT.md`](../volume-1/MIGRATION_AUDIT.md), [`../volume-1/audits/`](../volume-1/audits/) and [`../volume-1/translations/en/`](../volume-1/translations/en/). Do not rewrite the legacy tree.

## Exact next task

Proceed with the **volume-level English editorial consistency review** required by `VOLUME_PROCESSING_GUIDE.md` §12 across all 110 canonical English records. Review title/index agreement, translator-note exactness, names, honorifics, places, transliteration, institutions, spelling, compounds, punctuation, dates/page ranges, glossary decisions, source anomalies and stale status wording. Do not alter political meaning, attribution, uncertainty, figures, quotations, rhetorical force, source status or appended Tamil.

Create `translations/en/EDITORIAL_CONSISTENCY_REVIEW.md` when the review passes. Keep the final translation manifest, release report and release declaration blocked until the editorial gate is complete.
