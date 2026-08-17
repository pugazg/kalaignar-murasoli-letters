# Volume 1 — Canonical Migration Progress

- [x] Migration audit completed against existing legacy Volume 1 corpus
- [x] Controlling `Vol1.pdf` verified: 401 PDF pages, 400 printed pages
- [x] New canonical `volumes/volume-01/` scaffold established
- [x] Canonical Tamil page/letter migration complete: **401 / 401 pages; 110 / 110 letters**
- [x] Full-volume Tamil structural audit — **PASS**
- [x] Second visual/textual-fidelity verification — **PASS; PDF 001–401 / 401 complete**
- [ ] Legacy English record migration and source checking — **in progress; 0001–0060 / 110 source-checked**
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
- Canonically migrated English records: **60 / 110**
- Canonically source-checked English records: **60 / 110**
- Completed canonical English range: **0001–0060**
- Bilingual-aligned canonical English records: **0 / 110**
- Verified canonical English records: **0 / 110**
- Source-check reports:
  - [`translations/en/SOURCE_CHECK_0001_0010.md`](translations/en/SOURCE_CHECK_0001_0010.md)
  - [`translations/en/SOURCE_CHECK_0011_0020.md`](translations/en/SOURCE_CHECK_0011_0020.md)
  - [`translations/en/SOURCE_CHECK_0021_0030.md`](translations/en/SOURCE_CHECK_0021_0030.md)
  - [`translations/en/SOURCE_CHECK_0031_0040.md`](translations/en/SOURCE_CHECK_0031_0040.md)
  - [`translations/en/SOURCE_CHECK_0041_0050.md`](translations/en/SOURCE_CHECK_0041_0050.md)
  - [`translations/en/SOURCE_CHECK_0051_0060.md`](translations/en/SOURCE_CHECK_0051_0060.md)
- Letter 0002 was corrected against scan-verified PDF 030 so Kamaraj's Deepavali quotation includes the source-visible `என்பதை இந்த ஆண்டு காண்கிறோம்` before the following sentence
- Letter 0010 follows scan-verified PDF 063 `ரன்னர்` and therefore uses **Runner Cup**, not the stale legacy `Rainer` reading
- Letter 0018 preserves the deliberate censored ellipses on PDF 095 without reconstruction
- Letter 0019 restores and translates the scan-visible PDF 099 passages absent from the legacy reading copy
- Letter 0020 excludes the PDF 101 library stamp and handwritten accession marks as non-authorial artefacts
- Letter 0028 follows the source-printed sign-off date **28-12-1968**, preserving the source/date anomaly rather than silently normalising to the frozen legacy metadata
- Letters 0031–0040 are migrated and source-checked across PDF **136–177** with no new substantive English omission found
- Letter 0036 retains printed `சி. பி. சி.` / `C. P. C.` without speculative expansion
- Letter 0037 follows the scan-supported title `தூங்குவோமா?`, not the earlier OCR corruption `தாங்குவோமா?`
- Letters 0038–0040 preserve the source-supported membership directive, General Council programme, P. Kannan private-letter quotation, dramatic titles and closing Tirukkural
- Letters 0041–0050 are migrated and source-checked across PDF / printed pages **178–213** with no new substantive English omission identified
- Letters 0042–0044 preserve the linked anti-violence argument and political examples; letters 0045–0046 preserve the complete two-part Madurai conference sequence
- Letter 0047 preserves the `நாடு + அகம் = நாடகம்` wordplay and closing proverb reversal
- Letter 0048 preserves printed `சென்னை. / 10.10.1972` as source evidence despite the internal later-time indicator; no unsupported composition date is inferred
- Letter 0049 preserves Anna's complete 1961 quoted reply and `நெஞ்சகம் / அன்பகம் / அறிவகம்` wordplay
- Letter 0050 preserves the *Navasakthi* chronology, Madurai conference financial figures and elephant-pit image
- Letters 0051–0060 are migrated and source-checked across PDF / printed pages **214–249** with no new substantive English omission identified
- Letter 0051 preserves the earthen-lamp metaphor, personal Muthu/Padmavathi passage and complete Anna reform quotation
- Letter 0052 preserves the Anna memorial sequence, State-autonomy and anti-Hindi passages, and Kattabomman/Ettappan warning
- Letters 0053–0057 preserve the Dindigul political sequence, policy examples, 1952 Rajaji precedent and Rickshaw Fund appeal
- Letter 0054 follows source figure **(6908)** and retains `ஆறாயிரத்துத்தொள்ளாயிரத்து எட்டு`
- Letter 0058 follows authoritative date **29-05-1973**, not the stale legacy note claiming a 1978 metadata date
- Letter 0059 preserves the complete R. M. Veerappan quotation and cadre-history argument
- Letter 0060 preserves the plane-crash chronology and personal recollections of Mohan Kumaramangalam, Gurnam Singh and Baladhandayutham

## Exact next task

Migrate and source-check canonical English letters **0061–0070** as the next Volume 1 ten-letter batch. Use the preserved legacy bilingual records only as reusable drafts/evidence; verified canonical Tamil and the controlling `Vol1.pdf` remain authoritative. Preserve Kalaignar's thought order, rhetoric and political language. Keep bilingual alignment as a separate later gate and do not mark these records `verified` before that review.