# Volume 1 — Canonical Migration Guidelines

This document is **Volume 1 specific**. It supplements, but does not replace, the repository-level `VOLUME_PROCESSING_GUIDE.md`, `TRANSCRIPTION_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, `FUTURE_VOLUME_WORK_GUIDELINES.md`, and `PROJECT_HANDOVER.md`.

If this document conflicts with the generic batching cadence, the Volume 1-specific rules below control for `volumes/volume-01/`.

## 1. Controlling source

The supplied **Volume 1 scan (`Vol1.pdf`) is the controlling source** for the canonical migration.

Do not rely on:

- the filename alone;
- OCR as authority;
- the legacy `volumes/volume-1/` text as authority;
- printed contents titles when the actual letter heading differs;
- assumptions based on nearby volumes.

The scan must be inspected directly for every page migrated.

## 2. Source fidelity

Preserve source-supported Tamil exactly. Do not silently modernise, correct, normalise, reconstruct, regularise or improve Kalaignar's text.

Preserve, when supported by the scan:

- historical spelling;
- punctuation and quotation marks;
- hyphenation and dash usage;
- wording and repetitions;
- rhetorical sequences;
- names and labels;
- dates and numbers;
- unusual grammar;
- sign-off forms;
- source-shortened dates;
- title variants between contents pages and actual letter headings.

Distinguish printed text from stamps, handwriting, damage, show-through and other non-authorial marks.

## 3. Canonical versus legacy trees

The canonical migration lives in:

`volumes/volume-01/`

The earlier corpus remains in:

`volumes/volume-1/`

The legacy tree is provenance and migration assistance only. **Do not delete, rewrite or silently replace it.** Existing source-corrected Tamil and English may help locate or compare text, but every canonical Tamil page must be reconciled against the visible scan.

English migration remains blocked until the canonical Tamil volume and required Tamil audit gates are complete.

## 4. Volume 1 batching rule

For **Volume 1 alone**, each regular migration iteration must process **10 complete consecutive letters**.

Current rule:

1. Begin at the first PDF page of the next unprocessed letter.
2. Process exactly 10 complete consecutive letters.
3. Visually verify every page and every letter start/end boundary.
4. Finish the tenth letter through its actual closing/sign-off/date page.
5. Inspect the next PDF page only far enough to confirm the next letter boundary.
6. Do **not** commit any text belonging to the eleventh letter.
7. A final residue smaller than 10 letters is allowed only when the volume itself has fewer than 10 remaining letters.

This 10-letter rule overrides the repository's normal five-letter cadence only for Volume 1.

## 5. Page files

Create one canonical Markdown file for every migrated PDF page:

`volumes/volume-01/pages/page-NNN.md`

Each page file should carry front matter consistent with the existing Volume 1 pages, including where applicable:

- `volume`
- `pdf_page`
- `printed_page`
- `section`
- `letter_number`
- `letter_date`
- `letter_title_ta`
- `transcription_status`
- `source_note`

The page file must contain only text visible on that PDF page. Do not pull text forward from the next PDF page merely to complete a sentence or letter.

## 6. Letter chapter records

For each newly completed letter, create a chapter record under:

`volumes/volume-01/chapters/`

Follow the existing records for letters 0001–0016. Record:

- letter number;
- scan-supported title;
- ISO date;
- complete status;
- PDF page start/end;
- printed page start/end when determinable;
- link to the preserved legacy bilingual record where applicable;
- list of canonical page files;
- verified closing/sign-off/date boundary.

The actual letter-heading page controls the canonical title if it differs from the printed contents.

## 7. Boundary verification

Every iteration must directly verify:

- the first page of every letter;
- the heading/title;
- the salutation where present;
- the final body page;
- the sign-off form;
- the printed date;
- the first page of the following letter only to establish the stop boundary.

Do not infer a boundary solely from the contents page or legacy chapter grouping.

## 8. Known Volume 1 source notes

Preserve and continue documenting source anomalies rather than correcting them silently.

Known examples:

- PDF 039 prints page number **38** and PDF 040 prints **40**; the text is continuous, so printed page number **39** is treated as a source pagination anomaly rather than missing text.
- Letter 0008 prints the date in shortened form `(31-10-68)` on its closing page; page-level transcription preserves that source form.
- Actual heading forms may differ from printed contents entries; the actual letter heading controls canonical metadata.

Add further anomalies to `AUDIT.md` as they are discovered.

## 9. Required tracking updates after every 10-letter iteration

After completing an iteration, synchronise at minimum:

- `volumes/volume-01/chapters/README.md`
- `volumes/volume-01/metadata.yml`
- `volumes/volume-01/README.md`
- `volumes/volume-01/PROGRESS.md`
- `volumes/volume-01/AUDIT.md`
- repository root `README.md` Volume 01 status row, when the progress figures change.

Tracking must state the exact PDF boundary, completed letter range, completed-letter count and exact next task.

## 10. Do not start later gates early

Until all 401 canonical PDF pages have been migrated, do not begin:

- full-volume Tamil structural audit;
- second visual/textual-fidelity verification;
- canonical English migration/source checking;
- bilingual alignment;
- editorial consistency review;
- translation manifest;
- final release report.

The current page migration is a **first-pass visual transcription gate**, not final textual certification.

## 11. Commit discipline

Work directly on `main` unless the user explicitly instructs otherwise.

Prefer one coherent atomic commit per completed 10-letter migration iteration. Before reporting completion:

- confirm `main` points to the intended commit;
- inspect the compare/diff for accidental files;
- confirm no PDF was added;
- confirm no legacy bilingual file was modified;
- confirm the next-letter text was not accidentally included.

## 12. Current continuation rule

At the time this guideline was created, canonical coverage is **PDF 001–089 / 401** and letters **0001–0016** are complete.

The next regular iteration must process **letters 0017–0026**, beginning at **PDF 090**, and stop before letter 0027.
