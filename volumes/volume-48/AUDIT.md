# தொகுதி 48 — transcription iteration audit

**தணிக்கை நாள்:** 2026-08-07  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–254  
**இந்த iteration:** PDF பக்கங்கள் 226–254; கடிதங்கள் 3737–3741  
**மூல PDF:** `Vol48.pdf`  
**பதிவு செய்யப்பட்ட source SHA-256:** `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–254 அனைத்துக்கும் uninterrupted `page-001.md`–`page-254.md` இருப்பு.
2. புதிய 29 canonical page files ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. Five-letter scope 3737–3741; ஒவ்வொரு letter title, salutation, page boundary, closing, signature and date verification.
4. Printed contents entries 3737–3741 மற்றும் actual letter-start titles/date/page boundaries comparison.
5. Five chapter files, ordered canonical links, previous/next navigation and chapter index reconciliation.
6. `contents/index.md`, `chapters/README.md`, `metadata.yml`, `PROGRESS.md`, volume `README.md` மற்றும் root status range/count agreement.
7. Page-number continuity, duplicate canonical body, broken internal link, replacement Unicode (`U+FFFD`) and unexpected missing-body checks.
8. PDF page 255 visually inspected to verify that letter 3742 begins there; page 255 is not included in this iteration.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page files through current range | 254 |
| Present page files | 254 |
| Continuity | `page-001.md`–`page-254.md`, no gap |
| New pages in this iteration | 29 — PDF 226–254 |
| New complete letters | 5 — 3737–3741 |
| Total complete letters | 36 — 3706–3741 |
| Printed contents rows | 58 — letters 3706–3763 |
| New chapter records | 5 |
| Duplicate page body | none detected |
| Replacement Unicode | none detected |
| Broken internal links in completed range | none detected |
| New canonical pages visually compared | 29/29 |
| Next boundary | letter 3742 starts PDF 255 / printed 254 |

## Scan-proven corrections and preserved readings

- Letter titles and closing dates were taken from their actual start/end pages: 3737 (`18-4-2013`), 3738 (`19-4-2013`), 3739 (`21-04-2013`), 3740 (`22-4-2013`) and 3741 (`23-4-2013`).
- OCR-only malformed readings were rejected after scan comparison, including the title word `இந்தக்`, letter number 3738, `2007ஆம் ஆண்டு`, `50 கோடி`, `102 பேர்`, `நடவடிக்கைக் குழுவின்`, and the date `25-3-2013`.
- Letter 3738 preserves the printed anti-death-penalty argument, the names and dates cited, and the figures `104 நாடுகள்`, `39 நாடுகள்` and `90 சதவிகித` without expansion or outside correction.
- Letter 3739 retains both obituary sections, the printed `★ ★ ★` division, the mixed date style `21-04-2013`, and the source's unmatched closing parenthesis in `செய்தியாகும்.)`.
- Letter 3740 retains the printed company names and allegations, including `மெசர்ஸ் க்ருனிசேவ் மாநில ஆய்வு மற்றும் தயாரிப்பு ஸ்பேஸ் சென்டர்`, `மெசர்ஸ் மார்சன் கம்பெனி`, `50 கோடி லஞ்சமாகக் கேட்டார்கள்`, `டேப்ரிகார்டர் ஆதாரம்`, and the source-visible spacing `விவ சாயிகளைக்`.
- Letter 3741 retains the names and quotations of Sri Lankan Tamil refugees, mixed source forms `காமன்வெல்த்` / `காமன் வெல்த்`, `தென்னாப்பிரிக்கா வில்`, and the page-253 opening `(முதல் ஏப்ரல் 18ஆம்` exactly as printed.
- Source page boundaries are preserved, including `பார்வையாளராக` / `இருப்பதை` across PDF 226–227, `வாக்குச் சீட்டுக்களைப்` / `பறித்துக்` across 228–229, `அவைகளைப்` / `பெற்று` across 230–231, `மன்மோகன்` / `சிங்` across 232–233, `கையெழுத்திட்டன;` / `இந்தியா` across 235–236, `நம்மை` / `விட்டுப்` across 237–238, `சார்பில்` / `குப்புசாமி` across 239–240, `என்னைச்` / `சந்தித்து` across 240–241, `திராவிட` / `முன்னேற்றக்` across 242–243, `கோரியிருப்பதாலும்` / `கிடைக்காது` across 244–245, `நிலையில்,` / `அந்த` across 246–247, `எங்களை` / `இங்கே` across 249–250, `நிலையில்` / `எஞ்சியிருக்கும்` across 250–251, `ஏப்ரல் 14` / `(முதல் ஏப்ரல் 18ஆம்` across 252–253, and `காமன் வெல்த் நாடுகளின்` / `தலைமை நீதிபதிகளும்` across 253–254.
- PDF page 255 was inspected only to establish the next boundary and was not transcribed or included in this commit.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
