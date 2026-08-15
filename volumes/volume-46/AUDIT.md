# தொகுதி 46 — முழுத் தொகுதி Tamil structural audit

**தணிக்கை நாள்:** 2026-08-15  
**தணிக்கை செய்யப்பட்ட நிலை:** `first-pass-complete`  
**மூல PDF:** `Vol46.pdf`  
**மூல SHA-256:** `ff88d5a78a5ef4d96888ec2f5a0a3653a4f34b1bfbcb0317b5191242cc72cff9`  
**Audit தொடக்க main HEAD:** `89ac79aace44c3e70e08cab2883e20a48440debe`

முந்தைய transcription iteration audit பதிவுகள் `AUDIT-history-through-3622.md` மற்றும் `AUDIT-history-through-3642.md`-இல் பாதுகாக்கப்பட்டுள்ளன. Final-residue transcription audit-ன் verified boundaries மற்றும் source-numbering முடிவுகள் இந்த volume-level audit-ல் மீண்டும் reconcile செய்யப்பட்டுள்ளன.

## Audit பரப்பு

இந்த full-volume structural audit பின்வருவனவற்றை முழுத் தொகுதி அளவில் சரிபார்த்தது:

1. source PDF identity, SHA-256, byte size மற்றும் 402-page count;
2. source page rotation மற்றும் exact-duplicate-page structural signals;
3. canonical page-file coverage `page-001.md`–`page-402.md`;
4. front matter, contents, blank pages, 55 source-letter records மற்றும் back cover பிரிவு;
5. contents table ↔ chapter register ↔ letter PDF/printed ranges;
6. 55 source-record boundaries மற்றும் continuous page coverage;
7. source-numbering anomalies — missing/duplicated numbers source-இன்படி உள்ளனவா;
8. chapter navigation chain, குறிப்பாக numbering-anomaly transitions;
9. known contents-title / actual-heading distinctions;
10. source-incomplete / missing-printed-page state;
11. metadata, README, progress மற்றும் translation-gate consistency.

இந்த audit **second visual verification அல்ல**. ஒவ்வொரு canonical body-யையும் character-by-character scan-க்கு எதிராக மறுமுறை வாசிக்கும் textual-fidelity pass தனி gate ஆகும்.

## Source / PDF structural checks

| சோதனை | முடிவு |
|---|---|
| Source SHA-256 | metadata-ஐப் பொருந்துகிறது |
| Source byte size | `200631699` — metadata-ஐப் பொருந்துகிறது |
| PDF page count | **402** |
| Page rotation | **0° on 402 / 402 pages** |
| Low-resolution render-hash exact duplicates | **0** |
| Searchable authoritative text layer | இல்லை; scan controls transcription |

Fresh source-file recheck metadata-வில் பதிவு செய்யப்பட்ட hash, size மற்றும் page count-ஐ உறுதிசெய்தது. Whole-PDF low-resolution render-hash pass exact duplicate source-page image எதையும் கண்டறியவில்லை. இது textual-fidelity proof அல்ல; missing/duplicate-page structural signal மட்டுமே.

## Repository page coverage

| பகுதி | PDF பக்கங்கள் | Audit முடிவு |
|---|---:|---|
| front matter / contents / blanks | 1–23 | represented |
| source letters | 24–400 | represented |
| final printed blank page | 401 | represented |
| back cover | 402 | represented |
| canonical page-file range | 1–402 | **continuous** |

- `page-001.md` முன் அட்டையாகவும், `page-018.md` contents page ஆகவும், `page-023.md` blank page ஆகவும் சரியான structural metadata-உடன் உள்ளன.
- `page-024.md` first letter 3592-ஐ தொடங்குகிறது.
- PDF 401 printed page 400-ன் blank body state-ஐ பதிவு செய்கிறது.
- PDF 402 back cover ஆகப் பதிவு செய்யப்பட்டுள்ளது.
- Canonical structural range **402 / 402 source pages**.

## Letter / chapter reconciliation

