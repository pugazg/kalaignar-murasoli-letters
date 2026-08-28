# Volume 45 Audit

## Source

The scan is authoritative. OCR and external sources are not authoritative.

## Tamil QA status

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

Historical cumulative second-pass result: **243 corrected canonical page files / 623 correction spans**.

Direct scan verification resolved Letter 3576 to `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!`; stale control-layer `பார்!` wording is withdrawn. Letter 3575 retains the genuine contents `...!` versus letter-start `....!` difference. Letter 3586 is scan-proven as `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!`; stale `தமிழக அரசு...` wording is withdrawn.

Source anomalies remain preserved, including PDF 088 `ஒப்பங்கள்`, PDF 098 `112.2006-ல்`, PDF 083 `94 இலட்சம் மக்கள்`, PDF 170 `பொக்கம்`, PDF 176 `10ந்தேதியன்று`, PDF 177 `முஜா கி தீன்`, PDF 217 `011ஆம் ஆண்டு`, PDF 233 `பொத்தம் 31 கேள்விகளில் 22 1 கேள்விகள்`, PDF 248 `என்னருந் தமிழ் மக்களுக்குக்`, PDF 259 `16-10-1999ந்தேதி`, and PDF 290 `18-5-2001`. Later library stamp/handwriting on PDF 102 remains excluded from edition text. Source-specific punctuation, English/Latin material, joined/spaced forms, repetitions and anomalies are not globally normalized.

See `FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md` for the completed second-pass page log.

### Translation-discovered targeted scan correction — PDF 187
Status: **CORRECTED, then PASS — 2026-08-28**

During English drafting/source-check of Letter 3560, the canonical PDF 187→188 transition exposed an omitted physical-page tail. Direct scan comparison restored the omitted end of the Wall Street Journal quotation and the beginning of the Oxford Analytica / `India Deconstructed` passage through `என்ற ஒரு ஆய்வை`.

`pages/page-187.md` was corrected from the scan before Letter 3560 was marked source-checked. No wording was reconstructed from outside knowledge. The complete correction is documented in `translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md`.

PDF 187 was already one of the historical 243 corrected pages, so the historical tally remains **243 / 623**. This targeted repair adds **1 scan-proven correction span**, making the combined canonical correction tally **243 unique corrected page files / 624 spans**.

## Current Tamil QA boundary

- Canonical page coverage: **402 / 402**.
- Source-letter coverage: **55 / 55**, Letters 3537–3591.
- Full-volume Tamil structural audit: **PASS**.
- Historical second full-volume visual/textual-fidelity audit: **PASS — 243 corrected page files / 623 spans**.
- Translation-discovered post-audit correction: **PDF 187 / 1 additional span**.
- Combined canonical scan-proven correction tally: **243 unique page files / 624 spans**.
- Translation batches 3565–3591 exposed **no additional Tamil canonical correction**.

## English drafting QA boundary

- Pilot **3537–3539 / PDF 024–049**: PASS / style locked.
- Ten normal batches through **3585–3589 / PDF 358–390**: PASS / source-checked.
- Final batch **3590–3591 / PDF 391–401**: PASS / 2 of 2 source-checked.
- Current English total: **55 / 55 — Letters 3537–3591**.
- Cumulative translated source coverage: **PDF 024–401**.
- Bilingual alignment: **0 / 55**; not yet begun.

The final source check preserves Letter 3590's complete local-body election timetable, constituency-classification and nomination dispute, State Election Commission and *Dina Thanthi* material, false-case/re-arrest allegations, election-expense warning, media-bias argument and mobilisation close. Letter 3591 preserves the complete K.P.P. Samy arrest narrative, quoted Samy statement and police-transfer report, the full quoted **21-3-2002** Bala letter, M.K. Balan/Jayakumar/Jothi Krishnan comparisons, Madras High Court/Justice C.P. Selvam passage and the closing Valluvar Kural argument. No Tamil canonical change was required in 3590–3591.

## Main drafting closure

English main drafting is **COMPLETE — 55 / 55 source-checked**. These remain drafts for the purposes of final bilingual verification.

## Exact next activity

Begin the separate **full bilingual-alignment QA gate** across all 55 letters. Compare each English record directly against authoritative audited Tamil and correct any omission, addition, semantic drift, figure/date/name error, quotation loss or rhetorical-force distortion before marking it bilingual-aligned. Keep the later volume-level English editorial consistency review separate.
