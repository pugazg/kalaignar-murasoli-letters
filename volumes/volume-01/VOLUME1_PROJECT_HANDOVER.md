# Volume 1 — Project Handover

## Repository and source

Work on `pugazg/kalaignar-murasoli-letters` `main`. Canonical tree: `volumes/volume-01/`. Preserve `volumes/volume-1/` unchanged.

Controlling source: `Vol1.pdf`, SHA-256 `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`, 244,892,260 bytes, 401 PDF pages, first edition 2022, Seethai Pathippagam, no usable text layer. Do not commit the PDF.

## Volume 1 — COMPLETE

All regular archival and English gates are closed:

- canonical Tamil migration: **401 / 401 PDF pages**
- canonical letters: **110 / 110**
- Tamil structural audit: **PASS**
- full visual/textual-fidelity verification: **PASS — 401 / 401**
- source-check English: **110 / 110 PASS**
- bilingual alignment: **110 / 110 PASS**
- cumulative alignment corrections: **4 — 0014, 0043, 0058, 0059**
- English editorial consistency: **110 / 110 PASS**
- final translation manifest: **110 unique rows**
- final English release report: **COMPLETE**
- release-certified canonical English records: **110 / 110**

Authoritative release artifacts:

- `volumes/volume-01/translations/en/TRANSLATION_MANIFEST.csv`
- `volumes/volume-01/translations/en/RELEASE_REPORT.md`
- `volumes/volume-01/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
- `volumes/volume-01/translations/en/alignment/ALIGNMENT_MANIFEST.csv`

Canonical translation files were not mass-rewritten merely to change historical workflow frontmatter. The final manifest/release report are authoritative for release certification.

## Locked source controls

Do not silently change:

- printed-pagination anomaly around PDF 039–040 / printed page 39;
- 0028 source-printed date 28-12-1968;
- 0048 printed `சென்னை. / 10.10.1972`;
- 0063 undated status;
- 0070 source-printed English judicial quotation;
- 0109 actual heading `அவள் ஒரு தொடர்கதை!` versus contents `அவள் ஒரு தொடற்கதை!`, including opaque unreconstructed source wording;
- PDF 401 non-letter status;
- the four alignment corrections in 0014, 0043, 0058 and 0059.

## Future Volume 1 work

There is **no routine next Volume 1 gate**. Reopen a released Volume 1 record only for new source evidence or a specifically approved, narrowly documented correction. Any such change must preserve the scan → canonical Tamil → English authority order and must not rewrite the legacy tree.

For new volume work, return to the root processing guides and `START_NEXT_MURASOLI_VOLUME_PROMPT.md`.
