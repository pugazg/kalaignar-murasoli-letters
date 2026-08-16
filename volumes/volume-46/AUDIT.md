# தொகுதி 46 — முழுத் தொகுதி Tamil audit

**Structural audit date:** 2026-08-15  
**Final textual-fidelity completion:** 2026-08-16  
**மூல PDF:** `Vol46.pdf`  
**மூல SHA-256:** `ff88d5a78a5ef4d96888ec2f5a0a3653a4f34b1bfbcb0317b5191242cc72cff9`

முந்தைய transcription iteration audit பதிவுகள் `AUDIT-history-through-3622.md` மற்றும் `AUDIT-history-through-3642.md`-இல் பாதுகாக்கப்பட்டுள்ளன. இந்த volume-level audit, structural validation மற்றும் பின்னர் முடிக்கப்பட்ட முழு scan-based textual-fidelity gate ஆகிய இரண்டின் இறுதி நிலையைச் சுருக்குகிறது.

## 1. Source / PDF structural checks

| சோதனை | முடிவு |
|---|---|
| Source byte size | `200631699` |
| PDF page count | **402** |
| Page rotation | **0° on 402 / 402 pages** |
| Low-resolution render-hash exact duplicates | **0** |
| Searchable authoritative text layer | இல்லை; scan controls transcription |
| Canonical page files | **402 / 402** |

## 2. Repository coverage

| பகுதி | PDF பக்கங்கள் | முடிவு |
|---|---:|---|
| front matter / contents / blanks | 1–23 | represented |
| source letters | 24–400 | represented |
| final printed blank page | 401 | represented |
| back cover | 402 | represented |
| canonical page-file range | 1–402 | **continuous** |

PDF 401 printed page 400-ன் running header/page number-ஐ மட்டுமே கொண்டுள்ளது; body text இல்லை. PDF 402 back cover ஆகப் பாதுகாக்கப்பட்டுள்ளது.

## 3. Letter / chapter reconciliation

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

## 4. Source-numbering audit

Complete scan verification confirms:

- **3635 → 3637 → 3637**; source record `3636` இல்லை.
- இரண்டு `3637` records தனித்துவமான source records.
- பின்னர் **3643 → 3647**; source records `3644`, `3645`, `3646` இல்லை.
- Nominal numeric span 3592–3649 இருந்தாலும் actual source-record count **55**.
- Repository எந்த source number-ஐயும் silently repair / renumber செய்யவில்லை.

## 5. Contents / actual-heading distinctions

Source context-களை force-match செய்யாமல் பின்வரும் வேறுபாடுகள் பாதுகாக்கப்பட்டுள்ளன:

- 3620: contents `என்று தணியும் ஈழத்தமிழா தாகம்!`; actual `என்று தணியும் ஈழத்தமிழர் தாகம்!`.
- 3625: contents `ஒரு சுயமரியாதைக்காரனின் குளுரை!`; actual `ஒரு சுயமரியாதைக்காரனின் சூளுரை!`.
- 3634: contents comma; actual heading semicolon.
- second 3637: contents `...உடன்பிறப்புக்கள்!`; actual `...உடன்பிறப்புக்களே!`.
- 3647: contents `ஈழத்தமிழா இன்னல் களைந்திட வாரீர்!`; actual `ஈழத்தமிழர் இன்னல் களைந்திட வாரீர்!`.

## 6. Structural audit result

**PASS — Volume 46 full-volume Tamil structural audit complete.**

The structural audit validates source identity, page coverage, source boundaries, contents/chapter mappings, navigation and numbering anomalies. It is separate from the character-level scan comparison below.

## 7. Second visual / textual-fidelity verification

The mandatory scan-to-canonical second pass is now also complete.

- PDF pages visually compared: **402 / 402**.
- Actual source-letter records fully cleared: **55 / 55**.
- Cumulative scan-proven canonical corrections: **29 pages / 32 spans**.
- Final range: PDF **376–402**, with one corrected page / one corrected span.
- Final scan-proven correction: PDF 385 `பேரினால் பாதிக்கப்பட்டும்` → source `போரினால் பாதிக்கப்பட்டும்`.

Detailed reports:

- `translations/en/TEXTUAL_FIDELITY_AUDIT_001_025.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_026_050.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_051_075.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_076_100.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_101_125.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_126_150.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_151_175.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_176_200.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_201_225.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_226_250.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_251_275.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_276_300.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_301_325.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_326_350.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_351_375.md`
- `translations/en/TEXTUAL_FIDELITY_AUDIT_376_402.md`

## 8. Final Tamil gate status

**PASS — Volume 46 Tamil archival verification complete.**

- First-pass transcription: complete.
- Full-volume structural audit: complete.
- Full-volume second visual/textual-fidelity verification: complete.
- English translation: **not started, but no longer blocked by Tamil fidelity**.
- Bilingual alignment: not started.
- Editorial release review: not started.

## Exact next task

Begin the Volume 46 English translation workflow from the fully fidelity-verified canonical Tamil, following the repository's established translation, bilingual-alignment and editorial-review conventions.
