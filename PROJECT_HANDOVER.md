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
4. **3552–3556 / PDF 142–163 / 22 pages** — PASS — 5 / 5 aligned; English corrections 1; Tamil changes 0. Report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3552_3556.md`.

The fourth batch's English-only correction is in Letter 3554. Source `உங்களால் நிறைவேற்றப்பட்ட திட்டங்கள் என்று ஒவ்வொருவரும் கூறியபோது` reports words people addressed to Kalaignar. The earlier English could point `you` at the letter's reader; the aligned record now makes the relation explicit as **“when one person after another spoke to me of the schemes ‘you implemented,’ I gave myself marks.”** Canonical Tamil did not change.

Source-specific cautions retained in the fourth batch include Letter 3552's unusual title form `யாரா`, Letter 3555's joined source date forms in the reproduced earlier letter, and Letter 3556's political criticism retained strictly as source voice.

Current English QA totals:

- Source-checked: **55 / 55**
- Bilingual-aligned: **20 / 55 — 3537–3556 / PDF 024–163**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

### Exact next activity — bilingual-alignment batch 3557–3561

Align five complete consecutive letters:

- **3557** — PDF **164–169**
- **3558** — PDF **170–175**
- **3559** — PDF **176–180**
- **3560** — PDF **181–188**
- **3561** — PDF **189–196**

Combined next range: **PDF 164–196 / 33 canonical pages**.

Established source cautions within that range include PDF 170 `பொக்கம்`, PDF 176 `10ந்தேதியன்று`, PDF 177 `முஜா கி தீன்`, and the scan-proven PDF 187 restoration already documented in `TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md`. Preserve those forms/corrections exactly.

For every letter: read the complete authoritative audited Tamil and complete English record; compare title, salutation, paragraph order, substantive claims, lists, quotations, names, dates, figures, units, rhetoric, repetition and closing; correct only demonstrated English omission/addition/semantic drift; if any new Tamil defect is suspected, re-check the controlling scan before changing either layer; mark passed records `bilingual_alignment_status: aligned`; create a durable batch report and update controls.

Do **not** merge the later volume-level English editorial consistency review into bilingual alignment.

## 3. QA separation

Keep stages distinct:

1. Tamil batch/iteration audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. targeted scan correction if translation/alignment exposes a residual Tamil discrepancy;
5. English drafting/source check — **COMPLETE**;
6. bilingual alignment — **IN PROGRESS; 20 / 55 aligned; next 3557–3561 / PDF 164–196**;
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
