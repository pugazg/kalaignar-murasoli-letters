# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-29

Read this together with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`. If documents conflict, the controlling processing/batching/transcription guides take precedence.

## 1. Source authority

**The controlling source scan controls Tamil readings.** OCR, contents pages, another edition, outside historical knowledge, translations and inferred chronology may assist navigation but may not silently override the source. Historical wording, source errors, numbering anomalies, punctuation, quoted material, English text and physical boundaries are preserved and documented.

For English work, the audited canonical Tamil is the immediate QA source. Any English QA check that exposes a possible Tamil discrepancy must trigger targeted direct scan re-verification before either Tamil or English is changed.

## 2. Current active work — Volume 45 final English release packaging

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

During Letter 3560 source-check, direct scan comparison restored an omitted physical-page tail on PDF 187. During Letter 3583 alignment, direct scan re-check confirmed PDF 348→349 as `வாக்க` / `எதிரிகளை`; canonical Tamil remained unchanged and English was corrected conservatively to “enemies.”

### English drafting — COMPLETE

- Draft-translated: **55 / 55 — 3537–3591**
- Source-checked: **55 / 55 — 3537–3591**
- Cumulative translated canonical source: **PDF 024–401**

Locked conventions include `Udanpirappē`, `With affection, M.K.`, `lakh` / `crore`, **Samacheer Kalvi**, thought-preserving non-literary English, preservation of political force/irony/questions/repetition/quotations/names/dates/figures and complete audited Tamil under `Original Tamil — மூலத் தமிழ்`.

### Bilingual alignment — COMPLETE

All eleven batches passed. Final batch:

- **3587–3591 / PDF 370–401** — **PASS — 5 / 5 aligned; English corrections 1; Tamil changes 0; new scan re-checks 0.**
- Detailed report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3587_3591.md`.
- Machine-readable batch status: `volumes/volume-45/translations/en/alignment-status/3587-3591.yml`.

Cumulative bilingual alignment: **55 / 55 — 3537–3591 / PDF 024–401**.

### Volume-level English editorial consistency — COMPLETE

Durable report: `volumes/volume-45/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`.

Result: **PASS — 55 / 55 editorially reviewed**.

The review treated all 55 bilingual records as one English corpus and checked title/front-matter/index agreement, dates/page ranges, translator-note wording, names/honorifics, places/transliteration, institutional/legal/political terminology, glossary decisions, `lakh` / `crore`, spelling/compounds, punctuation/quotation treatment, source-supplied English, source-anomaly handling, stale control-layer wording and the durable record of complete appended Tamil.

Editorial pass results:

- Bilingual letter-body corrections: **0**
- Tamil canonical changes: **0**
- New scan re-checks: **0**
- Editorially reviewed: **55 / 55**
- Final verified English: **0 / 55**

The bilingual bodies intentionally retain their drafting-layer `translation_status: source-checked`; later sidecar-tracked records may retain implementation-level pending alignment front matter. The detailed reports/sidecars are the durable alignment authority, so the editorial pass did not bulk-rewrite large bilingual files simply to duplicate QA state.

### Exact next activity — translation manifest and final English release report

Prepare and validate the Volume 45 English release package:

1. create the machine-readable translation manifest with exactly **55 source-letter records, 3537–3591**;
2. verify one unique record per letter number and one valid English file path per record;
3. reconcile title, date, source PDF range and release status against the English index and durable QA records;
4. ensure every record is source-checked, bilingual-aligned and editorially reviewed before final verification;
5. create the final English release report;
6. promote final verified count only after manifest/report validation succeeds;
7. update volume metadata, README/progress/audit, English README/progress, root README, handover and next-chat prompt consistently.

Do **not** describe Volume 45 English as final-release complete until the manifest count reconciles to 55 and final release verification passes.

## 3. QA separation

Keep stages distinct:

1. Tamil batch/iteration audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. targeted scan correction if English QA exposes a residual Tamil discrepancy;
5. English drafting/source check — **COMPLETE**;
6. bilingual alignment — **COMPLETE; 55 / 55 aligned**;
7. volume-level English editorial consistency review — **COMPLETE; 55 / 55 reviewed**;
8. release manifest/report — **NEXT**.

## 4. Git/concurrency discipline

- Work on `main` as requested.
- Never force-push routine work.
- Recheck live `main` immediately before mutation.
- Preserve unrelated concurrent changes.
- Keep declared batch/gate scope explicit.
- Prefer one atomic Git-data commit where technically possible.
- Remove temporary branches/artifacts after integration.
- Verify live `main` after completed work.

## 5. Meaning of “Proceed with next activity”

Inspect live durable state, identify the next already-defined gate, execute it directly, and report completed scope, QA result, live commit SHA/state, counts and exact next activity. Do not ask the user to choose among routine next steps.
