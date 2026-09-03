# Next Chat Prompt — Volume 43 Tamil Fidelity Verification

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF:

`TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

Attach or otherwise resolve the controlling PDF in the fresh chat before direct visual verification.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state. Do not reset, repeat, or reopen later completed work because a copied checkpoint is older.

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
13. `volumes/volume-43/FULL_VOLUME_STRUCTURAL_AUDIT.md`
14. `volumes/volume-43/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`

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
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **IN PROGRESS — PDF 001–353 / 402 VERIFIED**
- English translation: **blocked pending Tamil fidelity gate**

The second-pass corrections through PDF 353 are recorded in `volumes/volume-43/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`. Letters **3428–3475** have completed the second direct fidelity pass through PDF **353**. Do not repeat PDF 001–353 unless a concrete defect is reported.

Preserve all documented contents/actual-title discrepancies independently; do not normalize one source layer to another. In particular, the actual Letter 3441 title on PDF 119 is `உடன் பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`, while the separately preserved printed-contents wording on PDF 019 is `உடன்பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`. The actual Letter 3464 title on PDF 279 is `பொதுக்கருத்து பற்றி பேரறிஞன் ரூசோவின் கருத்து என்ன?`, while the separately preserved printed-contents wording is `பொதுக்கருத்து பற்றி பேரறிஞர் ரூசோவின் கருத்து என்ன?`. Letter 3467 has a blank printed-contents date cell; the separate record reproduces the handwritten letter dated `2-11-1974`, and its actual-title spelling `மகராஜனுக்கு` must remain distinct from the contents-layer `மகாராஜனுக்கு`. Letters 3472–3474 have actual-start spelling `ஒய்யாரக்...` while the printed contents preserves `ஓய்யாரக்...`. For the next iteration, preserve the actual Letter 3476 title on PDF 354 as `நஞ்சை எண்ணாதே: நம்பிக் கெடாதே!` independently from the printed-contents semicolon form `நஞ்சை எண்ணாதே; நம்பிக் கெடாதே!`, and preserve the actual Letter 3477 title on PDF 358 as `இதோ: செப்பேடுகள் உரைத்திடும் உறுதி!` independently from the printed-contents semicolon form `இதோ; செப்பேடுகள் உரைத்திடும் உறுதி!`.

## Iteration cadence

Process **two complete letters per iteration**. Start at the current frontier, verify the first complete letter and then the immediately following complete letter in the same iteration, and stop at the end of the second letter. If scan-proven corrections are found, apply them before advancing the frontier.

## Exact next activity

Resume the required **second full-volume direct visual/textual-fidelity verification at PDF 354** and complete the next **two letters — 3476 and 3477 — in this iteration**, stopping at the end of Letter 3477. PDF 354 begins Letter **3476 — `நஞ்சை எண்ணாதே: நம்பிக் கெடாதே!`**. Letter 3477 begins at PDF 358, and PDF 364 begins Letter 3478, so stop at PDF 363.

For every page:

- compare the canonical physical-page record directly with the scan;
- apply only concrete scan-proven corrections;
- record each correction explicitly in `FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`;
- preserve contents-layer wording separately from actual-title metadata;
- do not re-transcribe already completed letters unless a concrete defect is found.

**Do not begin English translation until the fidelity audit reaches PDF 402 / 402 and is explicitly marked PASS.**

## Git discipline

Work directly on `main`. Re-fetch live `main` immediately before mutation, preserve concurrent work, prefer a candidate tree/commit that does not move `main` until validation is complete, publish one atomic commit, fast-forward with `force: false`, and verify parent → new HEAD changed-file scope.
