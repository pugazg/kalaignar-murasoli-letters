# தொகுதி 43 — Iteration Audit

## Intake / first iteration — PDF 001–023

**Date:** 2026-08-31  
**Result:** **PASS**

### Scope

- source identity and page-count verification;
- canonical page files `page-001.md` through `page-023.md`;
- cover/title/publication details;
- foreword and publisher note;
- printed contents PDF 018–022;
- blank PDF 023;
- source-letter inventory registration 3428–3483;
- no letter-body transcription.

### Batching exception

Repository policy normally requires a newly started volume's first commit to cover PDF 001–025. The user explicitly approved Volume 43's first iteration as **PDF 001–023**, ending immediately before Letter 3428 begins. This is a documented user-approved exception under the batching policy.

### Checks

- PDF physical page count independently verified as **402**; publication details print **400 pages**.
- SHA-256 recorded as `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`.
- No usable text layer detected.
- PDF 001–023 represented with uninterrupted canonical filenames.
- PDF 018–022 visually transcribed as the complete printed contents.
- Contents inventory is **56 records, 3428–3483**, with no numerical gap.
- Letter 3467's blank printed date cell is preserved as blank.
- PDF 023 is a blank page with reverse-side show-through.
- PDF 024 begins Letter 3428 and is intentionally outside this commit.
- No English translation was started.

### Next boundary

**PDF 024 / printed page 23 — Letter 3428, `காக்கும் கரங்களுமன்றோ?`.**

## Letter 3428 iteration — PDF 024–032

**Date:** 2026-08-31  
**Result:** **PASS**

### Scope

- canonical page files `page-024.md` through `page-032.md`;
- complete Letter **3428 — `காக்கும் கரங்களுமன்றோ?`**;
- printed pages **23–31**;
- title, salutation, body, embedded poem, figures, source English, closing and date;
- chapter record and source boundary;
- exact start of Letter 3429 at PDF 033.

### Visual checks

- PDF 024 visually confirms Letter 3428 title and `உடன்பிறப்பே,`.
- Every PDF page **024–032** was read directly from the scan and represented once.
- The embedded police lullaby on PDF 025 was preserved as printed, including historical/colloquial wording and ellipses.
- Historical salary figures, dates, arrest counts, recovered-property figures and monetary amounts were checked against the scan.
- Source-supplied English strings such as `Broad Line Computers System`, `Wescos Properties and Developers`, `Victory Equities and Forex India Limited`, and `Gold Quest International Pvt. Ltd.` were retained.
- Page-boundary continuations were not silently joined or moved to another page.
- PDF 032 visually confirms the closing `அன்புள்ள, மு.க.` and date `1-11-2009`.
- PDF 033 visually confirms the clean start of Letter 3429; no part of Letter 3429 is included in this iteration.
- No replacement Unicode or unintended zero-width residue is present.
- English translation remains blocked.

### Boundary result

Letter 3428 is **complete** at **PDF 024–032 / printed pages 23–31**.

**Next:** Letter 3429 begins **PDF 033 / printed page 32**. Under the normal post-exception policy, the next iteration is five complete records **3429–3433**, subject to scan-verified ending boundaries.

