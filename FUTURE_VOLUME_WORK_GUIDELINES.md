# Future Volume Work Guidelines — Kalaignar Murasoli Letters

**Status:** operational companion for all future volume work in this repository.

This document does **not** replace the repository’s controlling guides. If any wording here conflicts with [`VOLUME_PROCESSING_GUIDE.md`](VOLUME_PROCESSING_GUIDE.md), [`VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md), or [`TRANSCRIPTION_GUIDE.md`](TRANSCRIPTION_GUIDE.md), those controlling documents take precedence.

The purpose of this file is to capture the workflow that has proved reliable across the completed archival and English-release work, especially Volumes 46 and 49, so that future work can resume consistently in a fresh chat or by another worker.

---

## 1. Mandatory startup order

Before changing any target volume:

1. Fetch live `main` first and treat it as authoritative. Record the current HEAD before relying on a prompt, handover or checkpoint copied into a chat. If `main` has advanced, preserve the newer durable state and continue from it rather than regressing to an older recorded boundary.
2. Read `VOLUME_PROCESSING_GUIDE.md` completely.
3. Read `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md` completely.
4. Read `TRANSCRIPTION_GUIDE.md` completely.
5. Read `PROJECT_HANDOVER.md` and `NEXT_CHAT_PROMPT.md` completely.
6. Inspect the target volume’s existing `README.md`, `metadata.yml`, `AUDIT.md`, `PROGRESS.md`, `TRANSLATION_PLAN.md`, contents, chapter register and English workspace if they exist.
7. Inspect Volume 49 as the completed reference implementation.
8. Inspect Volume 46 as a completed example of source anomalies, multi-stage bilingual verification and final release packaging.
9. Inspect the repository before creating files. If the target volume has already been started, **continue it; do not create a duplicate volume tree**.
10. Inspect the actual attached source PDF scan before trusting filename, contents-page data, OCR or prior notes whenever the next activity requires source re-verification.
11. Preserve concurrent changes. A handover SHA is a checkpoint, not permission to overwrite a newer live branch.

Do not commit the source PDF itself unless the user explicitly requests that.

For an already-active English QA phase, also read every completed QA report through the live boundary, the current English manifest/progress/index, the target volume metadata/progress, the locked glossary, and the source-check report(s) covering the next records before editing them.

---

## 2. Source authority

Authority order:

1. **Attached/original PDF scan** — controlling source.
2. Visually verified `pages/page-NNN.md` canonical Tamil.
3. Contents/chapter records.
4. English translations.
5. Indexes, manifests and reports.

Never silently modernise, normalize, correct, reconstruct or improve the printed source.

Preserve source-supported:

- historical spelling;
- punctuation;
- wording and grammar;
- repetition;
- names and honorifics;
- dates and numbers;
- monetary and land units;
- English/Latin text printed in the source;
- quotations and lists;
- unusual typography;
- closings, signatures and post-closing text;
- numbering/date/title anomalies.

Library stamps, handwriting, later annotations, bleed-through, damage and non-source marks must be distinguished from printed source text.

OCR may assist drafting and discrepancy detection but is never authoritative.

---

## 3. Source intake for a new volume

Before the first transcription commit, establish and record only what the scan supports:

- expected and scan-confirmed volume number;
- source filename;
- SHA-256 and byte size when available;
- PDF page count;
- publisher, edition and year if printed;
- visible date range;
- provisional letter-number range;
- contents-page structure;
- searchable-text-layer status;
- blank, damaged, duplicated, rotated, missing or illegible source pages;
- known gaps between PDF page number and printed page number;
- current repository `main` HEAD.

Never assume another volume’s page offset, letter count, date format, contents accuracy, salutation, closing or scan completeness.

---

## 4. Required volume structure

For current-format volumes, use the structure defined by `VOLUME_PROCESSING_GUIDE.md`, including:

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
  ...
  translations/en/
    README.md
    PROGRESS.md
    GLOSSARY.md
    EDITORIAL_CONSISTENCY_REVIEW.md
    TEXTUAL_FIDELITY_AUDIT_*.md
    BILINGUAL_ALIGNMENT_REVIEW_*.md
    TRANSLATION_MANIFEST.*
    RELEASE_REPORT.md or FINAL_RELEASE_REPORT.md
    letters/NNNN-short-slug.md
```

Older repository volumes may use legacy structures. Do not rename released paths merely to imitate a newer volume. For a new volume, use the current structure unless the controlling guide is updated.

---

## 5. Tamil transcription batching

The mandatory transcription policy is:

### First commit

**Exactly PDF pages 001–025.**

Create one canonical Markdown page per PDF page, including covers, publisher matter, contents, blanks, illustrations and letter pages.

If PDF page 25 ends in the middle of a letter, stop exactly there and mark the letter `partial`.

### Immediate continuation

If page 25 interrupted a letter, the next commit begins at PDF 26 and finishes that letter first. Do not pad the commit with unrelated later letters.

### Normal iterations

After that boundary is clear:

**five complete consecutive letters = one normal transcription iteration / atomic commit.**

Do not include part of a sixth letter. A smaller or larger batch requires the documented exception rules or explicit user approval.

Every transcription iteration updates all applicable canonical pages, contents, chapter files, chapter index, metadata, progress, audit and volume README.

---

## 6. Canonical Tamil rules

Each PDF page gets one Markdown file. Preserve the page boundary exactly.

Important rules:

- Do not silently join a word visibly split across two source pages.
- Do not copy the same body into both page and chapter files; chapter records link to canonical page files.
- Use `[தெளிவில்லை]` only when printed text exists but cannot be read confidently.
- Do not use `[தெளிவில்லை]` to represent a page or passage that is genuinely absent from the source.
- Preserve printed English exactly when it is part of the archival source.
- Preserve source anomalies instead of correcting them from outside knowledge.
- Contents wording and actual letter-start wording may differ; preserve each in its own source context.
- A source date/number that appears wrong remains the source date/number unless a separate note documents the anomaly.

`first-pass-reviewed` means one visual comparison with the scan; it is not the second visual/textual-fidelity gate.

---

## 7. Source anomalies and source gaps

### Printed anomaly

If text is present but apparently wrong, contradictory or oddly numbered:

- preserve it;
- document it;
- do not silently repair it.

Volume 46 is the model for this principle: the source has no 3636, prints two distinct 3637 records, and has no 3644–3646. The archive preserves those facts exactly.

### Missing source material

If the sole available PDF genuinely omits a printed page or continuation:

- do not reconstruct from context;
- do not import another edition without explicit approval;
- mark the record `source-incomplete`;
- preserve all surviving text;
- record the missing printed page/gap wherever determinable;
- leave unavailable closing/date/signature information unguessed;
- carry the source-gap status consistently into metadata, chapter, audit, translation, manifest and release report.

Volume 47 letter 3681 is the current reference for a release-ready record that remains explicitly source-incomplete.

---

## 8. Tamil audit gates before English

English translation remains blocked until the required Tamil gates are complete.

Keep these gates distinct:

1. iteration/batch audit;
2. full-volume Tamil structural audit;
3. second visual verification;
4. translation textual-fidelity audit.

Passing one does not imply another.

Before translating a letter or batch, every relevant canonical Tamil page must have been compared against the scan for titles, paragraph order, names, dates, figures, quotations, lists, punctuation, source English, closings and omissions.

Scan-proven Tamil corrections belong in a textual-fidelity report. Do not silently change canonical Tamil during English review unless a fresh scan comparison proves the Tamil record wrong.

---

## 9. English translation policy

The target is a **thought-preserving, non-literary English translation**, not a polished rewrite detached from Kalaignar’s voice.

Preserve:

- thought and argument order;
- political directness;
- accusation and criticism;
- irony and sarcasm;
- rhetorical questions;
- repetition;
- quoted voices;
- chronology;
- figures, units and counts;
- source-specific institutional/legal terms;
- idiom imagery where possible;
- source-supplied English.

Do not compress, broaden, soften, reorder or supplement claims for elegance.

### Stable conventions learned from Volume 46

Unless a target volume’s approved translation plan documents a source-specific reason to differ:

- retain **`Udanpirappē`** for Kalaignar’s characteristic political-familial salutation;
- use **`With affection, M.K.`** where the source has the standard `அன்புள்ள, மு.க.` closing;
- retain Indian public-language quantities such as `lakh` and `crore`;
- preserve source-supplied English verbatim, including odd spelling/typography when it is genuinely printed;
- if the source prints an English passage and then separately prints a Tamil rendering/explanation, represent **both** in the bilingual English record; do not collapse the Tamil passage into a summary;
- translate long quotations from the audited canonical Tamil rather than substituting an outside version;
- preserve post-signature printed material in source position;
- preserve source numbering/title/date anomalies rather than repairing them.

### Bilingual record order

Each English record should contain, in the approved volume format:

1. front matter/status fields;
2. English title;
3. translator’s note;
4. Tamil source/date/page references;
5. complete English translation of all surviving source text;
6. source/anomaly notes only where needed;
7. complete available **`Original Tamil — மூலத் தமிழ்`** appendix.

The appended Tamil must match the audited canonical pages. It is not optional.

---

## 10. Translation batching and pilot

For a future volume that does not already have an approved translation plan:

1. run a small **pilot of three representative letters**;
2. perform a bilingual review of the pilot;
3. document and lock volume-specific translation conventions;
4. then proceed in **five actual source-record batches** by default;
5. perform a separate bilingual source-alignment gate before promoting each batch.

A target volume’s existing approved `TRANSLATION_PLAN.md` takes precedence over this default if it explicitly defines a different safe batch structure.

Do not create imaginary letter numbers to make a batch look consecutive. Batch by **actual source records in scan order**.

When the user says “Proceed with next activity,” continue the next clearly defined gate or batch without asking them to choose again, unless a genuine source ambiguity blocks safe work.

---

## 11. Translation statuses, alignment and fresh-chat continuation

Drafting/source-check and bilingual alignment are separate durable gates. Use the target volume’s existing manifest vocabulary; do not invent a different status scheme mid-volume.

For current Volume 44-style records, the normal progression is:

- translation drafted;
- `translation_status: source-checked` after the complete source-check gate passes;
- `bilingual_alignment_status: pending` until the separate meaning-level comparison is closed;
- required English correction(s), if any, applied;
- `bilingual_alignment_status: aligned` only after the batch is fully synchronized and verified;
- later editorial-review and release statuses remain pending until their own gates are executed.

Before bilingual alignment, check every surviving Tamil paragraph against English for:

- complete semantic coverage;
- no invented additions;
- names, dates, figures and units;
- quotations and attribution;
- lists and chronology;
- uncertainty and questions;
- rhetoric, sarcasm and repetition;
- source anomalies and gaps;
- closing/signature/date;
- complete audited Tamil appendix.

Record each batch’s result in `BILINGUAL_ALIGNMENT_REVIEW_<start>_<end>.md`, including exact English-only corrections and whether any fresh scan-proven Tamil correction was required.

### Durable alignment promotion rule

A review is **not** a completed alignment gate merely because the report text exists. A reviewed record becomes durably `aligned` only when all of the following have landed together on live `main`:

1. every required English meaning-level correction has actually been applied;
2. the English record front matter has the correct alignment status;
3. the corresponding manifest row has the same status;
4. the alignment report records the result and exact corrections;
5. English index/progress and applicable volume/root controls are synchronized; and
6. the resulting commit or net repository diff has been verified for the intended scope.

If one of these is still pending, keep the durable status pending and record the unfinished synchronization explicitly rather than overstating completion.

### Fresh-chat continuation rule

A fresh chat must reconstruct the current state from live GitHub, not from chat memory alone:

1. fetch live `main` and record HEAD;
2. read `PROJECT_HANDOVER.md` and `NEXT_CHAT_PROMPT.md` from that HEAD;
3. read the target volume’s English manifest/progress/index and all completed bilingual-alignment reports through the live boundary;
4. confirm the last actually aligned manifest row and the first pending row;
5. if the live boundary is newer than the prompt/handover checkpoint, preserve the newer state and derive the next batch from live files;
6. do not repeat a completed batch or reset status because an older handoff mentioned it; and
7. do not begin a later editorial/release gate while a current alignment batch is only partially synchronized.

For a normal alignment iteration, use **five actual source records in source order** unless the approved target-volume plan states otherwise. Stop before a sixth record. If the user asks to move to another chat, update the prompt, handover and this guideline when the workflow has learned a durable rule that the next worker must know.

---

## 12. Volume-level English editorial review

After all eligible letters are aligned, review the full English corpus as one work.

Check:

- title/frontmatter/index agreement;
- translator-note status wording;
- stale draft/pending fields;
- names, honorifics and place names;
- transliteration;
- institutional/legal terminology;
- British/Indian English spelling and compounds where appropriate;
- dates and page ranges;
- glossary consistency;
- source-incomplete labels;
- preservation of appended Tamil;
- source-number anomalies.

The editorial pass must **not** change political meaning, attribution, uncertainty, figures, quotations, rhetorical force or canonical Tamil.

Record the result in `EDITORIAL_CONSISTENCY_REVIEW.md`.

Volume 46 showed why this gate matters: its final pass found stale translator-note wording and a stale pending-range metadata field even after substantive translation verification was complete.

---

## 13. Release package

A completed English volume should contain:

- one bilingual English record for every actual source-letter record, including explicit source-incomplete records;
- English README/index;
- English progress tracker;
- glossary where used;
- textual-fidelity audit reports;
- bilingual alignment reports;
- editorial consistency review;
- machine-readable translation manifest;
- final release report;
- synchronized volume metadata and root status.

The manifest must reconcile exactly with actual source records. It must preserve duplicate printed numbers when the source genuinely duplicates them and must not invent missing numbers.

Before declaring release:

- manifest count = actual source-record count;
- all release-eligible records have the required verified/aligned state under that volume’s policy;
- every translated record includes complete available Tamil;
- source gaps are explicit everywhere;
- no temporary workflow/script/export file remains in `main`;
- README, metadata, progress and release report agree.

---

## 14. Git and repository hygiene

- Work on `main` when requested for this repository.
- Prefer one validated atomic commit per declared archival/translation/alignment iteration.
- Never force-push routine work.
- Recheck live `main` immediately before final mutation when concurrent work is possible.
- If `main` advanced, preserve that work and rebuild/rebase the candidate on the new HEAD instead of overwriting it.
- Do not overwrite changes from another volume/workstream.
- Use explicit commit messages naming volume and gate/range.
- Fast-forward routine work only with `force: false`.
- Compare parent → new HEAD (or the pre-activity clean checkpoint → final HEAD if repair commits were necessary) and verify the exact intended changed-file scope.
- Do not leave one-time GitHub Actions workflows, temporary OCR dumps, render files, cleanup scripts, probe/dummy files or export artefacts in final `main`.
- After a bulk operation, verify the physical files rather than relying only on a status summary.

---

## 15. Definition of done for a future volume

A volume is complete only when all applicable gates are closed:

1. source intake verified from scan;
2. every available PDF page represented canonically;
3. contents and chapter structure complete;
4. full-volume Tamil structural audit passed;
5. second visual/textual-fidelity verification complete;
6. all actual source letters translated for all surviving text;
7. bilingual alignment complete and durably synchronized;
8. volume-level English editorial review complete;
9. manifest validated against actual source records;
10. final release report created;
11. metadata/README/progress/root status synchronized;
12. temporary automation/work/probe files removed.

Only then describe the volume as **release-ready/completed**, subject to any explicitly documented source-incomplete limitation.
