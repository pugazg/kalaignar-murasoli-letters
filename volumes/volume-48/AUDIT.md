# தொகுதி 48 — transcription iteration audit

**தணிக்கை நாள்:** 2026-08-06  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–62  
**இந்த iteration:** PDF பக்கங்கள் 30–62; கடிதங்கள் 3707–3711  
**மூல PDF:** `Vol48.pdf`  
**பதிவு செய்யப்பட்ட source SHA-256:** `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–62 அனைத்துக்கும் uninterrupted `page-001.md`–`page-062.md` இருப்பு.
2. புதிய 33 canonical page files ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. Five-letter scope 3707–3711; ஒவ்வொரு letter title, salutation, page boundary, closing, signature and date verification.
4. Printed contents entries 3707–3711 மற்றும் actual letter-start titles/date/page boundaries comparison.
5. Five chapter files, ordered canonical links, previous/next navigation and chapter index reconciliation.
6. `contents/index.md`, `chapters/README.md`, `metadata.yml`, `PROGRESS.md` மற்றும் volume `README.md` range/count agreement.
7. Page-number continuity, duplicate canonical body, broken internal link, replacement Unicode (`U+FFFD`) and unexpected missing-body checks.
8. PDF page 63 visually inspected to verify that letter 3712 begins there; page 63 is not included in this iteration.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page files through current range | 62 |
| Present page files | 62 |
| Continuity | `page-001.md`–`page-062.md`, no gap |
| New pages in this iteration | 33 — PDF 30–62 |
| New complete letters | 5 — 3707–3711 |
| Total complete letters | 6 — 3706–3711 |
| Printed contents rows | 58 — letters 3706–3763 |
| New chapter records | 5 |
| Duplicate page body | none detected |
| Replacement Unicode | none detected |
| Broken internal links in completed range | none detected |
| New canonical pages visually compared | 33/33 |
| Next boundary | letter 3712 starts PDF 63 / printed 62 |

## Scan-proven corrections and preserved readings

- Letter 3707 title is **“இவையெல்லாம் பாராட்டாகத் தெரிகிறதா?”**; OCR’s `யாராட்டாகத்` was rejected.
- The unusual printed form `சொன்னதன்னியில்` on PDF page 30 is preserved without silent normalisation.
- Letter 3708 title is **“வென்றவர் சொல்வதெல்லாம் “வேதம் ஆகுமா?””**; OCR’s title error was corrected from the scan.
- The English quotation beginning `The Cauvery River Authority headed by the Prime Minister...` on PDF page 41 is preserved in full.
- PDF page 41 prints the date `30-3-1993`; OCR’s malformed date was corrected against the scan.
- Letter 3711 title prints `நாள்`, not OCR’s `நான்`.
- The unusual printed expressions `உண்மை விகாரங்களை` on PDF page 50 and `தூதுவரகத்திற்கு` on PDF page 62 are preserved.
- Graphic descriptions contained in letter 3711 are transcribed as source text without softening or outside additions.
- Page boundaries were preserved, including `மட்டும்` / `தான்` across PDF 31–32, `தலா 3` / `லட்சம்` across PDF 33–34, and `ஏக்கருக்கு` / `25 ஆயிரம்` across PDF 34–35.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
