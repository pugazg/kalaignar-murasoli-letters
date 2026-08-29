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

### English main drafting — COMPLETE

Locked conventions include `Udanpirappē`, `With affection, M.K.`, clear contemporary thought-preserving non-literary English, no summarising substantive source material, preservation of political force/irony/questions/repetition/quotations/names/dates/figures, `lakh` / `crore`, established **Samacheer Kalvi**, source-specific Tamil New Year / Thai / Chithirai claims without outside reconciliation, and complete audited Tamil under `Original Tamil — மூலத் தமிழ்` in every bilingual record.

Current drafting state:

- Draft-translated: **55 / 55 — 3537–3591**
- Source-checked: **55 / 55 — 3537–3591**
- Cumulative translated canonical source: **PDF 024–401**

### Bilingual alignment — IN PROGRESS

Nine batches are complete. Latest:

- **3577–3581 / PDF 290–337 / 48 pages** — **PASS — 5 / 5 aligned; English corrections 0; Tamil changes 0.**
- Detailed report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3577_3581.md`.
- Machine-readable batch status: `volumes/volume-45/translations/en/alignment-status/3577-3581.yml`.

Ninth-batch source-specific results:

- **3577:** exhaustive law-and-order catalogue aligns; PDF 290 `18-5-2001` is preserved exactly; the source's own opening “three months” and closing “two months” formulations remain distinct.
- **3578:** Jaffer Sait / Housing Board discretionary-quota history, allottee lists, measurements, joint venture, same-plot family sequence, suspension/Mandapam order and fasting-period argument align without correction.
- **3579:** all debt, borrowing, revenue, welfare, housing and power figures align; the two source-supplied *The Hindu* English passages remain verbatim.
- **3580:** false-case examples, judicial observations, land-grab argument, George IPS source English/Tamil layers and seven listed policing consequences align without correction.
- **3581:** complete `செம்மொழி வாழ்த்து`, Thanjavur conference contrast and detailed textbook-removal catalogue align without correction; Thai/Tamil-New-Year wording remains source-specific.

No Tamil canonical file changed during the ninth batch.

The large bilingual bodies for 3577–3581 retain their `translation_status: source-checked` drafting metadata. Their separate bilingual-alignment closure is recorded durably by the detailed report and machine-readable sidecar. Do not mistake that implementation detail for a missing QA gate.

Current English QA totals:

- Source-checked: **55 / 55**
- Bilingual-aligned: **45 / 55 — 3537–3581 / PDF 024–337**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

### Exact next activity — bilingual-alignment batch 3582–3586

Align five complete consecutive letters:

- **3582** — `இனிய விழா; நமது இனத்தின் விழா!` — PDF **338–344** — 25-8-2011
- **3583** — `அதிகாரம் இல்லை? அந்தநாள் ஞாபகம் இல்லையா?` — PDF **345–351** — 1-9-2011
- **3584** — `அடிநாதமே; அறுக்கப்படுவதா?` — PDF **352–357** — 8-9-2011
- **3585** — `அய்யோ பாவம்! அ.தி.மு.க. அமைச்சர்கள்!!` — PDF **358–364** — 10-9-2011
- **3586** — `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!` — PDF **365–369** — 12-9-2011

Combined next range: **PDF 338–369 / 32 canonical pages**.

Source cautions:

- Preserve Letter 3582's source-specific Thai / Chithirai / Tamil-New-Year claims without outside reconciliation.
- Preserve source-supplied English exactly wherever printed.
- Letter 3586 is scan-proven as beginning `கழக அரசு`; stale `தமிழக அரசு...` remains withdrawn.

For every letter: read the complete authoritative audited Tamil and complete English record; compare title, salutation, paragraph order, substantive claims, lists, quotations, names, dates, figures, units, rhetoric, repetition and closing; correct only demonstrated English omission/addition/semantic drift; if any new Tamil defect is suspected, re-check the controlling scan before changing either layer; create a durable batch report and machine-readable alignment status; update all controls.

Do **not** merge the later volume-level English editorial consistency review into bilingual alignment.

## 3. QA separation

Keep stages distinct:

1. Tamil batch/iteration audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. targeted scan correction if translation/alignment exposes a residual Tamil discrepancy;
5. English drafting/source check — **COMPLETE**;
6. bilingual alignment — **IN PROGRESS; 45 / 55 aligned; next 3582–3586 / PDF 338–369**;
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
