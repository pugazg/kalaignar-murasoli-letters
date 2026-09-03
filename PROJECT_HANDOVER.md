# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-09-03

Read this with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`.

## Fresh-chat rule

On a new chat, **fetch live `main` before relying on any checkpoint in this document**. If live `main` is newer than any recorded checkpoint, preserve the newer durable state and derive the next activity from the current repository controls. Never regress completed work because an older prompt or handover names an earlier boundary.

The durable Volume 43 Tamil gate is complete. English work should normally use audited canonical Tamil as its immediate source; return to the controlling scan only if a concrete Tamil defect is suspected.

## Source authority

The controlling scan controls Tamil readings. Audited canonical Tamil is the immediate English-QA source. OCR, translations, contents pages, outside sources and inferred chronology may not silently override the scan.

## Volume 43 — ACTIVE ENGLISH WORK

Controlling source: `TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

Current durable state:

- Printed pages: **400**
- Physical PDF pages: **402**
- Source SHA-256: `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`
- Source inventory: **56 records, 3428–3483**
- Canonical Tamil/source-page representation: **PDF 001–402 / 402**
- Completed Tamil letters: **56 / 56 — 3428–3483**
- Partial/source-incomplete records: **none**
- Full-volume Tamil structural audit: **PASS**
- Second full-volume direct visual/textual-fidelity verification: **PASS — 402 / 402**
- English translation/source-check: **3 / 56 — 3428–3430**
- Pilot review: **PASS — 3428–3430 / PDF 024–048**
- Translation conventions: **LOCKED**
- Bilingual alignment: **not started**
- English final release: **not started**

### Completed English pilot

- **3428** — PDF **024–032** — *Are They Not the Hands That Protect?* — source-checked
- **3429** — PDF **033–039** — *Let Us Relieve the Hardships of the Tamils Who Have Come Here Too!* — source-checked
- **3430** — PDF **040–048** — *Kerala Government, With Ears That Will Not Hear; Why Sting Like a Scorpion!* — source-checked

Every pilot record includes the complete audited Tamil appendix. `PILOT_REVIEW_3428_3430.md` is PASS and `GLOSSARY.md` contains the locked Volume 43 conventions. No canonical Tamil change was required during pilot source-check.

Source-checked does **not** mean bilingual-aligned. Alignment remains a later independent QA phase.

### Final genuine title-layer differences

Preserve these source layers independently:

- **3435:** contents `முடிந்த தொடாக்கதை; முடியாத வரலாறு!`; actual `முடிந்த தொடர்கதை; முடியாத வரலாறு!`.
- **3438:** contents `ஊனமுற்றோரின் ஊன்று கோலாகக் கழக அரசு!`; actual `ஊனமுற்றோரின் ஊன்றுகோலாகக் கழக அரசு!`.
- **3441:** contents `உடன்பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`; actual `உடன் பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`.
- **3463:** contents `மாற்றுத் திறனாளிகளும் - மனிதரே!`; actual `மாற்றுத் திறனாளிகளும் - மானிடரே!`.
- **3464:** contents `பொதுக்கருத்து பற்றி பேரறிஞர் ரூசோவின் கருத்து என்ன?`; actual `பொதுக்கருத்து பற்றி பேரறிஞன் ரூசோவின் கருத்து என்ன?`.
- **3467:** contents uses `மகாராஜனுக்கு`; actual uses `மகராஜனுக்கு`; contents date remains blank and the reproduced handwritten letter is separately dated `2/11/1974`.
- **3472–3474:** contents uses long `ஓய்யாரக்...`; actual starts use short `ஒய்யாரக்...`.

Earlier provisional discrepancy claims for **3430, 3476, 3477 and 3481** are superseded by the completed second Tamil pass.

### Exact next activity

Translate and source-check the first normal five-record English batch: **Letters 3431–3435 / PDF 049–086**.

Mandatory startup before changing English records:

- fetch live `main` first;
- read `volumes/volume-43/TRANSLATION_PLAN.md`, `translations/en/README.md`, `PROGRESS.md`, `GLOSSARY.md`, `PILOT_REVIEW_3428_3430.md` and `TRANSLATION_MANIFEST.csv`;
- use audited canonical Tamil as the immediate source;
- apply the locked Volume 43 conventions;
- draft/source-check exactly **3431, 3432, 3433, 3434 and 3435**;
- include the complete audited Tamil appendix in every record;
- stop at **PDF 086** and do not begin Letter 3436 / PDF 087;
- update the glossary only for genuinely new recurring terminology;
- keep bilingual meaning-level alignment as a later separate durable gate.

## Volume 44 — COMPLETE

Volume 44 remains complete through Tamil and English final-release gates: **53 / 53** source records, Tamil structural/fidelity PASS, English source-check/alignment/editorial/final-release PASS.

## Volume 45 — COMPLETE

Volume 45 remains complete through Tamil and English release gates.

## Fresh-window start instruction

In the next chat, paste the complete contents of `NEXT_CHAT_PROMPT.md` as the first message. The new chat should fetch live `main`, read the mandatory guides and English controls, and begin the exact Volume 43 regular batch without reopening completed Tamil verification unless a concrete defect is found.

## Git discipline

Work on `main` when requested. Prefer one validated atomic commit per declared activity. Never force-push routine work. Recheck live `main` immediately before mutation, preserve concurrent changes, rebuild on a newer HEAD if needed, fast-forward only with `force: false`, and verify parent → new HEAD changed-file scope afterward.
