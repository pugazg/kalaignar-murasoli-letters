# Next Chat Prompt — Volume 45 Bilingual Alignment Batch 3582–3586

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
   - every completed `BILINGUAL_ALIGNMENT_REVIEW_*.md` through `BILINGUAL_ALIGNMENT_REVIEW_3577_3581.md`
   - `volumes/volume-45/translations/en/alignment-status/README.md`
   - `volumes/volume-45/translations/en/alignment-status/3577-3581.yml`
5. Confirm live main-drafting closure: **55 / 55 source-checked, PDF 024–401**.
6. Confirm cumulative alignment closure: **3537–3581 / PDF 024–337 — 45 / 55 aligned**.

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
- Bilingual-aligned: **45 / 55 — 3537–3581 / PDF 024–337**
- Editorially reviewed: **0 / 55**
- Final verified English: **0 / 55**

Latest alignment batch:

- **3577–3581 / PDF 290–337** — **PASS — 5 / 5**; English corrections **0**; Tamil changes **0**.
- PDF 290 `18-5-2001` remains preserved exactly.
- Letter 3577's source itself uses the opening “three months” framing and the closing “two months” formulation; both are retained.
- Letter 3579's source-supplied *The Hindu* English passages remain verbatim.
- Letter 3580's source-supplied George IPS English quotation remains represented along with the source's Tamil rendering.
- Letter 3581's complete `செம்மொழி வாழ்த்து` and textbook-removal catalogue remain intact.
- Detailed report: `volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3577_3581.md`.
- Machine-readable status: `volumes/volume-45/translations/en/alignment-status/3577-3581.yml`.

Implementation note: the large bilingual bodies for 3577–3581 retain their drafting metadata as `translation_status: source-checked`; the separate bilingual-alignment closure is recorded by the detailed review and machine-readable sidecar. Do not treat that as an unperformed QA gate, and do not rewrite those huge files merely to duplicate status unless there is a clear repository-wide reason to migrate the metadata convention safely.

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
5. preserve locked `Udanpirappē`, `With affection, M.K.`, `lakh` / `crore`, Samacheer Kalvi and other glossary conventions unless the source requires otherwise;
6. do not perform stylistic rewriting merely because another English phrasing sounds smoother;
7. do not begin the separate volume-level English editorial consistency review;
8. record the completed gate in a durable alignment report and machine-readable status record;
9. update progress/metadata/handover controls and set the exact following batch.

## EXACT NEXT ALIGNMENT BATCH

Align five complete consecutive letters:

- **3582** — `இனிய விழா; நமது இனத்தின் விழா!` — PDF **338–344** — 25-8-2011
- **3583** — `அதிகாரம் இல்லை? அந்தநாள் ஞாபகம் இல்லையா?` — PDF **345–351** — 1-9-2011
- **3584** — `அடிநாதமே; அறுக்கப்படுவதா?` — PDF **352–357** — 8-9-2011
- **3585** — `அய்யோ பாவம்! அ.தி.மு.க. அமைச்சர்கள்!!` — PDF **358–364** — 10-9-2011
- **3586** — `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!` — PDF **365–369** — 12-9-2011

Combined next alignment range: **PDF 338–369 / 32 canonical pages**.

Established source cautions in this range:

- Letter **3582** contains source-specific Thai / Chithirai / Tamil-New-Year claims. Preserve them exactly in their own source framing; do not reconcile them with outside historical or calendrical knowledge.
- Preserve source-supplied English exactly wherever printed.
- Letter **3586** is scan-proven as `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!`; the former stale `தமிழக அரசு...` reading remains withdrawn.

Create a durable alignment report for **3582–3586**, record any English corrections and any scan-triggered Tamil corrections separately, update the cumulative bilingual-aligned count, and set the exact following alignment batch from live chapter boundaries.

Immediately before Git mutation, re-fetch live `main`; preserve unrelated concurrent changes. Prefer one atomic Git-data commit where technically possible. If connector limitations force an incremental sequence, preserve history, synchronize every durable control before stopping, compare the prior durable boundary to final live `main`, and verify live `main` afterward. Never force-push routine work.

When I say **“Proceed with next activity”**, execute this bilingual-alignment batch directly without asking me to choose a routine next step.
