# தொகுதி 47 — தொடக்க 25-பக்க batch audit

**தணிக்கை நாள்:** 2026-08-06  
**பரப்பு:** PDF பக்கங்கள் 1–25  
**மூல PDF:** `Vol47.pdf`  
**SHA-256:** `4c151357a822a8855e553de080b311d35934e9d844c81aff168b811cd8fd8558`

## செய்யப்பட்ட சோதனைகள்

1. PDF page count (`401`) மற்றும் byte size (`199112671`) பதிவு.
2. Scan cover/title page மூலம் தொகுதி எண் `47` மற்றும் `19.08.2012–19.02.2013` காலவரம்பு உறுதி.
3. PDF 1–25 அனைத்துக்கும் uninterrupted `page-001.md`–`page-025.md` இருப்பு.
4. ஒவ்வொரு Markdown கோப்பிலும் volume, PDF page, printed page, section, letter metadata மற்றும் transcription status front matter இருப்பு.
5. PDF 18–22 அச்சு contents rows அனைத்தும் `contents/index.md`-இல் 3647–3705 வரிசையில் பதிவு.
6. முதல் கடிதம் 3647-ன் title, address, paragraphs மற்றும் PDF 24–25 page boundary scan-க்கு எதிராக visual comparison.
7. PDF pages 5 and 23 blank-page descriptions scan-க்கு எதிராக உறுதி.
8. Chapter links PDF 24–25 வரிசையில் தொடர்ச்சியாக இருப்பு; letter continuation வெளிப்படையாகப் பதிவு.
9. Page-body hash comparison: இந்த batch-இல் duplicate canonical body இல்லை.
10. Unicode replacement marker (`U+FFFD`), தவறான page-number discontinuity மற்றும் broken internal link இல்லை.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected page files | 25 |
| Present page files | 25 |
| Continuity | `page-001.md`–`page-025.md`, no gap |
| Printed contents rows | 59 — letters 3647–3705 |
| Complete letters | 0 |
| Partial letters | 1 — letter 3647, PDF 24–25 |
| Duplicate page body | none |
| Replacement Unicode | none |
| Broken internal links | none in completed range |
| Canonical pages visually compared | 25/25 |

## Scan comparison-இல் செய்யப்பட்ட திருத்தங்கள் மற்றும் பாதுகாப்புகள்

- OCR or inferred modern spellings were not accepted; the rendered scan controlled the text.
- Contents date formatting was preserved exactly, including mixed zero-padding such as `31-08-2012`, `03-09-2012`, `5-10-2012`, and `19-2-2013`.
- Letter 3647 preserves the source wording `உச்ச நீதி மன்றம்` / `சிறப்பு நீதி மன்றம்` where printed, rather than normalising every occurrence to one form.
- PDF page 25 preserves the line-end split `நடந்து கொண்டிருக்` / `கிறது`; the continuation was not silently joined across the canonical page boundary.
- The quoted resignation passage on PDF page 25 was preserved as printed and ends before the letter itself ends.
- The page-25 ending was preserved without inventing the continuation; the letter resumes at PDF page 26.

## பாதுகாக்கப்பட்ட source observations

- PDF page 5 is blank with faint reverse-side show-through.
- PDF page 23 is blank with faint reverse-side contents show-through.
- Library stamps and handwritten library markings appear on title/publication/dedication pages and are described rather than interpreted.
- No source page in PDF 1–25 was silently corrected or reconstructed from outside knowledge.

## Pending

This is an **iteration/batch audit**, not the full-volume Tamil audit, not the later character-by-character second visual verification, and not the translation textual-fidelity audit. Letter 3647 remains incomplete at PDF page 25. Translation remains blocked.
