# NEXT CHAT PROMPT — Volume 42 / FINAL English Release Verification — 64 / 64

Continue directly in `pugazg/kalaignar-murasoli-letters`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable Tamil closure

- Controlling source: `TVA_BOK_0065826_கலைஞரின்_கடிதங்கள்_தொகுதி_42.pdf`
- Source SHA-256: `43f9b51fd3765144f707cce535cc9ed39892f911a126c3c3c005173a1efc1676`
- Source extent: **402 physical PDF pages / 400 printed pages**
- Canonical Tamil: **PDF 001–402 / 402 COMPLETE**
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS / COMPLETE / CLOSED**
- Unresolved Tamil fidelity items: **0**
- Actual source records: **64 — 3364–3376, 3154, 3378–3427**
- Letter **3427** closes at PDF **401 / printed 400**
- PDF **402** is non-letter back-cover / portrait / publisher-contact-price material; **no Letter 3428**

## English QA closure before release gate

- translation/source-check: **COMPLETE — 64 / 64**
- complete audited Tamil appendix: **64 / 64**
- bilingual alignment: **COMPLETE — 64 / 64**
- cumulative bilingual-alignment English corrections: **39**
- canonical Tamil changes during source-check/alignment: **0**
- English editorial consistency review: **PASS — 64 / 64**
- editorial English-only corrections: **2**
  - **3397:** `State Government` → **State government**
  - **3422:** `Union government` → **Union Government**
- editorial canonical Tamil changes: **0**
- new scan re-checks during editorial review: **0**
- unresolved English QA items: **0**
- editorial report: `volumes/volume-42/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`

## Protected source facts and anomalies to preserve

- Source number **3154** is genuine between 3376 and 3378; **do not invent 3377**.
- Letter **3392** genuinely duplicates its physical printing across PDF 209–212; the Tamil appendix preserves both copies.
- Letter **3389** retains the 2009 republication framing and **Source closing date: 01 April 2009**; do not invent an older external date.
- Letter **3401** uses source-specific **Kazhagam Udanpirappē**.
- Letter **3419** preserves scan-printed PDF 357 form `புறங்காந்திமடைந்து`.
- Letter **3425** actual PDF 386 title uses joined `திருந்தப்போகிறார்களா?`; the contents layer separately preserves `திருந்தப் போகிறார்களா?`.
- Letter **3427** ends at PDF 401; PDF 402 is non-letter matter.
- Preserve source-supplied English verbatim, including protected material in 3387, 3405, 3408, 3420, 3425 and 3426. In particular retain **Katcha Theevu**, **Samerian**, **SriLankan**, and **Quota and Rota** where they are printed source English.

## Exact next activity — FINAL English release verification

Perform the final release gate only. Do not reopen completed source-check, alignment or editorial work unless verification exposes a concrete inconsistency.

### 1. Create the translation manifest

Create:

`volumes/volume-42/translations/en/TRANSLATION_MANIFEST.csv`

Use the current-format columns:

`letter_number,occurrence,date,english_title,source_pdf_pages,translation_status,bilingual_alignment_status,editorial_review_status,final_release_status,source_incomplete,file`

Required identity:

- exactly **64 rows**;
- actual source records **3364–3376, 3154, 3378–3427**;
- **3154 occurrence = 1** and no 3377 row;
- unique English path for every row;
- `translation_status=source-checked` for all 64;
- `bilingual_alignment_status=aligned` for all 64;
- `editorial_review_status=reviewed` for all 64;
- `source_incomplete=false` for all 64;
- promote `final_release_status=verified` only after every release check passes.

### 2. Validate all bilingual files

For all 64 manifest rows verify:

- file exists and front-matter letter number/date/English title/PDF range agrees with manifest;
- `translation_status: source-checked` and `bilingual_alignment_status: aligned` remain intact;
- textual-fidelity-audit pointer remains valid;
- exactly one translator note and one complete `## Original Tamil — மூலத் தமிழ்` appendix;
- expected physical PDF page markers are present for the complete record range;
- ordinary letters retain the established salutation/closing conventions, while documented exceptions remain exceptions;
- the two editorial corrections in 3397 and 3422 remain present;
- protected source-supplied English remains unchanged.

### 3. Reconcile source coverage and anomalies

- manifest PDF ranges must cover the translated source-letter corpus **PDF 024–401** in source order, respecting the genuine 3392 duplicate printing inside its single record;
- verify **64 unique source records** and **64 unique English paths**;
- verify no missing or extra English record;
- verify source-incomplete rows: **0**;
- reconfirm Letter 3427 closes at PDF 401 and PDF 402 is non-letter matter;
- no Letter 3428 in Volume 42.

### 4. Create final release report

Create:

`volumes/volume-42/translations/en/RELEASE_REPORT.md`

Record Tamil archival QA, all English QA gates, manifest reconciliation, bilingual-file/Tamil-appendix validation, retained editorial corrections, protected source English/anomalies, final source boundary, and final release result.

### 5. Synchronize controls only after PASS

After all validation passes, mark Volume 42 English **FINAL RELEASE COMPLETE — 64 / 64** in:

- `volumes/volume-42/translations/en/PROGRESS.md`
- `volumes/volume-42/translations/en/README.md`
- `volumes/volume-42/TRANSLATION_PLAN.md`
- `volumes/volume-42/PROGRESS.md`
- `volumes/volume-42/README.md`
- `volumes/volume-42/AUDIT.md`
- `volumes/volume-42/metadata.yml`
- root `README.md`
- `PROJECT_HANDOVER.md`
- `NEXT_CHAT_PROMPT.md`

Do not describe the release as complete if manifest reconciliation or any bilingual-file validation fails.

Suggested commit message:

`Finalize Volume 42 English release`