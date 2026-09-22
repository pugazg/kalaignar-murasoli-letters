# NEXT CHAT PROMPT — Volume 41 / mandatory first transcription batch PDF 001–025

Continue directly in `pugazg/kalaignar-murasoli-letters`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Read first

1. `VOLUME_PROCESSING_GUIDE.md`
2. `SERIES_FRONT_MATTER_POLICY.md`
3. `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
4. `TRANSCRIPTION_GUIDE.md`
5. `FUTURE_VOLUME_WORK_GUIDELINES.md`
6. `volumes/volume-41/AUDIT.md`
7. `volumes/volume-41/PROGRESS.md`
8. `volumes/volume-41/README.md`
9. `volumes/volume-41/metadata.yml`

Refetch live `main` before editing and immediately before commit.

## Controlling source

`TVA_BOK_0065825_கலைஞரின்_கடிதங்கள்_தொகுதி_41.pdf`

- SHA-256: `950eeb8c97d1cd6b8ab6c4cfd47739264c1223c0f34ba1f0da85c41f90ef3418`
- size: **230,722,751 bytes**
- physical PDF pages: **402**
- printed pages: **400**
- visible date span: **25.11.2007–21.01.2009**
- provisional contents inventory: **58 records / 3306–3363**
- contents: **PDF 018–022**
- PDF 023: non-letter/blank page
- first letter **3306** begins **PDF 024 / printed 23**
- Letter 3306 continues through PDF 033; Letter 3307 begins PDF 034
- final letter **3363** begins PDF 398 / printed 397 and closes PDF 401 / printed 400
- PDF 402 is non-letter back-cover material
- the UI's 150-page view is only a preview limit; **do not treat it as the source extent**

## Exact activity

Perform the mandatory first transcription commit for **PDF 001–025 exactly**.

- Create `pages/page-001.md` through `page-025.md`.
- PDF 001–003: capture Volume 41-specific source text and metadata.
- PDF 004–017: compare directly against the approved Volume 43 shared-front-matter reference. Use reference-only records only where the printed source text truly matches; locally transcribe every deviation.
- PDF 018–022: transcribe all **58 contents rows** exactly as printed.
- PDF 023: preserve its actual blank/non-letter state.
- PDF 024–025: transcribe Letter **3306** exactly from scan.
- Create/update `contents/index.md`, `chapters/README.md`, Letter 3306 chapter record, `PROGRESS.md`, `metadata.yml`, `AUDIT.md`, Volume README and blocked translation controls.
- Mark Letter 3306 **partial** after PDF 025.
- Do **not** transcribe PDF 026 in this commit.
- Visually verify every one of PDF 001–025 against the scan.

Required commit message:

`Transcribe Volume 41 PDF pages 001-025`

## After this batch

The next activity must begin at **PDF 026** and finish Letter **3306** through PDF **033 / printed 32**. Stop before Letter **3307**, which begins PDF **034 / printed 33**.