| சோதனை | முடிவு |
|---|---|
| Actual source-letter records | **55** |
| Contents rows | **55** |
| Chapter records | **55** |
| Complete records | **55** |
| Partial/source-incomplete records | **0** |
| Missing printed pages | **none observed** |
| Letter PDF coverage | **24–400 continuous; no gap/overlap** |
| Contents → chapter resolution | **55 / 55** |
| Chapter → canonical page ranges | **55 / 55 reconciled** |

Chapter register-ல் adjacent ranges source order-இல் தொடர்ச்சியாக உள்ளன. முதல் record 3592 PDF 24–29; இறுதி record 3649 PDF 394–400. ஒவ்வொரு letter range-ன் முடிவு அடுத்த actual source record-ன் start-க்கு முன் சரியாக முடிகிறது; source numbering jump ஏற்பட்ட இடங்களிலும் page continuity உடையாது.

## Source-numbering audit

Complete scan மற்றும் repository structure இரண்டும் பின்வரும் anomalies-ஐ ஒரேபடி உறுதிசெய்கின்றன:

- **3635 → 3637 → 3637**; `3636` source record இல்லை.
- இரண்டு `3637` records தனித்துவமானவை:
  - first: PDF 336–342;
  - second: PDF 343 மட்டும்.
- பின்னர் **3643 → 3647**; `3644`, `3645`, `3646` source records இல்லை.
- இந்த anomalies காரணமாக nominal numeric span 3592–3649 இருந்தாலும் actual record count **55**.
- Repository எந்த source number-ஐயும் silently repair / renumber செய்யவில்லை.

## Navigation audit

Navigation chain-ன் normal sequence chapter register-உடன் reconcile செய்யப்பட்டது. High-risk anomaly/end transitions தனியாகச் சரிபார்க்கப்பட்டன:

- 3592: previous = none; next = 3593.
- 3635 → first 3637.
- first 3637 → second 3637.
- second 3637 → 3638.
- 3643 → 3647.
- 3647 → 3648.
- 3649: next = none / volume end.

இந்த transition targets அனைத்திற்கும் corresponding chapter files repository-ல் உள்ளன.

## Contents / actual-heading distinctions

Source context-களை force-match செய்யாமல் பின்வரும் வேறுபாடுகள் சரியாகப் பாதுகாக்கப்பட்டுள்ளன:

- 3620: contents `என்று தணியும் ஈழத்தமிழா தாகம்!`; actual `என்று தணியும் ஈழத்தமிழர் தாகம்!`.
- 3625: contents `ஒரு சுயமரியாதைக்காரனின் குளுரை!`; actual `ஒரு சுயமரியாதைக்காரனின் சூளுரை!`.
- 3634: contents comma; actual heading semicolon.
- second 3637: contents `...உடன்பிறப்புக்கள்!`; actual `...உடன்பிறப்புக்களே!`.
- 3647: contents `ஈழத்தமிழா இன்னல் களைந்திட வாரீர்!`; actual `ஈழத்தமிழர் இன்னல் களைந்திட வாரீர்!`.

## Prior first-pass fidelity evidence retained

Batch audits already document direct scan comparison for every newly transcribed page in its transcription iteration, including source-specific punctuation, page-boundary word splits, English passages, signatures/dates and malformed source forms. The full-volume structural audit found **no structural inconsistency requiring a Tamil canonical-page correction**.

Examples of source-faithful anomalies retained include:

- comma-less `அன்புள்ள` closings on 3632 and 3642;
- handwritten signature image description on the second 3637;
- PDF 373 malformed mixed-English `Chennai örgjiThis`;
- PDF 401 bleed-through not promoted to body text;
- PDF 402 portrait described without identifying the person from the image.

## Audit result

**PASS — Volume 46 full-volume Tamil structural audit complete.**

Structural state after this audit and subsequent fidelity work:

- source PDF pages represented: **402 / 402**;
- source-letter records: **55 / 55**;
- contents rows resolved: **55 / 55**;
- source-incomplete records: **0**;
- numbering anomalies reconciled: **yes**;
- structural metadata / chapter ranges / navigation: **reconciled**;
- full-volume audit status: **complete**;
- second visual/textual-fidelity verification: **in progress — PDF 001–100 passed**;
- scan-proven canonical corrections in PDF 001–100: **5 pages / 5 spans**;
- English translation: **not started**.

