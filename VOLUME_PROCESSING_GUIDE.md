# Master Processing Guide — Kalaignar’s Murasoli Letters, Volumes 1–48

This guide defines the reusable archival workflow for Volumes 1–48. **Volume 49 is the completed quality reference, not a source template.** Every earlier volume must be independently verified from its own scan.

Tamil transcription batching is governed by [`VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md), and [`TRANSCRIPTION_GUIDE.md`](TRANSCRIPTION_GUIDE.md) is also mandatory. If older wording or an example in this guide conflicts with the batching policy, **the batching policy takes precedence**.

The required end state for each volume is: page-faithful Tamil transcription, preserved contents and letter structure, scan-based audits, bilingual English records, bilingual alignment, editorial review, manifest/release records and explicit documentation of every source anomaly or source gap.

---

## 1. Source authority and fidelity

Use this authority order:

1. **Original PDF scan** — highest authority.
2. `pages/page-NNN.md` — canonical Tamil after visual review.
3. Contents and chapter records.
4. English translations.
5. Indexes, manifests and reports.

Never use OCR, contents pages, English translation, another edition or outside knowledge to silently correct the scan.

Every PDF page gets exactly one Markdown file, including covers, publication pages, contents, blanks, illustrations, advertisements and back cover.

Preserve visible wording, spelling, paragraph order, titles, quotations, lists, dates, figures, punctuation, signatures, closings, English/Latin text and page-boundary word splits. Do not modernise or regularise the source. Use `[தெளிவில்லை]` only for text that exists but cannot be read confidently.

`first-pass-reviewed` means the page has been visually compared with its scan once. It is not the later second visual verification.

---

## 2. Mandatory startup and volume intake

Before changing a new volume:

1. Read this guide, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md` and `TRANSCRIPTION_GUIDE.md` completely.
2. Inspect Volume 49 as the completed quality reference.
3. Inspect the most recently processed earlier volume only for current workflow conventions; do not copy its volume-specific facts.
4. Inspect repository state and continue existing target-volume work rather than creating duplicates.
5. Verify the volume number from the PDF scan itself.
6. Record the exact source filename, SHA-256, byte size and PDF page count.
7. Record publisher, edition and edition year where printed.
8. Identify provisional date and letter-number ranges.
9. Note blank, damaged, duplicated, rotated, illegible or missing source pages.
10. Check for a searchable text layer, but never treat it as authoritative.
11. Record the current `main` HEAD before write work.

Do not assume another volume’s letter count, page offset, date style, closing pattern, contents accuracy or scan completeness.

### Missing source pages / source-incomplete letters

If the printed sequence proves that material is genuinely absent from the **sole available source PDF**:

- do not reconstruct it from context;
- do not import wording from another edition unless the user separately approves a documented source-supplement workflow;
- preserve all surviving pages exactly;
- mark the affected letter `source-incomplete`, not falsely `complete`;
- record the missing printed page/gap where determinable;
- leave unavailable closing/signature/date information unguessed;
- record the defect in metadata, chapter record, progress and audit; and
- continue only when the next surviving boundary is visually clear.

A source-incomplete letter is different from a temporarily `partial` transcription. A volume can be release-ready **within the limits of the surviving source** when the gap is explicit and unreconstructed throughout the archive.

---

## 3. Required volume structure

```text
volumes/volume-NN/
  README.md
  metadata.yml
  AUDIT.md
  PROGRESS.md
  TRANSLATION_PLAN.md
  contents/index.md
  chapters/README.md
  chapters/NNNN-short-slug.md
  pages/page-001.md
  pages/page-002.md
  ...
  translations/en/
    README.md
    PROGRESS.md
    GLOSSARY.md
    EDITORIAL_CONSISTENCY_REVIEW.md
    textual-fidelity reports
    bilingual-alignment reports
    translation manifest
    final release report
    letters/NNNN-short-slug.md
```

Use `volume-01` through `volume-09` for single-digit volumes. Do not casually rename released paths.

Chapter and English filenames use the printed letter number plus a stable lowercase ASCII slug. Chapter files link to canonical page files and do **not** duplicate full Tamil text.

---

## 4. Metadata requirements

Use a machine-readable `metadata.yml`. Recommended fields include:

```yaml
volume: 48
title_ta: "கலைஞரின் கடிதங்கள் — தொகுதி 48"
author: "கலைஞர்"
date_from: null
date_to: null
letter_number_from: null
letter_number_to: null
letter_count: null
publisher: null
edition: null
edition_year: null
printed_pages: null
pdf_pages: null
source_file: null
source_sha256: null
source_size_bytes: null
transcription_page_range: null
transcription_status: "not-started"
recorded_letter_range: null
completed_letter_range: null
completed_letter_count: 0
partial_letter: null
source_incomplete_letters: []
source_incomplete_letter_count: 0
source_missing_printed_pages: []
audit_status: "not-started"
audit_date: null
second_visual_verification: "pending"
second_visual_verified_page_range: null
textual_fidelity_audit_reports: []
translation_status: "not-started"
translated_letter_range: null
translated_letter_count: 0
bilingual_alignment_status: "not-started"
english_release_status: "not-started"
source_observations: []
```

`recorded_letter_range` includes identified source-incomplete records. `completed_letter_range` contains normally completed letters. `partial_letter` is a temporary transcription boundary, not a permanent source gap.

Do not populate unsupported values merely for completeness.

---

## 5. Canonical page files

Recommended front matter:

```yaml
---
volume: 48
pdf_page: 1
printed_page: null
section: front-cover
letter_number: null
letter_date: null
letter_title_ta: null
transcription_status: first-pass-reviewed
source_note: null
---
```

Useful `section` values: `front-cover`, `front-matter`, `publisher-matter`, `contents`, `blank`, `letter`, `illustration`, `advertisement`, `back-cover`.

Describe non-text material factually in square brackets. Do not identify an uncertain person.

OCR is only a drafting/discrepancy aid. The scan controls every accepted reading.

---

## 6. Contents and chapter structure

Preserve the printed contents faithfully in `contents/index.md`.

For each letter record, track:

- letter number;
- contents title exactly as printed;
- printed date exactly as printed;
- ISO date where confidently determinable;
- printed start page;
- PDF start page;
- verified PDF end page;
- printed end page where determinable;
- chapter link; and
- source-incomplete status where applicable.

If the contents title differs from the actual letter-start title, preserve both in their own source contexts and document the discrepancy. Never force them to match.

Each chapter record contains metadata, ordered canonical-page links, source notes, previous/next navigation and later the English link.

---

## 7. Mandatory Tamil transcription batching

The former generic **10–20 page recommendation is retired**. Follow `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`.

### First commit

For a newly started volume, the first transcription commit is **exactly PDF pages 001–025**.

- Create `page-001.md` through `page-025.md`.
- Include every source page in that range.
- Visually compare all 25 files.
- Do not extend beyond PDF 25 just to finish a letter.
- Commit all applicable structural updates atomically.

### If PDF 25 interrupts a letter

Mark the letter `partial` and stop exactly at PDF 25. The next commit begins at PDF 26 and finishes that interrupted letter first. Do not add unrelated later letters merely to enlarge that completion commit.

### Regular iterations

After the initial batch and interrupted-letter completion, one normal iteration is:

**exactly five complete consecutive letters = one atomic commit.**

Start at the verified first page of letter 1; end at the verified closing/date page of letter 5; include no part of letter 6. A different batch size requires the documented exception/user-approval rules in the batching policy.

Every iteration updates all applicable page files, contents, chapter records/index, metadata, progress, audit, volume README and shared/root status where required.

### Pre-commit validation

Check:

- page-file continuity;
- visual scan comparison of every new/corrected page;
- no accidental duplicate canonical body;
- no `U+FFFD`;
- no unintended zero-width OCR residue;
- valid completed-range links;
- exact title/date/quotation/figure/English-string readings;
- verified closing/signature/date boundaries;
- preserved anomalies and source gaps; and
- exact next PDF page and next letter.

---

## 8. Full-volume Tamil audit

After every **available source PDF page** has a canonical file, run the full structural audit.

Verify source hash/page count, one file per PDF page, uninterrupted filenames, front matter, contents/letter counts, letter-number continuity or documented gaps, all surviving starts/ends, source-incomplete records, closing/date/signature pages where present, chapter/page-link continuity, duplicate bodies, invalid/replacement Unicode, large omissions, English/Latin passages, covers, blanks and back cover.

Automation may provide signals but does not replace visual verification.

Record separately:

1. iteration/batch audit;
2. full-volume structural audit;
3. second visual verification; and
4. textual-fidelity audit for translation.

Passing one does not imply the others.

---

## 9. Mandatory textual-fidelity gate before English

Do not begin English translation merely because transcription batches are complete.

Translation starts only after:

1. all available PDF pages are transcribed;
2. the full-volume Tamil structural audit passes; and
3. the relevant Tamil pages pass scan-based textual-fidelity review.

Before translating a batch, compare every available canonical page with the scan. Check titles, salutations/closings where present, paragraphs, quotations, names, dates, figures, lists, punctuation, intentional English, omissions, duplicates, OCR artefacts, anomalies and source gaps.

Record scan-proven corrections in the appropriate textual-fidelity report. A source-incomplete letter may be translated only for the surviving audited text; the missing continuation must remain explicit.

---

## 10. English translation

Each volume keeps an approved `TRANSLATION_PLAN.md` and follows the established Volume 49 quality standard.

Principles:

- preserve thought and argument order before literary elegance;
- translate every surviving substantive sentence/list/quotation/question;
- use clear non-literary contemporary English;
- preserve accusation, irony, repetition, sarcasm, rhetorical questions and attribution;
- retain `lakh`/`crore` unless project policy changes;
- do not add historical explanation as though it were source text;
- use minimal source notes; and
- never manufacture missing source material.

Required bilingual order:

1. English title;
2. approved translator’s note;
3. source/date/page metadata;
4. complete English translation of surviving text;
5. necessary source/anomaly notes;
6. complete available `Original Tamil — மூலத் தமிழ்`.

Normal status progression is `draft-translated` → `source-checked` → `reviewed` → `verified`. Do not skip documented bilingual comparison.

---

## 11. Source check and bilingual alignment

Before `source-checked`, verify every surviving Tamil paragraph has an English counterpart; all names/dates/figures/units/quotations/lists are represented; uncertainty and questions remain so; attribution is unchanged; no explanatory additions masquerade as source; source gaps remain explicit; and appended Tamil matches canonical pages.

Bilingual alignment is a separate meaning-level comparison against the available Tamil. Review argument sequence, substantive coverage, quotations, chronology, figures, lists, irony/repetition, political intensity, attribution and source anomalies/gaps.

Correct English unless a fresh scan comparison proves a Tamil transcription defect. Record alignment results and exact corrections in the appropriate report.

---

## 12. Volume-level English editorial review

After all eligible letters are aligned, review the volume as a single English work for title/index agreement, translator-note exactness, names, honorifics, places, transliteration, institutions, spelling, compounds, punctuation, dates/page ranges, glossary decisions and source-incomplete labels.

English editorial work must not alter political meaning, attribution, uncertainty, figures, quotations, rhetorical force, source-gap status or appended Tamil. Record the pass in `EDITORIAL_CONSISTENCY_REVIEW.md`.

---

## 13. Release artifacts and validation

Tamil/structural release requires complete source-page coverage, contents, one chapter per recorded letter, metadata, README, progress and audit.

English release requires one English record per recorded letter—including explicit source-incomplete records—plus English index/progress/glossary, fidelity reports, alignment reports, editorial review, manifest and final release report according to the approved reference/volume convention.

A release manifest must have exactly one record per released letter number, no duplicate letter numbers/file paths and explicit source-incomplete status where needed.

A volume may be marked editorial-release-complete only when:

- every source PDF page is represented;
- every surviving letter boundary is known or a source gap is documented;
- full Tamil audit is complete for surviving source;
- fidelity audits cover all available translated source pages;
- every letter translates and reproduces all surviving source text;
- source-incomplete letters preserve missing material as missing;
- source check and bilingual alignment pass;
- editorial review passes;
- manifest count reconciles with recorded letters;
- source-gap records agree across metadata/audit/manifest/report; and
- final/root status is updated.

---

## 14. Source anomalies versus source gaps

When printed text exists but appears wrong: **preserve it, document it, and explain cautiously if needed.** Never silently reconcile it with outside knowledge.

When material itself is absent: follow the source-incomplete rule in §2. Do not use `[தெளிவில்லை]` for a page that does not exist and do not treat a permanent source gap as a routine unfinished transcription.

Outside research may be recorded separately but never inserted as archival reconstruction without explicit approval.

---

## 15. Shared glossary

Each volume keeps a working glossary. Record Tamil term, approved English form, status (`approved`, `provisional`, `source-specific`), context and alternatives. Check completed volumes before introducing unnecessary variants, while allowing genuine context-specific differences.

---

## 16. Git and concurrency discipline

A declared transcription iteration should land as **one validated atomic commit**.

Before writing:

1. record current `main` HEAD;
2. prepare and validate the intended tree without moving `main` where possible;
3. recheck `main` immediately before final commit/ref update;
4. if `main` advanced, preserve the concurrent work and rebuild/rebase on the new HEAD;
5. create one atomic commit for the declared scope;
6. fast-forward `main` only with `force: false`;
7. compare parent → new HEAD and verify changed-file scope.

For a normal atomic iteration, expect one commit ahead and zero behind.

Never force-push routine work, overwrite concurrent volume changes, or allow temporary OCR/render/workflow/export files into final `main`.

Example transcription messages:

```text
Transcribe Volume 46 PDF pages 001-025
Complete Volume 46 letter NNNN — PDF pages 026-XXX
Transcribe Volume 46 letters NNNN-NNNN — PDF pages AAA-BBB
```

Use explicit messages for audit, translation, alignment and editorial release as well.

---

## 17. Parallel work

Parallel work is allowed only with unambiguous file ownership. Non-overlapping source/letter work can proceed when shared control files are coordinated.

Unsafe parallelism includes two workers editing the same page/control file, translation before required Tamil gates, chapter generation with unresolved boundaries, bilingual review of an actively edited translation, release while manifests/indexes are changing, or moving `main` from a stale parent and dropping concurrent commits.

Every batch declares exact page and letter scope.

---

## 18. Processing order and definition of done

For each volume, complete these gates:

1. source intake and metadata;
2. Tamil transcription under mandatory batching;
3. contents/chapter maintenance;
4. full-volume structural audit;
5. second visual/textual-fidelity verification;
6. English translation and source checking;
7. bilingual alignment;
8. volume-level English editorial review;
9. manifest/final release report;
10. root status update.

The 48-volume programme is done only when every source PDF page is represented, every recorded letter is indexed, all available Tamil has passed required audits, every normal letter has a verified bilingual record, every source-incomplete letter has a verified record containing all surviving text plus an explicit unreconstructed gap, every volume has a reconciled release package, and no required stage remains pending.

**Volume 49 remains the quality reference—not a template to copy blindly.** Preserve each earlier volume’s own printed structure, historical language, anomalies and source defects.
