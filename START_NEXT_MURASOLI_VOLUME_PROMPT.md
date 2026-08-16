# Reusable Prompt — Start or Continue the Next Murasoli Letters Volume

Copy the prompt below into a new chat/window and replace the bracketed values.

---

## Prompt

Continue the **Kalaignar Murasoli Letters multi-volume archival project**.

**GitHub repository:**  
`https://github.com/pugazg/kalaignar-murasoli-letters`

**Branch:**  
`main`

**Attached controlling source PDF:**  
`[SOURCE_PDF_FILENAME]`

**Expected volume:**  
`[VOLUME_NUMBER]`

Use the GitHub connector and work directly in the existing repository.

### MANDATORY STARTUP

Before making any change, read these repository documents completely and follow them:

1. `VOLUME_PROCESSING_GUIDE.md`
2. `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
3. `TRANSCRIPTION_GUIDE.md`
4. `FUTURE_VOLUME_WORK_GUIDELINES.md`
5. `PROJECT_HANDOVER.md`

Then inspect:

6. the repository root `README.md`;
7. the target `volumes/volume-[NN]/` directory if it already exists;
8. all target-volume `README`, metadata, progress, audit, contents, chapter and translation-plan files already present;
9. Volume 49 as the completed reference implementation;
10. Volume 46 as a completed reference for source anomalies, bilingual alignment and final English release packaging.

Do **not** restart or duplicate existing target-volume work. If the target volume already has work, continue exactly from the durable boundary recorded in its repository files.

### SOURCE AUTHORITY

The attached PDF scan is the controlling source for this edition.

Do not rely on the filename alone. Verify the volume number from the scan itself before creating or changing volume metadata.

Do not silently modernize, normalize, correct, reconstruct or improve the Tamil.

Preserve source-supported:

- spelling and grammar;
- punctuation and paragraph order;
- titles;
- quotations;
- dates, names, counts and figures;
- repetition and rhetorical structure;
- English/Latin text printed in the source;
- signatures and closings;
- post-closing printed text;
- numbering/date/title anomalies.

Distinguish printed text from library stamps, handwriting, later annotations, damage and bleed-through.

OCR or parsed text may assist transcription but is never authoritative. Every accepted Tamil reading must ultimately be supported by the scan.

Do not commit the source PDF into the repository unless explicitly instructed.

### NEW-VOLUME INTAKE

If this volume has not yet been started:

- confirm the volume number from the scan;
- record the exact source filename;
- record PDF page count and, where available, source SHA-256 and byte size;
- record publisher, edition and year only when printed;
- identify provisional visible date and letter-number ranges;
- inspect contents pages without assuming they are error-free;
- note blank, damaged, rotated, duplicated, illegible or missing source pages;
- check whether a searchable text layer exists, but do not treat it as authoritative;
- create the current-format volume structure required by `VOLUME_PROCESSING_GUIDE.md`.

### TAMIL TRANSCRIPTION BATCHING

For a newly started volume:

1. The **first transcription commit must be exactly PDF pages 001–025**.
2. Create one canonical Markdown file for every PDF page in that range, including covers, publication pages, contents, blanks, illustrations and letter pages.
3. Visually compare every new/corrected page with the scan before committing.
4. If PDF page 25 interrupts a letter, stop exactly at page 25 and mark that letter `partial`.
5. The next commit must begin at PDF page 26 and finish that interrupted letter first.
6. After that, the normal transcription iteration is **five complete consecutive actual source letters = one atomic commit**.
7. Do not include part of a sixth letter.
8. A smaller/larger batch is allowed only under the documented exception rules or explicit user approval.

Every transcription iteration must update all applicable:

- canonical `pages/page-NNN.md` files;
- `contents/index.md`;
- completed/partial chapter records;
- `chapters/README.md`;
- `metadata.yml`;
- `PROGRESS.md`;
- `AUDIT.md`;
- volume `README.md` when status changes.

Chapter records link to canonical pages; they must not duplicate the full Tamil text.

Preserve words split across source-page boundaries. Do not silently join them.

If a contents title differs from the actual letter-start title, preserve both in their own source contexts and document the discrepancy.

### SOURCE ANOMALIES AND GAPS

If printed text exists but appears wrong or inconsistent, preserve it and document it. Do not repair it using outside knowledge.

If the sole available source PDF genuinely omits material:

- do not reconstruct from context;
- do not import another edition without explicit approval;
- mark the record `source-incomplete`;
- preserve all surviving text;
- leave unavailable closing/date/signature data unguessed;
- carry the gap consistently through metadata, chapter, audit, translation, manifest and release report.

Do not invent missing letter numbers merely to create a consecutive sequence. Batch and index **actual source records in scan order**.

### TAMIL QA GATES BEFORE ENGLISH

Keep these four stages distinct:

1. iteration/batch audit;
2. full-volume Tamil structural audit;
3. second visual verification;
4. translation textual-fidelity audit.

Do **not** begin English translation simply because transcription batches are complete.

English translation may begin only after the required Tamil structural and scan-fidelity gates have passed for the relevant source material.

### ENGLISH TRANSLATION POLICY

Translate in clear contemporary English while **retaining Kalaignar’s language, thought order and rhetorical force**.

Do not reduce the letter to a summary or neutral academic paraphrase.

Preserve:

- argument sequence;
- political directness;
- criticism and accusation;
- irony and sarcasm;
- rhetorical questions;
- repetition;
- quotations and attributed voices;
- chronology;
- names, figures, dates and units;
- idiom imagery where possible;
- source-supplied English;
- source anomalies and source gaps.

Use the established conventions unless the target volume’s approved translation plan documents a source-specific exception:

- retain `Udanpirappē` for the standard characteristic salutation;
- use `With affection, M.K.` where the source has the standard `அன்புள்ள, மு.க.` closing;
- retain `lakh` / `crore` and equivalent source/public-language units;
- preserve genuinely printed source English verbatim;
- when the source prints English and then a separate Tamil rendering/explanation, represent **both** source passages in the bilingual record;
- translate long quotations from the audited canonical Tamil rather than substituting outside versions;
- preserve printed post-signature material in source position.

Every bilingual English record must include the **complete available audited Tamil** under:

`## Original Tamil — மூலத் தமிழ்`

