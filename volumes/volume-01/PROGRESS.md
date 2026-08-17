# Volume 1 — Canonical Migration Progress

- [x] Migration audit completed against existing legacy Volume 1 corpus
- [x] Controlling `Vol1.pdf` verified: 401 PDF pages, 400 printed pages
- [x] New canonical `volumes/volume-01/` scaffold established
- [x] Mandatory first batch: PDF 001–025 first-pass reviewed
- [x] Printed contents PDF 018–023 transcribed: 110 entries
- [x] Letter 0001 started at PDF 024 and correctly left partial at PDF 025
- [x] Interrupted letter 0001 completed from PDF 026 through its source closing at PDF 027
- [x] Initial regular five-letter batch: letters 0002–0006 / PDF 028–047
- [x] Volume 1 batch override adopted: **10 complete letters per regular iteration**
- [x] First ten-letter batch: letters 0007–0016 / PDF 048–089
- [x] Second ten-letter batch: letters 0017–0026 / PDF 090–126
- [x] Third ten-letter batch: letters 0027–0036 / PDF 127–160
- [x] Fourth ten-letter batch: letters 0037–0046 / PDF 161–199
- [x] Fifth ten-letter batch: letters 0047–0056 / PDF 200–235
- [x] User-approved expanded 20-letter batch: letters 0057–0076 / PDF 236–288
- [x] Sixth regular ten-letter batch: letters 0077–0086 / PDF 289–312
- [x] Seventh regular ten-letter batch: letters 0087–0096 / PDF 313–344
- [x] Eighth regular ten-letter batch: letters 0097–0106 / PDF 345–383
- [x] Final documented residue: letters 0107–0110 / PDF 384–400, plus non-letter back cover PDF 401
- [ ] Full-volume Tamil structural audit
- [ ] Second visual/textual-fidelity verification
- [ ] Legacy English record migration and source checking
- [ ] Bilingual alignment
- [ ] Volume-level editorial consistency review
- [ ] Translation manifest and final release report

## Current boundary

- Canonical page files: **401 / 401**
- Printed contents entries captured: **110 / 110**
- Canonically completed letters: **110 / 110**
- Completed canonical letter range: **0001–0110**
- Partial canonical letter: **none**
- Canonical letter coverage: **PDF 024–400**; PDF 401 is non-letter back cover
- Current regular Volume 1 batch size: **10 letters**; the completed 0057–0076 iteration was explicitly expanded to 20 letters by the user
- Source-pagination anomaly recorded: printed page number **39** is skipped between PDF 039 and PDF 040, with continuous text
- Letter 0063 has no printed date and remains undated rather than inferred
- Scan-controlled forms in the final residue include letter 0107's ஆட்சி / மாட்சி wordplay, letter 0108's source-bold constitutional quotations and `சனநாயக` terminology, letter 0109's decorative `∵` lists and opaque printed `நமப்பார்வதி பதேக்கள்!`, and letter 0110's long 1949 quotation and four-exclamation `தமிழகமே!!!!` form
- Latest batch audit: [`BATCH_0107_0110_AUDIT.md`](BATCH_0107_0110_AUDIT.md)
- Legacy bilingual records preserved: **110 / 110** under `../volume-1/`
- Canonically migrated/verified English records: **0 / 110**

## Exact next task

Run the **full-volume Tamil structural audit** across PDF **001–401** / canonical letters **0001–0110**. Confirm that every PDF page has exactly one canonical page record, all 110 printed contents entries map to canonical chapter records, all letter start/end boundaries and dates/titles are internally consistent, letter 0063 remains undated, the printed-page-39 anomaly is documented without inventing missing text, and PDF 401 is correctly classified as non-letter back cover. Keep the legacy bilingual corpus untouched and do not start English migration until the structural audit and second visual/textual-fidelity gate are complete.
