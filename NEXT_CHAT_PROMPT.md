# Next Chat Prompt — Volume 43 English Editorial Consistency Review

Continue the Kalaignar Murasoli Letters archival / bilingual project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF: `TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state. Do not reset, repeat or reopen completed Tamil transcription, Tamil fidelity verification, English source-check or bilingual alignment because an older copied checkpoint says otherwise.

## Mandatory startup

Before any repository change, read completely:

1. `VOLUME_PROCESSING_GUIDE.md`
2. `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
3. `TRANSCRIPTION_GUIDE.md`
4. `FUTURE_VOLUME_WORK_GUIDELINES.md`
5. `PROJECT_HANDOVER.md`
6. this `NEXT_CHAT_PROMPT.md`
7. `volumes/volume-43/README.md`
8. `volumes/volume-43/PROGRESS.md`
9. `volumes/volume-43/AUDIT.md`
10. `volumes/volume-43/metadata.yml`
11. `volumes/volume-43/FULL_VOLUME_STRUCTURAL_AUDIT.md`
12. `volumes/volume-43/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`
13. `volumes/volume-43/TRANSLATION_PLAN.md`
14. `volumes/volume-43/translations/en/README.md`
15. `volumes/volume-43/translations/en/PROGRESS.md`
16. `volumes/volume-43/translations/en/PROGRESS_ALIGNMENT_CHECKPOINT.md`
17. `volumes/volume-43/translations/en/GLOSSARY.md`
18. `volumes/volume-43/translations/en/TRANSLATION_MANIFEST.csv`
19. all six `volumes/volume-43/translations/en/BILINGUAL_ALIGNMENT_REVIEW_*.md` reports, through `BILINGUAL_ALIGNMENT_REVIEW_3473_3483.md`.

## Durable Volume 43 gates

- Tamil transcription/source-page representation: **COMPLETE — 56 / 56; PDF 001–402 / 402**
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — 402 / 402**
- English drafting/source-check: **COMPLETE — 56 / 56 — 3428–3483 / PDF 024–400**
- Translation conventions: **LOCKED**
- Bilingual meaning-level alignment: **COMPLETE — 56 / 56 — 3428–3483 / PDF 024–400**
- English corrections across the complete alignment phase: **0**
- Canonical Tamil changes across the complete alignment phase: **0**
- English editorial consistency review: **not started**
- Final English release verification: **not started**

Every English record contains the complete audited canonical Tamil under `## Original Tamil — மூலத் தமிழ்`. Source-check, bilingual alignment, editorial review and final release remain separate gates.

## Source-layer reminders

Final genuine printed-contents / actual-title differences remain **3435, 3438, 3441, 3463, 3464, 3467, 3472, 3473 and 3474**. Earlier provisional discrepancy claims for **3430, 3476, 3477 and 3481** are superseded by the completed second visual pass. Preserve the 3467 facsimile rule, 3477 85/86 copper-plate tension, 3481 source-supplied Wall Street Journal English and 3482 `3.54 மெட்ரிக் டன்` anomaly.

## Exact next activity — English editorial consistency review

Perform the separate volume-level editorial consistency review across all **56 aligned records, Letters 3428–3483 / PDF 024–400**. Follow the completed Volume 44 editorial gate as the repository precedent.

This is a **cross-record consistency gate, not a retranslation pass**. Check:

- title/front-matter/manifest/index agreement;
- dates, PDF ranges and source-boundary consistency;
- translator/source-check note conventions and headings;
- names, honorifics, place names and transliteration;
- institutions, schemes, legal/political/reservation terminology and locked glossary treatments;
- `lakh` / `crore` and other Indian public-language quantities;
- capitalization, punctuation and quotation treatment;
- genuinely source-supplied English, which must remain verbatim;
- continuation/conclusion markers and standard salutation/closing conventions;
- documented source anomalies without silent normalization;
- stale control-layer wording;
- presence/completeness of the appended audited Tamil in every bilingual record.

Only demonstrated consistency defects justify English edits. If a possible Tamil defect appears, return to the controlling scan before changing canonical Tamil.

Create `volumes/volume-43/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`. If the gate passes, update all 56 manifest `editorial_review_status` values from `pending` to `reviewed` and synchronize metadata/progress/handover controls. Keep `final_release_status` pending and do **not** perform final English release verification in the same activity.

## Git discipline

Re-fetch live `main` immediately before mutation, preserve concurrent work, validate the candidate changed-file scope, publish by fast-forward only with `force: false`, and verify the new HEAD afterward.
