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
- English pilot drafting: **COMPLETE — 3 / 53, Letters 3484–3486 / PDF 024–045**
- Pilot source-review / convention lock: **PASS — 3 / 3**
- English source-checked: **3 / 53 — 3484–3486**
- Pilot review corrections: **5 English spans across Letters 3484–3485**
- Tamil changes during pilot review: **0**
- Volume 44 translation conventions: **LOCKED**
- Regular English batches: **unlocked; exact next 3487–3491**
- Final bilingual alignment: **not started**
- English release: **not started**

The second Tamil fidelity gate found page-scale first-pass omissions/truncations concentrated in early reservation-history material. The thirteen affected page bodies were restored directly from the controlling scan. The repair did **not** change letter boundaries, dates, titles, contents/chapter ranges, the 53-record inventory or the structural PASS.

Durable Tamil audit records:

- `volumes/volume-44/FULL_VOLUME_STRUCTURAL_AUDIT.md`
- `volumes/volume-44/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`

Durable English pilot records:

- `volumes/volume-44/translations/en/PILOT_REVIEW_3484_3486.md`
- `volumes/volume-44/translations/en/GLOSSARY.md`
- `volumes/volume-44/translations/en/TRANSLATION_MANIFEST.csv`
- pilot bilingual files under `volumes/volume-44/translations/en/letters/`

The pilot review corrected two English alignment defects in Letter 3484 and three in Letter 3485; Letter 3486 required no correction. No audited Tamil reading became doubtful, so no canonical Tamil file was changed. The three pilot records are source-checked but have **not** passed the later final bilingual-alignment/editorial/release gates.

Final Tamil source boundaries remain 3535 PDF 381–390, 3536 PDF 391–399, and PDF 400 non-letter material. Letter 3536 preserves `(தொடர்ச்சி நாளை)` before the normal closing; no Letter 3537 exists.

### Exact next activity

Translate and source-check the first regular five-record English batch **Letters 3487–3491**.

- Use the complete audited canonical Tamil for every source record.
- Apply the locked Volume 44 conventions in `translations/en/PILOT_REVIEW_3484_3486.md` and `translations/en/GLOSSARY.md`.
- Preserve source thought/argument order, accusation, irony, repetition, rhetorical questions, figures, names, dates, quotations, source English, continuation markers and source anomalies.
- Include the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்` in every bilingual record.
- Source-check each completed English record against its full Tamil source before marking the batch complete.
- If a Tamil reading becomes doubtful, consult the controlling scan and record only scan-proven Tamil corrections; do not use OCR, contents wording or outside knowledge to silently repair it.
- Update the manifest/progress/index/control files and add glossary entries only for genuinely new recurring terminology.
- Stop after **3491**. **Do not start Letter 3492 in the same activity.**
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
