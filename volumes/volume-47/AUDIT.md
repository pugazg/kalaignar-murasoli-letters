# தொகுதி 47 — five-letter transcription iteration audit

**தணிக்கை நாள்:** 2026-08-12  
**மொத்த canonical பரப்பு:** PDF பக்கங்கள் 1–254  
**இந்த iteration:** PDF பக்கங்கள் 231–254; கடிதப் பதிவுகள் 3678–3682  
**மூல PDF:** `Vol47.pdf`  
**SHA-256:** `4c151357a822a8855e553de080b311d35934e9d844c81aff168b811cd8fd8558`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–254 அனைத்துக்கும் uninterrupted `page-001.md`–`page-254.md` canonical filename range இருப்பு.
2. புதிய canonical pages 231–254 ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. கடிதம் 3678: PDF 231–237 / printed 230–236; title, address, body, closing மற்றும் date verified.
4. கடிதம் 3679: PDF 238–243 / printed 237–242; title, English quotations, closing மற்றும் date verified.
5. கடிதம் 3680: PDF 244–248 / printed 243–247; title, image page, body, closing மற்றும் date verified.
6. கடிதம் 3681: PDF 249–252 / printed 248–251 கிடைக்கக்கூடிய source pages visually verified. PDF 252 நடுவில் முடிகிறது; printed page 252 source PDF-இல் இல்லை. Missing continuation, closing மற்றும் date ஊகிக்கப்படவில்லை; chapter status `source-incomplete`.
7. கடிதம் 3682: PDF 253–254 / printed 253–254; title, body, closing மற்றும் date verified.
8. PDF 255 visually inspected only to establish that letter 3683 starts there; `page-255.md` உருவாக்கப்படவில்லை, 3683 body இந்த iteration-இல் சேர்க்கப்படவில்லை.
9. Exactly five new chapter records 3678–3682 உருவாக்கப்பட்டன; 4 `complete`, 1 `source-incomplete`.
10. Previous letter 3677 next navigation, chapter index, contents register, metadata, progress, volume README மற்றும் root README consistency checked.
11. New page/front-matter mapping checked against verified printed pagination, including the source jump printed 251 → 253.
12. Duplicate canonical body, replacement Unicode (`U+FFFD`), zero-width residue மற்றும் completed/recorded-range broken-link checks.
13. Existing contents-vs-heading discrepancies for 3663 and 3674 remain preserved without reconciliation.
14. Volume 48 மற்றும் Volume 49 release files இந்த iteration-இல் மாற்றப்படவில்லை.
15. English translation files உருவாக்கப்படவில்லை; translation gate remains blocked.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page range | `page-001.md`–`page-254.md` |
| PDF filename continuity | no gap through PDF 254 |
| New canonical pages | 24 — PDF 231–254 |
| New letter records | 5 — letters 3678–3682 |
| New complete letters | 4 — 3678, 3679, 3680, 3682 |
| New source-incomplete letters | 1 — 3681 |
| Total complete letters | 35 — 3647–3680 and 3682 |
| Ordinary partial letters | 0 |
| Source missing printed pages | 1 — printed page 252 |
| Printed contents rows | 59 — letters 3647–3705 |
| Duplicate new page body | none detected |
| Replacement Unicode | none detected |
| Zero-width residue | none detected |
| Broken internal links | none detected in recorded range |
| New canonical pages visually compared | 24/24 |
| Next boundary | letter 3683 starts PDF 255 / printed 255 |

## Source gap — printed page 252

The scan itself establishes the discontinuity: PDF 252 carries printed page number **251** and letter 3681 continues to the bottom of that page, ending after `அடிப்படையான வேளாண்மை, வணிகம், சிறுதொழில் மற்றும்`. The next PDF page, PDF 253, begins letter 3682; its printed-page sequence is **253**, and PDF 254 is visibly printed page **254**. Therefore printed page **252** is absent from this only available PDF/edition. No external source, reconstructed prose, inferred closing or invented date was inserted.

The printed contents lists letter 3681 at printed page 248 dated `15-12-2012` and letter 3682 at printed page 253 dated `16-12-2012`; those contents forms are preserved as structural source data. The chapter record for 3681 distinguishes the contents-derived date from the missing closing/date page.

## Scan-proven readings and preservation decisions

- Letter 3678 preserves source forms including `மின் புழுதி நீக்க உபகரணங்கள் இல்லை`, `மாராட்டிய மாநில அரசு`, `திருப்பூர் மாநிலத்தில்`, `ஈரோடு மாநிலத்திலும்`, `நெசவாலைகள்`, `தெரிய வில்லை`, `செயற் குழு` and `வாழ் வாதாரத்திற்கு`.
- Letter 3679 preserves the printed English headline and English quotation on PDF 240, including their source punctuation and line sequence; PDF 241 preserves `பிரமாண்டமான`.
- Letter 3680's PDF 244 photograph is described factually. Its small printed caption is not reliably legible and is marked `[தெளிவில்லை]` rather than guessed. Source forms such as `கீவளூர் வட்டாரத்தில்`, `முதல,`, `ராஜகோபால இடத்திலும்`, `கல்யாணத்திடமும்` and `அவர்களை யெல்லாம்` remain unnormalised.
- Letter 3681 preserves actual heading spacing `3681.இருள்...`, `ஏ.எல். சுப்பிரமணியனும்`, `காதர்பாட்சா (எ) வெள்ளைச் சாமியும்`, `சமயநல்லூர் செல்வராஜும்`, `சூராதி சூரன்`, `16 மணிநேரம்,18 மணிநேரம்` and `“சான்றிதழ்” (?)`.
- Letter 3682 preserves source punctuation/repetition and the unusual PDF 254 reading `என்னரும் ஏழைத் தமிழர்களை`.
- Printed contents row 3663 versus actual PDF 128 heading and printed contents row 3674 versus actual PDF 203 heading remain separately preserved as previously audited.

## பாதுகாக்கப்பட்ட source observations

- PDF page 5 is blank with faint reverse-side show-through.
- PDF page 23 is blank with faint reverse-side contents show-through.
- Library stamps and handwritten library markings appear on title/publication/dedication pages and remain factual descriptions only.
- No source defect had been observed through PDF 230; the first confirmed source-page omission is printed page 252 within the later PDF 231–254 region.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison of the available scan pages, not the full-volume Tamil structural audit, not the later character-by-character second visual verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
