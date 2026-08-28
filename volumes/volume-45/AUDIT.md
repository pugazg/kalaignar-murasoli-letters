# Volume 45 Audit

## Source

The scan is authoritative. OCR and external sources are not authoritative.

## Intake observations

- Volume number verified from scan as 45.
- Contents pages are navigation aids only.
- Source anomalies must be preserved.

## Tamil QA status

### First-pass transcription / iteration coverage

- Batch 001 — PDF 001–025: first-pass reviewed.
- Immediate continuation — Letter 3537, PDF 026–033: first-pass reviewed.
- Letters 3538–3542, PDF 034–068: first-pass reviewed.
- Letters 3543–3547, PDF 069–110: first-pass reviewed.
- Letters 3548–3552, PDF 111–144: first-pass reviewed.
- Letters 3553–3557, PDF 145–169: first-pass reviewed.
- Letters 3558–3562, PDF 170–200: first-pass reviewed.
- Letters 3563–3567, PDF 201–235: first-pass reviewed.
- Letters 3568–3572, PDF 236–265: first-pass reviewed.
- Letters 3573–3577, PDF 266–305: first-pass reviewed.
- Letters 3578–3582, PDF 306–344: first-pass reviewed.
- Letters 3583–3587, PDF 345–376: first-pass reviewed.
- Letters 3588–3591, PDF 377–401: first-pass reviewed.
- PDF 402: back cover / publisher matter reviewed.

Important first-pass source conditions remain preserved: PDF 098 unusual `112.2006-ல்`; PDF 102 later library stamp/handwriting excluded; PDF 164 `ஆகஸ்ட் 13ஆம் தேதியன்றே`; PDF 166 direct-scan transcription after weak OCR; PDF 208/232/237/241/253/315/325/335/347/385 and other documented pages received direct scan re-reading where OCR was inadequate; Letter 3567's repeated 10-6-2011 material is not deduplicated; Letter 3681 belongs to another volume and does not affect this volume.

### Scan-proven contents/title correction pass — PDF 018–022
Status: corrected during second-pass direct scan re-verification.

- Source three-column contents structure restored.
- False contents/letter-start discrepancy records withdrawn for 3565, 3568–3570, 3572, 3579, 3581 and 3586.
- Direct scan verification at PDF 284 resolved Letter 3576 in favor of the source start-title `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!`.
- Genuine source-context difference retained: Letter 3575 contents `...!` vs letter-start `....!`.

### Full-volume Tamil structural audit
Status: **PASS**

- Canonical coverage: PDF 001–402.
- Front matter / contents: PDF 001–023.
- Canonical source letters: 55 actual records, 3537–3591, PDF 024–401.
- Back cover / publisher matter: PDF 402.
- No partial source letter remains.
- Chapter ranges and contents mappings reconcile with the canonical page layer.
- See `FULL_VOLUME_STRUCTURAL_AUDIT.md` for the structural gate report.

### Second full-volume visual/textual-fidelity audit
Status: **PASS — verified PDF 001–402 / 402**

- PDF 001–060: cumulative checkpoint 37 corrected page files / 75 correction spans.
- PDF 061–085: 18 corrected page files / 29 correction spans.
- PDF 086–110: 12 corrected page files / 26 correction spans.
- PDF 111–135: 8 corrected page files / 14 correction spans.
- PDF 136–160: 8 corrected page files / 13 correction spans.
- PDF 161–185: 15 corrected page files / 63 correction spans.
- PDF 186–210: 19 corrected page files / 64 correction spans.
- PDF 211–235: 22 corrected page files / 63 correction spans.
- PDF 236–260: 23 corrected page files / 73 correction spans.
- PDF 261–285: 19 corrected page files / 74 correction spans.
- PDF 286–310: 21 corrected page files / 67 correction spans.
- PDF 311–335: 9 corrected page files / 15 correction spans.
- PDF 336–360: 7 corrected page files / 16 correction spans.
- PDF 361–385: 9 corrected page files / 13 correction spans; 16 pages passed unchanged.
- PDF 386–402: **16 corrected page files / 18 correction spans; 1 page passed unchanged**.
- PDF 386–401 had systematic spurious zero-width OCR characters removed. This is source-fidelity cleanup, not language normalization.
- PDF 388 additionally restores source spacing `பொறியியல் தொழில் நுட்பவியல்`.
- PDF 389 additionally restores source punctuation `காரணம், அவர்கள்`.
- PDF 402 back cover / publisher matter passed unchanged.
- Direct scan verification at PDF 284 resolved the earlier Letter 3576 title record to `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!`; stale control-layer `பார்!` wording is withdrawn.
- Source anomalies remain preserved, including PDF 088 `ஒப்பங்கள்`, PDF 098 `112.2006-ல்`, PDF 083 `94 இலட்சம் மக்கள்`, PDF 170 `பொக்கம்`, PDF 176 `10ந்தேதியன்று`, PDF 177 `முஜா கி தீன்`, PDF 217 `011ஆம் ஆண்டு`, PDF 233 `பொத்தம் 31 கேள்விகளில் 22 1 கேள்விகள்`, PDF 248 `என்னருந் தமிழ் மக்களுக்குக்`, PDF 259 `16-10-1999ந்தேதி`, and PDF 290 `18-5-2001`.
- Later library stamp/handwriting on PDF 102 remains excluded from edition text.
- Source-specific punctuation, English/Latin material, joined/spaced forms, repetitions and anomalies are not globally normalized.
- Historical cumulative second-pass result: **243 corrected canonical page files / 623 correction spans**.
- See `FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md` for the completed second-pass page log.

