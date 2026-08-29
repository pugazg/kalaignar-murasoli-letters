# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-29

Read this with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`.

## Source authority

The controlling scan controls Tamil readings. Audited canonical Tamil is the immediate English-QA source. OCR, translations, contents pages, outside sources and inferred chronology may not silently override the scan.

## Volume 44 — ACTIVE

Controlling source: `TVA_BOK_0065830_கலைஞரின்_கடிதங்கள்_தொகுதி_44.pdf`

Source intake is complete:

- Scan-confirmed volume: **44**
- PDF pages: **400**
- SHA-256: `573d65d7b7d3a8e3cc158b7f91af3a9382ac90ea1eaa37e8c0022b5a64dc747d`
- Source size: **202,106,488 bytes**
- Printed publisher: **சீதை பதிப்பகம்**
- Printed edition/year: **1st Edition — 2022**
- Cover/title date span: **18.07.2010–11.03.2011**
- Printed contents: PDF **018–022**
- Provisional contents inventory: **53 records, 3484–3536**
- Canonical Tamil: **0 / 400**
- English: **blocked**

PDF 024 begins letter 3484 at printed page 23. PDF 025 continues the same letter. Therefore the next activity is the mandatory first transcription commit **PDF 001–025 exactly**, ending with letter 3484 `partial`. PDF 026 must not be included in that first commit.

The following commit must begin at PDF 026 and finish letter 3484 before normal five-complete-letter iterations begin.

## Volume 45 — COMPLETE

Controlling source: `TVA_BOK_0065831_கலைஞரின்_கடிதங்கள்_தொகுதி_45.pdf`

- PDF pages: **402**
- Canonical Tamil: **001–402 / 402**
- Source letters: **55 / 55 — 3537–3591**
- Structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — 402 / 402**
- English source-checked/aligned/editorially reviewed/final verified: **55 / 55**
- Source-incomplete records: **0**

Release artifacts remain under `volumes/volume-45/translations/en/`.

## Git discipline

Work on `main` when requested, never force-push routine work, recheck live `main` immediately before mutation, preserve concurrent changes, prefer one atomic Git-data commit, and verify final changed-file scope afterward.
