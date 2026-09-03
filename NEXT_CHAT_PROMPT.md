# Next Chat Prompt — Volume 43 English Translation

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
8. `volumes/volume-43/metadata.yml`
9. `volumes/volume-43/FULL_VOLUME_STRUCTURAL_AUDIT.md`
10. `volumes/volume-43/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`
11. `volumes/volume-43/TRANSLATION_PLAN.md`
12. `volumes/volume-43/translations/en/README.md`
13. `volumes/volume-43/translations/en/PROGRESS.md`
14. `volumes/volume-43/translations/en/GLOSSARY.md`
15. `volumes/volume-43/translations/en/PILOT_REVIEW_3428_3430.md`
16. `volumes/volume-43/translations/en/TRANSLATION_MANIFEST.csv`

## Durable Volume 43 state

- Tamil canonical/source coverage: **PDF 001–402 / 402 — complete**
- Tamil source records: **56 / 56 — 3428–3483**
- Structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — 402 / 402**
- Partial/source-incomplete records: **none**
- English translated/source-checked: **3 / 56 — 3428–3430**
- English pilot: **PASS — PDF 024–048**
- Volume 43 English conventions: **LOCKED**
- Bilingual meaning-level alignment: **not started**
- Editorial/final-release gates: **not started**

The controlling scan remains the highest Tamil authority if a possible Tamil defect is discovered. For normal English work, audited canonical Tamil is the immediate source. Do not reopen completed Tamil verification without a concrete defect.

## Completed English pilot — do not repeat

1. **3428** — PDF **024–032** — `Are They Not the Hands That Protect?` — source-checked
2. **3429** — PDF **033–039** — `Let Us Relieve the Hardships of the Tamils Who Have Come Here Too!` — source-checked
3. **3430** — PDF **040–048** — `Kerala Government, With Ears That Will Not Hear; Why Sting Like a Scorpion!` — source-checked

Every pilot record contains its complete audited Tamil appendix. Pilot source-check required **0 canonical Tamil changes**.

## Locked English policy

Follow `TRANSLATION_PLAN.md` and `translations/en/GLOSSARY.md`. Preserve thought/argument order, political directness, accusation, irony, rhetorical questions, repetition, dates, figures, units, lists, quotations, source-supplied English and source anomalies. Retain `Udanpirappē`, standard `With affection, M.K.`, and public-language `lakh` / `crore`. Do not silently reconcile claims from outside knowledge.

`source-checked` and `bilingual_alignment_status: aligned` are separate gates. Do not mark a record aligned during ordinary translation/source-check.

## Exact next activity

Translate and source-check the first normal five-record batch — **Letters 3431–3435 / PDF 049–086**:

1. **3431** — PDF **049–053**
2. **3432** — PDF **054–060**
3. **3433** — PDF **061–069**
4. **3434** — PDF **070–075**
5. **3435** — PDF **076–086**

Stop after **Letter 3435 / PDF 086**. PDF **087** begins Letter 3436; do not include it in the same activity.

For each record:

- draft the complete thought-preserving English translation from audited canonical Tamil;
- source-check every title, paragraph, figure, quotation, list, date and closing;
- include the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்` with physical source-page markers;
- add glossary entries only for genuinely new recurring terminology or source-supported distinctions;
- update English manifest/README/progress, metadata and handover controls;
- keep bilingual alignment for the later separate alignment phase.

## Git discipline

Work directly on `main`. Re-fetch live `main` immediately before mutation, preserve concurrent work, prepare and validate a candidate tree/commit before moving `main`, publish one atomic commit, fast-forward with `force: false`, and verify parent → new HEAD changed-file scope.
