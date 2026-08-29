# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-29

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

### Bilingual alignment — IN PROGRESS

Ten batches are complete. Latest:

- **3582–3586 / PDF 338–369 / 32 pages** — **PASS — 5 / 5 aligned; English corrections 1; Tamil changes 0.**
- Detailed report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3582_3586.md`.
- Machine-readable batch status: `volumes/volume-45/translations/en/alignment-status/3582-3586.yml`.

Tenth-batch source-specific results:

- **3582:** Thai / Chithirai / Tamil-New-Year claims, quoted scholarly statements, bill chronology and closing position align without outside reconciliation.
- **3583:** Article 161, mercy-petition chronology, source-supplied English and Thiagu/Kaliyaperumal material align after one English-only correction; direct scan confirmed `வாக்க` / `எதிரிகளை` across PDF 348→349.
- **3584:** democracy, Omandurar, Samacheer Kalvi, tax, agricultural-welfare and Tamil-New-Year-law sequences align without correction.
- **3585:** Rule 110, policy-note copying and complete sports-development catalogue align without correction.
- **3586:** the scan-proven `கழக அரசு...` title, Rajiv Gandhi / *Nenjukku Neethi* material, Eelam narrative and death-sentence commutation argument align without correction.

No Tamil canonical file changed during the tenth alignment batch.

The large bilingual bodies retain their `translation_status: source-checked` drafting metadata. Their separate bilingual-alignment closure is recorded durably by the detailed report and machine-readable sidecar. Do not mistake that implementation detail for a missing QA gate.

Current English QA totals:

- Source-checked: **55 / 55**
- Bilingual-aligned: **50 / 55 — 3537–3586 / PDF 024–369**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

### Exact next activity — final bilingual-alignment batch 3587–3591

Align five complete consecutive letters:

- **3587** — `மாமியார் உடைத்ததும்; மருமகள் உடைத்ததும்!` — PDF **370–376** — 13-9-2011
- **3588** — `கல்வி; கருகிடும் மொட்டாவதா?` — PDF **377–382** — 14-9-2011
- **3589** — `எத்தனை காலமோ; இந்த ஏட்டிக்குப் போட்டி?` — PDF **383–390** — 19-9-2011
- **3590** — `விரைந்தெழுவீர்; வெற்றிக்கனி பறித்திட!` — PDF **391–396** — 24-9-2011
- **3591** — `அடங்காமை ஆறிருள் உய்த்து விடும்!` — PDF **397–401** — 27-9-2011

Combined final alignment range: **PDF 370–401 / 32 canonical pages**.

For every letter: read the complete authoritative audited Tamil and complete English record; compare title, salutation, paragraph order, substantive claims, lists, quotations, names, dates, figures, units, rhetoric, repetition and closing; correct only demonstrated English omission/addition/semantic drift; if any new Tamil defect is suspected, re-check the controlling scan before changing either layer; create a durable batch report and machine-readable alignment status; update all controls.

Do **not** begin the volume-level English editorial consistency review inside the final alignment iteration. After the final five letters pass and the **55 / 55 bilingual-aligned** boundary is durably recorded, editorial consistency becomes the next gate.

## 3. QA separation

Keep stages distinct:

1. Tamil batch/iteration audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. targeted scan correction if translation/alignment exposes a residual Tamil discrepancy;
5. English drafting/source check — **COMPLETE**;
6. bilingual alignment — **IN PROGRESS; 50 / 55 aligned; final batch 3587–3591 / PDF 370–401 next**;
7. volume-level English editorial consistency review;
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
