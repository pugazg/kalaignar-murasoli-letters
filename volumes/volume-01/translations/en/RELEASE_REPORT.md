# Volume 1 — Final English Release Report

Status: **RELEASE COMPLETE — 110 / 110 canonical English records certified for Volume 1.**

## Release identity

- Work: **கலைஞரின் கடிதங்கள் — தொகுதி 1 / Kalaignar's Murasoli Letters — Volume 1**
- Canonical tree: `volumes/volume-01/`
- Preserved legacy tree: `volumes/volume-1/`
- Controlling source: supplied `Vol1.pdf`
- Source identity: SHA-256 `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`
- Source size: **244,892,260 bytes**
- PDF pages: **401**
- Publisher-printed pages: **400**
- Canonical letter range: **0001–0110**
- Letter source span: **PDF 024–400**
- PDF 401: non-letter back cover / publisher advertisement

## Completion status

| Gate | Result |
|---|---|
| Canonical Tamil page migration | **401 / 401 complete** |
| Canonical letters | **110 / 110 complete** |
| Tamil structural audit | **PASS** |
| Full visual/textual-fidelity verification | **PASS — PDF 001–401 / 401** |
| Canonical English migration/source check | **110 / 110 PASS** |
| Complete canonical Tamil witnesses in English records | **110 / 110 certified by completed source-check/alignment/editorial gates** |
| Bilingual alignment | **110 / 110 PASS** |
| Alignment-driven English corrections | **4 — 0014, 0043, 0058, 0059** |
| Volume-level English editorial consistency | **110 / 110 PASS** |
| New English prose/quotation corrections in editorial pass | **0** |
| Translation manifest | **110 unique rows** |
| Final English release certification | **110 / 110 RELEASED** |

## Release manifest

[`TRANSLATION_MANIFEST.csv`](TRANSLATION_MANIFEST.csv) contains exactly one release row for every canonical letter **0001–0110**.

Validation performed for the release inventory:

- **110** unique letter numbers;
- **110** unique canonical English file paths;
- complete sequential range **0001–0110** with no missing release record;
- canonical Tamil title/date/PDF coverage reconciled to the scan-verified chapter register;
- printed-page ranges preserved, including the Volume 1 pagination anomaly around printed page 39;
- source-check, bilingual-alignment and editorial-review certification represented for every row through the completed gate records referenced by this release;
- the applicable ten-letter bilingual-alignment report recorded for every row;
- the full-volume Tamil fidelity gate applies to every released record;
- source exceptions recorded explicitly rather than normalised.

The manifest is the authoritative release ledger. Its release statuses certify completed workflow state and are not intended to reproduce stale source-check-era fields literally from every canonical Markdown record.

## Preserved source controls and exceptions

The release deliberately preserves the following source-controlled conditions:

- **0005:** PDF 039 prints page 38 and PDF 040 prints page 40; printed page number 39 is skipped while the text remains continuous.
- **0028:** the source-printed closing date **28-12-1968** controls over conflicting legacy metadata.
- **0048:** the printed `சென்னை. / 10.10.1972` evidence is retained; no later composition date is inferred from historical context in the body.
- **0063:** no date is printed in the source; the letter remains intentionally undated.
- **0070:** the judicial inquiry's printed English sentence remains verbatim, including source punctuation and syntax.
- **0109:** actual PDF-392 heading `அவள் ஒரு தொடர்கதை!` controls over the contents-page variant `அவள் ஒரு தொடற்கதை!`; opaque source wording including `நமப்பார்வதி பதேக்கள்!` remains unreconstructed.
- **0110:** the final letter ends on PDF 400 with **01-12-1974**; PDF 401 is non-letter material.

These are archival facts or source conditions, not defects to be silently repaired.

## English release policy

The released English remains thought-preserving and non-literary. Kalaignar's argument order, political directness, rhetorical questions, repetitions, satire, movement vocabulary, quotations, figures and historical framing remain controlled by the canonical Tamil and completed bilingual-alignment gate.

`Udanpirappē` remains the established rendering when the source uses Kalaignar's characteristic address. Source-specific salutations, sign-offs and intentional English are not forcibly normalised.

The four alignment corrections in **0014, 0043, 0058 and 0059** remain locked. No release-stage rewrite of canonical English prose was required.

## Record architecture and release certification

The canonical English corpus retains three migration-era presentation phases:

- **0001–0040:** early shared translator-note/frontmatter schema;
- **0041–0060:** compact schema without record-local translator-note blocks;
- **0061–0110:** later letter-specific note / `quality_controls` schema.

This presentation variation was reviewed and accepted by the completed editorial-consistency gate. Release certification therefore lives in the dedicated manifest and release report rather than forcing a 110-file frontmatter rewrite that would create archival churn without changing translated content.

The same principle applies to old fields such as `bilingual_alignment_status: "pending"`, `bilingual_alignment_checked: false` or `editorial_consistency_checked: false`: the completed gate reports and final manifest are authoritative for workflow state.

## Preservation and change summary

This release gate changes **no canonical Tamil** and makes **no new canonical English prose/quotation correction**.

The legacy `volumes/volume-1/` tree remains untouched and continues to serve only as provenance/migration evidence.

`metadata.yml` is not mass-rewritten during release certification. The dedicated audit, alignment, editorial and release artifacts are the authoritative completion records.

## Final release declaration

**Volume 1 is complete through English editorial release within the controlling source.**

The repository now contains the complete canonical Tamil volume, completed Tamil structural and visual/textual-fidelity audits, all **110** canonical bilingual English records, all source-check reports, all bilingual-alignment reports and manifest, the volume-level editorial consistency review, the **110-row final translation manifest**, and this final release report.

No further Volume 1 translation gate remains open. Any future change to a released record should be evidence-driven, narrowly documented, and must preserve the source-authority hierarchy and legacy provenance.
