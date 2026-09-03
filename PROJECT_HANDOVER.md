# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-09-03

Read this with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`.

## Fresh-chat rule

On a new chat, **fetch live `main` before relying on any checkpoint in this document**. If live `main` is newer than any recorded checkpoint, preserve the newer durable state and derive the next activity from the current repository controls. Never regress completed work because an older prompt or handover names an earlier boundary.

The durable Volume 43 Tamil gates are complete. English translation/source-check is now the active phase. Any commit SHA copied into a prompt or handover is only a checkpoint; live `main` remains authoritative.

For a fresh chat, the controlling Volume 43 PDF is only required if a possible Tamil defect must be reopened. English work should normally use audited canonical Tamil as its immediate source.

## Source authority

The controlling scan controls Tamil readings. Audited canonical Tamil is the immediate English-QA source. OCR, translations, contents pages, outside sources and inferred chronology may not silently override the scan.

## Volume 43 — ACTIVE ENGLISH WORK

Controlling source: `TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

Current durable Tamil state:

- Printed pages: **400**
- Physical PDF pages: **402**
- Source SHA-256: `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`
- Date span: **01.11.2009–17.07.2010**
- Source inventory: **56 records, 3428–3483**
- Canonical Tamil/source-page representation: **PDF 001–402 / 402**
- Completed Tamil letters: **56 / 56 — 3428–3483**
- Partial/source-incomplete records: **none**
- Full-volume Tamil structural audit: **PASS**
- Second full-volume direct visual/textual-fidelity verification: **PASS — 402 / 402**

Current durable English state:

- Pilot **3428–3430 / PDF 024–048**: **PASS — 3 / 3 source-checked**
- Translation conventions: **LOCKED**
- Normal batch 1 **3431–3435 / PDF 049–086**: **PASS — 5 / 5 source-checked**
- Normal batch 2 **3436–3440 / PDF 087–118**: **PASS — 5 / 5 source-checked**
- Normal batch 3 **3441–3445 / PDF 119–156**: **PASS — 5 / 5 source-checked**
- Normal batch 4 **3446–3450 / PDF 157–198**: **PASS — 5 / 5 source-checked**
- Cumulative English source-check: **23 / 56 — 3428–3450**
- Canonical Tamil changes during English work: **0**
- Bilingual meaning-level alignment: **not started**
- Editorial consistency review: **not started**
- Final English release verification: **not started**

Every English record includes the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்`, with physical source-page markers retained. `source-checked` must remain distinct from the later `aligned` gate.

### Batch 4 durable notes

- **3446** preserves the source-supplied Caldwell English and the sequence of Saiva Siddhanta / Karanthai Tamil Sangam resolutions. Older Tamil quotations are translated for meaning; exact wording remains in the Tamil appendix.
- **3447** preserves Pavanar’s fifteen source-supplied English evidence headings exactly; Lemuria, linguistic ancestry, historical precedence and related propositions remain source-framed.
- **3448** translates the Tamil rendering of the government expert report actually printed in the canonical source; comparative-linguistic, archaeological and chronological claims are not externally reconciled.
- **3449** translates the Tamil rendering of Professor George L. Hart’s statement rather than importing an outside English version; university resolutions and the Salini Ilanthiraiyan episode are retained as printed.
- **3450** preserves the 2003 speech, source figures, expected institutional consequences, participant lists and final political criticism as source-attributed material.
- No audited Tamil defect was suspected during this batch; **0 Tamil changes**.

### Final genuine title-layer differences

Preserve these source layers independently:

- **3435:** contents `முடிந்த தொடாக்கதை; முடியாத வரலாறு!`; actual `முடிந்த தொடர்கதை; முடியாத வரலாறு!`.
- **3438:** contents `ஊனமுற்றோரின் ஊன்று கோலாகக் கழக அரசு!`; actual `ஊனமுற்றோரின் ஊன்றுகோலாகக் கழக அரசு!`.
- **3441:** contents `உடன்பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`; actual `உடன் பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`.
- **3463:** contents `மாற்றுத் திறனாளிகளும் - மனிதரே!`; actual `மாற்றுத் திறனாளிகளும் - மானிடரே!`.
- **3464:** contents `பொதுக்கருத்து பற்றி பேரறிஞர் ரூசோவின் கருத்து என்ன?`; actual `பொதுக்கருத்து பற்றி பேரறிஞன் ரூசோவின் கருத்து என்ன?`.
- **3467:** contents uses `மகாராஜனுக்கு`; actual uses `மகராஜனுக்கு`; contents date remains blank and the reproduced handwritten letter is separately dated `2/11/1974`.
- **3472–3474:** contents uses long `ஓய்யாரக்...`; actual starts use short `ஒய்யாரக்...`.

Earlier provisional discrepancy claims for **3430, 3476, 3477 and 3481** are superseded by the completed second pass.

### Exact next activity

Translate and source-check **Letters 3451–3455 / PDF 199–245** as Volume 43 normal English batch 5:

- **3451 — PDF 199–207** — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் -7 கடிதமல்ல; காலத்தால் அழிக்க முடியாத செப்பேடு!`
- **3452 — PDF 208–211** — `வாழ்த்து குவிக்கின்றேன்; வளமார் தமிழக மக்களுக்கு!`
- **3453 — PDF 212–234** — `ஒரு “தலைவன்” இருக்கிறான் மயங்காதே!`
- **3454 — PDF 235–240** — `அம்மவோ; இந்த நாளில் அந்த நாள் நினைவு!`
- **3455 — PDF 241–245** — `“வேலியே பயிரை மேய்வதா?”`

Mandatory English startup before changing records:

- read `volumes/volume-43/TRANSLATION_PLAN.md` completely;
- read `volumes/volume-43/translations/en/README.md`, `PROGRESS.md`, `GLOSSARY.md` and `TRANSLATION_MANIFEST.csv`;
- use audited canonical Tamil as the immediate source;
- use the controlling scan only if a concrete Tamil defect is suspected;
- create complete bilingual records including `## Original Tamil — மூலத் தமிழ்`;
- source-check every paragraph, figure, quotation, date, title and closing;
- update the glossary only for genuinely new recurring terms;
- stop after **3455 / PDF 245** and do not begin **3456 / PDF 246**;
- keep bilingual meaning-level alignment as a later separate durable gate.

## Volume 44 — COMPLETE

Volume 44 remains complete through Tamil structural/fidelity gates and all English source-check, bilingual-alignment, editorial-review and final-release gates: **53 / 53**.

## Volume 45 — COMPLETE

Volume 45 remains complete through Tamil and English release gates: **55 / 55**.

## Fresh-window start instruction

In the next chat, paste the complete contents of `NEXT_CHAT_PROMPT.md` as the first message. The new chat should fetch live `main`, read the mandatory guides and controls, and begin the exact Volume 43 English batch without reopening completed Tamil verification unless a concrete defect is found.

## Git discipline

Work on `main` when requested. Prefer one validated atomic commit per declared activity. Never force-push routine work. Recheck live `main` immediately before mutation, preserve concurrent changes, rebuild on a newer HEAD if needed, fast-forward only with `force: false`, and verify parent → new HEAD changed-file scope afterward.
