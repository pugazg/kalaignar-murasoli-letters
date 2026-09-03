# Next Chat Prompt — Volume 43 English Translation Batch 2

Continue the Kalaignar Murasoli Letters archival / bilingual project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF:

`TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state. Do not reset, repeat or reopen completed Tamil or English work because a copied checkpoint is older.

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
16. `volumes/volume-43/translations/en/GLOSSARY.md`
17. `volumes/volume-43/translations/en/TRANSLATION_MANIFEST.csv`
18. `volumes/volume-43/translations/en/PILOT_REVIEW_3428_3430.md`

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

The controlling scan remains the highest authority if a possible Tamil defect is discovered, but do not reopen completed Tamil verification without a concrete defect report.

## Durable English boundary

- Pilot **3428–3430 / PDF 024–048**: **PASS — 3 / 3 source-checked**
- Volume 43 translation conventions: **LOCKED**
- Normal batch 1 **3431–3435 / PDF 049–086**: **PASS — 5 / 5 source-checked**
- Cumulative source-check: **8 / 56 — 3428–3435**
- Canonical Tamil changes during English work: **0**
- Bilingual meaning-level alignment: **not started; separate later gate**
- Editorial review: **not started**
- Final English release: **not started**

Every completed English record contains the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்`, with physical source-page markers.

## Source-layer reminder

Final genuine printed-contents / actual-title differences are **3435, 3438, 3441, 3463, 3464, 3467, 3472, 3473 and 3474**.

For already translated Letter **3435**, the English record follows actual PDF 076 `முடிந்த தொடர்கதை; முடியாத வரலாறு!`; printed contents independently preserves `முடிந்த தொடாக்கதை; முடியாத வரலாறு!`.

For the next batch, Letter **3438** has a genuine difference: printed contents `ஊனமுற்றோரின் ஊன்று கோலாகக் கழக அரசு!`; actual PDF 099 `ஊனமுற்றோரின் ஊன்றுகோலாகக் கழக அரசு!`. English title metadata must follow the actual letter-start source while the Tamil appendix remains canonical.

## English policy

Use audited canonical Tamil as the immediate translation source. Preserve thought/argument order, political directness, accusation, irony, rhetorical questions, repetition, quotations, names, dates, figures, units, source-supplied English and documented source anomalies. Do not silently improve or reconcile historical/political claims from outside knowledge.

Follow `volumes/volume-43/TRANSLATION_PLAN.md` and the locked treatments in `translations/en/GLOSSARY.md`. `source-checked` does not mean `aligned`.

## Exact next activity

Translate and source-check exactly **five records — Letters 3436–3440 / PDF 087–118**:

1. **3436 — PDF 087–092**
2. **3437 — PDF 093–098**
3. **3438 — PDF 099–103**
4. **3439 — PDF 104–111**
5. **3440 — PDF 112–118**

Stop before **Letter 3441 / PDF 119**.

For every record:

- create the complete thought-preserving English translation;
- source-check every Tamil paragraph against the English;
- preserve dates, figures, quotations, rhetoric and closings;
- include the complete audited Tamil appendix with physical page markers;
- if a Tamil defect is suspected, inspect the controlling scan before changing canonical Tamil;
- update manifest, English progress/README, metadata and handover controls;
- update the glossary only for genuinely new recurring terms;
- do not perform bilingual meaning-level alignment in this activity.

## Git discipline

Work directly on `main`. Re-fetch live `main` immediately before mutation, preserve concurrent work, build a candidate tree/commit without moving `main`, validate parent → candidate changed-file scope, publish one atomic commit, fast-forward with `force: false`, and verify parent → new HEAD afterward.
