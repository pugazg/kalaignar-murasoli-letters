# தொகுதி 48 — தொடக்க 25-பக்க batch audit

**தணிக்கை நாள்:** 2026-08-06  
**பரப்பு:** PDF பக்கங்கள் 1–25  
**மூல PDF:** `Vol48.pdf`  
**SHA-256:** `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`

## செய்யப்பட்ட சோதனைகள்

1. PDF page count (`402`) மற்றும் byte size (`214390300`) பதிவு.
2. Scan title page மூலம் தொகுதி எண் `48` மற்றும் காலவரம்பு உறுதி.
3. PDF 1–25 அனைத்துக்கும் uninterrupted `page-001.md`–`page-025.md` இருப்பு.
4. ஒவ்வொரு Markdown கோப்பிலும் volume, PDF page, printed page, section மற்றும் transcription status front matter இருப்பு.
5. PDF 18–22 அச்சு contents rows அனைத்தும் `contents/index.md`-இல் 3706–3763 வரிசையில் பதிவு.
6. முதல் கடிதம் 3706-ன் title, address, paragraphs மற்றும் PDF 24–25 page boundary scan-க்கு எதிராக visual comparison.
7. PDF page 23 blank-page description scan-க்கு எதிராக உறுதி.
8. Chapter links PDF 24–25 வரிசையில் தொடர்ச்சியாக இருப்பு; letter continuation வெளிப்படையாகப் பதிவு.
9. Page-body hash comparison: இந்த batch-இல் duplicate canonical body இல்லை.
10. Replacement Unicode character (`�`) மற்றும் தவறான page-number discontinuity இல்லை.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected page files | 25 |
| Present page files | 25 |
| Continuity | `page-001.md`–`page-025.md`, no gap |
| Printed contents rows | 58 — letters 3706–3763 |
| Complete letters | 0 |
| Partial letters | 1 — letter 3706, PDF 24–25 |
| Duplicate page body | none |
| Broken internal links | none in the completed range |
| Canonical pages visually compared | 25/25 |

## Scan comparison-இல் செய்யப்பட்ட திருத்தங்கள்

- OCR or inferred modern spellings were not accepted; the rendered scan controlled the text.
- The page-25 ending was preserved without inventing the continuation; the sentence resumes in the next batch at PDF page 26.
- Printed date formats in the contents were retained exactly rather than normalised in the transcription table.
- The first letter title was preserved as printed with `ஐ.நா.` punctuation.

## பாதுகாக்கப்பட்ட source observations

- PDF page 23 is blank with faint reverse-side show-through.
- Library stamps and handwritten library markings appear on the title/publication pages and are described rather than interpreted.
- No source page in PDF 1–25 was silently corrected or reconstructed from outside knowledge.

## Pending

This is a **batch audit**, not the full-volume Tamil audit and not the later character-by-character second visual verification. Letter 3706 remains incomplete at PDF page 25. Translation remains blocked.
