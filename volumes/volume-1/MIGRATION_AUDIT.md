# Volume 1 — Canonical Structure Migration Audit

**Status:** migration planning complete; legacy content preserved unchanged  
**Target:** bring the existing Volume 1 corpus into the same archival model used by Volumes 46–49 without discarding or silently rewriting the existing work.

## 1. Controlling source now available

The controlling source is the newly supplied **Vol1.pdf**.

Programmatic inspection of the supplied file records:

- PDF pages: **401**
- File size: **244,892,260 bytes**
- SHA-256: `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`
- Cover/title date range: **22.10.1968–01.12.1974**
- Printed book pages: **400**
- Edition: **1st edition, 2022**
- Publisher: **Seethai Pathippagam**

The scan itself confirms the archival sequence used by the existing Volume 1 material:

- contents run through **110 letters**;
- letter **1 — “ஜாக்குலின்கள்”** begins at PDF/source page **24**;
- letter **110 — `கயிற்றில் தொங்கிய கணபதி!`** begins at source page **396**;
- the final letter ends on PDF/source page **400** with date **01-12-1974**;
- PDF page **401** is the back cover.

The supplied source therefore appears to be the complete Volume 1 scan required for canonical migration.

## 2. Existing legacy Volume 1 state

Current repository path:

`volumes/volume-1/`

Current top-level structure contains only:

```text
audits/
translations/
```

It does **not** yet expose the canonical later-volume structure:

```text
README.md
metadata.yml
AUDIT.md
PROGRESS.md
TRANSLATION_PLAN.md
contents/index.md
chapters/
pages/
translations/en/README.md
translations/en/PROGRESS.md
...
```

The legacy work is substantial and must be preserved:

- bilingual chapter files: **110**;
- existing chapter checks: **110 / 110 passed**;
- English translation words recorded by the legacy audit: **90,317**;
- source-corrected Tamil words recorded by the legacy audit: **49,867**;
- existing translation audit: **passed**;
- existing structural regression: **passed**.

The existing bilingual files already contain:

1. translator note;
2. English translation;
3. source-corrected Tamil reading copy.

This material is valuable migration input. It must **not** be thrown away and must **not** be assumed automatically equivalent to the newer canonical-page / second-visual-verification / bilingual-alignment workflow.

## 3. Core migration principle

This is a **normalization and revalidation project**, not a fresh transcription project and not a blind folder rename.

Authority order during migration:

1. supplied Volume 1 PDF scan;
2. newly created visually verified canonical `pages/page-NNN.md` layer;
3. contents/chapter records;
4. migrated bilingual English records;
5. manifests/reports.

Existing source-corrected Tamil and English are reusable drafts/reference material. The scan remains controlling.

No existing Tamil or English wording is to be silently modernized, normalized, reconciled with outside knowledge or rewritten merely to fit the newer folder model.

## 4. Required target structure

The canonical end state should match the later-volume model:

```text
volumes/volume-01/
  README.md
  metadata.yml
  AUDIT.md
  PROGRESS.md
  TRANSLATION_PLAN.md
  contents/
    index.md
  chapters/
    README.md
    0001-<slug>.md
    ...
    0110-<slug>.md
  pages/
    page-001.md
    ...
    page-401.md
  translations/
    en/
      README.md
      PROGRESS.md
      GLOSSARY.md
      EDITORIAL_CONSISTENCY_REVIEW.md
      TRANSLATION_MANIFEST.csv
      RELEASE_REPORT.md
      textual-fidelity reports
      bilingual-alignment reports
      letters/
        0001-<slug>.md
        ...
        0110-<slug>.md
  legacy/
    ... preserved legacy provenance where needed ...
```

The repository master guide specifies `volume-01` through `volume-09` for single-digit volumes. The current `volume-1` path should therefore be treated as the legacy path. The final path migration should occur only after internal links and references have been reconciled and the new tree is validated.

## 5. Migration phases

### Phase A — freeze and inventory legacy corpus

- preserve every current legacy file and blob;
- inventory all 110 bilingual records and all legacy audit files;
- reconcile legacy source-page lists with the supplied scan;
- do not delete or rewrite legacy files during this phase.

### Phase B — build canonical page spine

Create one canonical Markdown file for **every PDF page 001–401**.

- include covers, title/publication matter, foreword, contents, blanks and back cover;
- use the existing source-corrected Tamil as assistance only;
- visually compare each accepted page with the supplied scan;
- preserve page boundaries and printed anomalies;
- never reconstruct from the English translation.

