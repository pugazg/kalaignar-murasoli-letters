# மின்னாக்க முன்னேற்றம் — தொகுதி 47

- [x] Repository-level processing, transcription and batching guides read
- [x] Volume 49 reference implementation reviewed
- [x] Completed Volume 48 release preserved untouched
- [x] Volume number, source filename, SHA-256, byte size and 401-page count recorded
- [x] Canonical Tamil transcription complete for PDF 1–401
- [x] Complete letters 3647–3680 and 3682–3705: 58 letters
- [x] Source-incomplete letter 3681: available PDF 249–252 / printed 248–251; printed page 252 missing
- [x] All 59 letter records 3647–3705 present
- [x] Full-volume Tamil structural audit
- [ ] Second visual verification / close character-level review — in progress
  - [x] PDF 001–025 — 25/25 visually compared; 4 canonical pages corrected
  - [x] PDF 026–050 — 25/25 visually compared; 4 canonical pages corrected
  - [x] User-requested 15-letter fidelity batch 3650–3664 — new pages PDF 051–140, 90/90 visually compared; 2 canonical pages corrected
  - [ ] PDF 141–401
- [ ] Mandatory textual-fidelity audits before any translation — in progress
  - [x] `translations/en/TEXTUAL_FIDELITY_AUDIT_001_025.md`
  - [x] `translations/en/TEXTUAL_FIDELITY_AUDIT_026_050.md`
  - [x] `translations/en/TEXTUAL_FIDELITY_AUDIT_051_140.md`
  - [ ] PDF 141 onward
- [ ] English translation
- [ ] Bilingual alignment and editorial release

## Source gap — letter 3681

The only available Volume 47 source jumps from **PDF 252 / printed page 251** to **PDF 253 / printed page 253**. PDF 252 ends letter 3681 in the middle of the sentence after `அடிப்படையான வேளாண்மை, வணிகம், சிறுதொழில் மற்றும்`; PDF 253 starts letter 3682. Printed page **252** is absent. The missing continuation, closing and printed date have not been reconstructed or guessed.

## Second visual / textual-fidelity progress

Cumulative second-pass source coverage is now **PDF 001–140**.

- Earlier corrections: PDF **002, 003, 004, 016, 027, 044, 048, 049**.
- This 15-letter batch: PDF **052** `கேட்டபதைப்போல` → `கேட்பதைப்போல`; PDF **054** `வெளியேந்தோரின்` → `வெளிவந்தோரின்`, and `வெளியேகொண்டுவரப்பட்டுள்ள` → `வெளிக்கொணரப்பட்டுள்ள`.
- Letters **3650–3664** now have complete second-pass source coverage. Letter 3650 combines the previous PDF 047–050 audit with this batch's PDF 051–052.
- All 15 closing/signature/date pages were visually checked: PDF **052, 059, 064, 071, 078, 083, 089, 096, 099, 110, 116, 121, 127, 132, 140**.
- The printed-contents/actual-heading discrepancy for letter **3663** remains preserved: contents `நெஞ்சைத் துளைத்திடும் கொடுமை இது!`; PDF 128 heading `நெஞ்சைத் துளைத்திடும் தொடர்கதை இது!`.
- PDF **141** was inspected only to verify that letter **3665** begins there; no 3665 body is included in this audit batch.

English translation remains unstarted while the project-level Tamil fidelity gate is in progress.

## Next exact task

Proceed with the next 15-letter second-pass fidelity batch, **letters 3665–3679**, beginning at **PDF 141**. Based on verified chapter boundaries, that batch runs through **PDF 243**; PDF 244 begins letter 3680 and is the next boundary page.
