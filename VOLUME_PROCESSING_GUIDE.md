# Master Processing Guide — Kalaignar’s Murasoli Letters, Volumes 1–48

This guide defines the reusable workflow for processing the remaining **48 PDF volumes** in this repository. It is based on the completed Volume 49 workflow, but it must not assume that another volume has the same page structure, letter count, date pattern, typography or source quality.

The objective is to produce, for every volume:

1. a page-faithful Tamil transcription;
2. a preserved contents/index and letter register;
3. traceable letter-level navigation;
4. documented scan-to-text verification;
5. complete bilingual Tamil–English letter files;
6. bilingual alignment and editorial review records; and
7. a release manifest and final volume report.

---

## 1. Non-negotiable principles

### 1.1 Source hierarchy

Use this authority order throughout the project:

1. **Original PDF scan** — highest authority.
2. **`pages/page-NNN.md` files** — canonical Tamil transcription after review.
3. **Contents and chapter files** — structural records derived from the canonical pages.
4. **English translation files** — interpretive layer; never authoritative over the Tamil.
5. **Indexes, manifests and reports** — derived metadata.

When two derived files disagree, resolve the conflict against the PDF scan and canonical page files. Never use an English translation to “correct” the Tamil.

### 1.2 One PDF page, one Markdown file

Every PDF page must have exactly one corresponding Markdown file, including:

- covers;
- title and copyright pages;
- publisher material;
- contents pages;
- blank pages;
- letter pages;
- photographs or illustrations;
- advertisements; and
- the back cover.

A blank or image-only page is still a page and must not be skipped.

### 1.3 No silent correction

Do not silently correct:

- spelling;
- punctuation;
- dates;
- names;
- figures;
- malformed English strings;
- inconsistent title forms; or
- apparent factual errors.

Preserve what is visibly printed. Document an anomaly with `source_note`, a page note or a letter-specific note. Corrections to the canonical transcription are allowed only when a visual comparison proves that the Markdown differs from the scan.

### 1.4 No guessing

When text cannot be read confidently, use a visible marker such as:

```text
[தெளிவில்லை]
```

For partially readable text, retain the readable portion and mark only the uncertain section. Do not invent a likely word from context.

### 1.5 Tamil remains authoritative

Every English letter must reproduce the complete audited Tamil letter under:

```markdown
## Original Tamil — மூலத் தமிழ்
```

The Tamil section is not a summary or selected quotation. It must be assembled from the canonical page files in PDF order.

---

## 2. Volume intake

Process one PDF as one independently auditable volume.

Before transcription begins:

1. Confirm the intended volume number from the scan itself.
2. Record the exact source filename.
3. Calculate and record the SHA-256 hash.
4. Record the source byte size and PDF page count.
5. Identify the publisher, edition and edition year where printed.
6. Identify the visible date range and letter-number range, but mark them provisional until the contents and all letter starts are checked.
7. Note damaged, missing, duplicated, rotated or illegible scan pages.
8. Check whether the PDF has searchable text, but do not treat embedded text or OCR as authoritative.

Do not assume that:

- each volume contains the same number of letters;
- all letter numbers are consecutive;
- printed and PDF page numbers have a constant offset;
- every letter has the standard closing;
- the contents pages are error-free; or
- the volume date range is internally consistent.

---

## 3. Required directory structure

Create a separate directory for every volume:

```text
volumes/
  volume-NN/
    README.md
    metadata.yml
    AUDIT.md
    PROGRESS.md
    TRANSLATION_PLAN.md
    contents/
      index.md
    chapters/
      README.md
      NNNN-short-slug.md
    pages/
      page-001.md
      page-002.md
      ...
    translations/
      en/
        README.md
        PROGRESS.md
        GLOSSARY.md
        EDITORIAL_CONSISTENCY_REVIEW.md
        RELEASE_REPORT.md
        TRANSLATION_MANIFEST.csv
        TEXTUAL_FIDELITY_AUDIT_*.md
        BILINGUAL_ALIGNMENT_REVIEW_*.md
        letters/
          NNNN-short-slug.md
```

Use `volume-01` through `volume-09` if zero-padded volume names are adopted. Once the repository chooses a volume-directory convention, use it consistently and do not rename released paths casually.

---

## 4. Naming conventions

### 4.1 Page files

Use zero-padded PDF page numbers:

```text
page-001.md
page-002.md
page-010.md
page-100.md
```

Choose padding wide enough for the volume’s total PDF page count. For this collection, three digits should normally be sufficient.

