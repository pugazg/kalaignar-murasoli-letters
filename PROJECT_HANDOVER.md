# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-09-03

Read this with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`.

## Fresh-chat rule

On a new chat, **fetch live `main` before relying on any checkpoint in this document**. If live `main` is newer than any recorded checkpoint, preserve the newer durable state and derive the next activity from the current repository controls. Never regress completed work because an older prompt or handover names an earlier boundary.

The durable Volume 43 Tamil gate is now complete. Any commit SHA copied into a prompt or handover is only a checkpoint; live `main` remains authoritative.

For a fresh chat, the controlling Volume 43 PDF is only required if a possible Tamil defect must be re-opened. English work should normally use audited canonical Tamil as its immediate source.

## Source authority

The controlling scan controls Tamil readings. Audited canonical Tamil is the immediate English-QA source. OCR, translations, contents pages, outside sources and inferred chronology may not silently override the scan.

## Volume 43 — ACTIVE ENGLISH WORK

Controlling source: `TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

Current durable state:

- Printed pages: **400**
- Physical PDF pages: **402**
- Source SHA-256: `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`
- Source size: **229,557,034 bytes**
- Date span: **01.11.2009–17.07.2010**
- Printed contents: **PDF 018–022**
- Source inventory: **56 records, 3428–3483**
- Canonical Tamil/source-page representation: **PDF 001–402 / 402**
- Completed Tamil letters: **56 / 56 — 3428–3483**
- Partial/source-incomplete records: **none**
- Full-volume Tamil structural audit: **PASS**
- Second full-volume direct visual/textual-fidelity verification: **PASS — 402 / 402**
- English translation: **READY FOR PILOT — 0 / 56 translated**

### Final fidelity closure

The second direct visual/textual-fidelity pass has now covered the complete source **PDF 001–402 / 402**. The final continuation directly checked PDFs **375–402**, comprising Letters **3480–3483**, PDF 401 non-letter end matter and PDF 402 back-cover / publisher material.

Final-range scan-proven corrections include:

- PDF 376 — `“சிவில்”. “மெக்கானிகல்”` → `“சிவில்”, “மெக்கானிகல்”`;
- PDF 377 — `தொழில்கல்வி` → `தொழிற்கல்வி`;
- PDF 380 — Letter 3481 actual title `வேண்டாத விமர்சனங்கள்? மறப்போம்! மன்னிப்போம்!` → `வேண்டாத விமர்சனங்கள்; மறப்போம்! மன்னிப்போம்!`;
- PDF 388 — removed an editorially introduced leading hyphen before `ஆதிதிராவிடர் நலத்துறைக்கு`;
- PDF 391 — restored the printed semicolon after the 2007–2008 food-production figure;
- PDF 396 — restored the printed typographic opening single quotation mark in `‘மலிவு விலையில்...`.

The final pass also reconciles the consolidated printed-contents register with earlier direct contents-page corrections: Letter 3430 is `கேளாக் காதினராய் கேரள அரசினர்; தேளாய்க் கொட்டுவதோ!`, and Letter 3441 printed contents is `உடன்பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`.

### Final genuine title-layer differences

Preserve these source layers independently:

- **3435:** contents `முடிந்த தொடாக்கதை; முடியாத வரலாறு!`; actual `முடிந்த தொடர்கதை; முடியாத வரலாறு!`.
- **3438:** contents `ஊனமுற்றோரின் ஊன்று கோலாகக் கழக அரசு!`; actual `ஊனமுற்றோரின் ஊன்றுகோலாகக் கழக அரசு!`.
- **3441:** contents `உடன்பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`; actual `உடன் பிறப்புகளில் ஒருவனாக விடுக்கும் வேண்டுகோள்!`.
- **3463:** contents `மாற்றுத் திறனாளிகளும் - மனிதரே!`; actual `மாற்றுத் திறனாளிகளும் - மானிடரே!`.
- **3464:** contents `பொதுக்கருத்து பற்றி பேரறிஞர் ரூசோவின் கருத்து என்ன?`; actual `பொதுக்கருத்து பற்றி பேரறிஞன் ரூசோவின் கருத்து என்ன?`.
- **3467:** contents uses `மகாராஜனுக்கு`; actual uses `மகராஜனுக்கு`; contents date remains blank and the reproduced handwritten letter is separately dated `2/11/1974`.
- **3472–3474:** contents uses long `ஓய்யாரக்...`; actual starts use short `ஒய்யாரக்...`.

Earlier provisional discrepancy claims for **3430, 3476, 3477 and 3481** are superseded by the completed second pass. Letters 3476, 3477 and 3481 use semicolons in both the printed contents and actual letter starts.

### Exact next activity

Begin the **Volume 43 English translation pilot — Letters 3428–3430 / PDF 024–048**.

Mandatory English startup before changing records:

- read `volumes/volume-43/TRANSLATION_PLAN.md` completely;
- read `volumes/volume-43/translations/en/README.md` and `PROGRESS.md`;
- inspect the completed Volume 44 English plan, pilot review and glossary as repository reference;
- use audited canonical Tamil as the immediate source;
- use the controlling scan only if a concrete Tamil defect is suspected;
- draft/source-check exactly **3428, 3429 and 3430** and stop before 3431;
- create complete bilingual records including `## Original Tamil — மூலத் தமிழ்`;
- lock Volume 43 translation conventions after the pilot source-check;
- keep bilingual meaning-level alignment as a later separate durable gate.

## Volume 44 — COMPLETE

Controlling source: `TVA_BOK_0065830_கலைஞரின்_கடிதங்கள்_தொகுதி_44.pdf`

Final durable state:

- PDF pages: **400**
- Source inventory: **53 records, 3484–3536**
- Canonical Tamil pages: **001–400 / 400**
- Completed Tamil letters: **53 / 53 — 3484–3536**
- Full-volume Tamil structural audit: **PASS**
- Second full-volume visual/textual-fidelity verification: **PASS — 400 / 400**
- English source-checked: **53 / 53**
- Bilingual alignment: **COMPLETE — 53 / 53**
- English editorial consistency review: **PASS — 53 / 53**
- English final release verification: **PASS — 53 / 53**

No further Volume 44 English QA or release gate remains pending unless a concrete defect is reported or a new audit is explicitly requested.

## Volume 45 — COMPLETE

Volume 45 remains complete through Tamil and English release gates.

## Fresh-window start instruction

In the next chat, paste the complete contents of `NEXT_CHAT_PROMPT.md` as the first message. The new chat should fetch live `main`, read the mandatory guides and controls, and begin the exact Volume 43 English pilot without reopening completed Tamil verification unless a concrete defect is found.

## Git discipline

Work on `main` when requested. Prefer one validated atomic commit per declared activity. Never force-push routine work. Recheck live `main` immediately before mutation, preserve concurrent changes, rebuild on a newer HEAD if needed, fast-forward only with `force: false`, and verify parent → new HEAD changed-file scope afterward.
