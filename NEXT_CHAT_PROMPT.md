# NEXT CHAT PROMPT — Volume 42 / Bilingual Alignment Batch 2 — 3369–3373 / PDF 050–073

Continue directly in `pugazg/kalaignar-murasoli-letters`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable Tamil closure

- Controlling source: `TVA_BOK_0065826_கலைஞரின்_கடிதங்கள்_தொகுதி_42.pdf`
- Source SHA-256: `43f9b51fd3765144f707cce535cc9ed39892f911a126c3c3c005173a1efc1676`
- Source extent: **402 physical PDF pages / 400 printed pages**
- Canonical Tamil: **PDF 001–402 / 402 COMPLETE**
- Full-volume Tamil structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS / COMPLETE / CLOSED — PDF 001–402 / 402**
- Unresolved Tamil fidelity items: **0**
- Actual source records: **64 — 3364–3376, 3154, 3378–3427**
- Source-incomplete records: **0**
- Letter **3427** closes at PDF **401 / printed 400**
- PDF **402** is non-letter material; **no Letter 3428**

## English source-check closure

- translated/source-checked: **64 / 64 COMPLETE**
- complete audited Tamil appendix in every English record: **64 / 64**
- canonical Tamil changes during English source-check: **0**
- unresolved English source-check items: **0**
- glossary/conventions: **LOCKED / extended through 3427**
- source number **3154** remains genuine; **3377 does not exist at that position**

## Bilingual alignment durable state

- Batch 1 **3364–3368 / PDF 024–049**: **PASS — 5 / 5 aligned**
- cumulative alignment: **5 / 64**
- English corrections in Batch 1: **1**
- canonical Tamil changes in Batch 1: **0**
- unresolved alignment items: **0**
- durable report: `volumes/volume-42/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3364_3368.md`

### Batch 1 correction to preserve

Letter **3364 / PDF 026** was missing one source sentence in English. Alignment restored:

> **It is not reasonable to expect the activities of departments such as defence to be openly known to everyone.**

No other Batch 1 English correction was required.

## Locked alignment method

1. Compare the complete audited canonical Tamil against the English body in source order.
2. Verify title, every substantive paragraph, figures, dates, quotations, lists, names, rhetoric, claims and closing.
3. Preserve source-supplied English verbatim where printed as source wording.
4. Correct English only where meaning is incomplete, shifted or inaccurate.
5. Document every substantive English correction in the durable alignment report.
6. If a Tamil defect is suspected, return to the controlling scan before changing canonical Tamil.
7. Record English corrections separately from canonical Tamil changes.
8. Set `bilingual_alignment_status: aligned` only after the record passes.
9. Keep editorial consistency review and final release verification as later separate gates.

Read `volumes/volume-42/translations/en/GLOSSARY.md` before alignment and preserve all locked terminology.

## Exact next activity — Bilingual Alignment Batch 2

Align exactly five records:

1. **3369 — PDF 050–055 / printed 49–54** — `புதியதோர் விதி செய்வோம்!`
2. **3370 — PDF 056–061 / printed 55–60** — `இங்கும் அங்குமுள்ள தமிழர்களைக் காத்திட!`
3. **3371 — PDF 062–065 / printed 61–64** — `இன்று என் வாழ்விலோர் திருநாள்!`
4. **3372 — PDF 066–069 / printed 65–68** — `இது எப்போதும் உங்கள் உயிர்!`
5. **3373 — PDF 070–073 / printed 69–72** — `அனைவர் அகமும் அன்பகம் ஆகிட...!`

### Required startup

Read completely before editing:

1. `VOLUME_PROCESSING_GUIDE.md`
2. `volumes/volume-42/TRANSLATION_PLAN.md`
3. `volumes/volume-42/translations/en/README.md`
4. `volumes/volume-42/translations/en/PROGRESS.md`
5. `volumes/volume-42/translations/en/GLOSSARY.md`
6. `volumes/volume-42/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3364_3368.md`
7. source-check reports covering 3369–3373
8. the five English records
9. canonical Tamil pages PDF **050–073**

### Output

- meaning-level PASS/FAIL for each record;
- English corrections only where required by source meaning;
- canonical Tamil changes only if a concrete scan-proven defect is found;
- set `bilingual_alignment_status: aligned` after each PASS;
- create `volumes/volume-42/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3369_3373.md`;
- update alignment progress and repository controls atomically.

Stop after **3373 / PDF 073**. Do **not** begin **3374 / PDF 074** in the same activity.

Suggested commit message:

`Align Volume 42 letters 3369-3373`
