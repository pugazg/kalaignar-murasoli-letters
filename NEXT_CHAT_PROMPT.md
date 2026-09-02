# Next Chat Prompt — Continue Murasoli Letters Volume 43

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF:

`TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

Attach or otherwise resolve the controlling PDF in the fresh chat before page-level visual verification.

## Live-main rule for a fresh chat

**Fetch live `main` first and treat it as authoritative.** If `main` has advanced beyond any checkpoint copied into this prompt, preserve the newer durable state and continue from it. Do not reset, overwrite, repeat, or reopen later completed work merely because this prompt records an older checkpoint.

**Last completed source-work activity when this prompt was refreshed:** `Transcribe Volume 43 Letters 3474-3478` — the commit containing this prompt. Later commits may advance the durable state; live `main` remains authoritative.

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

The controlling scan is the highest authority. OCR is a drafting aid only. Do not silently normalize spelling, punctuation, old Tamil glyph readings, titles, quotations, figures, dates, signatures, closings, English/Latin text, handwritten facsimiles, or source-layer differences.

## Volume 43 durable boundary

- Printed pages: **400**
- Physical PDF pages: **402**
- Source SHA-256: `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`
- Source inventory: **56 records, 3428–3483**
- Date span: **01.11.2009–17.07.2010**
- Printed contents: **PDF 018–022**
- Canonical Tamil/source-page representation: **PDF 001–370 / 402**
- Completed Tamil letters: **51 / 56 — 3428–3478**
- English translation: **blocked pending Tamil gates**

Latest completed boundaries:

- **3474** — PDF 340–347 — actual title `ஒய்யாரக் கொண்டையாம், தாழம்பூவாம்.. 3` — closes `02-06-2010`
- **3475** — PDF 348–353 — closes `16-6-2010`
- **3476** — PDF 354–357 — actual title `நஞ்சை எண்ணாதே: நம்பிக் கெடாதே!` — closes `17-6-2010`
- **3477** — PDF 358–363 — actual title `இதோ: செப்பேடுகள் உரைத்திடும் உறுதி!` — closes `19-6-2010`
- **3478** — PDF 364–370 — closes `4-7-2010`

Documented contents/actual-title discrepancies must remain source-layer specific:

- 3430: printed contents differs from actual PDF 040 title.
- 3435: contents `முடிந்த தொடாக்கதை; முடியாத வரலாறு!`; PDF 076 `முடிந்த தொடர்கதை; முடியாத வரலாறு!`.
- 3438: contents `ஊனமுற்றோரின் ஊன்று கோலாகக் கழக அரசு!`; PDF 099 `ஊனமுற்றோரின் ஊன்றுகோலாகக் கழக அரசு!`.
- 3463: contents `மாற்றுத் திறனாளிகளும் - மனிதரே!`; PDF 274 `மாற்றுத் திறனாளிகளும் - மானிடரே!`.
- 3464: contents `பொதுக்கருத்து பற்றி பேரறிஞர் ரூசோவின் கருத்து என்ன?`; PDF 279 `பொதுக்கருத்து பற்றி பேரறிஞன் ரூசோவின் கருத்து என்ன?`.
- 3467: contents uses `மகாராஜனுக்கு`; PDF 299 uses `மகராஜனுக்கு`.
- 3472–3474: contents uses long `ஓய்யாரக்...`; PDF 326, 332 and 340 use short `ஒய்யாரக்...`.
- 3476: contents uses `நஞ்சை எண்ணாதே; நம்பிக் கெடாதே!`; PDF 354 uses `நஞ்சை எண்ணாதே: நம்பிக் கெடாதே!`.
- 3477: contents uses `இதோ; செப்பேடுகள் உரைத்திடும் உறுதி!`; PDF 358 uses `இதோ: செப்பேடுகள் உரைத்திடும் உறுதி!`.

For Letter 3467, preserve the printed contents date cell as blank. The reproduced letter's `2/11/1974` date is a separate source-layer fact. The handwritten facsimile pages were retained as facsimile source representations rather than silently guessing uncertain handwriting.

PDF **371 / printed page 370** cleanly begins Letter **3479 — `“பந்த்”தால் விளையப் போகும் பயன் என்ன?`**.

## Exact next activity

Transcribe the final **five complete Volume 43 source records, Letters 3479–3483**, beginning with Letter 3479 at **PDF 371 / printed page 370**.

For this iteration:

- determine every letter's actual end/date directly from the scan;
- process exactly five complete consecutive letters and complete the Volume 43 letter inventory;
- do not invent Letter 3484 from any following non-letter source pages;
- create every canonical page record covered by the five letters and classify any remaining physical source pages directly from the scan;
- create the five chapter records and update the chapter index;
- preserve printed contents independently from actual letter titles and only advance verification notes where source checking supports it;
- synchronize `metadata.yml`, `PROGRESS.md`, `AUDIT.md`, the Volume 43 README, root `README.md`, `PROJECT_HANDOVER.md`, and this `NEXT_CHAT_PROMPT.md`;
- keep English translation blocked until the full-volume Tamil gates are explicitly satisfied;
- run precommit checks for page continuity, duplicate bodies, U+FFFD/unwanted zero-width residue, exact title/date/quotation/figure/English strings, verified closing/date boundaries, and final source-page classification.

## Git discipline

Work directly on `main` as requested. Before mutation, re-fetch the target files and recheck live `main`. Preserve concurrent work. Prefer a candidate tree/commit that does not move `main` until validation is complete. Publish one atomic commit, fast-forward `main` with `force: false`, and verify parent → new HEAD changed-file scope afterward.