The Tamil appendix is mandatory and remains authoritative.

### TRANSLATION PILOT AND BATCHES

If the target volume does not already have an approved translation plan:

1. draft a representative **three-letter pilot**;
2. perform bilingual source-alignment review of the pilot;
3. document and lock volume-specific translation conventions;
4. then proceed by default in **five actual source-record translation batches**;
5. after each batch, run a separate bilingual alignment gate before promotion to verified.

If an existing approved target-volume `TRANSLATION_PLAN.md` explicitly defines another safe translation batch structure, follow it.

Do not mark a draft `verified` merely because the English exists.

### BILINGUAL ALIGNMENT

For each letter/batch, compare the English against the audited Tamil for:

- title and salutation;
- closing/date/signature;
- complete paragraph and argument sequence;
- names, dates, figures and units;
- quotations and lists;
- attribution;
- uncertainty and questions;
- irony, repetition and political force;
- duplicated/parenthetical source material;
- source anomalies and gaps;
- complete audited Tamil appendix.

Correct English-only fidelity issues before promotion.

Change canonical Tamil only when a fresh direct scan comparison proves the Tamil transcription itself is wrong, and document that scan-proven correction.

### FINAL ENGLISH RELEASE

After all eligible records have passed bilingual alignment:

1. run a full-volume English editorial consistency review;
2. check stale draft/pending translator-note wording and metadata;
3. verify title/frontmatter/index agreement;
4. verify names, place names, transliteration, institutions and recurring terminology;
5. verify all bilingual files retain the complete available Tamil appendix;
6. build and validate a translation manifest with one row per actual source record;
7. create the final English release report;
8. synchronize volume metadata, README and progress;
9. update root repository status where needed;
10. remove any temporary one-time workflow/script/export artefacts.

Do not declare the volume complete until the physical files, manifest and release report all reconcile.

### GIT / CONCURRENCY RULES

- Work on `main` as requested.
- Do not force-push routine work.
- Recheck repository state before writes when concurrent work is possible.
- Preserve unrelated concurrent changes.
- Keep each declared iteration scope explicit.
- Prefer one validated atomic commit per normal batch/gate where technically possible.
- Do not leave temporary GitHub Actions workflows or OCR/render/export artefacts in the final tree.

### WHEN I SAY “PROCEED WITH NEXT ACTIVITY”

When I say **“Proceed with next activity”** or **“Proceed with next iteration”**:

- inspect the repository state;
- identify the next clearly defined batch/gate from the target volume’s durable progress files;
- execute that activity directly;
- do not ask me to choose among routine next steps;
- do not return after each individual letter when the active batch calls for multiple letters;
- report the completed source/letter/page scope, QA result, commit SHA where applicable, and the exact next activity.

Ask a clarifying question only if a genuine source ambiguity, missing attachment, repository conflict or policy decision prevents safe continuation.

### COMPLETION REPORT FORMAT

After each activity, report concisely:

- what records/pages/gate were completed;
- exact PDF/printed-page scope where applicable;
- important source anomalies preserved;
- QA/alignment result;
- canonical Tamil changes, if any, and why;
- commit SHA/message where applicable;
- current counts/status;
- exact next activity.

Do not claim completion unless the repository files physically reflect it.

---

## Minimal variables to replace

- `[SOURCE_PDF_FILENAME]`
- `[VOLUME_NUMBER]`

Everything else in the prompt should normally remain unchanged.
