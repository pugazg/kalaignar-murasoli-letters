# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-28

Read this together with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`. If documents conflict, the controlling processing/batching/transcription guides take precedence.

## 1. Source authority

**The controlling source scan controls Tamil readings.** OCR, contents pages, another edition, outside historical knowledge, translations and inferred chronology may assist navigation but may not silently override the source. Historical wording, source errors, numbering anomalies, punctuation, quoted material, English text and physical boundaries are preserved and documented.

For English work, the audited canonical Tamil is the immediate translation/alignment source. Any alignment check that exposes a possible Tamil discrepancy must trigger targeted direct scan re-verification before either Tamil or English is changed.

## 2. Current active work — Volume 45 English bilingual alignment

### Tamil archival boundary — complete

- Controlling source: `TVA_BOK_0065831_கலைஞரின்_கடிதங்கள்_தொகுதி_45.pdf`
- Source PDF pages: **402**
- Source date range: **12.03.2011–27.09.2011**
- Canonical Tamil: **001–402 / 402 complete**
- Source letters: **55 / 55 — 3537–3591**
- Full-volume Tamil structural audit: **PASS**
- Second full-volume direct visual/textual-fidelity verification: **PASS — 402 / 402**
- Historical second-pass correction tally: **243 canonical page files / 623 correction spans**
- Translation-discovered targeted correction: **PDF 187 / 1 additional scan-proven span**
- Combined canonical correction tally: **243 unique corrected page files / 624 spans**

Letter 3576 is scan-proven as `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!`; the earlier `பார்!` control-layer reading is withdrawn. Letter 3575 retains a genuine source-context punctuation difference: contents `...!` versus letter-start `....!`. Letter 3586 is scan-proven as `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!`; the former `தமிழக அரசு...` reading is withdrawn.

### Translation-discovered PDF 187 correction

During Letter 3560 source-check, the canonical PDF 187→188 transition exposed an omitted physical-page tail. Direct scan comparison restored the end of the Wall Street Journal quotation and the beginning of the Oxford Analytica / `India Deconstructed` passage through `என்ற ஒரு ஆய்வை`. PDF 187 was already one of the historical 243 corrected pages, so the historical tally remains **243 / 623** while the combined tally is **243 / 624**. See `volumes/volume-45/translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md`.

### English main drafting — COMPLETE

Locked conventions:

- `உடன்பிறப்பே` → **Udanpirappē**;
- `அன்புள்ள, மு.க.` → **With affection, M.K.**;
- clear contemporary, thought-preserving, non-literary English;
- no summarising of substantive source material;
- preserve political directness, irony, questions, repetition, quotations, names, dates and figures;
- retain `lakh` / `crore`;
- retain **Samacheer Kalvi** where the established scheme name recurs;
- preserve each source claim concerning **Tamil New Year / first day of Thai / Chithirai** without outside reconciliation;
- no external historical correction of source facts or anomalies;
- complete audited Tamil reproduced under `Original Tamil — மூலத் தமிழ்` in every bilingual record.

Drafting record:

- Pilot **3537–3539 / PDF 024–049** — PASS / STYLE LOCKED
- Ten normal five-letter batches through **3585–3589 / PDF 358–390** — PASS
- Final batch **3590–3591 / PDF 391–401** — PASS — Tamil changes 0

Current cumulative English drafting state:

- Draft-translated: **55 / 55 — 3537–3591**
- Source-checked: **55 / 55 — 3537–3591**
- Cumulative translated canonical source: **PDF 024–401**

### Bilingual alignment — IN PROGRESS

First alignment batch completed:

- **3537** — PDF 024–033
- **3538** — PDF 034–041
- **3539** — PDF 042–049
- **3540** — PDF 050–056
- **3541** — PDF 057–060

Combined range: **PDF 024–060 / 37 canonical pages**.

Result: **PASS — 5 / 5 aligned**.

- English semantic corrections required/applied: **0**
- Tamil canonical corrections required: **0**
- Durable report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3537_3541.md`
- The aligned letter records retain `translation_status: source-checked` and now carry `bilingual_alignment_status: aligned` plus the batch-report link.
- Existing source-specific anomalies in Letters 3539–3540 remained preserved; no outside reconstruction was introduced.

Current English QA totals:

- Source-checked: **55 / 55**
- Bilingual-aligned: **5 / 55**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

### Exact next activity — bilingual-alignment batch 3542–3546

Align five complete consecutive letters:

- **3542** — `மக்கள் நல்வாழ்வு மற்றும் குடும்ப நலத்துறையின் ஐந்தாண்டு சாதனைகள் (3)` — PDF **061–068** — 16-03-2011
- **3543** — `நகராட்சி நிர்வாகத் துறையின் ஐந்தாண்டு சாதனைகள்!` — PDF **069–079** — 17-03-2011
- **3544** — `நகராட்சி நிர்வாகத் துறையின் ஐந்தாண்டு சாதனைகள்!` — PDF **080–088** — 18-03-2011
- **3545** — `நகராட்சி நிர்வாகத் துறையின் ஐந்தாண்டு சாதனைகள்!` — PDF **089–098** — 19-03-2011
- **3546** — `கவசங்களையும் கேடயங்களையும் என்றும் பிரித்திடேன்!` — PDF **099–103** — 19-03-2011

Combined next range: **PDF 061–103 / 43 canonical pages**.

For every letter:

1. read the authoritative audited Tamil pages and the English bilingual record completely;
2. compare English against Tamil paragraph by paragraph and claim by claim;
3. check title, paragraph order, names, dates, figures, units, quotations, rhetorical questions, repetition and closing;
4. correct any omission, addition, semantic drift or factual distortion in English;
5. if alignment exposes a possible Tamil defect, stop and re-check the controlling scan before changing either layer;
6. mark passed records `bilingual_alignment_status: aligned` while retaining their source-checked drafting history;
7. create a durable alignment report and update cumulative alignment counts and exact next batch.

Source-specific cautions for the next batch:

- Letter 3545 / PDF 098 preserves the unusual printed form `112.2006-ல்`; do not silently correct it.
- Letter 3546 / PDF 102 contains later library stamp/handwriting already excluded from canonical edition text; do not reintroduce it.

Do **not** merge the later volume-level English editorial consistency review into bilingual alignment.

## 3. QA separation

Keep stages distinct:

1. Tamil batch/iteration audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. targeted scan correction if translation/alignment exposes a residual Tamil discrepancy;
5. English drafting/source check — **COMPLETE**;
6. bilingual alignment — **IN PROGRESS; 5 / 55 aligned; next 3542–3546 / PDF 061–103**;
7. volume-level English editorial consistency review;
8. release manifest/report.

## 4. Git/concurrency discipline

- Work on `main` as requested.
- Never force-push routine work.
- Recheck live `main` immediately before mutation.
- Preserve unrelated concurrent changes.
- Keep declared batch/gate scope explicit.
- Prefer atomic commits where technically possible.
- Do not rewrite earlier incremental connector history.
- Remove temporary artifacts from repository trees.
- Verify live `main` after completed work.

## 5. Meaning of “Proceed with next activity”

Inspect live durable state, identify the next already-defined batch/gate, execute it directly, and report completed scope, QA result, live commit SHA/state, counts and exact next activity. Do not ask the user to choose among routine next steps.
