# Next Chat Prompt — Volume 45 English Release Packaging

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Active work: **Volume 45 English translation manifest + final release verification/report**.

Use the GitHub connector and work directly on `main`.

## MANDATORY STARTUP

Before making any repository change:

1. Fetch live `main` and treat it as authoritative.
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
   - all completed `BILINGUAL_ALIGNMENT_REVIEW_*.md`
   - `volumes/volume-45/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
   - `volumes/volume-45/translations/en/alignment-status/README.md`
   - `volumes/volume-45/translations/en/alignment-status/3587-3591.yml`
5. Inspect Volume 46's completed manifest/release package only as a workflow/quality reference; do not copy Volume 46-specific facts into Volume 45.
6. Confirm live QA closure before release work:
   - source-checked **55 / 55**;
   - bilingual-aligned **55 / 55**;
   - editorially reviewed **55 / 55**;
   - final verified **0 / 55**.

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
- Source-checked: **55 / 55 — 3537–3591 / PDF 024–401**
- Bilingual-aligned: **55 / 55 — COMPLETE**
- Editorially reviewed: **55 / 55 — PASS**
- Final verified English: **0 / 55**

Editorial review:

- Durable report: `volumes/volume-45/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
- Result: **PASS — 55 / 55**
- Bilingual letter-body editorial corrections: **0**
- Tamil changes: **0**
- New scan re-checks: **0**

The bilingual bodies intentionally retain their drafting-layer `translation_status: source-checked`; later sidecar-tracked records may also retain implementation-level pending alignment front matter. Do not bulk-rewrite those large files merely to duplicate central QA state.

## SOURCE AUTHORITY

The audited canonical Tamil remains the immediate English-QA authority. The controlling scan remains ultimate textual authority.

Do not use outside knowledge, another edition, expected modern wording or historical reconstruction to alter source facts. Preserve source-specific anomalies, dates, figures, repetitions, quotations, source-supplied English/Latin material and physical source boundaries.

If final release verification reveals a possible Tamil discrepancy, re-check the controlling scan before changing either layer and record every scan-proven post-audit correction durably.

## EXACT NEXT ACTIVITY — TRANSLATION MANIFEST + FINAL RELEASE REPORT

Prepare the complete Volume 45 English release package.

1. Inspect the existing `translations/en/letters/` directory and English README/index.
2. Create a machine-readable translation manifest using the established completed-volume convention, with exactly **55 records — Letters 3537–3591**.
3. For every manifest row verify:
   - unique letter number;
   - correct English file path;
   - English title;
   - source date;
   - source PDF start/end range;
   - source-check complete;
   - bilingual alignment complete via durable report/sidecar;
   - editorial review complete;
   - no source-incomplete condition for Volume 45.
4. Validate manifest count = **55**, duplicate letter numbers = **0**, duplicate file paths = **0**, missing English records = **0**.
5. Confirm each released bilingual record retains the complete available `Original Tamil — மூலத் தமிழ்` appendix under the already-passed QA record.
6. Create the final English release report documenting all Tamil/English QA gates, correction accounting, manifest validation and final release result.
7. Only after all validation passes, promote final verified English to **55 / 55** and mark Volume 45 English final release complete.
8. Synchronize `metadata.yml`, volume README/progress/audit, English README/progress, root README, project handover and next-chat prompt.

Do not alter canonical Tamil or substantive English during release packaging unless a demonstrated defect is found. If any such defect is suspected, follow the source-authority rules rather than silently correcting it.

Immediately before Git mutation, re-fetch live `main`; preserve unrelated concurrent changes. Prefer one atomic Git-data commit using blobs/tree/commit/ref where technically possible. Never force-push routine work.

When I say **“Proceed with next activity”**, execute this release-packaging/final-verification gate directly without asking me to choose a routine next step.
