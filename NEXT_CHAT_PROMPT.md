# Next Chat Prompt — Volume 45 Bilingual Alignment Batch 3562–3566

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
   - all bilingual alignment reports through `BILINGUAL_ALIGNMENT_REVIEW_3557_3561.md`
5. Confirm live main-drafting closure: **55 / 55 source-checked, PDF 024–401**.
6. Confirm cumulative alignment closure: **3537–3561 / PDF 024–196 — 25 / 55 aligned**.

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
- Bilingual-aligned: **25 / 55 — 3537–3561 / PDF 024–196**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

Alignment batch results:

- **3537–3541 / PDF 024–060** — PASS — 5 / 5; English corrections 0; Tamil changes 0.
- **3542–3546 / PDF 061–103** — PASS — 5 / 5; English corrections 1; Tamil changes 0.
- **3547–3551 / PDF 104–141** — PASS — 5 / 5; English corrections 0; Tamil changes 0.
- **3552–3556 / PDF 142–163** — PASS — 5 / 5; English corrections 1; Tamil changes 0.
- **3557–3561 / PDF 164–196** — PASS — 5 / 5; English corrections 2; Tamil changes 0.

Fifth-batch English-only corrections:

1. **Letter 3560:** the Pranab Mukherjee overdraft sentence now states that the Tamil Nadu government had not **had to obtain** an overdraft even for a day because of having no money in its account; the previous wording inverted the causal sense.
2. **Letter 3561:** unsupported `ancient` was removed from `மண்ணுலகின் முதன்மை மொழி`; the aligned English is **“the world's foremost language.”**

Established source forms remain preserved: PDF 170 `பொக்கம்`, PDF 176 `10ந்தேதியன்று`, PDF 177 `முஜா கி தீன்`, and the scan-proven PDF 187 restoration.

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

## EXACT NEXT ALIGNMENT BATCH

Align five complete consecutive letters:

- **3562** — `“சில நேரங்களில் சில மனிதர்கள்!”` — PDF **197–200** — 13-5-2011
- **3563** — `இறுதிப் போரில் நாம் வெல்வது திண்ணம்!` — PDF **201–208** — 22-5-2011
- **3564** — `“ஈயத்தைப் பார்த்து இளித்ததாம் பித்தளை!”` — PDF **209–217** — 3-6-2011
- **3565** — `இன்று நடப்பது; அன்றே நடந்ததுதான்!` — PDF **218–222** — 11-6-2011
- **3566** — `அதுவே ஓர் ஆறுதல்தான்!` — PDF **223–230** — 13-6-2011

Combined next alignment range: **PDF 197–230 / 34 canonical pages**.

**Source caution:** PDF 217 contains the scan-preserved anomaly `011ஆம் ஆண்டு`. Do not silently normalise it to an expected year form.

Create a durable alignment report for **3562–3566**, record any English corrections and any scan-triggered Tamil corrections separately, update the cumulative bilingual-aligned count, and set the exact following alignment batch from live chapter boundaries.

Immediately before Git mutation, re-fetch live `main`; preserve unrelated concurrent changes; prefer one atomic Git-data commit; compare parent→new commit; fast-forward `main` with `force:false`; then verify live `main`.

When I say **“Proceed with next activity”**, execute this bilingual-alignment batch directly without asking me to choose a routine next step.
