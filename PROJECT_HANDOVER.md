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

Locked conventions include `Udanpirappē`, `With affection, M.K.`, clear contemporary thought-preserving non-literary English, no summarising substantive source material, preservation of political force/irony/questions/repetition/quotations/names/dates/figures, `lakh` / `crore`, established **Samacheer Kalvi**, source-specific Tamil New Year / Thai / Chithirai claims without outside reconciliation, and complete audited Tamil under `Original Tamil — மூலத் தமிழ்` in every bilingual record.

Current drafting state:

- Draft-translated: **55 / 55 — 3537–3591**
- Source-checked: **55 / 55 — 3537–3591**
- Cumulative translated canonical source: **PDF 024–401**

### Bilingual alignment — IN PROGRESS

Completed batches:

1. **3537–3541 / PDF 024–060 / 37 pages** — PASS — 5 / 5 aligned; English corrections 0; Tamil changes 0. Report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3537_3541.md`.
2. **3542–3546 / PDF 061–103 / 43 pages** — PASS — 5 / 5 aligned; English corrections 1; Tamil changes 0. Report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3542_3546.md`.
3. **3547–3551 / PDF 104–141 / 38 pages** — PASS — 5 / 5 aligned; English corrections 0; Tamil changes 0. Report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3547_3551.md`.

The second batch's English-only correction was in Letter 3545: source `தொழில் வரி உரிமம்` / `தொழில்வரி` is represented as **Profession-tax licences** / **profession-tax revenue**, replacing the earlier broader **Trade licences** wording. Canonical Tamil did not change.

The third batch required no English or Tamil correction. Source-specific cautions remained preserved, including Letter 3548's PDF 114 `4 கோடியே 58 ஆயிரம் ரூபாய்`, Letter 3550's source-supplied English Election Commission sentence, and Letter 3551's PDF 139 **20 acres / ₹8 crore** Semmozhi Park figures without cross-letter reconciliation.

Current English QA totals:

- Source-checked: **55 / 55**
- Bilingual-aligned: **15 / 55 — 3537–3551 / PDF 024–141**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

### Exact next activity — bilingual-alignment batch 3552–3556

Align five complete consecutive letters:

- **3552** — `யாரா உஷார்! பதுங்கி வருகிறது பணநாயகம்!` — PDF **142–144** — 30-03-2011
- **3553** — `“குற்றம் பார்க்கின் சுற்றம் இல்லை”!` — PDF **145–149** — 05-04-2011
- **3554** — `மதிப்பிற்குரிய மதிப்பெண் என்ன?` — PDF **150–154** — 13-04-2011
- **3555** — `அன்றைக்கே எழுதியது; இன்றைக்கும் பொருந்துகிறதே!` — PDF **155–159** — 17-04-2011
- **3556** — `பார்த்தும் மறந்தாரே “காரத்”!` — PDF **160–163** — 21-04-2011

Combined next range: **PDF 142–163 / 22 canonical pages**.

For every letter: read the complete authoritative audited Tamil and complete English record; compare title, salutation, paragraph order, substantive claims, lists, quotations, names, dates, figures, units, rhetoric, repetition and closing; correct only demonstrated English omission/addition/semantic drift; if any Tamil defect is suspected, re-check the controlling scan before changing either layer; mark passed records `bilingual_alignment_status: aligned`; create a durable batch report and update controls.

Do **not** merge the later volume-level English editorial consistency review into bilingual alignment.

## 3. QA separation

Keep stages distinct:

1. Tamil batch/iteration audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. targeted scan correction if translation/alignment exposes a residual Tamil discrepancy;
5. English drafting/source check — **COMPLETE**;
6. bilingual alignment — **IN PROGRESS; 15 / 55 aligned; next 3552–3556 / PDF 142–163**;
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
