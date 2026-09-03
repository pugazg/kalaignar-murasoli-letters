# Next Chat Prompt — Volume 43 English Translation Pilot

Continue the Kalaignar Murasoli Letters archival / bilingual project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF:

`TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state. Do not reset, repeat or reopen completed Tamil work because a copied checkpoint is older.

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
11. `volumes/volume-43/FULL_VOLUME_STRUCTURAL_AUDIT.md`
12. `volumes/volume-43/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`
13. `volumes/volume-43/TRANSLATION_PLAN.md`
14. `volumes/volume-43/translations/en/README.md`
15. `volumes/volume-43/translations/en/PROGRESS.md`
16. Volume 44's completed English translation plan / pilot / glossary as reference for repository conventions.

## Volume 43 durable Tamil boundary

- Printed pages: **400**
- Physical PDF pages: **402**
- Source SHA-256: `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`
- Source inventory: **56 records, 3428–3483**
- Date span: **01.11.2009–17.07.2010**
- Canonical Tamil/source-page representation: **PDF 001–402 / 402 — complete**
- Completed Tamil letters: **56 / 56 — 3428–3483**
- Partial/source-incomplete records: **none**
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — PDF 001–402 / 402**
- PDF **401**: non-letter end matter
- PDF **402**: back cover / portrait / publisher-contact-price material
- No Letter **3484** is created in Volume 43
- English translation: **READY FOR PILOT — 0 / 56 translated**

The controlling scan remains the highest authority if a possible Tamil defect is discovered, but do not reopen completed Tamil verification without a concrete defect report.

## Final title-layer reconciliation

The genuine printed-contents / actual-letter-title differences after the completed fidelity pass are **3435, 3438, 3441, 3463, 3464, 3467, 3472, 3473 and 3474**.

Important final supersessions:

- Letter 3430's corrected printed-contents wording matches its actual title; it is **not** a title-layer discrepancy.
- Letter 3476 actual title uses a semicolon, matching the printed contents; the earlier colon reading is superseded.
- Letter 3477 actual title uses a semicolon, matching the printed contents; the earlier colon reading is superseded.
- Letter 3481 actual title is `வேண்டாத விமர்சனங்கள்; மறப்போம்! மன்னிப்போம்!`, matching the printed contents; the earlier question-mark reading is superseded.
- Letter 3441 is a genuine difference: contents `உடன்பிறப்புகளில்...`; actual PDF 119 `உடன் பிறப்புகளில்...`.

## English policy

Use audited canonical Tamil as the immediate translation source. Preserve thought/argument order, political directness, accusation, irony, rhetorical questions, repetition, quotations, names, dates, figures, units, source-supplied English and documented source anomalies. Do not silently improve or reconcile historical/political claims from outside knowledge.

Follow `volumes/volume-43/TRANSLATION_PLAN.md`. Every English record must include the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்`.

## Exact next activity

Draft and source-check the **three-letter Volume 43 English pilot — Letters 3428–3430 / PDF 024–048**:

1. **3428 — `காக்கும் கரங்களுமன்றோ?` — PDF 024–032**
2. **3429 — `இங்கு வந்துள்ள தமிழர்க்கும் இடர் களைவோம்!` — PDF 033–039**
3. **3430 — `கேளாக் காதினராய் கேரள அரசினர்; தேளாய்க் கொட்டுவதோ!` — PDF 040–048**

Do **not** include Letter 3431 in this pilot.

For each pilot record:

- create the complete thought-preserving English translation;
- source-check every Tamil paragraph against the English;
- preserve dates, figures, quotations, rhetoric and closings;
- include the complete audited Tamil appendix;
- if a Tamil defect is suspected, inspect the controlling scan before changing canonical Tamil;
- update the English pilot review/progress and lock Volume 43 translation conventions after the pilot source-check;
- keep bilingual meaning-level alignment as a later separate durable gate.

## Git discipline

Work directly on `main`. Re-fetch live `main` immediately before mutation, preserve concurrent work, prefer a candidate tree/commit that does not move `main` until validation is complete, publish one atomic commit, fast-forward with `force: false`, and verify parent → new HEAD changed-file scope.
