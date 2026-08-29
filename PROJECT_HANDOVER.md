# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-29

Read this together with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`. If documents conflict, the controlling processing/batching/transcription guides take precedence.

## 1. Source authority

**The controlling source scan controls Tamil readings.** OCR, contents pages, another edition, outside historical knowledge, translations and inferred chronology may assist navigation but may not silently override the source. Historical wording, source errors, numbering anomalies, punctuation, quoted material, English text and physical boundaries are preserved and documented.

For English work, the audited canonical Tamil is the immediate translation/alignment source. Any English QA check that exposes a possible Tamil discrepancy must trigger targeted direct scan re-verification before either Tamil or English is changed.

## 2. Current active work — Volume 45 English editorial consistency

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

Letter 3576 is scan-proven as `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!`; the earlier `பார்!` reading is withdrawn. Letter 3575 retains a genuine source-context punctuation difference: contents `...!` versus letter-start `....!`. Letter 3586 is scan-proven as `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!`; the former `தமிழக அரசு...` reading is withdrawn.

### Translation-discovered PDF 187 correction

During Letter 3560 source-check, the canonical PDF 187→188 transition exposed an omitted physical-page tail. Direct scan comparison restored the end of the Wall Street Journal quotation and the beginning of the Oxford Analytica / `India Deconstructed` passage through `என்ற ஒரு ஆய்வை`. PDF 187 was already one of the historical 243 corrected pages, so the historical tally remains **243 / 623** while the combined tally is **243 / 624**. See `volumes/volume-45/translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md`.

### Alignment-triggered PDF 348→349 scan re-check

During Letter 3583 alignment, the English phrase “class enemies” raised a source-normalization concern. The canonical Tamil is split across PDF 348→349 as `வாக்க` / `எதிரிகளை`. Direct scan re-render and inspection confirmed that exact printed form. Canonical Tamil was therefore left unchanged. The aligned English was corrected from **“the policy of eliminating class enemies”** to the conservative **“a policy of eliminating enemies.”** This was an English-only correction and does not alter the Tamil correction tally.

### English main drafting — COMPLETE

Locked conventions include `Udanpirappē`, `With affection, M.K.`, clear contemporary thought-preserving non-literary English, no summarising substantive source material, preservation of political force/irony/questions/repetition/quotations/names/dates/figures, `lakh` / `crore`, established **Samacheer Kalvi**, source-specific Tamil New Year / Thai / Chithirai claims without outside reconciliation, and complete audited Tamil under `Original Tamil — மூலத் தமிழ்` in every bilingual record.

Current drafting state:

- Draft-translated: **55 / 55 — 3537–3591**
- Source-checked: **55 / 55 — 3537–3591**
- Cumulative translated canonical source: **PDF 024–401**

### Bilingual alignment — COMPLETE

All eleven batches are complete. Final batch:

- **3587–3591 / PDF 370–401 / 32 pages** — **PASS — 5 / 5 aligned; English corrections 1; Tamil changes 0; new scan re-checks 0.**
- Detailed report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3587_3591.md`.
- Machine-readable batch status: `volumes/volume-45/translations/en/alignment-status/3587-3591.yml`.

Final-batch source-specific results:

- **3587:** the 311-acre Thirumazhisai / Rule 110 / policy-note / 2006 satellite-town sequence aligns; the source's successive `1-9-2006` / `31-8-2006` formulations remain preserved rather than externally harmonised.
- **3588:** Samacheer Kalvi, school-day, textbook, examination, teacher-ratio, recruitment and counselling sequences align without correction.
- **3589:** one English-only correction removed the unprinted distancing hedge “in the source's argument” and restored the direct force of `நாசமாக்கி அழித்திடும்` as **“will destroy”** in the engineering-university paragraph. Canonical Tamil is unchanged.
- **3590:** local-body election, nomination, constituency-category, campaign, false-case, election-expense and media arguments align without correction.
- **3591:** K.P.P. Samy, M.K. Balan, police-transfer, High Court and Valluvar-Kural sequences align without correction.

The large bilingual bodies retain their drafting-layer `translation_status: source-checked` and pending alignment front-matter convention. Their separate bilingual-alignment closure is recorded durably by the detailed reports and machine-readable sidecars. Do not mistake that implementation detail for a missing QA gate.

Current English QA totals:

- Source-checked: **55 / 55 — 3537–3591 / PDF 024–401**
- Bilingual-aligned: **55 / 55 — 3537–3591 / PDF 024–401**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

### Exact next activity — volume-level English editorial consistency review

Perform the separate **Volume 45 English editorial consistency review across all 55 bilingual records**.

Review the volume as one English work for:

- English title / YAML / index agreement;
- translator-note wording and any stale drafting-status language;
- names, honorifics, places and transliteration;
- institutional, legal and political terminology;
- British/Indian English spelling and compounds where applicable;
- punctuation and quotation consistency;
- dates and PDF/printed-page ranges;
- glossary decisions and avoidable variants;
- source-anomaly and source-specific labels;
- stale `pending` / drafting fields in control layers;
- preservation and completeness of every `Original Tamil — மூலத் தமிழ்` appendix.

The editorial review may correct demonstrated English consistency defects but must **not** alter political meaning, attribution, uncertainty, figures, quotations, rhetorical force, source-specific anomalies or canonical Tamil. If a possible Tamil transcription defect appears, re-check the controlling scan directly before changing either layer.

Create/update `volumes/volume-45/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md` (or the established repository-equivalent durable editorial report), update all controls, and only after this gate passes make the translation manifest / final release report the next activity. Do **not** combine the editorial review and release packaging into one routine step.

## 3. QA separation

Keep stages distinct:

1. Tamil batch/iteration audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. targeted scan correction if English QA exposes a residual Tamil discrepancy;
5. English drafting/source check — **COMPLETE**;
6. bilingual alignment — **COMPLETE; 55 / 55 aligned**;
7. volume-level English editorial consistency review — **NEXT**;
8. release manifest/report.

## 4. Git/concurrency discipline

- Work on `main` as requested.
- Never force-push routine work.
- Recheck live `main` immediately before mutation.
- Preserve unrelated concurrent changes.
- Keep declared batch/gate scope explicit.
- Prefer atomic commits where technically possible.
- If connector limitations cause an incremental publication sequence, do not rewrite history merely to make it atomic; make the durable boundary internally consistent before stopping.
- Remove temporary artifacts from repository trees.
- Verify live `main` after completed work.

## 5. Meaning of “Proceed with next activity”

Inspect live durable state, identify the next already-defined batch/gate, execute it directly, and report completed scope, QA result, live commit SHA/state, counts and exact next activity. Do not ask the user to choose among routine next steps.
