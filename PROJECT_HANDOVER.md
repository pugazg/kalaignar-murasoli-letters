# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-16

This document is the current project-level handover for continuing the multi-volume Kalaignar Murasoli Letters archive in a new chat/window or with another worker.

It should be read together with:

1. [`VOLUME_PROCESSING_GUIDE.md`](VOLUME_PROCESSING_GUIDE.md)
2. [`VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md)
3. [`TRANSCRIPTION_GUIDE.md`](TRANSCRIPTION_GUIDE.md)
4. [`FUTURE_VOLUME_WORK_GUIDELINES.md`](FUTURE_VOLUME_WORK_GUIDELINES.md)
5. [`START_NEXT_MURASOLI_VOLUME_PROMPT.md`](START_NEXT_MURASOLI_VOLUME_PROMPT.md)

If these documents conflict, the mandatory repository processing/batching/transcription guides take precedence.

---

## 1. Project purpose

The repository preserves Kalaignar’s Murasoli letters as a page-faithful archival corpus and, where completed, as verified bilingual Tamil–English records.

The core archival rule is simple:

> **The source scan controls.**

OCR, contents pages, another edition, outside historical knowledge, English translations and inferred chronology can help identify questions, but none may silently override what is printed in the controlling scan.

The project is not a modernization or copy-editing exercise. Historical wording, source errors, numbering anomalies, punctuation, quoted material, political rhetoric, English text and missing-source conditions are preserved and documented.

---

## 2. Current completed reference volumes

### Volume 46

Volume 46 is fully complete through English release.

- Source PDF pages: **402**
- Canonical Tamil page coverage: **001–402 / 402**
- Actual source-letter records: **55**
- Source-letter PDF span: **24–400**
- English bilingual records: **55 / 55**
- Bilingual alignment: **55 / 55 verified**
- Volume-level English editorial review: complete
- Translation manifest: **55 rows**
- Editorial English word count recorded in release metadata: **90,510**
- Final English release report: complete

Volume 46 is especially important as a reference for preserving source anomalies:

- no source letter **3636**;
- two distinct consecutive source records both numbered **3637**;
- no source letters **3644–3646**.

Those numbers were **not repaired**. The translation manifest and bilingual records represent the actual source records rather than a normalized sequence.

Volume 46 also established several translation lessons now captured in `FUTURE_VOLUME_WORK_GUIDELINES.md`, including separate treatment of source-supplied English and a following Tamil rendering, preservation of `Udanpirappē`, thought-order fidelity, complete audited Tamil appendices, and a separate bilingual alignment gate.

### Volume 47

Volume 47’s English workflow is release-ready within the limits of the surviving source.

Its `translations/en/PROGRESS.md` records:

- **59 / 59** letter records draft-translated;
- **59 / 59** bilingual aligned;
- volume-level English editorial consistency complete;
- translation manifest/final release report complete;
- one explicit source-incomplete letter: **3681**, because printed page **252** is absent from the sole available source PDF.

Do not reconstruct that missing page unless new source evidence is supplied and the source-supplement workflow is explicitly approved.

### Volume 48

Volume 48 is an established completed English reference in the repository and may be consulted for current-format conventions.

### Volume 49

Volume 49 remains the principal completed quality reference implementation for structure and English release conventions.

Its final English release contains **53 / 53** verified bilingual records and a 53-row translation manifest. It is a reference implementation only; never copy its volume-specific facts into another volume.

---

## 3. Other repository trees

The repository also contains other volume directories, including legacy/nonuniform trees such as `volume-1` and later-numbered volume directories.

Do **not** infer their processing status or required structure merely from folder existence. Some older/later trees may use a different pipeline or layout.

For any target volume:

1. inspect its actual directory first;
2. read its own progress/audit/release files;
3. continue existing work where present;
4. do not rename released paths merely to make them look like Volume 46/49;
5. use the current processing guide for new work unless the target already has a documented approved workflow.

---

## 4. Mandatory new-volume startup

When a new PDF is attached with an expected volume number:

1. read all controlling root guides and this handover;
2. inspect the repository for an existing target volume;
3. inspect the actual PDF scan before trusting its filename;
4. confirm the volume number from the scan itself;
5. record source filename, hash/size/page count where available;
6. record printed publisher/edition/year only when supported by the scan;
7. identify provisional contents/date/letter ranges without assuming they are accurate;
8. note damaged, duplicated, blank, rotated, missing or illegible pages;
9. check for a text layer but never use it as final authority;
10. create/continue the target volume without uploading the PDF into the repository unless explicitly instructed.

If the target volume already exists, **continue it rather than creating a duplicate**.

---

## 5. Tamil transcription handoff rules

The mandatory batching policy is:

- first new-volume transcription commit = **PDF 001–025 exactly**;
- if PDF 25 interrupts a letter, next commit starts at PDF 26 and finishes that letter first;
- after that, default iteration = **five complete consecutive letters**;
- one canonical Markdown file per PDF page;
- do not include part of a sixth letter;
- every new/corrected page is visually compared with the scan before commit;
- update contents, chapters, metadata, progress, audit and README together with the batch.

Chapter records link to canonical pages. Do not duplicate the full canonical Tamil body into chapter files.

At every iteration end, record the exact next PDF page and next letter.

---

## 6. Distinguish four Tamil QA layers

Never merge these into one status:

1. iteration/batch audit;
2. full-volume Tamil structural audit;
3. second visual verification;
4. translation textual-fidelity audit.

English translation remains blocked until the required Tamil gates are complete.

A scan-proven correction made during later fidelity review must be documented. An English-review concern does not justify changing canonical Tamil unless the scan proves the Tamil transcription wrong.

---

## 7. Source anomalies and source-incomplete records

### Source anomaly

If printed text exists but seems wrong, preserve it and document it.

Examples include:

- duplicate letter number;
- skipped printed number;
- unusual/incorrect-looking printed date;
- contents title differing from actual letter-start title;
- malformed printed English;
- inconsistent figures or claims.

Do not silently reconcile these with outside sources.

### Source-incomplete record

If material is genuinely absent from the sole controlling PDF:

- preserve only surviving text;
- mark the record `source-incomplete`;
- do not invent the missing continuation;
- do not guess a closing/date/signature;
- carry the gap through metadata, audit, chapter, translation, manifest and release report.

Volume 47 letter 3681 is the reference example.

---

## 8. English translation handoff rules

The English edition is intended to preserve Kalaignar’s voice and thought structure, not merely convey a modern prose summary.

Preserve:

- argument sequence;
- rhetorical questions;
- accusation and political force;
- sarcasm/irony;
- repetition;
- quotations and attributed voices;
- names, figures, dates and units;
- idiom imagery where possible;
- source-supplied English;
- anomalies and source gaps.

Do not silently soften, compress, reorder, explain away or modernize the source.

The bilingual record must include the **complete available audited Tamil** under `Original Tamil — மூலத் தமிழ்`.

For a future volume without an already approved translation plan, use this default approach:

1. three-letter translation pilot;
2. bilingual review of the pilot;
3. lock volume-specific conventions;
4. draft five actual source records per batch;
5. run a separate bilingual alignment review;
6. correct English-only issues where required;
7. promote only after the alignment gate passes.

If the source numbering skips or duplicates numbers, batch by actual records in scan order. Never invent missing numbers.

---

## 9. Important Volume 46 translation lessons

These points should not be lost in future work:

- `Udanpirappē` is retained as Kalaignar’s characteristic political-familial address rather than flattened into “brother/comrade”.
- The standard `அன்புள்ள, மு.க.` closing is rendered consistently as `With affection, M.K.` where applicable.
- Source-supplied English remains verbatim when genuinely printed.
- If an English passage is printed and followed by a separate Tamil rendering/explanation, **both source passages are represented** in the bilingual record. Do not replace the Tamil passage with a summary of the English.
- Long quotations are translated from the audited canonical Tamil, not replaced by an outside edition or web version.
- `lakh`/`crore` and other source/public-language units are preserved under the locked convention unless a later project-wide policy changes them.
- Post-signature printed material remains part of the archival record.
- Editorial cleanup happens only after substantive bilingual alignment.

---

## 10. English release gate

After all letters are aligned:

1. run a full-volume editorial consistency review;
2. check stale translator-note wording and stale status fields;
3. verify title/frontmatter/index agreement;
4. verify names, transliteration, institutional terms and spelling consistency;
5. verify all English records retain the complete available Tamil appendix;
6. build a machine-readable translation manifest;
7. validate manifest count against actual source records;
8. create the final English release report;
9. synchronize metadata, README, progress and root status;
10. remove temporary workflows/scripts used only for one-time bulk operations.

Do not mark a volume complete based only on a summary file. Verify the physical files and release inventory.

---

## 11. Git/concurrency discipline

The repository is used for direct archival work on `main`.

Rules:

- never force-push routine work;
- record/recheck `main` before write operations when concurrent work is possible;
- preserve changes from other volume workstreams;
- keep iteration scope explicit;
- prefer atomic commits for declared batches;
- use clear commit messages naming volume, stage and range;
- remove temporary workflow/export/test files after successful use;
- verify the resulting repository tree after bulk status operations.

---

## 12. What “Proceed with next activity” means

When the user says **“Proceed with next activity”** or **“Proceed with next iteration”**:

- inspect the current target volume status;
- identify the next already-defined gate/batch;
- execute it directly;
- do not ask the user to choose among routine next steps;
- do not stop after each letter when the active plan calls for a multi-letter batch;
- report what was completed, source/page scope, QA result, commit SHA where applicable, and the exact next activity.

Ask a question only when a real source ambiguity, missing attachment, repository conflict or policy decision prevents safe continuation.

---

## 13. Definition of a clean handoff at any interruption

Before ending a long-running volume session, ensure the repository itself contains enough state for continuation:

- exact completed page range;
- exact completed/partial letter range;
- source anomalies/gaps discovered so far;
- current audit status;
- current translation/alignment/editorial status;
- exact next PDF page and letter;
- current applicable conventions;
- no uncommitted conceptual dependency known only to the chat.

`PROGRESS.md`, `AUDIT.md`, metadata and batch/review reports should carry the durable state. The chat should never be the sole place where critical archival decisions exist.

---

## 14. Recommended continuation command

For a completely new target volume, use [`START_NEXT_MURASOLI_VOLUME_PROMPT.md`](START_NEXT_MURASOLI_VOLUME_PROMPT.md).

For an already-started volume, use the same prompt but explicitly tell the worker to inspect existing target-volume files and **continue from the recorded boundary rather than restarting**.
