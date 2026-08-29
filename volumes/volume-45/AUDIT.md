# Volume 45 Audit

## Source

The scan is authoritative. OCR, outside sources, another edition and historical expectation are not authoritative. The audited canonical Tamil is the immediate source for English translation/alignment; the scan remains ultimate authority if English review exposes a possible Tamil discrepancy.

## Tamil QA status

### Full-volume Tamil structural audit
Status: **PASS**

- Canonical coverage: PDF **001–402 / 402**.
- Front matter / contents: PDF **001–023**.
- Canonical source letters: **55 / 55 actual records, 3537–3591, PDF 024–401**.
- Back cover / publisher matter: PDF **402**.
- No partial source letter remains.
- Chapter ranges and contents mappings reconcile with the canonical page layer.

### Second full-volume visual/textual-fidelity audit
Status: **PASS — PDF 001–402 / 402**

Historical cumulative second-pass result: **243 corrected canonical page files / 623 correction spans**.

Direct scan verification resolved Letter 3576 to `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!`; stale `பார்!` is withdrawn. Letter 3575 retains the genuine contents `...!` versus actual letter-start `....!` difference. Letter 3586 is scan-proven as `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!`; stale `தமிழக அரசு...` is withdrawn.

Preserved source anomalies include PDF 088 `ஒப்பங்கள்`, PDF 098 `112.2006-ல்`, PDF 083 `94 இலட்சம் மக்கள்`, PDF 170 `பொக்கம்`, PDF 176 `10ந்தேதியன்று`, PDF 177 `முஜா கி தீன்`, PDF 217 `011ஆம் ஆண்டு`, PDF 233 `பொத்தம் 31 கேள்விகளில் 22 1 கேள்விகள்`, PDF 248 `என்னருந் தமிழ் மக்களுக்குக்`, PDF 259 `16-10-1999ந்தேதி`, and PDF 290 `18-5-2001`. Later library stamp/handwriting on PDF 102 remains excluded from edition text. Source-specific punctuation, English/Latin material, joined/spaced forms, repetitions and anomalies are not globally normalized.

See `FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md` for the completed second-pass page log.

### Translation-discovered targeted scan correction — PDF 187
Status: **CORRECTED, then PASS — 2026-08-28**

During English drafting/source-check of Letter 3560, the canonical PDF 187→188 transition exposed an omitted physical-page tail. Direct scan comparison restored the omitted end of the Wall Street Journal quotation and the beginning of the Oxford Analytica / `India Deconstructed` passage through `என்ற ஒரு ஆய்வை`.

PDF 187 was already one of the historical 243 corrected pages, so the historical tally remains **243 / 623**. This targeted repair adds **1 scan-proven correction span**, making the combined canonical correction tally **243 unique corrected page files / 624 spans**.

## Current Tamil QA boundary

- Canonical page coverage: **402 / 402**.
- Source-letter coverage: **55 / 55 — 3537–3591**.
- Full-volume Tamil structural audit: **PASS**.
- Second full-volume visual/textual-fidelity audit: **PASS**.
- Historical second-pass correction tally: **243 pages / 623 spans**.
- Translation-discovered post-audit correction: **PDF 187 / 1 span**.
- Combined canonical scan-proven correction tally: **243 unique pages / 624 spans**.
- Drafting batches 3565–3591 and alignment batches 3537–3581 exposed **no additional Tamil canonical correction**.

## English drafting QA boundary

- Pilot **3537–3539 / PDF 024–049**: PASS / style locked.
- Main drafting through **3591 / PDF 401**: **COMPLETE — 55 / 55 source-checked**.
- Cumulative translated source coverage: **PDF 024–401**.

## Bilingual alignment QA boundary

Completed alignment batches:

- **3537–3541 / PDF 024–060** — PASS — English corrections 0; Tamil changes 0.
- **3542–3546 / PDF 061–103** — PASS — English corrections 1; Tamil changes 0.
- **3547–3551 / PDF 104–141** — PASS — English corrections 0; Tamil changes 0.
- **3552–3556 / PDF 142–163** — PASS — English corrections 1; Tamil changes 0.
- **3557–3561 / PDF 164–196** — PASS — English corrections 2; Tamil changes 0.
- **3562–3566 / PDF 197–230** — PASS — English corrections 2; Tamil changes 0.
- **3567–3571 / PDF 231–260** — PASS — English corrections 1; Tamil changes 0.
- **3572–3576 / PDF 261–289** — PASS — English corrections 2; Tamil changes 0.
- **3577–3581 / PDF 290–337** — **PASS — 5 / 5 aligned; English corrections 0; Tamil changes 0.**

Current cumulative alignment: **45 / 55 — Letters 3537–3581 / PDF 024–337**.

The ninth batch directly compared all five complete bilingual records against their complete audited Tamil. It preserved PDF 290 `18-5-2001`; Letter 3577's own opening “three months” versus closing “two months” wording; Letter 3579's source-supplied *The Hindu* English; Letter 3580's George IPS English quotation and its Tamil rendering; and Letter 3581's complete `செம்மொழி வாழ்த்து` and textbook-removal catalogue. No English or Tamil correction was required.

Durable report: `translations/en/BILINGUAL_ALIGNMENT_REVIEW_3577_3581.md`.

For this batch, machine-readable alignment closure is additionally recorded in `translations/en/alignment-status/3577-3581.yml`. The large bilingual letter bodies retain their `translation_status: source-checked`; the report and sidecar record this separate meaning-level alignment gate. This does not imply editorial review or final release verification.

Current English QA totals:

- Source-checked: **55 / 55**.
- Bilingual-aligned: **45 / 55**.
- Editorially reviewed: **0 / 55**.
- Final verified for release: **0 / 55**.

## Exact next activity

Align **Letters 3582–3586 / PDF 338–369** as the next five-complete-letter bilingual-alignment batch:

- **3582** — `இனிய விழா; நமது இனத்தின் விழா!` — PDF 338–344.
- **3583** — `அதிகாரம் இல்லை? அந்தநாள் ஞாபகம் இல்லையா?` — PDF 345–351.
- **3584** — `அடிநாதமே; அறுக்கப்படுவதா?` — PDF 352–357.
- **3585** — `அய்யோ பாவம்! அ.தி.மு.க. அமைச்சர்கள்!!` — PDF 358–364.
- **3586** — `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!` — PDF 365–369.

Combined next range: **PDF 338–369 / 32 canonical pages**. Preserve Letter 3582's source-specific Thai/Chithirai/Tamil-New-Year claims without outside reconciliation, preserve source-supplied English exactly where printed, and retain Letter 3586's scan-proven title beginning `கழக அரசு`. If a possible Tamil defect appears, re-check the controlling scan before changing either layer. Keep the later volume-level English editorial consistency review separate.
