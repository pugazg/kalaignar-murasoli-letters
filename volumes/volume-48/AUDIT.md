# தொகுதி 48 — transcription iteration audit

**தணிக்கை நாள்:** 2026-08-07  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–225  
**இந்த iteration:** PDF பக்கங்கள் 200–225; கடிதங்கள் 3732–3736  
**மூல PDF:** `Vol48.pdf`  
**பதிவு செய்யப்பட்ட source SHA-256:** `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–225 அனைத்துக்கும் uninterrupted `page-001.md`–`page-225.md` இருப்பு.
2. புதிய 26 canonical page files ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. Five-letter scope 3732–3736; ஒவ்வொரு letter title, salutation, page boundary, closing, signature and date verification.
4. Printed contents entries 3732–3736 மற்றும் actual letter-start titles/date/page boundaries comparison.
5. Five chapter files, ordered canonical links, previous/next navigation and chapter index reconciliation.
6. `contents/index.md`, `chapters/README.md`, `metadata.yml`, `PROGRESS.md`, volume `README.md` மற்றும் root status range/count agreement.
7. Page-number continuity, duplicate canonical body, broken internal link, replacement Unicode (`U+FFFD`) and unexpected missing-body checks.
8. PDF page 226 visually inspected to verify that letter 3737 begins there; page 226 is not included in this iteration.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page files through current range | 225 |
| Present page files | 225 |
| Continuity | `page-001.md`–`page-225.md`, no gap |
| New pages in this iteration | 26 — PDF 200–225 |
| New complete letters | 5 — 3732–3736 |
| Total complete letters | 31 — 3706–3736 |
| Printed contents rows | 58 — letters 3706–3763 |
| New chapter records | 5 |
| Duplicate page body | none detected |
| Replacement Unicode | none detected |
| Broken internal links in completed range | none detected |
| New canonical pages visually compared | 26/26 |
| Next boundary | letter 3737 starts PDF 226 / printed 225 |

## Scan-proven corrections and preserved readings

- Letter titles and closing dates were taken from their actual start/end pages: 3732 (`12-4-2013`), 3733 (`14-4-2013`), 3734 (`15-4-2013`), 3735 (`16-4-2013`) and 3736 (`17-4-2013`).
- OCR-only malformed readings were rejected after scan comparison, including title errors in letters 3733–3735, the `110வது` rule references, the date `31-7-1998`, and the closing date on PDF page 225.
- Letter 3733 retains the printed `தினமலர்` and `தினத்தந்தி` extracts, including the English railway expression `ரன்-த்ரூ`, and preserves its criticism of Assembly procedure without abridgement.
- Letter 3734's account of a child's killing and the printed sequence `செய்வினை - குடுகுடுப்பைக்காரன் - தாயத்து - தோஷம் - நரபலி` are transcribed as source material without softening.
- Letter 3735 retains the fishing-attack statistics, welfare amounts and the source-visible spacing `பணி களைத்`; PDF page 217 was manually recovered with an alternate OCR layout after the initial draft was blank.
- Letter 3736 retains all printed English passages beginning `The root cause of everything...`, `MGR himself who does not want...`, and `What’s in a Name?`, including source grammar and punctuation rather than silently rewriting them.
- Source page boundaries are preserved, including `பாதித்` / `திட்டங்களை` across PDF 200–201, `மூலமாக` / `அல்ல` across 201–202, `என்று` / `செய்யப்பட்ட` across 202–203, `பன்னாட்டு` / `கூட்டுறவு` across 204–205, `பார்த்தால்,` / `கல்லணையைக்` across 205–206, `விடுதலைச்` / `சிறுத்தைகள்` across 210–211, `செய்வினையை` / `அகற்றிவிடுவதாக` across 213–214, `வரையறுத்திட` / `முடியாத` across 214–215, `மீன் வளம்` / `அதிகரிக்கும்` across 218–219, `சூட்ட` / `வேண்டுமென்று` across 220–221, `பொறுப்புகளை` / `அளித்தார்` across 221–222, `கழகம்` / `பொறுப்பேற்ற` across 222–223, and `popular.` / `So he` across 223–224.
- PDF page 226 was inspected only to establish the next boundary and was not transcribed or included in this commit.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
