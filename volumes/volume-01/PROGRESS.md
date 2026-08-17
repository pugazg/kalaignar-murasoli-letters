# Volume 1 — Canonical Migration Progress

- [x] Migration audit completed against existing legacy Volume 1 corpus
- [x] Controlling `Vol1.pdf` verified: 401 PDF pages, 400 printed pages
- [x] New canonical `volumes/volume-01/` scaffold established
- [x] Canonical Tamil page/letter migration complete: **401 / 401 pages; 110 / 110 letters**
- [x] Full-volume Tamil structural audit — **PASS**
- [x] Second visual/textual-fidelity verification — **PASS; PDF 001–401 / 401 complete**
- [ ] Legacy English record migration and source checking — **in progress; 0001–0010 / 110 source-checked**
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
- Full-volume second visual/textual-fidelity verification: **PASS — PDF 001–401 / 401 complete**; closure report: [`FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md)
- Cumulative second-pass corrections: **159 canonical pages / 274 spans**
- Letters **0001–0110** have complete second-pass source-page coverage
- Source-pagination anomaly recorded: printed page number **39** is skipped between PDF 039 and PDF 040, with continuous text
- Letter 0063 has no printed date and remains undated rather than inferred
- Printed-contents wording remains literal where it differs from actual heading pages; letter 0109 contents `அவள் ஒரு தொடற்கதை!` differs from actual PDF-392 heading `அவள் ஒரு தொடர்கதை!`
- Legacy bilingual records preserved unchanged: **110 / 110** under `../volume-1/`
- Canonically migrated English records: **10 / 110**
- Canonically source-checked English records: **10 / 110**
- Completed canonical English range: **0001–0010**
- Bilingual-aligned canonical English records: **0 / 110**
- Verified canonical English records: **0 / 110**
- First canonical English source-check report: [`translations/en/SOURCE_CHECK_0001_0010.md`](translations/en/SOURCE_CHECK_0001_0010.md)
- Letter 0002 was corrected against scan-verified PDF 030 so Kamaraj's Deepavali quotation includes the source-visible `என்பதை இந்த ஆண்டு காண்கிறோம்` before the following sentence
- Letter 0010 follows scan-verified PDF 063 `ரன்னர்` and therefore uses **Runner Cup**, not the stale legacy `Rainer` reading
- Letter 0009's embedded Tamil incorporates the second-pass source forms from PDFs 058 and 060–062

## Exact next task

Migrate and source-check canonical English letters **0011–0020** as the next Volume 1 ten-letter batch. Use the preserved legacy bilingual records only as reusable drafts/evidence; verified canonical Tamil and the controlling `Vol1.pdf` remain authoritative. Preserve Kalaignar's thought order, rhetoric and political language. Keep bilingual alignment as a separate later gate and do not mark these records `verified` before that review.