### Translation-discovered targeted scan correction — PDF 187
Status: **CORRECTED, then PASS — 2026-08-28**

During English drafting/source-check of Letter 3560, the canonical transition from PDF 187 to PDF 188 proved syntactically discontinuous: page 187 ended during the Wall Street Journal passage after `நிலங்கள், சாலைகள்`, while page 188 began `நடத்தியது.` in the Oxford Analytica passage.

The controlling PDF page 187 was re-rendered and directly compared. The scan proved that the canonical page had omitted the physical-page tail containing:

- the continuation and close of the Wall Street Journal quotation about basic infrastructure and single-window government approvals; and
- the beginning of the Oxford Analytica / `India Deconstructed` passage through the page-ending words `என்ற ஒரு ஆய்வை`.

`pages/page-187.md` was corrected from the scan before Letter 3560 was marked source-checked. No wording was reconstructed from outside knowledge. The complete correction is documented in `translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md`.

PDF 187 was already one of the 243 unique page files corrected during the historical second pass, so the unique corrected-page count remains **243**. This targeted repair adds **1 scan-proven correction span**, making the combined canonical correction tally **243 unique corrected page files / 624 spans**, while the historical second-pass tally remains **243 / 623**.

## Current Tamil QA boundary

- Canonical page coverage: **402 / 402**.
- Source-letter coverage: **55 / 55**, Letters 3537–3591.
- Full-volume Tamil structural audit: **PASS**.
- Historical second full-volume visual/textual-fidelity audit: **PASS — 243 corrected page files / 623 spans**.
- Translation-discovered post-audit correction: **PDF 187 / 1 additional span**.
- Combined canonical scan-proven correction tally: **243 unique page files / 624 spans**.
- Translation batches 3565–3569 and 3570–3574 exposed **no additional Tamil canonical correction**.

## English QA boundary

- Pilot **3537–3539 / PDF 024–049**: PASS / style locked.
- Normal batches through **3570–3574 / PDF 249–274**: source-checked.
- Current English total: **38 / 55 — Letters 3537–3574**.
- Cumulative translated source coverage: **PDF 024–274**.
- Bilingual alignment: **0 / 55**; not yet begun.

The 3570–3574 source check explicitly preserves the Omandurar Secretariat figures and political argument; Letter 3571's TANSI/inquiry narrative, source `12.462 சதுர மீட்டர்` and split `26-` / `10-99ந்தேதி` page boundary; Letter 3572's attributed tax/debt/Samacheer statements and `100 Karunanidhis` reversal; Letter 3573's Manohara and Mahakali/Bhadrakali imagery; and Letter 3574's full Samacheer Kalvi chronology with the source-printed English High Court sentence represented separately from the source's Tamil rendering.

## Exact next activity

Translate **Letters 3575–3579 / PDF 275–319** as the next normal five-letter drafting/source-check batch. Preserve Letter 3575's genuine contents/start punctuation difference and Letter 3576's scan-proven `பாரீர்!` start title. Continue to treat any translation-exposed Tamil discontinuity as a trigger for targeted direct scan re-verification before changing either layer. Do not begin the separate bilingual-alignment gate during drafting.
