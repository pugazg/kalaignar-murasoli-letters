# Next Chat Prompt — Continue Murasoli Letters Volume 43

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF:

`TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

Attach or otherwise resolve the controlling PDF in the fresh chat before page-level visual verification.

## Live-main rule for a fresh chat

**Fetch live `main` first and treat it as authoritative.** If `main` has advanced beyond any checkpoint copied into this prompt, preserve the newer durable state and continue from it. Do not reset, overwrite, repeat, or reopen later completed work merely because this prompt records an older checkpoint.

**Last completed source-work checkpoint when this prompt was refreshed:** `d495e1a0fc3dd8878b75fee590bb602d3a2dded8` — `Transcribe Volume 43 Letters 3454-3458`. Later commits may be documentation-only; live `main` remains authoritative.

## Mandatory startup

Before making any repository change, read completely:

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
11. the Volume 43 contents/chapter controls relevant to the active range.

The controlling scan is the highest authority. OCR is a drafting aid only. Do not silently normalize spelling, punctuation, old Tamil glyph readings, titles, quotations, figures, dates, signatures, closings, English/Latin text, or source-layer differences.

## Volume 43 durable boundary

- Printed pages: **400**
- Physical PDF pages: **402**
- Source SHA-256: `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`
- Source inventory: **56 records, 3428–3483**
- Date span: **01.11.2009–17.07.2010**
- Printed contents: **PDF 018–022**
- Canonical Tamil pages: **PDF 001–278 / 402**
- Completed Tamil letters: **36 / 56 — 3428–3463**
- English translation: **blocked pending Tamil gates**

Latest completed boundaries:

- **3459** — PDF 257–259 — closes `19-02-2010`
- **3460** — PDF 260–265 — closes `20-02-2010`
- **3461** — PDF 266–270 — closes `26-2-2010`
- **3462** — PDF 271–273 — closes `28-2-2010`
- **3463** — PDF 274–278 — closes `2-3-2010`

Documented contents/actual-title discrepancies must remain source-layer specific:

- 3430: printed contents differs from actual PDF 040 title.
- 3435: contents `முடிந்த தொடாக்கதை; முடியாத வரலாறு!`; PDF 076 `முடிந்த தொடர்கதை; முடியாத வரலாறு!`.
- 3438: contents `ஊனமுற்றோரின் ஊன்று கோலாகக் கழக அரசு!`; PDF 099 `ஊனமுற்றோரின் ஊன்றுகோலாகக் கழக அரசு!`.
- 3463: contents `மாற்றுத் திறனாளிகளும் - மனிதரே!`; PDF 274 `மாற்றுத் திறனாளிகளும் - மானிடரே!`.

Printed contents Letter 3467 has a blank date cell; preserve it as blank until the source letter itself is reached and verified.

PDF **279 / printed page 278** begins Letter **3464 — `பொதுக்கருத்து பற்றி பேரறிஞர் ரூசோவின் கருத்து என்ன?`**.

## Exact next activity

Transcribe the next **five complete Volume 43 source records, Letters 3464–3468**, beginning with Letter 3464 at **PDF 279 / printed page 278**.

For this iteration:

- determine every letter's actual end/date directly from the scan;
- process exactly five complete consecutive letters and stop before Letter 3469;
- create every canonical page record covered by those letters;
- create the five chapter records and update the chapter index;
- preserve printed contents independently from actual letter titles and only advance verification notes where source checking supports it;
- synchronize `metadata.yml`, `PROGRESS.md`, `AUDIT.md`, the Volume 43 README, root `README.md`, `PROJECT_HANDOVER.md`, and this `NEXT_CHAT_PROMPT.md`;
- keep English translation blocked and do not start it;
- run precommit checks for page continuity, duplicate bodies, U+FFFD/unwanted zero-width residue, exact title/date/quotation/figure/English strings, verified closing/date boundaries, and the next-letter start.

## Git discipline

Work directly on `main` as requested. Before mutation, re-fetch the target files and recheck live `main`. Preserve concurrent work. Prefer a candidate tree/commit that does not move `main` until validation is complete. Publish one atomic commit, fast-forward `main` with `force: false`, and verify parent → new HEAD changed-file scope afterward.
