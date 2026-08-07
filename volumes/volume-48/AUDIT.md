# தொகுதி 48 — transcription iteration audit

**தணிக்கை நாள்:** 2026-08-07  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–167  
**இந்த iteration:** PDF பக்கங்கள் 137–167; கடிதங்கள் 3722–3726  
**மூல PDF:** `Vol48.pdf`  
**பதிவு செய்யப்பட்ட source SHA-256:** `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–167 அனைத்துக்கும் uninterrupted `page-001.md`–`page-167.md` இருப்பு.
2. புதிய 31 canonical page files ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. Five-letter scope 3722–3726; ஒவ்வொரு letter title, salutation, page boundary, closing, signature and date verification.
4. Printed contents entries 3722–3726 மற்றும் actual letter-start titles/date/page boundaries comparison.
5. Five chapter files, ordered canonical links, previous/next navigation and chapter index reconciliation.
6. `contents/index.md`, `chapters/README.md`, `metadata.yml`, `PROGRESS.md`, volume `README.md` மற்றும் root status range/count agreement.
7. Page-number continuity, duplicate canonical body, broken internal link, replacement Unicode (`U+FFFD`) and unexpected missing-body checks.
8. PDF page 168 visually inspected to verify that letter 3727 begins there; page 168 is not included in this iteration.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page files through current range | 167 |
| Present page files | 167 |
| Continuity | `page-001.md`–`page-167.md`, no gap |
| New pages in this iteration | 31 — PDF 137–167 |
| New complete letters | 5 — 3722–3726 |
| Total complete letters | 21 — 3706–3726 |
| Printed contents rows | 58 — letters 3706–3763 |
| New chapter records | 5 |
| Duplicate page body | none detected |
| Replacement Unicode | none detected |
| Broken internal links in completed range | none detected |
| New canonical pages visually compared | 31/31 |
| Next boundary | letter 3727 starts PDF 168 / printed 167 |

## Scan-proven corrections and preserved readings

- Letter titles and closing dates were taken from their actual start/end pages: 3722 (`27-3-2013`), 3723 (`28-3-2013`), 3724 (`29-3-2013`), 3725 (`31-3-2013`) and 3726 (`1-4-2013`).
- OCR-only malformed readings and omitted lines were rejected after scan comparison; PDF page 141 was transcribed manually from the scan because the OCR draft did not provide usable text.
- Letter 3723 retains the complete printed English passages beginning `The ceding of this tiny island...`, `On behalf of the Government of Tamil Nadu...` and `The best possible solution is to get the island of Katcha Theevu...`.
- Letter 3724 retains the English headline `From a bitter critic of LTTE to a champion of Tamil Eelam`.
- Unusual printed readings including `ஜூலை 4ந்தேதி`, the date `6-1-1974`, `ஷரத்து`, `கித்தாப்பில்`, `அபிலாஷை`, `ராஜ்ய ரீதியில்`, `ரிமாண்ட்` and `பிறாண்ட` are preserved without silent normalisation.
- Source page boundaries are preserved, including `தோழமைக்` / `கொண்டு` across PDF 137–138, `தொப்பிகளைப் பறித்து` / `அவர்கள் முகத்திலேயே` across PDF 139–140, `அந்த எண்ணத்தின்` / `அடிப்படையிலே` across PDF 142–143, and `The best possible solution is to get the island of Katcha Theevu` across PDF 148–149. The source distinction between `வெளியேற்றப்பட்டனர்` and `வெளியேறினர்` on PDF 166–167 is also retained.
- PDF page 168 was inspected only to establish the next boundary and was not transcribed or included in this commit.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
