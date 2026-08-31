# Next Chat Prompt — Continue Murasoli Letters

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

## Live-main rule for a fresh chat

**Fetch live `main` first and treat it as authoritative.** If `main` has advanced beyond any checkpoint copied into a prompt, preserve the newer durable state and continue from it. Do not reset or overwrite later completed work.

Before changing anything, read the repository processing guides, `PROJECT_HANDOVER.md`, this `NEXT_CHAT_PROMPT.md`, and the controls for the active source/volume.

## Volume 44 durable boundary

Volume 44 is **complete through all Tamil archival and English release gates**.

- Controlling source: `TVA_BOK_0065830_கலைஞரின்_கடிதங்கள்_தொகுதி_44.pdf`
- PDF pages: **400**
- Source SHA-256: `573d65d7b7d3a8e3cc158b7f91af3a9382ac90ea1eaa37e8c0022b5a64dc747d`
- Source inventory: **53 records, 3484–3536**
- Canonical Tamil pages: **400 / 400 — PDF 001–400**
- Completed Tamil letters: **53 / 53 — 3484–3536**
- Full-volume Tamil structural audit: **PASS**
- Second full-volume visual/textual-fidelity verification: **PASS — 400 / 400**
- English drafted/source-checked: **53 / 53 — 3484–3536 / PDF 024–399**
- Translation conventions: **LOCKED**
- Bilingual alignment: **COMPLETE — 53 / 53 — 3484–3536 / PDF 024–399**
- Canonical Tamil changes across all alignment batches: **0**
- English editorial consistency review: **PASS — 53 / 53**
- English final release verification: **PASS — 53 / 53**
- Final release manifest: **53 rows; 53 unique letter numbers; 53 unique English paths; 0 duplicates; 0 missing English records; 0 source-incomplete rows**
- English/Tamil body changes during final release verification: **0**

Final release report: `volumes/volume-44/translations/en/RELEASE_REPORT.md`.

PDF 399 preserves `(தொடர்ச்சி நாளை)` followed by the normal closing, so Letter 3536 is complete in this source. PDF 400 is non-letter back-cover / portrait / publisher material. Do not invent Letter 3537.

## Exact next activity

There is **no further Volume 44 QA or release gate pending**. Derive the next activity from live `main` and the next source/volume explicitly supplied by the user. Do not reopen or repeat Volume 44 release work unless a concrete defect is reported or a new audit is explicitly requested.

Before any future mutation, recheck live `main`, preserve concurrent work, prefer a validated atomic commit, use a normal fast-forward with `force: false`, and verify parent → new HEAD changed-file scope.
