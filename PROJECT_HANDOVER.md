# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-28

This document is the current project-level handover. Read it together with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`. If documents conflict, the controlling processing/batching/transcription guides take precedence.

## 1. Source authority

The repository preserves Kalaignar’s Murasoli letters as a page-faithful archival corpus and, where completed, verified bilingual Tamil–English records.

**The controlling source scan controls Tamil readings.** OCR, contents pages, another edition, outside historical knowledge, translations and inferred chronology may assist navigation but may not silently override the source. Historical wording, source errors, numbering anomalies, punctuation, quoted material, English text and physical boundaries are preserved and documented.

For English work, the audited canonical Tamil is the immediate translation source; the scan remains ultimate authority if a translation check exposes a possible Tamil discrepancy.

## 2. Current active work — Volume 45 English translation

### Tamil archival boundary — complete

- Controlling source: `TVA_BOK_0065831_கலைஞரின்_கடிதங்கள்_தொகுதி_45.pdf`
- Source PDF pages: **402**
- Source date range: **12.03.2011–27.09.2011**
- Canonical Tamil: **001–402 / 402 complete**
- Source letters: **55 / 55, 3537–3591 complete**
- Letter 3591 closing: **PDF 401 / printed page 400 / `27-9-2011`**
- PDF 402: back cover / publisher matter
- Full-volume Tamil structural audit: **PASS**
- Second full-volume direct visual/textual-fidelity verification: **PASS — 402 / 402**
- Final cumulative second-pass corrections: **243 canonical page files / 623 correction spans**

The final fidelity batch was PDF 386–402: 16 corrected page files / 18 spans; PDF 402 passed unchanged. The earlier Letter 3576 `பார்!` control-layer reading was withdrawn; direct scan verification establishes `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!`. The genuine Letter 3575 source-context difference remains: contents `...!` versus start `....!`.

Confirmed printed anomalies documented in the Tamil audits must remain source-exact. Do not normalize them from outside knowledge.

### English translation startup — completed pilot

English translation began only after the complete Tamil fidelity checkpoint was verified on live `main`.

Reference workflow inspected before startup:

- Volume 49 translation plan and bilingual implementation — principal reference;
- Volume 47 translation plan, glossary, alignment and completed release controls — supporting reference.

Volume 45 now has:

- `volumes/volume-45/TRANSLATION_PLAN.md`
- `volumes/volume-45/translations/en/README.md`
- `volumes/volume-45/translations/en/PROGRESS.md`
- `volumes/volume-45/translations/en/GLOSSARY.md`
- `volumes/volume-45/translations/en/PILOT_REVIEW_3537_3539.md`
- `volumes/volume-45/TRANSLATION_PILOT_CHECKPOINT.md`

Pilot status:

- Pilot letters: **3537–3539**
- Audited canonical pilot source: **PDF 024–049**
- Draft-translated: **3 / 55**
- Source-checked: **3 / 55**
- Bilingual-aligned: **0 / 55**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**
- Tamil canonical changes during pilot: **0**
- Pilot review: **PASS — STYLE LOCKED**

Pilot bilingual records:

1. `translations/en/letters/3537-rural-development-and-panchayat-raj-five-year-achievements-2.md`
2. `translations/en/letters/3538-rural-development-and-panchayat-raj-five-year-achievements-3.md`
3. `translations/en/letters/3539-health-and-family-welfare-five-year-achievements-1.md`

Each contains source metadata, the locked standard translator’s note, complete English translation, minimal necessary notes, and complete audited Tamil under `Original Tamil — மூலத் தமிழ்`.

A source-coverage correction was made during review of Letter 3539 English so that the scan-audited `1,70,803` eye-defect figure and `1,02,779` spectacles figure are both represented. This changed English only; Tamil remained untouched.

### Locked English conventions

- `உடன்பிறப்பே` → **Udanpirappē**.
- `அன்புள்ள, மு.க.` → **With affection, M.K.**
- clear contemporary, thought-preserving, non-literary English;
- no summarising of substantive source material;
- preserve political directness, irony, questions, repetition, quotations, names, dates and figures;
- `lakh` / `crore` retained;
- no external historical correction of source facts/anomalies;
- complete audited Tamil reproduced in every bilingual record;
- minimal explanatory notes only where needed;
- pilot style is now locked.

Normal post-pilot drafting cadence for Volume 45: **five complete consecutive letters per drafting iteration**.

### Exact next activity

Translate **Letters 3540–3544** as one five-complete-letter drafting iteration.

For each letter:

1. read the complete chapter boundary and every audited canonical Tamil page;
2. translate every substantive heading, paragraph, list, quotation, figure and rhetorical question;
3. use the locked Volume 45 translator’s note and glossary conventions;
4. reproduce the complete audited Tamil under `Original Tamil — மூலத் தமிழ்`;
5. source-check the complete English against the full canonical Tamil range;
6. update glossary only for genuinely new recurring terms;
7. update English progress, Volume 45 controls, handover and next-chat boundary;
8. make the batch durable on `main` and verify live GitHub.

Do **not** mark drafting records final `verified`; bilingual alignment remains a later separate QA gate.

## 3. Completed reference volumes

- **Volume 01:** fully released; 401 / 401 pages, 110 / 110 letters, Tamil gates PASS, 110 / 110 final bilingual release.
- **Volume 46:** complete through English release; 55 actual source records; preserves numbering anomalies including missing 3636 and 3644–3646 and duplicated 3637.
- **Volume 47:** 59 / 59 English release-ready within surviving source; Letter 3681 remains source-incomplete because printed page 252 is absent.
- **Volume 48:** completed English release reference.
- **Volume 49:** principal structural/translation quality reference; 53 / 53 verified and released.

Never copy volume-specific facts from a reference volume into Volume 45.

## 4. QA separation

Keep stages distinct:

1. Tamil batch/iteration audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. English drafting/source check;
5. bilingual alignment;
6. volume-level English editorial consistency review;
7. release manifest/report.

For Volume 45, Tamil stages are complete; English stage 4 has completed the pilot only.

## 5. Git/concurrency discipline

- Work on `main` as requested.
- Never force-push routine work.
- Recheck live `main` immediately before mutation.
- Preserve unrelated concurrent changes.
- Keep declared batch scope explicit.
- Prefer atomic commits for normal defined batches where technically possible.
- Remove temporary render/OCR/export artifacts from repository trees.
- Compare intended parent→new commit and fetch live `main` afterward.

The English initialization/pilot was written incrementally through connector content writes and therefore exists as a short sequence of commits rather than one atomic startup commit. Do not rewrite or force-push that history; continue forward from live `main`.

## 6. Meaning of “Proceed with next activity”

Inspect live durable state, identify the next already-defined batch/gate, execute it directly, and report completed scope, QA result, live commit SHA, counts/status and exact next activity. Do not ask the user to choose among routine next steps.

## 7. Clean interruption rule

The repository, not the chat, must carry the durable completed range, QA state and exact next activity. At this handover boundary, Volume 45 English is complete through **Letters 3537–3539 / 3 of 55 source-checked**, style locked, with exact next drafting batch **3540–3544**.
