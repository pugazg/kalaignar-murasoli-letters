# Volume Transcription Batching Policy — Volumes 1–48

**Status:** Mandatory repository policy for starting and continuing every new Tamil transcription volume.

This policy records the workflow proven during Volume 48. Where its transcription-batch rules conflict with the older recommended `10–20 PDF pages` wording in §9 of `VOLUME_PROCESSING_GUIDE.md`, **this policy takes precedence**.

---

## 1. Before the first transcription commit

For every new volume:

1. Read `VOLUME_PROCESSING_GUIDE.md`, `TRANSCRIPTION_GUIDE.md`, and this policy.
2. Inspect the completed reference volume and the most recently processed earlier volume.
3. Confirm that the target `volumes/volume-NN/` directory has not already been started.
4. Verify the volume number from the scan itself.
5. Record the exact filename, SHA-256, byte size, PDF page count, publisher, edition/year, visible date range, letter-number range, and scan anomalies.
6. Create the required volume structure, metadata, progress, contents, chapter register, batch audit, translation-plan gate, page directory, and blocked English-translation directory.

Do not infer that another volume has the same page offset, contents layout, date format, letter count, or front matter.

---

## 2. Mandatory first batch: PDF pages 001–025

The first transcription commit for a new volume must cover **exactly PDF pages 001–025**.

Required commit message pattern:

```text
Transcribe Volume NN PDF pages 001-025
```

Rules:

- Create one canonical Markdown file for every PDF page from `page-001.md` through `page-025.md`.
- Include covers, publication pages, forewords, contents pages, blanks, illustrations, and letter pages without omission.
- Visually compare all 25 Markdown pages with the corresponding rendered scan before committing.
- OCR may assist drafting, but the scan controls every accepted reading.
- Update all structural and progress files in the same atomic commit.

### When PDF page 25 falls inside a letter

Do **not** extend the first commit beyond page 25 merely to finish the letter.

Instead:

- preserve the exact page-25 ending;
- create or update the chapter record with `status: partial`;
- leave `pdf_page_end` and `printed_page_end` unresolved where necessary;
- state explicitly that the letter continues at PDF page 26;
- record the exact next task in `PROGRESS.md`; and
- never invent or copy the continuation from another source.

A partial first-letter boundary is valid only when it is clearly documented.

---

## 3. Immediate continuation after page 25

The next transcription commit must begin at **PDF page 26**.

When page 25 ended inside a letter, this commit must finish that interrupted letter before beginning another letter.

Required commit message pattern:

```text
Complete Volume NN letter NNNN — PDF pages 026-XXX
```

The commit must:

- add every remaining canonical page belonging to that letter;
- verify the closing, signature/date, final printed page, and exact PDF end;
- change the chapter record from `partial` to `complete`;
- update the contents register, chapter index, metadata, progress, and batch audit; and
- identify the next exact PDF page and letter.

When PDF page 25 does not interrupt a letter, begin the next letter at page 26 and complete that letter as the next batch.

---

## 4. Default workflow after the first letter

After the initial 25-page batch and completion of any interrupted letter, process **one complete letter per commit by default**.

Required commit message pattern:

```text
Complete Volume NN letter NNNN — PDF pages AAA-BBB
```

Rules:

- Begin at the verified first page of the letter.
- Continue through its verified closing/date page.
- Do not include part of the following letter merely to enlarge the batch.
- A long or difficult letter still remains one letter-level batch unless technical limits make that impossible.
- Group multiple letters only when the user explicitly approves a grouped batch; every included letter must be complete and the exact range must be declared.
- Never leave an incomplete letter unmarked.

---

## 5. Files that must be updated in every transcription batch

Every commit must update all applicable records, not only `pages/`:

1. `pages/page-NNN.md` canonical page files
2. `contents/index.md`
3. the current `chapters/NNNN-short-slug.md`
4. `chapters/README.md`
5. `PROGRESS.md`
6. `metadata.yml`
7. `AUDIT.md` with the exact batch scope
8. `README.md` when the completed range or letter count changes materially
9. translation-gate records when needed, without starting translation

Chapter files link to canonical page files; they must not duplicate the full letter text.

---

## 6. Mandatory visual verification within each batch

Before every transcription commit:

- compare every new or corrected Markdown page directly with its scan;
- verify page and paragraph boundaries;
- verify title, salutation, closing, signature, date, quotations, names, figures, and intentional English text;
- preserve source spelling, punctuation, malformed wording, and visible anomalies;
- preserve words split across PDF page boundaries rather than silently joining them;
- check for missing page files, duplicated bodies, replacement Unicode, and broken internal links; and
- record scan-proven corrections in the batch audit.

`first-pass-reviewed` means the page has been visually compared once. It does not mean the later character-by-character second verification is complete.

### Contents title versus letter title

- `contents/index.md` must preserve the wording printed in the contents pages.
- The chapter record and letter pages must preserve the wording printed at the letter start.
- When the two differ, retain both and document the discrepancy; do not silently force them to match.

---

## 7. Audit levels must remain distinct

Do not merge these statuses:

1. **Batch audit** — validates the exact pages and letters in the current commit.
2. **Full-volume Tamil structural audit** — performed only after every PDF page has a canonical Markdown file.
3. **Second visual verification** — later character-by-character or equivalent close comparison.
4. **Textual-fidelity audit for translation** — mandatory visual scan comparison for every page included in a translation batch.

A passed batch audit does not unlock English translation.

---

## 8. Translation remains blocked

Do not begin English translation merely because one or more letters are complete.

Translation may begin only after:

- all PDF pages in the volume are transcribed;
- the full-volume Tamil structural audit passes; and
- the relevant Tamil pages pass the mandatory textual-fidelity audit required before translation.

The approved translation batch rule remains separate: normally five complete letters or the smaller page-based limit stated in the master guide.

---

## 9. Commit and branch discipline

- Prefer one atomic commit for each declared batch.
- The commit must contain only files required for that volume batch.
- Direct commits to `main` are allowed for this repository when the complete tree has been validated before moving the ref.
- Do not create one commit per page.
- Do not force-push `main`.
- Use a temporary branch only when technically necessary; remove or neutralise it after integration.
- Do not leave temporary workflows, test files, export files, or cleanup scripts in the final tree.

---

## 10. Completion report after every batch

Report:

- exact PDF pages added;
- exact printed pages covered;
- letters completed or left partial;
- structural files updated;
- audit result and preserved anomalies;
- final commit SHA and commit message; and
- the exact next PDF page and letter.

Do not report a letter or volume as complete unless its verified end boundary has been reached.
