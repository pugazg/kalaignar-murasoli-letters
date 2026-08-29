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

Preserved source anomalies include PDF 088 `ஒப்பங்கள்`, PDF 098 `112.2006-ல்`, PDF 083 `94 இலட்சம் மக்கள்`, PDF 170 `பொக்கம்`, PDF 176 `10ந்தேதியன்று`, PDF 177 `முஜா கி தீன்`, PDF 217 `011ஆம் ஆண்டு`, PDF 233 `பொத்தம் 31 கேள்விகளில் 22 1 கேள்விகள்`, PDF 248 `என்னருந் தமிழ் மக்களுக்குக்`, PDF 259 `16-10-1999ந்தேதி`, PDF 290 `18-5-2001`, and the physical PDF 348→349 form `வாக்க` / `எதிரிகளை`. Later library stamp/handwriting on PDF 102 remains excluded from edition text. Source-specific punctuation, English/Latin material, joined/spaced forms, repetitions and anomalies are not globally normalized.

See `FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md` for the completed second-pass page log.

### Translation-discovered targeted scan correction — PDF 187
Status: **CORRECTED, then PASS — 2026-08-28**

During English drafting/source-check of Letter 3560, the canonical PDF 187→188 transition exposed an omitted physical-page tail. Direct scan comparison restored the omitted end of the Wall Street Journal quotation and the beginning of the Oxford Analytica / `India Deconstructed` passage through `என்ற ஒரு ஆய்வை`.

PDF 187 was already one of the historical 243 corrected pages, so the historical tally remains **243 / 623**. This targeted repair adds **1 scan-proven correction span**, making the combined canonical correction tally **243 unique corrected page files / 624 spans**.

### Alignment-triggered scan re-check — PDF 348→349
Status: **SCAN CONFIRMED; NO TAMIL CHANGE — 2026-08-29**

During bilingual alignment of Letter 3583, the English phrase “class enemies” raised a possible source-normalization issue. The canonical Tamil is split physically across PDF 348→349 as `வாக்க` / `எதிரிகளை`. A direct re-render and scan inspection confirmed that the printed page really ends with `வாக்க` and the following page begins `எதிரிகளை`.

The canonical Tamil therefore remains unchanged. The English was corrected conservatively from **“the policy of eliminating class enemies”** to **“a policy of eliminating enemies”**, avoiding a silent normalization to the unprinted `வர்க்க எதிரிகளை`. This event does not change the Tamil correction counts.

## Current Tamil QA boundary

- Canonical page coverage: **402 / 402**.
- Source-letter coverage: **55 / 55 — 3537–3591**.
- Full-volume Tamil structural audit: **PASS**.
- Second full-volume visual/textual-fidelity audit: **PASS**.
- Historical second-pass correction tally: **243 pages / 623 spans**.
- Translation-discovered post-audit correction: **PDF 187 / 1 span**.
- Combined canonical scan-proven correction tally: **243 unique pages / 624 spans**.
- Alignment re-check PDF 348→349: **source form confirmed; no Tamil correction**.
- Drafting batches 3565–3591 and alignment batches 3537–3586 exposed **no additional Tamil canonical correction** beyond the already recorded PDF 187 event.

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
- **3577–3581 / PDF 290–337** — PASS — English corrections 0; Tamil changes 0.
- **3582–3586 / PDF 338–369** — **PASS — 5 / 5 aligned; English corrections 1; Tamil changes 0.**

Current cumulative alignment: **50 / 55 — Letters 3537–3586 / PDF 024–369**.

The tenth batch directly compared all five complete bilingual records against their complete audited Tamil. Letter 3583 required one English-only correction after direct scan confirmation of the source form `வாக்க` / `எதிரிகளை`; no Tamil change was required. Letter 3582's Thai/Chithirai/Tamil-New-Year claims remain source-specific and unreconciled externally. Letter 3586 retains its scan-proven title beginning `கழக அரசு`.

Durable report: `translations/en/BILINGUAL_ALIGNMENT_REVIEW_3582_3586.md`.

Machine-readable alignment closure: `translations/en/alignment-status/3582-3586.yml`. The large bilingual letter bodies retain their `translation_status: source-checked`; the report and sidecar record the separate meaning-level alignment gate. This does not imply editorial review or final release verification.

Current English QA totals:

- Source-checked: **55 / 55**.
- Bilingual-aligned: **50 / 55**.
- Editorially reviewed: **0 / 55**.
- Final verified for release: **0 / 55**.

## Exact next activity

Complete the **final bilingual-alignment batch, Letters 3587–3591 / PDF 370–401**:

- **3587** — `மாமியார் உடைத்ததும்; மருமகள் உடைத்ததும்!` — PDF 370–376.
- **3588** — `கல்வி; கருகிடும் மொட்டாவதா?` — PDF 377–382.
- **3589** — `எத்தனை காலமோ; இந்த ஏட்டிக்குப் போட்டி?` — PDF 383–390.
- **3590** — `விரைந்தெழுவீர்; வெற்றிக்கனி பறித்திட!` — PDF 391–396.
- **3591** — `அடங்காமை ஆறிருள் உய்த்து விடும்!` — PDF 397–401.

Combined final range: **PDF 370–401 / 32 canonical pages**. Preserve source anomalies, source-supplied English, dates, figures, punctuation and physical boundaries exactly. If a possible Tamil defect appears, re-check the controlling scan before changing either layer. Keep the later volume-level English editorial consistency review separate until the final five records have passed alignment and the **55 / 55** alignment boundary is durably recorded.
