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
- Current English source-check total: **55 / 55 — Letters 3537–3591**.
- Cumulative translated source coverage: **PDF 024–401**.

English main drafting is **COMPLETE — 55 / 55 source-checked**.

## Bilingual alignment QA boundary

First alignment batch completed:

- **3537–3541 / PDF 024–060** — **PASS — 5 / 5 aligned**.
- English semantic corrections required/applied: **0**.
- Tamil canonical corrections required: **0**.
- Durable report: `translations/en/BILINGUAL_ALIGNMENT_REVIEW_3537_3541.md`.

The first batch directly checked complete Tamil↔English coverage including titles, salutations, paragraph order, claims, quotations, dates, figures, units, rhetorical force and closings. Existing documented source anomalies in Letters 3539–3540 were retained without external normalisation.

Current English QA totals:

- Source-checked: **55 / 55**.
- Bilingual-aligned: **5 / 55**.
- Editorially reviewed: **0 / 55**.
- Final verified for release: **0 / 55**.

## Exact next activity

Align **Letters 3542–3546 / PDF 061–103** as the next five-complete-letter bilingual-alignment batch. Preserve Letter 3545's unusual printed `112.2006-ல்` on PDF 098 and the existing exclusion of later library stamp/handwriting on Letter 3546 / PDF 102. If alignment exposes any possible Tamil defect, re-check the controlling scan before changing either layer. Keep the later volume-level English editorial consistency review separate.
