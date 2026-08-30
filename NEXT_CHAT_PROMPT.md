# Next Chat Prompt — Continue Murasoli Letters Volume 44

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Attach the controlling source PDF again when starting a fresh chat:

`TVA_BOK_0065830_கலைஞரின்_கடிதங்கள்_தொகுதி_44.pdf`

## Durable boundary

**Volume 44 Tamil archival preparation is complete through both required full-volume gates. English translation/source-check coverage is complete through Letter 3491.**

- PDF pages: **400**
- Source SHA-256: `573d65d7b7d3a8e3cc158b7f91af3a9382ac90ea1eaa37e8c0022b5a64dc747d`
- Source inventory: **53 records, 3484–3536**
- Canonical Tamil pages: **400 / 400 — PDF 001–400**
- Completed Tamil letters: **53 / 53 — 3484–3536**
- Partial/source-incomplete letters: **none**
- Full-volume Tamil structural audit: **PASS**
- Second full-volume visual/textual-fidelity verification: **PASS — 400 / 400**
- Second-pass corrections: **13 canonical pages — 040, 041, 042, 047, 051, 052, 054, 056, 059, 060, 061, 062, 065**
- Pilot source-review / convention lock: **PASS — 3484–3486**
- First regular English batch: **PASS — 3487–3491 / PDF 046–087**
- English drafted/source-checked: **8 / 53 — 3484–3491 / PDF 024–087**
- Tamil changes during first regular English batch: **0**
- Volume 44 translation conventions: **LOCKED**
- Final bilingual alignment: **not started**
- English editorial review: **not started**
- English release: **not started**

English QA artifacts:

- `volumes/volume-44/translations/en/PILOT_REVIEW_3484_3486.md`
- `volumes/volume-44/translations/en/BATCH_SOURCE_CHECK_3487_3491.md`
- `volumes/volume-44/translations/en/GLOSSARY.md`
- `volumes/volume-44/translations/en/TRANSLATION_MANIFEST.csv`

English records now exist for Letters **3484–3491** under `volumes/volume-44/translations/en/letters/`. Each contains a complete source-checked English translation and the complete audited Tamil appendix. Source-check PASS does **not** imply final bilingual alignment or release readiness.

## Exact next activity

Execute the next regular **five-actual-source-record English drafting/source-check batch — Letters 3492–3496**.

1. Fetch live `main` first and treat it as authoritative.
2. Read the locked pilot review, first regular-batch report and current glossary before drafting:
   - `volumes/volume-44/translations/en/PILOT_REVIEW_3484_3486.md`
   - `volumes/volume-44/translations/en/BATCH_SOURCE_CHECK_3487_3491.md`
   - `volumes/volume-44/translations/en/GLOSSARY.md`
3. Use each letter's complete audited canonical Tamil as the immediate source. Do not translate from contents wording, OCR or outside material.
4. Preserve thought/argument order, political directness, accusation, irony, repetition, rhetorical questions, figures, names, dates, quotations, source English, continuation/conclusion markers and source anomalies.
5. Use the locked terminology consistently unless the actual source requires a different treatment.
6. Include the complete audited Tamil under `## Original Tamil — மூலத் தமிழ்` in every bilingual record, with physical source-page markers.
7. Source-check every completed English record against its full Tamil source before recording the batch as complete.
8. If a Tamil reading becomes doubtful, consult the controlling scan and record only scan-proven Tamil corrections separately. Do not silently revise audited Tamil from OCR, contents wording or outside knowledge.
9. Update the English index, progress, manifest and relevant Volume 44/root control files; add glossary entries only for genuinely new recurring terminology.
10. Stop after **Letter 3496**. **Do not begin Letter 3497 in the same activity.** Final bilingual alignment/editorial/release QA remain separate later gates.

Before changing anything, fetch live `main`, preserve concurrent unrelated work, and use a normal fast-forward update without force.
