# Next Chat Prompt — Volume 43 Tamil Full-Volume Audit

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF:

`TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

Attach or otherwise resolve the controlling PDF in the fresh chat before direct visual verification.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state.

**Last completed source-work commit:** `bc32fc3c7dcf538930357a04ae260d679a2785d6` — `Transcribe Volume 43 Letters 3479-3483`.

**Live-main checkpoint immediately before this handoff refresh:** `e69aed134f25b09e3ba021e2777ce315707bcde5` — `Remove accidental noop marker`. The handoff-refresh commit containing this prompt will be newer. If live `main` has advanced again, preserve the newer durable state. Do not reset, repeat, or reopen later completed work.

## Mandatory startup

Before any repository change, read completely:

1. `VOLUME_PROCESSING_GUIDE.md`
2. `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
3. `TRANSCRIPTION_GUIDE.md`
4. `FUTURE_VOLUME_WORK_GUIDELINES.md`
5. `PROJECT_HANDOVER.md`
6. this `NEXT_CHAT_PROMPT.md`
7. `volumes/volume-43/README.md`
8. `volumes/volume-43/PROGRESS.md`
9. `volumes/volume-43/AUDIT.md`
10. `volumes/volume-43/metadata.yml`
11. `volumes/volume-43/contents/index.md`
12. `volumes/volume-43/chapters/README.md`

The controlling scan is the highest authority. OCR is only a drafting/discrepancy aid. Do not silently normalize spelling, punctuation, old Tamil glyph readings, titles, quotations, figures, dates, signatures, closings, English/Latin text, facsimiles, or source-layer differences.

## Volume 43 durable boundary

- Printed pages: **400**
- Physical PDF pages: **402**
- Source SHA-256: `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`
- Source inventory: **56 records, 3428–3483**
- Date span: **01.11.2009–17.07.2010**
- Canonical Tamil/source-page representation: **PDF 001–402 / 402 — first-pass complete**
- Completed Tamil letters: **56 / 56 — 3428–3483**
- Partial/source-incomplete records: **none**
- PDF **401**: non-letter end matter
- PDF **402**: back cover / portrait / publisher-contact-price material
- No Letter **3484** is created in Volume 43
- English translation: **blocked pending Tamil gates**

Final five source records:

- **3479** — PDF 371–374 — closes `7-7-2010`
- **3480** — PDF 375–379 — closes `12-7-2010`
- **3481** — PDF 380–385 — actual title `வேண்டாத விமர்சனங்கள்? மறப்போம்! மன்னிப்போம்!` — closes `14-7-2010`
- **3482** — PDF 386–393 — closes `16-7-2010`
- **3483** — PDF 394–400 — closes `17-07-2010`

Preserve all documented contents/actual-title discrepancies independently, including Letter **3481**: printed contents has `வேண்டாத விமர்சனங்கள்; மறப்போம்! மன்னிப்போம்!`, while actual PDF 380 has `வேண்டாத விமர்சனங்கள்? மறப்போம்! மன்னிப்போம்!`.

## Exact next activity

Run the **full Volume 43 Tamil structural audit**, then the required **second direct visual/textual-fidelity verification**.

For the structural audit, validate at minimum:

- canonical page continuity **001–402** with no gaps or duplicates;
- exactly **56 source records, 3428–3483**, with no invented 3484;
- chapter start/end ranges and page links;
- contents-layer wording vs actual-title metadata;
- all closings/dates and final source-page classifications;
- metadata, progress, audit, README and handover synchronization;
- duplicate page bodies and U+FFFD / U+200B / U+200C / U+200D / U+FEFF residue.

Then compare the full volume directly against the controlling scan for the second visual/textual-fidelity gate. Record every correction explicitly. **Do not re-transcribe completed letters unless a concrete audit defect is found. Do not begin English translation until both Tamil gates are PASS.**

## Git discipline

Work directly on `main`. Re-fetch live `main` immediately before mutation, preserve concurrent work, prefer a candidate tree/commit that does not move `main` until validation is complete, publish one atomic commit, fast-forward with `force: false`, and verify parent → new HEAD changed-file scope.
