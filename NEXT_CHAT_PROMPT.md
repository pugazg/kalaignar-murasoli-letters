# Next Chat Prompt — Volume 45 English Editorial Consistency Review

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Active work: **Volume 45 volume-level English editorial consistency review**.

Use the GitHub connector and work directly on `main`.

## MANDATORY STARTUP

Before making any repository change:

1. Fetch live `main` and treat it as authoritative over every SHA/count in this prompt.
2. Read completely:
   - `VOLUME_PROCESSING_GUIDE.md`
   - `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
   - `TRANSCRIPTION_GUIDE.md`
   - `FUTURE_VOLUME_WORK_GUIDELINES.md`
   - `PROJECT_HANDOVER.md`
   - this `NEXT_CHAT_PROMPT.md`
3. Read the active Volume 45 controls completely:
   - `volumes/volume-45/README.md`
   - `volumes/volume-45/PROGRESS.md`
   - `volumes/volume-45/AUDIT.md`
   - `volumes/volume-45/metadata.yml`
   - `volumes/volume-45/FULL_VOLUME_STRUCTURAL_AUDIT.md`
   - `volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`
4. Read the English controls completely:
   - `volumes/volume-45/TRANSLATION_PLAN.md`
   - `volumes/volume-45/TRANSLATION_PILOT_CHECKPOINT.md`
   - `volumes/volume-45/translations/en/README.md`
   - `volumes/volume-45/translations/en/PROGRESS.md`
   - `volumes/volume-45/translations/en/GLOSSARY.md`
   - `volumes/volume-45/translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md`
   - every completed `BILINGUAL_ALIGNMENT_REVIEW_*.md`, including `BILINGUAL_ALIGNMENT_REVIEW_3587_3591.md`
   - `volumes/volume-45/translations/en/alignment-status/README.md`
   - `volumes/volume-45/translations/en/alignment-status/3587-3591.yml`
5. Read Volume 46's completed editorial reference completely before designing or recording the Volume 45 editorial pass:
   - `volumes/volume-46/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
   Use it as a workflow/quality reference only; do not copy Volume 46-specific facts into Volume 45.
6. Confirm live main-drafting closure: **55 / 55 source-checked, PDF 024–401**.
7. Confirm cumulative bilingual-alignment closure: **55 / 55 — 3537–3591 / PDF 024–401**.

## CURRENT DURABLE VOLUME 45 STATE

Tamil archival layer:

- Source PDF pages: **402**
- Canonical Tamil: **001–402 / 402 complete**
- Source letters: **55 / 55 — 3537–3591 complete**
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — 402 / 402**
- Historical second-pass corrections: **243 canonical page files / 623 correction spans**
- Translation-discovered targeted correction: **PDF 187 / 1 additional scan-proven span**
- Combined canonical correction tally: **243 unique page files / 624 spans**

English layer:

- Main drafting: **COMPLETE**
- Draft-translated: **55 / 55 — 3537–3591**
- Source-checked: **55 / 55 — 3537–3591**
- Cumulative translated source: **PDF 024–401**
- Bilingual-aligned: **55 / 55 — 3537–3591 / PDF 024–401 — COMPLETE**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

Final alignment batch:

- **3587–3591 / PDF 370–401** — **PASS — 5 / 5**; English corrections **1**; Tamil changes **0**; new scan re-checks **0**.
- **3587:** 311-acre Thirumazhisai / Rule 110 / policy-note / 2006 satellite-town sequence aligns; successive source `1-9-2006` / `31-8-2006` formulations remain preserved.
- **3588:** Samacheer Kalvi, school-day, examination, teacher-ratio, recruitment and counselling sequences align without correction.
- **3589:** one English-only correction removed the unprinted hedge “in the source's argument” and restored direct `நாசமாக்கி அழித்திடும்` as **“will destroy”** in the engineering-university paragraph. Canonical Tamil is unchanged.
- **3590:** local-election and campaign sequence aligns without correction.
- **3591:** K.P.P. Samy / M.K. Balan / High Court / Valluvar sequence aligns without correction.
- Detailed report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3587_3591.md`.
- Machine-readable status: `volumes/volume-45/translations/en/alignment-status/3587-3591.yml`.

Implementation note: the bilingual bodies retain their drafting-layer `translation_status: source-checked` and pending alignment front-matter convention. The separate bilingual-alignment closure is recorded by the detailed reports and machine-readable sidecars. Do not treat that implementation detail as an unperformed alignment gate, and do not rewrite all large bilingual bodies merely to duplicate the already-durable alignment status.

## SOURCE AUTHORITY

The audited canonical Tamil remains the immediate English-QA authority. The controlling scan remains ultimate textual authority.

Do not use outside knowledge, another edition, expected modern wording or historical reconstruction to alter source facts. Preserve source-specific anomalies, dates, figures, repetitions, quotations, source-supplied English/Latin material and physical source boundaries.

If editorial review reveals a possible Tamil discrepancy, re-check the controlling scan before changing either layer and record every scan-proven post-audit correction durably.

## EXACT NEXT ACTIVITY — VOLUME-LEVEL ENGLISH EDITORIAL CONSISTENCY REVIEW

Review **all 55 bilingual records, Letters 3537–3591**, as one English volume. This is a consistency/editorial QA gate after source-check and bilingual alignment; it is not a new translation pass and must not become free stylistic rewriting.

Check systematically:

1. English title consistency between YAML, H1, English README/index and source record.
2. Date, source PDF range and printed-page metadata agreement.
3. Standard translator's note wording and removal/correction of any stale drafting-status language in control layers.
4. Names, initials, honorifics, place names and transliteration consistency.
5. Institutional, administrative, constitutional, legal, political and scheme terminology.
6. Locked conventions including `Udanpirappē`, `With affection, M.K.`, `lakh`, `crore`, **Samacheer Kalvi** and established glossary decisions.
7. British/Indian English spelling, compounds, capitalisation and punctuation where consistency can be improved without changing source meaning.
8. Quotation marks, quoted voices, source-supplied English and attribution.
9. Repetition, rhetorical questions, irony, accusation and political intensity — these must not be softened or rewritten away.
10. Stale `pending`, draft or pre-alignment wording in volume/control metadata; distinguish implementation-level letter front matter from actual QA closure before changing large files.
11. Every bilingual record must retain a complete `Original Tamil — மூலத் தமிழ்` appendix in canonical physical-page order.
12. Source anomalies and source-specific claims must remain explicit and unreconciled with outside knowledge.

Correct only demonstrated editorial-consistency defects. Do not revise passages merely because another English wording sounds smoother. Do not change canonical Tamil unless a fresh direct scan check proves a Tamil defect.

Create `volumes/volume-45/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md` with the complete review scope, checks performed, exact English/control corrections, Tamil/scan events if any, and PASS/FAIL result. Update `README.md`, `PROGRESS.md`, metadata, volume controls, project handover and next-chat prompt consistently.

If the editorial consistency review passes across all **55 / 55** records, set **translation manifest and final English release report** as the exact next activity. Do **not** execute release packaging in the same routine activity.

Immediately before Git mutation, re-fetch live `main`; preserve unrelated concurrent changes. Prefer one atomic Git-data commit where technically possible. If connector limitations force an incremental sequence, preserve history, synchronize every durable control before stopping, compare the prior durable boundary to final live `main`, and verify live `main` afterward. Never force-push routine work.

When I say **“Proceed with next activity”**, execute this complete Volume 45 editorial consistency review directly without asking me to choose a routine next step.
