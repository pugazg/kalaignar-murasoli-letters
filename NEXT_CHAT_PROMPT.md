# Next Chat Prompt — Volume 43 Final English Release Verification

Continue the Kalaignar Murasoli Letters archival / bilingual project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF: `TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state. Do not reset, repeat or reopen completed Tamil transcription, Tamil fidelity verification, English source-check, bilingual alignment or editorial consistency review because an older copied checkpoint says otherwise.

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
19. `volumes/volume-43/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
20. all six `volumes/volume-43/translations/en/BILINGUAL_ALIGNMENT_REVIEW_*.md` reports.

## Durable Volume 43 gates

- Tamil transcription/source-page representation: **COMPLETE — 56 / 56; PDF 001–402 / 402**
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — 402 / 402**
- English drafting/source-check: **COMPLETE — 56 / 56 — 3428–3483 / PDF 024–400**
- Bilingual meaning-level alignment: **COMPLETE — 56 / 56**
- English editorial consistency review: **PASS — 56 / 56**
- Editorial English-only corrections: **2** — 3481 lakh-unit treatment; 3483 Union Government terminology
- Canonical Tamil changes during editorial review: **0**
- Final English release verification: **not started**

All 56 manifest rows must now be `source-checked`, `aligned`, `reviewed`, with `final_release_status: pending`. Every bilingual record must retain its complete audited Tamil appendix.

## Exact next activity — final English release verification

Perform only the separate final release gate:

- reconcile `TRANSLATION_MANIFEST.csv` to exactly **56 actual source records, Letters 3428–3483**;
- require **56 unique letter numbers and 56 unique English paths**;
- confirm every manifest row is `source-checked`, `aligned`, `reviewed`, `final_release_status: pending`, `source_incomplete=false`;
- confirm every manifest path exists and each record has complete front matter, English body, source references and one complete `Original Tamil — மூலத் தமிழ்` appendix;
- verify title/date/PDF-range agreement and the six alignment-review links;
- reconfirm Letter **3483** ends at **PDF 400**; PDF **401–402** are non-letter matter; no Letter 3484 exists;
- confirm protected source-English and documented anomalies remain intact;
- confirm no temporary workflow/script/export/probe file would enter `main`;
- create `volumes/volume-43/translations/en/RELEASE_REPORT.md`;
- only after all checks pass, set all 56 manifest final-release statuses to the repository’s completed value and synchronize metadata/progress/README/handover/root controls.

Do not perform new translation, re-alignment or Tamil correction unless the release audit exposes a concrete defect requiring the appropriate earlier authority.

## Git discipline

Re-fetch live `main` immediately before mutation, preserve concurrent work, validate the candidate changed-file scope, publish by fast-forward only with `force: false`, and verify the new HEAD afterward.
