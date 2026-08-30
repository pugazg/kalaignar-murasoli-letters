# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-30

Read this with `VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `TRANSCRIPTION_GUIDE.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `NEXT_CHAT_PROMPT.md`.

## Source authority

The controlling scan controls Tamil readings. Audited canonical Tamil is the immediate English-QA source. OCR, translations, contents pages, outside sources and inferred chronology may not silently override the scan.

## Volume 44 — ACTIVE

Controlling source: `TVA_BOK_0065830_கலைஞரின்_கடிதங்கள்_தொகுதி_44.pdf`

Current durable state:

- PDF pages: **400**
- Source SHA-256: `573d65d7b7d3a8e3cc158b7f91af3a9382ac90ea1eaa37e8c0022b5a64dc747d`
- Source inventory: **53 records, 3484–3536**
- Canonical Tamil pages: **001–400 / 400**
- Completed Tamil letters: **53 / 53 — 3484–3536**
- Partial/source-incomplete letters: **none**
- Full-volume Tamil structural audit: **PASS**
- Second full-volume visual/textual-fidelity verification: **PASS — 400 / 400**
- Fidelity corrections: **13 canonical pages — 040, 041, 042, 047, 051, 052, 054, 056, 059, 060, 061, 062, 065**
- English pilot source review / convention lock: **PASS — 3484–3486**
- Regular English batch 1: **PASS — 3487–3491 / PDF 046–087**
- Regular English batch 2: **PASS — 3492–3496 / PDF 088–117**
- Regular English batch 3: **PASS — 3497–3501 / PDF 118–153**
- English source-checked: **18 / 53 — 3484–3501 / PDF 024–153**
- Tamil changes during regular English batches: **0**
- Volume 44 translation conventions: **LOCKED**
- Final bilingual alignment: **not started**
- English editorial review: **not started**
- English release: **not started**

The second Tamil fidelity gate restored thirteen page-scale first-pass omissions/truncations directly from the controlling scan without changing boundaries, dates, titles or the 53-record inventory.

Durable Tamil audit records:

- `volumes/volume-44/FULL_VOLUME_STRUCTURAL_AUDIT.md`
- `volumes/volume-44/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`

Durable English QA records:

- `volumes/volume-44/translations/en/PILOT_REVIEW_3484_3486.md`
- `volumes/volume-44/translations/en/BATCH_SOURCE_CHECK_3487_3491.md`
- `volumes/volume-44/translations/en/BATCH_SOURCE_CHECK_3492_3496.md`
- `volumes/volume-44/translations/en/BATCH_SOURCE_CHECK_3497_3501.md`
- `volumes/volume-44/translations/en/GLOSSARY.md`
- `volumes/volume-44/translations/en/TRANSLATION_MANIFEST.csv`
- bilingual files under `volumes/volume-44/translations/en/letters/`

All eighteen English records through 3501 contain the complete audited Tamil appendix and are source-checked, but they have **not** passed the later final bilingual-alignment/editorial/release gates.

Regular batch 3 retained the source-framed Bardhan/Maoist material in 3497, the full Anbil remembrance in 3498, health/insurance figures and anomalies in 3499, Social Welfare/Nutritious Meal material and source-era `அரவாணிகள்` terminology in 3500, and housing/Siruthavur/West Bengal reporting in 3501. The internally opaque audited phrase on PDF 125 in 3498 was surfaced explicitly rather than silently repaired; no canonical Tamil changed.

Final Tamil source boundaries remain 3535 PDF 381–390, 3536 PDF 391–399, and PDF 400 non-letter material. Letter 3536 preserves `(தொடர்ச்சி நாளை)` before the normal closing; no Letter 3537 exists.

### Exact next activity

Translate and source-check the next regular five-record English batch **Letters 3502–3506**.

- Use the complete audited canonical Tamil for every source record.
- Apply the locked Volume 44 conventions in `translations/en/PILOT_REVIEW_3484_3486.md` and `translations/en/GLOSSARY.md`.
- Read all completed regular-batch reports before drafting the next batch.
- Preserve source thought/argument order, accusation, irony, repetition, rhetorical questions, figures, names, dates, quotations, source English, continuation/conclusion markers and source anomalies.
- Include the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்` in every bilingual record.
- Source-check each completed English record against its full Tamil source before marking the batch complete.
- If a Tamil reading becomes doubtful, consult the controlling scan and record only scan-proven Tamil corrections; do not use OCR, contents wording or outside knowledge to silently repair it.
- Update the manifest/progress/index/control files and add glossary entries only for genuinely new recurring terminology.
- Stop after **3506**. **Do not start Letter 3507 in the same activity.**
- Keep final bilingual alignment, editorial review and release verification as later separate QA gates.

## Volume 45 — COMPLETE

Controlling source: `TVA_BOK_0065831_கலைஞரின்_கடிதங்கள்_தொகுதி_45.pdf`

- PDF pages: **402**
- Canonical Tamil: **001–402 / 402**
- Source letters: **55 / 55 — 3537–3591**
- Structural audit: **PASS**
- Second direct visual/textual-fidelity verification: **PASS — 402 / 402**
- English source-checked/aligned/editorially reviewed/final verified: **55 / 55**
- Source-incomplete records: **0**

## Git discipline

Work on `main` when requested, never force-push routine work, recheck live `main` immediately before mutation, preserve concurrent changes, prefer one atomic Git-data commit, and verify final changed-file scope afterward.
