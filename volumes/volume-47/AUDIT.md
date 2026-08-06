# தொகுதி 47 — தொடக்க transcription iteration audit

**தணிக்கை நாள்:** 2026-08-06  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–30  
**இந்த iteration:** PDF பக்கங்கள் 26–30; கடிதம் 3647 நிறைவு  
**மூல PDF:** `Vol47.pdf`  
**SHA-256:** `4c151357a822a8855e553de080b311d35934e9d844c81aff168b811cd8fd8558`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–30 அனைத்துக்கும் uninterrupted `page-001.md`–`page-030.md` இருப்பு.
2. புதிய canonical pages 26–30 ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. கடிதம் 3647-ன் தொடர்ச்சி, quoted passages, English passages, final argument, closing, signature மற்றும் date verification.
4. Chapter record PDF 24–30 மற்றும் printed 23–29 என complete boundary-க்கு மாற்றப்பட்டது.
5. Contents first row, chapter index, metadata, progress மற்றும் volume/root status range/count agreement.
6. Page-number continuity, front matter, duplicate canonical body, replacement Unicode (`U+FFFD`) மற்றும் broken internal link checks.
7. PDF page 31 visually inspected; கடிதம் 3648 அங்கே தொடங்குவது உறுதி செய்யப்பட்டது. Page 31 இந்த commit-இல் சேர்க்கப்படவில்லை.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page files through current range | 30 |
| Present page files | 30 |
| Continuity | `page-001.md`–`page-030.md`, no gap |
| New pages in this iteration | 5 — PDF 26–30 |
| Complete letters | 1 — letter 3647 |
| Partial letters | 0 |
| Printed contents rows | 59 — letters 3647–3705 |
| Duplicate page body | none detected |
| Replacement Unicode | none detected |
| Broken internal links | none detected in completed range |
| New canonical pages visually compared | 5/5 |
| Next boundary | letter 3648 starts PDF 31 / printed 30 |

## Scan-proven corrections and preserved readings

- OCR or inferred modern spellings were not accepted; the rendered scan controlled the canonical text.
- PDF page 26 preserves the printed English spelling `embarassment`, the form `Special Lokayuk Court`, and the source's complete *The Hindu* quotation.
- PDF page 27 preserves `Justice Mohan Shantana goundar` and the source's standalone second question mark before the English parenthetical passage.
- PDF pages 28–29 preserve colloquial and source-specific forms including `லோக் ஆயுக்தா வில்`, `தேவை யில்லாத`, and the in-page split `இழுத்தடிக்` / `கிறார்கள்`.
- PDF page 30 preserves the source's Tamil ordering `(Immortal)` and `(Mortal)` without reconciling it to the following English quotation.
- PDF page 30 preserves printed spacing such as `விருப்பத் திற்கும்` and `நடுநிலையாளர் களே!` rather than silently regularising it.
- The closing `அன்புள்ள, மு.க.` and printed date `19-8-2012` were visually verified.

## பாதுகாக்கப்பட்ட source observations

- PDF page 5 is blank with faint reverse-side show-through.
- PDF page 23 is blank with faint reverse-side contents show-through.
- Library stamps and handwritten library markings appear on title/publication/dedication pages and remain factual descriptions only.
- No missing, duplicated, rotated, damaged or illegible source page was observed in PDF 1–30.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second visual verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
