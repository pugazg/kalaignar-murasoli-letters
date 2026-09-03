# Next Chat Prompt — Volume 43 Bilingual Alignment — Next 10 Records

Continue the Kalaignar Murasoli Letters archival / bilingual project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF:

`TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve the newest durable state. Do not reset, repeat or reopen completed Tamil transcription, Tamil fidelity verification, English source-check or completed alignment because a copied checkpoint is older.

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
19. `volumes/volume-43/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3428_3432.md`
20. `volumes/volume-43/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3433_3442.md`
21. `volumes/volume-43/translations/en/BILINGUAL_ALIGNMENT_SYNC_3428_3442.md`

## Durable Volume 43 gates

- Tamil transcription/source-page representation: **COMPLETE — 56 / 56; PDF 001–402 / 402**
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — 402 / 402**
- English drafting/source-check: **COMPLETE — 56 / 56 — 3428–3483**
- Canonical Tamil changes during English source-check: **0**
- Translation conventions: **LOCKED**
- Bilingual meaning-level alignment: **IN PROGRESS — 15 / 56 aligned — 3428–3442 / PDF 024–137**
- English corrections required by completed alignment reviews: **0**
- Canonical Tamil changes exposed by completed alignment reviews: **0**
- Editorial consistency review: **not started**
- Final English release verification: **not started**

Every English record contains the complete audited canonical Tamil under `## Original Tamil — மூலத் தமிழ்` with physical PDF markers. `source-checked`, `aligned`, editorial review and final release remain separate gates.

## Source-layer reminder

Final genuine printed-contents / actual-title differences are **3435, 3438, 3441, 3463, 3464, 3467, 3472, 3473 and 3474**. Earlier provisional discrepancy claims for **3430, 3476, 3477 and 3481** are superseded by the completed second visual pass.

## Alignment policy

Compare the English body against the complete audited Tamil appendix and canonical page files at meaning level. Check every title, paragraph, sentence, figure, date, quotation, list item, rhetorical turn and closing. Preserve source-supplied English verbatim where the source printed it. Preserve source-attributed political, legal, historical and religious claims without outside adjudication.

If English meaning is incomplete or inaccurate, correct the English record and document the correction. If a Tamil defect is suspected, return to the controlling scan before any canonical Tamil change. Record English corrections separately from Tamil changes.

## Exact next activity — process 10 letters

Perform bilingual alignment for **exactly 10 records, Letters 3443–3452 / PDF 138–211**:

1. **3443 — PDF 138–142** — `அவர்களும் நாமும்; ஒரு ஒப்பீடு!`
2. **3444 — PDF 143–148** — `இதோ மீண்டும் என் அன்பு அழைப்பு!`
3. **3445 — PDF 149–156** — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் - 1`
4. **3446 — PDF 157–164** — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் - 2`
5. **3447 — PDF 165–172** — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் - 3`
6. **3448 — PDF 173–181** — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் - 4`
7. **3449 — PDF 182–190** — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் - 5`
8. **3450 — PDF 191–198** — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் - 6`
9. **3451 — PDF 199–207** — `செம்மொழி வரலாற்றில் சில செப்பேடுகள் - 7`
10. **3452 — PDF 208–211** — `வளமார் தமிழகம் வாழ்த்துகள் பொழிகிறேன்!`

Stop before **Letter 3453 / PDF 212**.

For these 10 records:

- compare Tamil ↔ English linearly and completely;
- correct English only where alignment requires it;
- reopen Tamil only if a concrete source defect is found;
- set `bilingual_alignment_status: aligned` only after the individual record passes;
- create one durable 10-record bilingual-alignment review report;
- update manifest and alignment progress controls after review;
- report English corrections and canonical Tamil changes separately;
- do not perform editorial consistency review or final release verification in the same activity.

## Git discipline

Work directly on `main`. Re-fetch live `main` immediately before mutation, preserve concurrent work, build a candidate tree/commit without moving `main`, validate parent → candidate changed-file scope, publish by fast-forward only with `force: false`, and verify parent → new HEAD afterward.
