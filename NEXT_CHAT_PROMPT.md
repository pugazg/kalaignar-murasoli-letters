# Next Chat Prompt — Volume 45 Bilingual Alignment Batch 3537–3541

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Active work: **Volume 45 English bilingual-alignment QA**.

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
3. Read the active Volume 45 controls:
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
   - `volumes/volume-45/translations/en/DRAFT_SOURCE_CHECK_3590_3591.md`
5. Confirm live main-drafting closure: **55 / 55 source-checked, PDF 024–401**.

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
- Bilingual-aligned: **0 / 55**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

## SOURCE AUTHORITY

The audited canonical Tamil is the immediate alignment authority. The controlling scan remains ultimate textual authority.

Do not use outside knowledge, another edition, expected modern wording or historical reconstruction to alter source facts. Preserve source-specific anomalies, dates, figures, repetitions, quoted material, English/Latin material and physical source boundaries.

If alignment reveals a possible Tamil discrepancy, re-check the controlling scan before changing either layer and record every scan-proven post-audit correction durably.

## ALIGNMENT RULES

For each bilingual record:

1. read the complete audited Tamil source pages and the complete English record;
2. compare title, salutation, paragraph order, every substantive claim, list item, quotation, name, date, figure, unit, rhetorical question, repetition and closing;
3. correct English omissions, additions, mistranslations or semantic drift;
4. preserve source anomalies rather than silently normalising them;
5. preserve the locked `Udanpirappē`, `With affection, M.K.`, `lakh` / `crore`, Samacheer Kalvi and other glossary conventions unless the source requires otherwise;
6. do not perform stylistic rewriting merely because another English phrasing sounds smoother;
7. do not begin the separate volume-level English editorial consistency review;
8. after a letter passes direct Tamil↔English comparison, change its `bilingual_alignment_status` from `pending` to `aligned` while retaining its drafting/source-check history;
9. record the alignment batch in a durable QA report and update progress/metadata/handover controls.

## EXACT FIRST ALIGNMENT BATCH

Align five complete consecutive letters:

- **3537** — PDF **024–033**
- **3538** — PDF **034–041**
- **3539** — PDF **042–049**
- **3540** — PDF **050–056**
- **3541** — PDF **057–060**

Combined first alignment range: **PDF 024–060 / 37 canonical pages**.

Create a durable alignment report for **3537–3541**, record any English corrections and any scan-triggered Tamil corrections separately, update the cumulative bilingual-aligned count, and set the exact next alignment batch from live chapter boundaries.

Immediately before Git mutation, re-fetch live `main`; preserve unrelated concurrent changes; prefer one atomic Git-data commit; compare parent→new commit; fast-forward `main` with `force:false`; then verify live `main`.

When I say **“Proceed with next activity”**, execute this first bilingual-alignment batch directly without asking me to choose a routine next step.
