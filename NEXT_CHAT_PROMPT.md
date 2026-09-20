# NEXT CHAT PROMPT — Volume 42 / second full-volume visual-textual fidelity gate — Batch 1 PDF 001–023

Continue directly in `pugazg/kalaignar-murasoli-letters`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable state

- Controlling source: `TVA_BOK_0065826_கலைஞரின்_கடிதங்கள்_தொகுதி_42.pdf`
- Source SHA-256: `43f9b51fd3765144f707cce535cc9ed39892f911a126c3c3c005173a1efc1676`
- Source extent: **402 physical PDF pages / 400 printed pages**
- First-pass canonical coverage: **PDF 001–402 / 402 COMPLETE**
- Full-volume Tamil structural audit: **PASS**
- Structural report: `volumes/volume-42/FULL_VOLUME_STRUCTURAL_AUDIT.md`
- Printed contents: **64 / 64 rows**
- Completed actual source records: **64 — 3364–3376, 3154, 3378–3427**
- Partial/source-incomplete records: **0**
- Second full-volume direct visual/textual-fidelity verification: **NOT STARTED**
- English translation: **BLOCKED**

## Verified source facts that must remain intact

1. **Numbering anomaly:** printed contents and actual PDF **092 / printed 91** both print **3154** between 3376 and 3378. Do not invent 3377.
2. **Letter 3392 duplication:** the source genuinely repeats the title/body across PDF 209–212; preserve both physical copies.
3. **Letter 3388 title layout:** actual PDF 187 prints main title `அந்த நினைவுக்கு ஒரு நன்றி!!` plus separate subtitle `(கலைஞர் கவிதைக் கடிதம்)`; printed contents shows them inline.
4. **Letter 3425 spacing difference:** printed contents uses `திருந்தப் போகிறார்களா?`, actual PDF 386 uses joined `திருந்தப்போகிறார்களா?`.
5. **Volume ending:** Letter 3427 closes on PDF 401 / printed 400; PDF 402 is non-letter back-cover material; no Letter 3428 exists in Volume 42.

## Exact next activity — second-pass Batch 1

Directly compare **PDF 001–023** against the controlling scan.

This batch covers:

- PDF **001–003** — Volume 42-local cover/title/publication matter;
- PDF **004–017** — recurring series front matter, currently shared-reference verified;
- PDF **018–022** — printed contents;
- PDF **023** — blank page after contents.

### Required method

1. Read `VOLUME_PROCESSING_GUIDE.md`, `TRANSCRIPTION_GUIDE.md`, `SERIES_FRONT_MATTER_POLICY.md`, and `volumes/volume-42/FULL_VOLUME_STRUCTURAL_AUDIT.md`.
2. Render and visually inspect the controlling scan for **every physical page 001–023**.
3. Compare each page directly with its canonical `pages/page-NNN.md` record. The scan is authoritative.
4. For shared-reference pages 004–017, confirm the reference remains valid; if the Volume 42 scan differs in printed wording, replace that page with a local exact transcription instead of forcing the shared reference.
5. Check all visible Tamil/English text, punctuation, spacing distinctions where textually material, volume/date/publication fields, contents rows, page numbers, line breaks where meaningful, and non-text classification.
6. Apply only scan-proven corrections. Do not normalize spelling, punctuation, dates, titles or source anomalies from outside knowledge.
7. Create/update `volumes/volume-42/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md` with:
   - gate context and method;
   - durable verified frontier **PDF 001–023 / 402**;
   - every scan-proven correction, or an explicit no-correction result for checked ranges;
   - canonical Tamil changes count.
8. Synchronize `metadata.yml`, `PROGRESS.md`, `AUDIT.md`, Volume 42 `README.md`, root `README.md`, `PROJECT_HANDOVER.md`, and this prompt only as appropriate for the partial second-pass frontier.
9. **Stop before PDF 024 / Letter 3364.**

Do not mark the full second visual/textual-fidelity gate PASS after this batch. Do not begin English translation.

After Batch 1, continue the second pass sequentially from **PDF 024**, normally using complete-letter groups while preserving the durable verified frontier.

Suggested commit message:

`Verify Volume 42 fidelity PDF pages 001-023`
