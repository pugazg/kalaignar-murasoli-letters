# Next Chat Prompt — Volume 43 English Translation Batch 5

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
- Normal batch 2 **3436–3440 / PDF 087–118**: **PASS — 5 / 5 source-checked**
- Normal batch 3 **3441–3445 / PDF 119–156**: **PASS — 5 / 5 source-checked**
- Normal batch 4 **3446–3450 / PDF 157–198**: **PASS — 5 / 5 source-checked**
- Cumulative source-check: **23 / 56 — 3428–3450**
- Canonical Tamil changes during English work: **0**
- Bilingual meaning-level alignment: **not started; separate later gate**
- Editorial review: **not started**
- Final English release: **not started**

Every completed English record contains the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்`, with physical source-page markers.

## Batch 4 translation notes

- Letter **3446** preserves source-supplied Caldwell English and the historical institutional-resolution sequence.
- Letter **3447** preserves Pavanar’s fifteen source-supplied English evidence headings exactly; Lemuria and language-history propositions remain source-framed.
- Letter **3448** translates the Tamil rendering of the government expert report printed in the canonical source; do not substitute an outside English report.
- Letter **3449** translates the Tamil rendering of Professor George L. Hart’s statement printed in the canonical source; do not substitute an outside English statement.
- Letter **3450** preserves the full 2003 speech, figures, expected institutional effects, participant list and political criticism as source-attributed material.
- No Tamil defect was suspected; **0 canonical Tamil changes**.

## Source-layer reminder

Final genuine printed-contents / actual-title differences are **3435, 3438, 3441, 3463, 3464, 3467, 3472, 3473 and 3474**. Preserve those source layers independently when their records are reached.

## English policy

Use audited canonical Tamil as the immediate translation source. Preserve thought/argument order, political directness, accusation, irony, rhetorical questions, repetition, quotations, names, dates, figures, units, source-supplied English and documented source anomalies. Do not silently improve or reconcile historical/political claims from outside knowledge.

Follow `volumes/volume-43/TRANSLATION_PLAN.md` and the locked treatments in `translations/en/GLOSSARY.md`. `source-checked` does not mean `aligned`.

## Exact next activity

Translate and source-check exactly **five records — Letters 3451–3455 / PDF 199–245**:

1. **3451 — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் -7 கடிதமல்ல; காலத்தால் அழிக்க முடியாத செப்பேடு!` — PDF 199–207**
2. **3452 — `வாழ்த்து குவிக்கின்றேன்; வளமார் தமிழக மக்களுக்கு!` — PDF 208–211**
3. **3453 — `ஒரு “தலைவன்” இருக்கிறான் மயங்காதே!` — PDF 212–234**
4. **3454 — `அம்மவோ; இந்த நாளில் அந்த நாள் நினைவு!` — PDF 235–240**
5. **3455 — `“வேலியே பயிரை மேய்வதா?”` — PDF 241–245**

Stop before **Letter 3456 / PDF 246**.

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
