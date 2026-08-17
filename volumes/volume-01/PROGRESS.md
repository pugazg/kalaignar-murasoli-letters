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
- [x] Full-volume Tamil structural audit
- [ ] Second visual/textual-fidelity verification — **in progress; PDF 001–100 / 401 complete**
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
- Full-volume Tamil structural audit: **PASS — complete**; report: [`FULL_VOLUME_STRUCTURAL_AUDIT.md`](FULL_VOLUME_STRUCTURAL_AUDIT.md)
- Second visual/textual-fidelity verification: **in progress — PDF 001–100 / 401 complete**
- Fidelity reports completed:
  - [`translations/en/TEXTUAL_FIDELITY_AUDIT_001_025.md`](translations/en/TEXTUAL_FIDELITY_AUDIT_001_025.md)
  - [`translations/en/TEXTUAL_FIDELITY_AUDIT_026_050.md`](translations/en/TEXTUAL_FIDELITY_AUDIT_026_050.md)
  - [`translations/en/TEXTUAL_FIDELITY_AUDIT_051_075.md`](translations/en/TEXTUAL_FIDELITY_AUDIT_051_075.md)
  - [`translations/en/TEXTUAL_FIDELITY_AUDIT_076_100.md`](translations/en/TEXTUAL_FIDELITY_AUDIT_076_100.md)
- Cumulative second-pass corrections: **36 canonical pages / 74 spans**
- PDF 076–100 required scan-proven corrections on **18 canonical pages / 44 spans**
- PDF 076 removes a duplicated paragraph that belongs to the end of PDF 075; the source starts directly with `இந்த அசைக்க முடியாத மனதிடத்துடன்...`
- PDFs 082–095 restore scan-controlled abbreviation spacing, source hyphenation and extensive source-bold emphasis, including `பி. சோ.`, `தி. மு. க.`, `தி. மு.`, `1966 ஆம்`, and the newspaper/judicial quotation blocks
- PDF 087 restores source `பையனுக்கு தொண்டையில்`; PDF 088 removes a first-pass closing quotation mark absent from the scan
- PDFs 097–100 restore the source-bold Morarji Desai, Assembly, Anna and Hindi-policy quotation blocks
- Letters **0001–0019** now have complete second-pass source-page coverage
- The structural audit confirmed exactly one canonical page record for PDF 001–401 and exactly 110 numbered canonical chapter records, with continuous letter coverage PDF 024–400 and no gap or overlap
- Source-pagination anomaly recorded: printed page number **39** is skipped between PDF 039 and PDF 040, with continuous text
- Letter 0063 has no printed date and remains undated rather than inferred
- Printed-contents wording remains literal where it differs from actual heading pages; letter 0109 contents `அவள் ஒரு தொடற்கதை!` differs from actual PDF-392 heading `அவள் ஒரு தொடர்கதை!`
- Legacy bilingual records preserved: **110 / 110** under `../volume-1/`
- Canonically migrated/verified English records: **0 / 110**

## Exact next task

Continue the **second visual/textual-fidelity verification with PDF 101–125**, comparing every canonical Markdown page directly against the controlling scan, applying only scan-proven corrections and recording the next range audit/cumulative status. Keep the legacy bilingual corpus untouched. Do not begin canonical English migration while the required second visual/textual-fidelity gate remains incomplete.