## முக்கிய status boundary

`full-volume-audit-complete` என்பது canonical structure, source boundaries, numbering, mappings மற்றும் page coverage pass ஆனது என்பதையே குறிக்கிறது. Second visual/textual-fidelity verification தனியாக source scan-க்கு எதிரான close review ஆகத் தொடர்கிறது.

Repository guide-ன்படி English translation தொடங்குவதற்கு relevant Tamil pages mandatory scan-based textual-fidelity review pass ஆக வேண்டும்.

## Second visual / textual-fidelity verification progress

### Report 1 — PDF 001–025

Detailed report: [TEXTUAL_FIDELITY_AUDIT_001_025.md](translations/en/TEXTUAL_FIDELITY_AUDIT_001_025.md)

- PDF pages visually compared: **25 / 25**.
- Scan-proven canonical corrections: **0**.
- Front/publication matter, contents, blanks and PDF 024–025 beginning of letter 3592 passed.
- PDF 024 `நிகழ்ந்` → PDF 025 `துள்ளன.` remains preserved as a source page-boundary split.

### Report 2 — PDF 026–050

Detailed report: [TEXTUAL_FIDELITY_AUDIT_026_050.md](translations/en/TEXTUAL_FIDELITY_AUDIT_026_050.md)

- New PDF pages visually compared: **25 / 25**.
- Scan-proven canonical corrections: **0**.
- Letter 3592 completed at PDF 029 with source closing/date checked.
- Letters 3593, 3594 and 3595 passed through closing/date pages PDF 036, 044 and 049.
- PDF 031 English legal phrases and PDF 039 Colin Gonsalves English quotation were checked against the scan.
- PDF 044 printed parenthetical note after the closing/date was preserved.
- PDF 047 Purananuru quotation was checked line by line.
- PDF 049 source-specific final `தமிழ!` remains distinct from the heading/contents `தமிழா!`.

### Report 3 — PDF 051–075

Detailed report: [TEXTUAL_FIDELITY_AUDIT_051_075.md](translations/en/TEXTUAL_FIDELITY_AUDIT_051_075.md)

- New PDF pages visually compared: **25 / 25**.
- Scan-proven canonical corrections: **2 pages / 2 spans**.
- PDF 052 restored source quotation marks around `‘பூஜை’`.
- PDF 066 corrected first-pass `உண்டு,` to scan-supported `உண்டே,`.
- Letters 3596, 3597, 3598 and 3599 passed through closing/date pages PDF 056, 063, 066 and 074.

### Report 4 — PDF 076–100

Detailed report: [TEXTUAL_FIDELITY_AUDIT_076_100.md](translations/en/TEXTUAL_FIDELITY_AUDIT_076_100.md)

- New PDF pages visually compared: **25 / 25**.
- Scan-proven canonical corrections: **3 pages / 3 spans**.
- PDF 079 corrected first-pass `கண்ணா` to source `கண்ணீர்`.
- PDF 097 corrected first-pass `உலகிய` to source `உலவிய`.
- PDF 099 restored source spacing `சட்ட முன் வடிவை` instead of joined `சட்ட முன்வடிவை`.
- Letters 3600, 3601 and 3602 passed through closing/date pages PDF 079, 087 and 094.
- PDF 095–100 is only partial coverage for letter 3603.

### Cumulative fidelity state

- Second-pass coverage: **PDF 001–100 / 402**.
- Total pages second-pass checked: **100**.
- Total scan-proven canonical corrections: **5 pages / 5 spans**.
- Complete source letters with full second-pass coverage: **3592–3602**.
- Letter 3603: PDF 095–100 checked so far; fidelity gate incomplete.

This second-pass progress does not alter the full-volume structural-audit conclusion and does not certify PDF 101 onward.

## Exact next task

Continue second visual / textual-fidelity verification with **PDF 101–125**. Correct only scan-proven canonical defects and record the range in the next fidelity report. Do not begin English translation in this activity.
