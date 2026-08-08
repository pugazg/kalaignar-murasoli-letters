# தொகுதி 48 — transcription iteration audit

**தணிக்கை நாள்:** 2026-08-08  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–286  
**இந்த iteration:** PDF பக்கங்கள் 255–286; கடிதங்கள் 3742–3746  
**மூல PDF:** `Vol48.pdf`  
**பதிவு செய்யப்பட்ட source SHA-256:** `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`

## செய்யப்பட்ட சோதனைகள்

1. இந்த iteration-க்கு பயன்படுத்தப்பட்ட attached 402-page scan-இன் SHA-256 (`1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`) மற்றும் byte size (`214390300`) repository metadata-வுடன் நேரடியாகப் பொருந்துவது உறுதிசெய்யப்பட்டது.
2. PDF 255–286 புதிய 32 canonical page files ஒவ்வொன்றும் rendered scan-உடன் page-by-page visual comparison செய்யப்பட்டது.
3. Five-letter scope 3742–3746; ஒவ்வொரு letter title, salutation, page boundary, closing, signature and date scan-க்கு எதிராகச் சரிபார்க்கப்பட்டது.
4. Printed contents entries 3742–3746 மற்றும் actual letter-start titles/date/page boundaries ஒப்பிடப்பட்டன. Letter 3743-இன் முந்தைய index reading `கழகத்தே` scan-இல் தெளிவாக `கழுதையே` என்பதால் canonical structural record திருத்தப்பட்டது.
5. Five chapter files, ordered canonical links, previous/next navigation and chapter index reconciliation செய்யப்பட்டன; 3741 chapter-இன் next navigation 3742 chapter-க்கு இணைக்கப்பட்டது.
6. `contents/index.md`, `chapters/README.md`, `metadata.yml`, `PROGRESS.md`, volume `README.md` மற்றும் root status range/count agreement சரிபார்க்கப்பட்டது.
7. புதிய 32 page files-இல் page-number continuity, duplicate body, replacement Unicode (`U+FFFD`), missing body and letter metadata checks செய்யப்பட்டன.
8. PDF page 287 தனியாக visually inspected செய்து letter 3747 அங்கே தொடங்குவது உறுதிசெய்யப்பட்டது; page 287 இந்த iteration-இல் transcribe செய்யப்படவில்லை.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page files through current range | 286 |
| Present canonical range after integration | `page-001.md`–`page-286.md` |
| New pages in this iteration | 32 — PDF 255–286 |
| New complete letters | 5 — 3742–3746 |
| Total complete letters | 41 — 3706–3746 |
| Printed contents rows | 58 — letters 3706–3763 |
| New chapter records | 5 |
| Duplicate new page body | none detected |
| Replacement Unicode | none detected |
| New canonical pages visually compared | 32/32 |
| Next boundary | letter 3747 starts PDF 287 / printed 286 |

## Scan-proven corrections and preserved readings

- Letter 3742 is complete on PDF 255–259 and preserves the printed mixed date form `27-04-2013`, the references to the 19 Eelam Tamils in Dubai, and the printed resolution-style quoted passages without outside historical correction.
- Letter 3743 is complete on PDF 260–266. The scan, including the actual letter-opening title, reads **`கனவா? நனவா? கழுதையே சும்மா இரு என்ற கதையா?`**. The prior derived index/chapter register incorrectly had `கழகத்தே`; this iteration corrects that transcription defect to `கழுதையே`.
- Letter 3744 is complete on PDF 267–272. Scan-specific forms are preserved, including `கொடநாடு`, `பயன்படுத்தப்பட்டுப் படாதபாடுபட்டுக் கொண்டிருக்கிறது`, and the source-visible wording at page boundaries; no grammatical normalisation was applied.
- Letter 3745 is complete on PDF 273–279 and preserves the printed welfare-board counts, figures, organisation names, punctuation and date `30-4-2013` as visible in the scan.
- Letter 3746 is complete on PDF 280–286 and preserves the printed English passage `Long Pending Schemes in specific States that have national significance, like the Sethu Samuthiram Project....will be completed expeditiously`, the English sentence `The Ramayana is not history or biography. It is a part of Hindu mythology`, source forms `ஆடம்ஸ் பிரிட்ஜ்` / `ஆதாம் பாலம்`, `NEERI`, the figures `829 கோடி`, `424 மைல்`, `8 கோடி மனித நாள்`, and the source-visible `வேலை வாய்ப்புக் கிடும்` without silent correction.
- The five verified boundaries are: 3742 PDF 255–259 / printed 254–258; 3743 PDF 260–266 / printed 259–265; 3744 PDF 267–272 / printed 266–271; 3745 PDF 273–279 / printed 272–278; 3746 PDF 280–286 / printed 279–285.
- PDF page 287 was inspected only to establish the next boundary, where **3747 — அண்ணா அறிவித்த எழுச்சி நாள் எதற்காக?** begins; it is not included in this iteration.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second verification, and not the mandatory textual-fidelity audit that unlocks translation. The existing second-pass fidelity status remains through PDF 128 only. English translation remains blocked.
