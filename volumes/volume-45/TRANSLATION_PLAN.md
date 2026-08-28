# Volume 45 English Translation Plan

## Objective

Create a clear, faithful English translation of Volume 45 that preserves Kalaignar's thought order, political judgement, evidence, irony, direct address, repetition, rhetorical questions and emotional emphasis without turning the letters into literary or academic rewrites.

The audited canonical Tamil is the immediate translation/alignment source. The controlling scan remains the ultimate textual authority.

## Tamil QA prerequisite

Both Tamil gates are complete and durable:

- full-volume Tamil structural audit: **PASS**;
- second full-volume direct visual/textual-fidelity verification: **PASS — PDF 001–402 / 402**.

Historical second-pass correction tally: **243 canonical page files / 623 correction spans**. Letter 3560 translation/source-check exposed one residual omission on already-corrected PDF 187, directly repaired from the scan. Combined canonical tally: **243 unique page files / 624 scan-proven spans**. See [`translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md`](translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md).

If translation or alignment exposes a possible Tamil discrepancy, stop at that point and re-check the controlling scan before changing either layer.

## Mandatory translator’s note and bilingual order

Every translated letter uses the locked standard translator’s note and this order:

1. YAML source/translation metadata;
2. English title;
3. standard translator’s note;
4. Tamil chapter link, canonical PDF range and date;
5. complete English translation;
6. letter-specific notes only where necessary;
7. **Original Tamil — மூலத் தமிழ்**, reproduced in full from audited canonical page files in physical page order.

The Tamil section is never a summary or selected extract.

## Translation principles

1. Preserve thought order before ornament.
2. Do not summarise substantive source material.
3. Use direct, natural contemporary English without adding interpretation.
4. Preserve political force, irony, accusation, repetition and rhetorical questions.
5. Preserve quoted voices and attribution.
6. Preserve names, institutions, dates, figures and units; do not correct them from outside knowledge.
7. Retain `lakh` and `crore`.
8. Do not silently repair source anomalies.
9. A translation- or alignment-discovered Tamil discrepancy requires targeted scan comparison before either layer changes.
10. Preserve deliberate source repetition.
11. Add only minimal explanatory notes.
12. Keep every translation traceable to its chapter and canonical pages.

Working terminology is maintained in [`translations/en/GLOSSARY.md`](translations/en/GLOSSARY.md). Core locked forms include `Udanpirappē`, `With affection, M.K.`, DMK / AIADMK, `lakh` / `crore`, **Samacheer Kalvi**, and the source-specific **Tamil New Year / first day of Thai** treatment where those terms recur.

## Workflow status

### Phase 1 — Pilot and style lock — COMPLETE

- **3537–3539 / PDF 024–049** — **3 / 3 source-checked; PASS — STYLE LOCKED**.

### Phase 2 — Main translation drafting — COMPLETE

Completed drafting iterations:

- **3540–3544 / PDF 050–088** — PASS
- **3545–3549 / PDF 089–122** — PASS
- **3550–3554 / PDF 123–154** — PASS
- **3555–3559 / PDF 155–180** — PASS
- **3560–3564 / PDF 181–217** — PASS; PDF 187 scan-proven Tamil repair
- **3565–3569 / PDF 218–248** — PASS; Tamil changes 0
- **3570–3574 / PDF 249–274** — PASS; Tamil changes 0
- **3575–3579 / PDF 275–319** — PASS; Tamil changes 0
- **3580–3584 / PDF 320–357** — PASS; Tamil changes 0
- **3585–3589 / PDF 358–390** — PASS; Tamil changes 0
- **3590–3591 / PDF 391–401** — PASS; Tamil changes 0

Main drafting state: **3537–3591 / 55 of 55 source-checked**, audited canonical PDF **024–401**.

### Phase 3 — Bilingual alignment QA — IN PROGRESS

Completed:

- **3537–3541 / PDF 024–060** — **PASS — 5 / 5 aligned**; English corrections 0; Tamil changes 0.
- **3542–3546 / PDF 061–103** — **PASS — 5 / 5 aligned**; English corrections 1; Tamil changes 0.
- **3547–3551 / PDF 104–141** — **PASS — 5 / 5 aligned**; English corrections 0; Tamil changes 0.
- **3552–3556 / PDF 142–163** — **PASS — 5 / 5 aligned**; English corrections 1; Tamil changes 0.
- **3557–3561 / PDF 164–196** — **PASS — 5 / 5 aligned**; English corrections 2; Tamil changes 0.
- **3562–3566 / PDF 197–230** — **PASS — 5 / 5 aligned**; English corrections 2; Tamil changes 0.
- **3567–3571 / PDF 231–260** — **PASS — 5 / 5 aligned**; English corrections 1; Tamil changes 0.

Current cumulative alignment: **35 / 55 — 3537–3571 / PDF 024–260**.

The seventh batch's correction was English-only. In Letter 3571, the source phrase `அப்படிப்பட்ட குற்றவாளி கிருஷ்ணமூர்த்தியுடன்` is now represented as **“Krishnamoorthy, whom the source describes as ‘such a criminal.’”** rather than the softer “such an accused person.” Canonical Tamil remained unchanged, including the established anomalies PDF 233 `பொத்தம் 31 கேள்விகளில் 22 1 கேள்விகள்`, PDF 248 `என்னருந் தமிழ் மக்களுக்குக்`, and PDF 259 `16-10-1999ந்தேதி`.

Exact next alignment batch:

- **3572–3576 / PDF 261–289** — five complete letters / 29 canonical pages.

Preserve Letter 3575's genuine contents `...!` versus actual letter-start `....!` title difference; preserve the scan-proven Letter 3576 title `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!` and keep the former `பார்!` reading withdrawn. Preserve source-supplied English such as PDF 276 `xxxx”` exactly. Compare every English record directly against its authoritative audited Tamil, letter by letter and page by page. Correct any omission, addition, semantic drift, figure/date/name error, quotation loss, paragraph-order change or rhetorical-force distortion before marking a letter bilingual-aligned.

Alignment remains distinct from later editorial and release gates. `source-checked` is retained as the drafting status; `bilingual_alignment_status: aligned` records completion of this gate.

### Phase 4 — English editorial consistency review

Perform a separate volume-level consistency pass only after bilingual alignment is complete across all 55 letters.

### Phase 5 — Volume release

Prepare the complete English index, translation manifest, editorial review and final release report. Tamil remains canonical.

## Status labels

- `draft-translated` — complete English draft exists;
- `source-checked` — English has been checked for coverage against all audited canonical Tamil pages for that letter;
- `bilingual-aligned` / `bilingual_alignment_status: aligned` — direct Tamil↔English meaning/alignment QA complete;
- `reviewed` — English meaning, tone and readability passed editorial review;
- `verified` — final release verification complete.

All **55 / 55** letters are source-checked. **35 / 55** are bilingual-aligned. None has yet passed the later volume-level editorial/release `verified` gate.

## Exact next activity

Align **Letters 3572–3576 / PDF 261–289** as the next five-complete-letter bilingual-alignment batch. If any new possible Tamil defect appears, re-check the controlling scan before changing either layer. Keep the later editorial consistency review separate.
