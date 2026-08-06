# தொகுதி 48 — transcription iteration audit

**தணிக்கை நாள்:** 2026-08-07  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–136  
**இந்த iteration:** PDF பக்கங்கள் 99–136; கடிதங்கள் 3717–3721  
**மூல PDF:** `Vol48.pdf`  
**பதிவு செய்யப்பட்ட source SHA-256:** `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–136 அனைத்துக்கும் uninterrupted `page-001.md`–`page-136.md` இருப்பு.
2. புதிய 38 canonical page files ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. Five-letter scope 3717–3721; ஒவ்வொரு letter title, salutation, page boundary, closing, signature and date verification.
4. Printed contents entries 3717–3721 மற்றும் actual letter-start titles/date/page boundaries comparison.
5. Five chapter files, ordered canonical links, previous/next navigation and chapter index reconciliation.
6. `contents/index.md`, `chapters/README.md`, `metadata.yml`, `PROGRESS.md`, volume `README.md` மற்றும் root status range/count agreement.
7. Page-number continuity, duplicate canonical body, broken internal link, replacement Unicode (`U+FFFD`) and unexpected missing-body checks.
8. PDF page 137 visually inspected to verify that letter 3722 begins there; page 137 is not included in this iteration.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page files through current range | 136 |
| Present page files | 136 |
| Continuity | `page-001.md`–`page-136.md`, no gap |
| New pages in this iteration | 38 — PDF 99–136 |
| New complete letters | 5 — 3717–3721 |
| Total complete letters | 16 — 3706–3721 |
| Printed contents rows | 58 — letters 3706–3763 |
| New chapter records | 5 |
| Duplicate page body | none detected |
| Replacement Unicode | none detected |
| Broken internal links in completed range | none detected |
| New canonical pages visually compared | 38/38 |
| Next boundary | letter 3722 starts PDF 137 / printed 136 |

## Scan-proven corrections and preserved readings

- Letter titles and closing dates were taken from their actual start/end pages: 3717 (`10-3-2013`), 3718 (`11-3-2013`), 3719 (`12-3-2013`), 3720 (`14-3-2013`) and 3721 (`21-3-2013`).
- OCR-only malformed readings and omitted lines were rejected after scan comparison; page 121’s missing sentence ending `அத்தனை அரசியல் தலைவர்களும் பாராட்டினார்கள்.` and page 109’s question ending `பண்டித நேரு அவர்கள் தென்னாப்பிரிக்காவின் நிறவெறிப் பிரச்சினையில் தலையிட்டிருக்க முடியுமா?` were restored from the scan.
- Letter 3717 retains the complete printed English passage beginning `The Tamil Nadu Government is yet to complete its share...`.
- Unusual printed readings including `சாராம் சத்தை` on PDF page 125, `அழுத்தம் தருவக சொன்னதன்னியில்;` on PDF page 127 and `கண்ணீர் நீலிக்கண்ணீரே` on PDF page 134 are preserved without silent normalisation.
- Source page boundaries are preserved, including `தமிழக அரசு` / `22-6-2007` across PDF 99–100, `எதிர்பார்த்` / `திருந்தோமோ` across PDF 108–109, `வேண்டிய` / `நன்றி அல்ல` across PDF 121–122, `அவர்களுக்கு` / `ஆறுதல்` across PDF 127–128, and `குரல்` / `கொடுத்தாலும்` across PDF 135–136.
- PDF page 137 was inspected only to establish the next boundary and was not transcribed or included in this commit.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