### 4.2 Chapter and translation files

Use the printed letter number followed by a stable lowercase English slug:

```text
3764-what-was-left-out-of-the-list-of-achievements.md
```

Rules:

- use the printed letter number, not an invented sequence;
- use ASCII hyphens in filenames;
- omit punctuation and diacritics from the slug;
- do not rename a released slug merely to improve style;
- prevent duplicate slugs; and
- preserve the same slug between the chapter and English letter where practical.

### 4.3 Batch reports

Use explicit letter ranges:

```text
TEXTUAL_FIDELITY_AUDIT_1201_1205.md
BILINGUAL_ALIGNMENT_REVIEW_1201_1205.md
```

A single unusually long letter may receive its own report.

---

## 5. `metadata.yml` requirements

Every volume must have a machine-readable metadata file. Use this template and add fields only when needed:

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
audit_status: "not-started"
audit_date: null
second_visual_verification: "pending"
translation_status: "not-started"
bilingual_alignment_status: "not-started"
english_release_status: "not-started"
```

Update metadata when a stage is actually completed. Do not mark the volume complete because only the first batch is complete.

Recommended controlled values:

- `not-started`
- `in-progress`
- `first-pass-complete`
- `full-volume-audit-complete`
- `source-checked`
- `verified`
- `editorial-release-complete`

---

## 6. Page transcription

### 6.1 Recommended page front matter

```yaml
---
volume: 48
pdf_page: 1
printed_page: null
section: cover
letter_number: null
letter_date: null
letter_title_ta: null
transcription_status: first-pass-reviewed
source_note: null
---
```

Recommended `section` values:

- `front-cover`
- `front-matter`
- `publisher-matter`
- `contents`
- `blank`
- `letter`
- `illustration`
- `advertisement`
- `back-cover`

For a letter page, populate the letter number and date when known. For a page spanning two letters, record the primary section in front matter and describe the boundary visibly in the body or notes.

### 6.2 Transcription rules

Preserve as far as the scan allows:

- title wording and line order;
- paragraph order;
- quotations;
- list order and numbering;
- names and initials;
- dates and figures;
- rupee values and units;
- intentional English text;
- punctuation that affects meaning;
- signatures, closings and dates; and
- visible separators such as `***`.

Do not modernise Tamil spelling or regularise spacing merely for readability.

### 6.3 Non-text content

Describe non-text content in square brackets:

```text
[படம்: கலைஞர் பொதுக்கூட்டத்தில் பேசும் புகைப்படம்]
[முத்திரை]
[கையொப்பம்]
[வெற்றுப் பக்கம்]
```

Descriptions must be factual and limited to what is visible. Do not identify an uncertain person.

### 6.4 OCR policy

OCR is a drafting and discrepancy-detection aid only.

Allowed uses:

- obtaining a first-pass text layer;
- finding likely omissions;
- comparing Latin or English strings;
- prioritising pages for manual review; and
- detecting duplicated or unexpectedly short pages.

Not allowed:

- accepting OCR without visual comparison;
- replacing visibly printed text because OCR suggests a more plausible word;
- using OCR confidence as proof of correctness; or
- repeatedly OCRing a page instead of inspecting the scan.

---

## 7. Contents and letter register

Create `contents/index.md` as a faithful structural record, not merely a convenient generated list.

For every letter record:

- letter number;
- Tamil title as printed;
- printed date as printed;
- normalised ISO date in metadata where reasonably determinable;
- printed starting page;
- PDF starting page;
- PDF ending page after boundary verification; and
- chapter link.

Preserve contents-page order even when an apparent error exists. Document differences between the printed contents and the actual letter page.

The contents register and chapter metadata must agree. Any mismatch blocks volume release.

---

## 8. Chapter records

Create one chapter file per letter. Chapter records are navigation and metadata files; the canonical Tamil remains in `pages/`.

A chapter record should include:

```yaml
---
volume: 48
letter_number: 3700
title_ta: "..."
date_printed: "..."
date_iso: null
pdf_page_start: 100
pdf_page_end: 107
printed_page_start: 98
printed_page_end: 105
status: complete
---
```

Then include:

- ordered links to every canonical page;
- previous and next letter navigation;
- source anomalies affecting the letter; and
- a link to the English translation after it exists.

Do not manually copy the full Tamil letter into chapter records. Duplication creates drift.

---

## 9. Transcription batches and checkpoints

Recommended transcription batch size:

- **10–20 PDF pages** during initial OCR/transcription; or
- one complete letter when a letter is unusually long or complex.

At the end of every batch:

1. verify all expected page filenames exist;
2. compare each page with its scan;
3. check page-number continuity;
4. check that no body is duplicated;
5. update the volume progress file;
6. update letter boundaries if discovered; and
7. commit the batch with an explicit page range.

Do not leave a letter silently incomplete at a batch boundary. Mark continuation clearly.

---

## 10. Full-volume Tamil audit

After every PDF page is transcribed, create `AUDIT.md` and run a full structural audit before translation is declared ready.

The audit must verify:

- PDF hash and page count;
- one Markdown file for every PDF page;
- uninterrupted page filenames;
- front-matter validity;
- contents rows and letter count;
- letter-number continuity or documented gaps;
- every letter start and end;
- title, date, closing and signature pages against scans;
- chapter count and page-link continuity;
- duplicate files and duplicate bodies;
- invalid or replacement Unicode;
- missing large passages;
- Latin and English text pages; and
- covers, blanks and non-letter pages.

Useful automated signals include text length, image ink density, duplicate hashes and fresh OCR comparison, but the report must not imply that automation replaces human visual verification.

The audit must list:

- checks performed;
- counts obtained;
- anomalies preserved;
- corrections made to the transcription; and
- verification still pending.

A full-volume structural audit is not the same as a character-by-character second visual verification. Record those statuses separately.

---

## 11. Mandatory textual-fidelity audit before translation

Before translating a letter batch, visually compare every corresponding canonical Tamil page against the PDF scan.

Recommended translation/audit batch size:

- **five letters**, or
- **25–40 PDF pages**, whichever is smaller.

Use a smaller batch for dense tables, legal quotations, long lists or poor scans.

The audit must check:

- letter number and title;
- salutation and closing;
- page and paragraph boundaries;
- every quoted passage;
- names, dates and figures;
- list items;
- punctuation affecting meaning;
- intentional English expressions;
- omissions, duplicated text and OCR artefacts; and
- printed anomalies.

Correct scan-proven transcription defects before drafting English. Record each correction in `TEXTUAL_FIDELITY_AUDIT_<range>.md`.

Set the translation front matter to:

```yaml
source_textual_fidelity_audit: visual-scan-verified
```

only after the relevant pages pass.

---

## 12. English translation workflow

Each volume should have its own `TRANSLATION_PLAN.md`, normally copied from the approved project plan and adjusted only for volume-specific issues.

### 12.1 Pilot and style lock

For the first untranslated volume after Volume 49, translate three representative letters before bulk work:

- one ordinary political letter;
- one list-, figure- or quotation-heavy letter; and
- one rhetorically or culturally difficult letter.

Review the pilot for titles, address, closing, terminology, quotations, notes and rhetorical force. Update the shared glossary before continuing.

Later volumes may reuse the locked style, but new historical terms or older orthography must still be reviewed.

### 12.2 Translation principles

- Preserve thought and argument order before literary elegance.
- Translate every substantive sentence, list item, quotation and question.
- Use clear contemporary English without converting the letters into academic prose.
- Preserve accusation, irony, repetition, sarcasm and emotional emphasis.
- Keep attribution explicit; do not turn a reported allegation into an established fact.
- Retain `lakh` and `crore` unless the project later adopts a documented global conversion policy.
- Use established English forms for names and institutions where certain; otherwise transliterate.
- Do not add historical explanation inside the body unless it is present in the source.
- Use minimal letter-specific notes.
- Document source anomalies instead of fixing them silently.

### 12.3 Mandatory translator’s note

Use the approved note consistently below every English title. The current approved wording is maintained in each volume’s `TRANSLATION_PLAN.md`; it must not drift between letters.

### 12.4 Required bilingual letter order

1. English title
2. mandatory translator’s note
3. source links, date and page range
4. complete English translation
5. necessary letter-specific notes
6. complete `Original Tamil — மூலத் தமிழ்`

### 12.5 Translation front matter

Recommended fields:

```yaml
---
volume: 48
letter_number: 3700
title_en: "..."
title_ta: "..."
date: 2013-01-01
source_pdf_page_start: 100
source_pdf_page_end: 107
source_printed_page_start: 98
source_printed_page_end: 105
translation_status: draft-translated
bilingual_alignment_status: pending
source_textual_fidelity_audit: visual-scan-verified
---
```

Status progression:

1. `draft-translated`
2. `source-checked`
3. `reviewed`
4. `verified`

Do not skip directly from draft to verified without a documented bilingual comparison.

---

## 13. Source check after translation

Before a translation is marked `source-checked`, verify:

- every Tamil paragraph has an English counterpart;
- title, salutation, closing and date are represented;
- every name, date, figure and unit is present;
- quotations remain attributed and visibly quoted;
- list order is complete;
- uncertainty remains uncertainty;
- rhetorical questions remain questions;
- responsibility is not shifted to a different person or institution;
- no explanatory sentence has been added as though it were in the source; and
- the complete Tamil section matches the canonical page files.

Update the English index and progress tracker after each batch.

---

## 14. Bilingual alignment review

Bilingual alignment is a separate final meaning-level review. It must compare the English directly with the complete Tamil, not merely rely on the earlier translation process.

For each letter verify:

- paragraph and argument sequence;
- complete substantive coverage;
- quotations and reported speech;
- names, dates, counts, money and percentages;
- legal and institutional chronology;
- lists and enumerations;
- irony, wordplay and repeated phrases;
- political intensity and attribution; and
- source-specific anomalies.

Correct only the English unless a fresh scan comparison proves a Tamil transcription defect.

Create `BILINGUAL_ALIGNMENT_REVIEW_<range>.md` with:

- scope and page range;
- approximate English word count;
- result by letter;
- exact corrections made;
- preserved anomalies;
- canonical Tamil change count; and
- next batch.

A letter becomes `verified` only after this review passes.

---

## 15. Volume-level English editorial consistency pass

After all letters in a volume are verified, review the volume as a single English work.

Check:

- title and index agreement;
- front-matter consistency;
- translator’s note exactness;
- names, initials and honorifics;
- place-name spelling;
- transliteration;
- institutions and party terminology;
- British/Indian English spelling;
- compound words and hyphenation;
- title apostrophes, quotation marks and dashes;
- page ranges and dates;
- glossary decisions; and
- byte-for-byte preservation of appended Tamil sections.

This pass may improve spelling and consistency. It must not alter political meaning, responsibility, attribution, uncertainty, figures, quotations or rhetorical strength.

Record all changes in `EDITORIAL_CONSISTENCY_REVIEW.md`.

---

## 16. Release artifacts

A volume is not released merely because every English letter exists. The following artifacts are required:

### Tamil and structural release

- complete `pages/` directory;
- `contents/index.md`;
- one chapter record per letter;
- `metadata.yml`;
- volume `README.md`;
- `PROGRESS.md`; and
- `AUDIT.md`.

### English release

- complete `translations/en/letters/` directory;
- English `README.md` index;
- English `PROGRESS.md`;
- `GLOSSARY.md`;
- all textual-fidelity audit reports;
- all bilingual alignment reports;
- `EDITORIAL_CONSISTENCY_REVIEW.md`;
- `TRANSLATION_MANIFEST.csv`; and
- `RELEASE_REPORT.md`.

### Required manifest columns

```csv
letter_number,date,english_title,tamil_title,source_pdf_pages,source_printed_pages,translation_status,bilingual_alignment_status,source_textual_fidelity_audit,english_word_count,file,bilingual_alignment_report
```

The manifest must contain exactly one row per released letter, with no duplicate letter numbers or file paths.

---

## 17. Release validation gate

A volume may be marked `editorial-release-complete` only when all checks below pass.

### Source and transcription

- [ ] Source filename, hash, size and page count recorded
- [ ] Every PDF page has one Markdown file
- [ ] Page filenames are continuous
- [ ] Every page has valid front matter
- [ ] Covers, blanks and back cover are represented
- [ ] Contents pages are transcribed
- [ ] Every letter boundary is known
- [ ] One chapter record exists per letter
- [ ] Full-volume Tamil audit is complete

### Translation

- [ ] Every translation batch has a scan-fidelity audit
- [ ] Every letter contains the mandatory translator’s note
- [ ] Every letter includes complete English
- [ ] Every letter includes complete canonical Tamil
- [ ] Every letter is source-checked
- [ ] Every letter passes bilingual alignment
- [ ] Every letter is marked `verified`

### Editorial release

- [ ] English titles match index and front matter
- [ ] Names and recurring terms follow the glossary
- [ ] Tamil sections are unchanged by editorial work
- [ ] Manifest row count equals letter count
- [ ] Progress files show no unfinished required stage
- [ ] Editorial consistency report exists
- [ ] Final release report exists
- [ ] Root repository status is updated

Any failed item keeps the volume in progress.

---

## 18. Source-anomaly policy

Use this three-part method whenever the source appears wrong:

1. **Preserve** the visibly printed form in the canonical Tamil.
2. **Document** the anomaly and where it appears.
3. **Explain cautiously** in English only when the anomaly affects comprehension.

Do not silently reconcile an anomaly using outside knowledge.

Examples include:

- a date inconsistent with the volume chronology;
- different spellings of the same name within one letter;
- conflicting counts in separate paragraphs;
- a malformed English phrase printed in the source;
- an unusual closing; or
- a contents-page title differing from the letter title page.

Outside research may be recorded separately, but it must not be inserted into the archival transcription as a correction.

---

## 19. Shared glossary policy

Each volume keeps a working `GLOSSARY.md`, but recurring decisions should remain compatible across the collection.

For every glossary entry record:

- Tamil term;
- approved English form;
- status (`approved`, `provisional`, `source-specific`);
- scope or context; and
- notes on alternatives.

Before introducing a new English form, search completed volumes. Do not create unnecessary variants for the same institution, honorific, place or movement term.

Do not force identical English where the Tamil meaning genuinely changes by context.

---

## 20. Git and repository hygiene

### 20.1 Branching

Recommended branch names:

```text
volume-48-intake
volume-48-pages-001-020
volume-48-letters-3700-3704
volume-48-translation-3700-3704
volume-48-alignment-3700-3704
volume-48-editorial-release
```

One branch should have one clear purpose. Do not let temporary automation or export files enter the final `main` tree.

### 20.2 Commit messages

Use explicit scope:

```text
Transcribe Volume 48 PDF pages 001-020
Complete Volume 48 letters 3700-3704
Audit Volume 48 Tamil pages 100-136
Translate Volume 48 letters 3700-3704
Verify Volume 48 translations 3700-3704
Complete Volume 48 English editorial release
```

A commit message should state what was verified, not merely “update files”.

### 20.3 Safe writes

- Never have two processes update the same file simultaneously.
- Re-fetch a file before replacing it through the contents API.
- Validate generated indexes and manifests before commit.
- Avoid force-pushing `main`.
- Delete temporary branches after their work is safely integrated, or retain them only under a documented repository policy.
- Do not rewrite released history merely to tidy batch commits.

### 20.4 Temporary automation

A temporary workflow may export or validate a large batch, but it must:

- have the minimum required permissions;
- validate the intended branch and source commit;
- exclude itself and temporary scripts from the final release commit;
- fail closed when counts or invariants do not match; and
- be removed when the task is complete.

---

## 21. Parallel-work rules

Parallel work is allowed only when file ownership is unambiguous.

Safe parallelism:

- different non-overlapping PDF page ranges;
- different non-overlapping letter batches after canonical pages are stable;
- audit of one batch while transcription continues on a later batch; and
- translation of one audited batch while a later batch is being audited.

Unsafe parallelism:

- two workers editing the same page files;
- translation before scan audit;
- chapter generation while letter boundaries remain unresolved;
- bilingual review against an English file still being edited; or
- volume release while manifest and index counts are changing.

Every batch must declare its exact page and letter range.

---

## 22. Recommended processing order for Volumes 1–48

Unless source availability or scan quality requires another order, process volumes numerically:

```text
Volume 01 → Volume 02 → ... → Volume 48
```

For each volume, complete these gates in order:

1. source intake and metadata;
2. full page inventory;
3. page-by-page Tamil transcription;
4. contents and chapter register;
5. full-volume structural audit;
6. batch textual-fidelity audits;
7. English translation and source checking;
8. bilingual alignment verification;
9. volume-level English editorial review; and
10. manifest, release report and root status update.

A later volume may begin intake while an earlier volume is in translation, but no volume should be called complete until all ten gates pass.

---

## 23. Definition of done for the 48-volume programme

The remaining programme is complete only when, for every volume from 1 through 48:

- every PDF page is represented;
- every letter is structurally indexed;
- every canonical Tamil page has passed the required audits;
- every letter has a complete verified bilingual file;
- every volume has an editorial release package;
- every volume manifest reconciles with its contents and chapter records;
- all source anomalies are documented;
- root-level status records identify the final release commit; and
- no required stage remains marked pending.

Volume 49 is the reference implementation, not a template to copy blindly. Reuse its controls, reports and release discipline while allowing each earlier volume’s printed structure and historical language to remain source-specific.
