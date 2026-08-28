# Next Chat Prompt — Volume 45 English Translation Batch 3550–3554

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Active work: **Volume 45 English translation drafting**.

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
   - `volumes/volume-45/translations/en/PILOT_REVIEW_3537_3539.md`
   - `volumes/volume-45/translations/en/DRAFT_SOURCE_CHECK_3540_3544.md`
   - `volumes/volume-45/translations/en/DRAFT_SOURCE_CHECK_3545_3549.md`
5. Inspect completed bilingual records 3537–3549, especially the immediately preceding 3545–3549 batch, before drafting the next batch.
6. Confirm the live durable boundary before doing work.

## CURRENT DURABLE VOLUME 45 STATE

Tamil archival layer:

- Source PDF pages: **402**
- Canonical Tamil: **001–402 / 402 complete**
- Source letters: **55 / 55, 3537–3591 complete**
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — 402 / 402**
- Second-pass corrections: **243 canonical page files / 623 correction spans**

English layer:

- Pilot: **3537–3539 / PDF 024–049 — PASS / STYLE LOCKED**
- First normal drafting batch: **3540–3544 / PDF 050–088 — PASS / source-checked**
- Second normal drafting batch: **3545–3549 / PDF 089–122 — PASS / source-checked**
- Draft-translated: **13 / 55 — 3537–3549**
- Source-checked: **13 / 55 — 3537–3549**
- Bilingual-aligned: **0 / 55**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**
- Tamil canonical changes during 3545–3549: **0**
- Exact next letter: **3550**
- Exact next drafting batch: **3550–3554**

## NEXT BATCH SOURCE BOUNDARIES

- **3550 — தேவர் திருமகனின் பொன்மொழி என்ன?** — PDF **123–128**, printed **122–127**, date **23-03-2011**
- **3551 — நாடு வாழ நாம் புரிந்த சாதனைகள்!** — PDF **129–141**, printed **128–140**, date **28-03-2011**
- **3552 — யாரா உஷார்! பதுங்கி வருகிறது பணநாயகம்!** — PDF **142–144**, printed **141–143**, date **30-03-2011**
- **3553 — “குற்றம் பார்க்கின் சுற்றம் இல்லை”!** — PDF **145–149**, printed **144–148**, date **5-4-2011**
- **3554 — மதிப்பிற்குரிய மதிப்பெண் என்ன?** — PDF **150–154**, printed **149–153**, date **13-4-2011**

Combined next-batch source range: **PDF 123–154**.

## SOURCE / TRANSLATION AUTHORITY

The audited canonical Tamil is the immediate translation source. The controlling scan remains ultimate textual authority.

Do not use outside knowledge, another edition, expected modern wording or historical reconstruction to alter source facts. Preserve source-specific anomalies, dates, figures, repetitions, quoted material, English/Latin material and source boundaries.

If translation reveals a possible Tamil discrepancy, stop on that point and re-check the controlling scan before changing either layer.

The completed 3545–3549 batch deliberately preserved source-specific material including PDF 089's unfinished scanning phrase, PDF 098 `112.2006-ல்`, the Letter 3546 title dash and “hero/heroine” wordplay, Letter 3547's exact water/employment figures, Letter 3548's historical Welfare Board name / PDF 114 amount / PDF 116 dates, and Letter 3549's complete metaphor-and-verse sequence. Treat this as the model: do not silently “fix” unusual source text during English drafting.

## LOCKED TRANSLATION STYLE

Use the Volume 45 plan exactly:

- clear contemporary, thought-preserving, non-literary English;
- do not summarize substantive content;
- preserve argument order, political force, irony, repetition and rhetorical questions;
- preserve names, dates, figures, units, quotations and attribution;
- retain `Udanpirappē`;
- close with `With affection, M.K.` where the source closes that way;
- retain `lakh` and `crore`;
- use the locked standard translator’s note verbatim;
- use glossary treatments where the same source terms recur;
- add minimal explanatory notes only where genuinely necessary;
- reproduce **complete audited Tamil** under `Original Tamil — மூலத் தமிழ்` in every bilingual record.

Completed files are `source-checked`, not final bilingual-alignment `verified` records. Keep alignment as a later distinct QA stage.

## EXACT NEXT ACTIVITY

Complete **Letters 3550–3554 in one five-complete-letter drafting iteration**.

For each letter:

1. read its complete chapter record and exact canonical PDF range;
2. read every canonical Tamil page in that range completely;
3. translate every substantive heading, paragraph, list, quotation, figure and rhetorical question;
4. create one bilingual Markdown record under `volumes/volume-45/translations/en/letters/` using the locked structure;
5. append the complete audited Tamil in physical page order under `Original Tamil — மூலத் தமிழ்`;
6. source-check English against the full audited canonical Tamil before marking `source-checked`;
7. update glossary only for new recurring terms;
8. create a `DRAFT_SOURCE_CHECK_3550_3554.md` batch QA record;
9. update translation progress, Volume 45 progress/metadata/README, root README, project handover and this next-chat prompt;
10. recheck live `main` before the final mutation;
11. make the declared five-letter batch/control update atomic where technically possible;
12. compare the intended parent→new commit, fast-forward without force and verify live `main` afterward.

## IMPORTANT

Do not re-run completed batches unless a specific source-backed correction is needed. Do not begin the later full bilingual-alignment gate during this drafting batch.

When I say **“Proceed with next activity”**, execute the next already-defined batch directly without asking me to choose a routine next step.
