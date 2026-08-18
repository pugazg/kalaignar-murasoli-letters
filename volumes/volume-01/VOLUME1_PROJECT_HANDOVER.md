# Volume 1 — Project Handover

## Repository and source

Work on `pugazg/kalaignar-murasoli-letters` `main`. Active canonical tree: `volumes/volume-01/`. Preserve `volumes/volume-1/` unchanged.

Controlling source: `Vol1.pdf`, SHA-256 `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`, 244,892,260 bytes, 401 PDF pages, first edition 2022, Seethai Pathippagam, no usable text layer. Do not commit the PDF.

## Mandatory startup in a new window

Read the repository processing/transcription/batching/future-work guides, root `PROJECT_HANDOVER.md`, Volume 1 migration/project/alignment handovers, Volume 1 README/PROGRESS/AUDIT/metadata/chapter README, all English `SOURCE_CHECK_*.md` reports, English README/PROGRESS/GLOSSARY, all alignment reports/manifest, and `translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`. Then inspect current `main`; repository state is authoritative.

## Completed gates — do not restart

- Tamil canonical migration: **401 / 401 PDF pages**, **110 / 110 letters**
- Tamil structural audit: **PASS**
- full visual/textual-fidelity verification: **PASS — 401 / 401**
- second-pass corrections: **159 pages / 274 spans**
- canonical English migration/source check: **110 / 110**
- every canonical English record includes complete canonical Tamil
- bilingual alignment: **110 / 110 PASS**
- volume-level English editorial consistency: **110 / 110 PASS**
- legacy bilingual records: **110 / 110**, preserved unchanged

## English QA closure so far

The alignment gate completed in eleven ten-letter batches with **4** cumulative English prose/quotation corrections: **0014, 0043, 0058 and 0059**. The editorial consistency pass required **0** additional canonical English prose/quotation corrections and **0** canonical Tamil edits.

The editorial report is [`translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`](translations/en/EDITORIAL_CONSISTENCY_REVIEW.md). It documents the inherited presentation phases: 0001–0040 early schema with shared standard note; 0041–0060 compact migration schema without record-local note blocks; 0061–0110 later schema with letter-specific notes. Dedicated gate reports are authoritative; canonical records are not mass-rewritten solely to update historical workflow fields.

Important controls that remain untouchable include 0028 printed date 28-12-1968; 0048 printed `சென்னை. / 10.10.1972`; 0063 undated status; 0070 verbatim source-printed English judicial quotation; 0109 contents `அவள் ஒரு தொடற்கதை!` versus actual heading `அவள் ஒரு தொடர்கதை!` plus opaque `நமப்பார்வதி பதேக்கள்!`; and 0110's complete 1949 quotation through PDF 400.

## Active gate — final release artifacts

Verified/release-certified records remain **0 / 110** until the dedicated release gate is completed.

The exact next activity is to prepare the **final translation manifest and English release report**:

1. inventory exactly one canonical English record per letter **0001–0110**;
2. validate unique letter IDs and unique canonical file paths;
3. validate title, date, PDF/printed-page range and source path against the canonical records/chapter register;
4. verify complete `Original Tamil — மூலத் தமிழ்` appendices;
5. record source-check **110 / 110**, alignment **110 / 110 PASS**, editorial review **110 / 110 PASS**, and the four alignment corrections;
6. preserve every source anomaly and the PDF 401 non-letter boundary;
7. create the final English release report and synchronize Volume 1/root status.

Use [`translations/en/EDITORIAL_RELEASE_CHECKLIST.md`](translations/en/EDITORIAL_RELEASE_CHECKLIST.md) as the release checklist. Do not modify the legacy tree or bulk-rewrite canonical files solely for status nomenclature.