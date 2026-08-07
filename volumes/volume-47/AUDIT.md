# தொகுதி 47 — five-letter transcription iteration audit

**தணிக்கை நாள்:** 2026-08-06  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–64  
**இந்த iteration:** PDF பக்கங்கள் 31–64; கடிதங்கள் 3648–3652  
**மூல PDF:** `Vol47.pdf`  
**SHA-256:** `4c151357a822a8855e553de080b311d35934e9d844c81aff168b811cd8fd8558`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–64 அனைத்துக்கும் uninterrupted `page-001.md`–`page-064.md` canonical range இருப்பு.
2. புதிய canonical pages 31–64 ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. கடிதங்கள் 3648–3652 அனைத்துக்கும் title, address, body, closing, signature, printed date மற்றும் next-letter boundary verification.
4. ஐந்து chapter records, chapter index, contents boundaries, metadata, progress மற்றும் volume/root status agreement.
5. புதிய 34 page files-க்கு front-matter/page-number/printed-page/letter mapping validation.
6. Duplicate canonical body, replacement Unicode (`U+FFFD`) மற்றும் completed-range broken-link checks.
7. PDF page 65 visually inspected; கடிதம் 3653 அங்கே தொடங்குவது உறுதி செய்யப்பட்டது. Page 65 இந்த iteration-இல் சேர்க்கப்படவில்லை.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page range | `page-001.md`–`page-064.md` |
| Continuity | no gap through PDF 64 |
| New pages in this iteration | 34 — PDF 31–64 |
| New complete letters | 5 — letters 3648–3652 |
| Total complete letters | 6 — letters 3647–3652 |
| Partial letters | 0 |
| Printed contents rows | 59 — letters 3647–3705 |
| Duplicate new page body | none detected |
| Replacement Unicode | none detected |
| Broken internal links | none detected in completed range |
| New canonical pages visually compared | 34/34 |
| Next boundary | letter 3653 starts PDF 65 / printed 64 |

## Scan-proven readings and preservation decisions

- OCR or inferred modern spellings were not accepted; rendered page images controlled the canonical text.
- PDF page 36 preserves the scan reading `பிரச்சினை ஓரளவேனும் குறைக்கப்பட்ட தமிழகத்திற்கு`.
- PDF page 37 preserves the source's parenthetical question mark `(?)`.
- PDF page 43 preserves the printed English spelling `casualities` rather than silently correcting it.
- PDF pages 50–51 preserve source-specific spacing such as `பொருளாதாரத் தைச்`, `பற்றாக்குறை பைச்` and `தொடங்கி யிருக்குமே`.
- Letter 3650 preserves the printed date `31-08-2012` and the page-52 signature `மு.க` without adding a final period.
- PDF page 55 preserves the scan reading `வாதத்திற்காக ஒப்புக் கொண்டு`; PDF page 58 preserves `இன்று திரிபுவாதம் பேசுகின்ற நெடுமாறன்`.
- PDF pages 63–64 preserve the source's poem, punctuation, stanza order and final slogans without literary normalisation.
- Mixed printed date formats across the five letters were retained exactly: `25-8-2012`, `30-8-2012`, `31-08-2012`, `03-09-2012`, `10-9-2012`.

## பாதுகாக்கப்பட்ட source observations

- PDF page 5 is blank with faint reverse-side show-through.
- PDF page 23 is blank with faint reverse-side contents show-through.
- Library stamps and handwritten library markings appear on title/publication/dedication pages and remain factual descriptions only.
- No missing, duplicated, rotated, damaged or illegible source page was observed in PDF 1–64.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second visual verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