Because this is a migration of an already-complete corpus, the ordinary new-volume batching policy should be adapted conservatively: the first canonical migration commit should still establish **PDF 001–025** as a controlled first batch, followed by verified complete-letter batches unless a documented migration-specific exception is required.

### Phase C — canonical contents and chapter records

- migrate the 110-letter contents list into `contents/index.md`;
- preserve the printed contents wording and dates;
- create one chapter record per actual source letter;
- link chapters to canonical page files rather than duplicating Tamil text;
- verify actual letter-start titles against the scan and document any contents/title differences.

### Phase D — full Tamil structural audit

After all 401 canonical pages exist:

- verify exactly one page file per PDF page;
- verify all 110 source records and start/end boundaries;
- check titles, dates, closings, signatures, figures, quotations, intentional English and page-boundary splits;
- record source anomalies rather than correcting them silently.

### Phase E — mandatory second visual / textual-fidelity gate

The legacy claim `source-corrected` is useful provenance but does not replace the later project's explicit scan-based second gate.

Before English is certified under the newer standard, every translated source page must be visually rechecked against the scan and scan-proven corrections recorded.

### Phase F — migrate/revalidate English

The existing **110 English translations should be reused**, not automatically retranscribed/retranslated.

For every record:

- map legacy title/date/source pages into current front matter;
- retain Kalaignar's argument order, direct political voice, criticism, irony, repetition, quotations and rhetorical questions;
- preserve `Udanpirappē` where source-supported;
- append the complete newly audited canonical Tamil;
- distinguish source-supplied English from translator English;
- initially classify migrated records as requiring current-workflow verification rather than treating legacy `passed` as equivalent to current `verified`.

### Phase G — bilingual alignment

Run Tamil–English meaning-level comparison across all 110 records.

Check omissions/additions, argument sequence, names, dates, figures, quotations, lists, attribution, sarcasm, repetition, rhetorical force and source anomalies.

Correct English only when the current audited Tamil proves a translation problem. Correct Tamil only when a fresh scan comparison proves a canonical transcription defect.

### Phase H — editorial consistency and release

After 110 / 110 records pass alignment:

- run volume-level English editorial consistency review;
- generate the current translation manifest;
- generate the final English release report;
- synchronize README, metadata and progress;
- certify the normalized Volume 1 release only after all counts reconcile.

## 6. Legacy preservation policy

Do not erase the earlier method merely because a newer structure exists.

Legacy audit artifacts should remain available as provenance, either:

- under `legacy/` / `audits/legacy/`; or
- in their existing immutable Git history plus a migration note pointing to the commit boundary.

The preferred final structure is to retain enough legacy artifacts in-tree to explain the origin of the migrated English/Tamil corpus without allowing them to masquerade as the canonical current-workflow audit.

## 7. What can be reused directly

Likely reusable after validation:

- 110-letter order;
- dates;
- source-page membership;
- source-verified titles as candidate actual-letter titles;
- English translations;
- translator-note concepts;
- source-corrected Tamil reading copies as comparison aids;
- existing audit/manifest data as migration evidence.

## 8. What must be newly created or re-certified

Required under the current archival model:

- 401 canonical `pages/page-NNN.md` files;
- canonical `contents/index.md`;
- 110 current-format chapter records;
- volume `README.md`;
- `metadata.yml`;
- `AUDIT.md` and current `PROGRESS.md`;
- `TRANSLATION_PLAN.md` / locked Volume 1 translation conventions;
- explicit second visual/textual-fidelity reports;
- current-format bilingual files with complete canonical Tamil appendices;
- explicit bilingual-alignment reports;
- editorial consistency review;
- current translation manifest;
- final release report.

## 9. Safety rule before destructive path migration

Do **not** rename/delete `volumes/volume-1/` at the beginning.

First build and validate the canonical replacement structure. Only after:

- all 401 pages reconcile;
- all 110 letters reconcile;
- all migrated files are accounted for;
- internal links validate; and
- legacy provenance is preserved,

should the repository switch definitively to `volumes/volume-01/` and remove or archive the obsolete path.

## 10. Exact next activity

Begin **Phase A/B migration setup** without altering the legacy bilingual corpus:

1. create the current Volume 1 metadata/progress/README scaffold;
2. establish canonical **PDF 001–025** page files by comparing the supplied scan with available legacy material;
3. preserve pages 001–023 as front matter/contents and begin letter 0001 at PDF 024;
4. stop exactly at PDF 025, leaving letter 0001 explicitly partial at that migration boundary;
5. validate the first canonical batch before proceeding to PDF 026 onward.

Until that first canonical batch is validated, the existing 110 bilingual records remain **legacy-complete but not yet certified under the Volume 46–49 canonical workflow**.
