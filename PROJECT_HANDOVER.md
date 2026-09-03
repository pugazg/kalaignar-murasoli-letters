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
- Normal batch 5 **3451–3455 / PDF 199–245**: **PASS — 5 / 5 source-checked**
- Cumulative English source-check: **28 / 56 — 3428–3455**
- Canonical Tamil changes during English work: **0**
- Bilingual meaning-level alignment: **not started**
- Editorial consistency review: **not started**
- Final English release verification: **not started**

Every English record includes the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்`, with physical source-page markers retained. `source-checked` must remain distinct from the later `aligned` gate.

### Batch 5 durable notes

- **3451** closes the seven-part `செம்மொழி வரலாற்றில் சில செப்பேடுகள்` sequence. The recurring image remains **copper-plate record**. Sonia Gandhi’s 8 November 2005 source-supplied English letter is preserved exactly as printed; its surrounding Tamil explanation is translated separately.
- **3452** preserves the Tamil New Year/Pongal imagery, Tiruvalluvar-year account, new Assembly/Secretariat and library/conference references, and welfare-policy figures in source order.
- **3453** preserves the Fort St George Assembly-history chronology, dated laws/resolutions, political rebuttals, source-supplied English audit/Wikipedia passages, debt/housing/growth figures and the closing M.G.R. song exchange. Political accusations remain explicitly source-attributed.
- **3454** preserves the author’s Anna memorial chronology, private recollections, quoted speeches, death imagery and the audited source ellipsis lengths on PDFs 237–238.
- **3455** preserves the Uttaramerur/*kudavolai* democracy argument and the Pennagaram/Election Commission criticism, including the Dr Ramadoss statement, as source-attributed political material.
- No audited Tamil defect was suspected during this batch; **0 Tamil changes**.
- No genuinely new recurring translation term was introduced; `GLOSSARY.md` remains unchanged.

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

Translate and source-check **Letters 3456–3460 / PDF 246–265** as Volume 43 normal English batch 6:

- **3456 — PDF 246–249** — `மனித நேயமும், மாசற்ற அரசியல் நாகரிகமும்!`
- **3457 — PDF 250–253** — `அவனும் சிரித்தான்; நானும் சிரித்தேன்!`
- **3458 — PDF 254–256** — `புள்ளியைத் தொடர்ந்து போட வேண்டிய கோலம்!`
- **3459 — PDF 257–259** — `கரும்பில் அரசியல்!`
- **3460 — PDF 260–265** — `தேசிய ஆதி திராவிடர் ஆணையமும், தி.மு.கழக அரசும்!`

Mandatory English startup before changing records:

- read `volumes/volume-43/TRANSLATION_PLAN.md` completely;
- read `volumes/volume-43/translations/en/README.md`, `PROGRESS.md`, `GLOSSARY.md` and `TRANSLATION_MANIFEST.csv`;
- use audited canonical Tamil as the immediate source;
- use the controlling scan only if a concrete Tamil defect is suspected;
- create complete bilingual records including `## Original Tamil — மூலத் தமிழ்`;
- source-check every paragraph, figure, quotation, date, title and closing;
- update the glossary only for genuinely new recurring terms;
- stop after **3460 / PDF 265** and do not begin **3461 / PDF 266**;
- keep bilingual meaning-level alignment as a later separate durable gate.

## Volume 44 — COMPLETE

Volume 44 remains complete through Tamil structural/fidelity gates and all English source-check, bilingual-alignment, editorial-review and final-release gates: **53 / 53**.

## Volume 45 — COMPLETE

Volume 45 remains complete through Tamil and English release gates: **55 / 55**.

## Fresh-window start instruction

In the next chat, paste the complete contents of `NEXT_CHAT_PROMPT.md` as the first message. The new chat should fetch live `main`, read the mandatory guides and controls, and begin the exact Volume 43 English batch without reopening completed Tamil verification unless a concrete defect is found.

## Git discipline

Work on `main` when requested. Prefer one validated atomic commit per declared activity. Never force-push routine work. Recheck live `main` immediately before mutation, preserve concurrent changes, rebuild on a newer HEAD if needed, fast-forward only with `force: false`, and verify parent → new HEAD changed-file scope afterward.