# Start Next Chat — Volume 1 Canonical Migration

Copy the prompt below into a new chat and attach the controlling **Volume 1 PDF scan (`Vol1.pdf`)**.

---

Continue the Kalaignar Murasoli Letters **Volume 1 canonical migration** directly in:

`pugazg/kalaignar-murasoli-letters`

Work on `main`.

Active canonical tree:

`volumes/volume-01/`

Legacy preserved tree:

`volumes/volume-1/`

The attached **`Vol1.pdf` scan is the controlling source** for this edition.

## Mandatory startup

Before making any change, read these repository files completely and follow them exactly:

1. `VOLUME_PROCESSING_GUIDE.md`
2. `TRANSCRIPTION_GUIDE.md`
3. `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
4. `FUTURE_VOLUME_WORK_GUIDELINES.md`
5. `PROJECT_HANDOVER.md`
6. `volumes/volume-01/VOLUME1_MIGRATION_GUIDELINES.md`
7. `volumes/volume-01/VOLUME1_PROJECT_HANDOVER.md`
8. `volumes/volume-01/README.md`
9. `volumes/volume-01/PROGRESS.md`
10. `volumes/volume-01/AUDIT.md`
11. `volumes/volume-01/metadata.yml`
12. `volumes/volume-01/chapters/README.md`

Then inspect the current repository state on `main` and confirm whether any Volume 1 work beyond the recorded boundary has already been started. If it exists, continue it; do not duplicate or overwrite valid later work.

## Source authority

The attached scan is authoritative.

Do not silently modernise, correct, normalise, reconstruct, regularise or improve Kalaignar's Tamil.

Preserve source-supported:

- historical spelling;
- punctuation and quotation marks;
- wording and repetitions;
- names and labels;
- dates and numbers;
- unusual grammar;
- rhetorical sequences;
- sign-off forms;
- title variants between contents and actual heading pages.

Distinguish printed text from stamps, handwriting, damage, show-through and other non-authorial marks.

OCR and the legacy Volume 1 corpus may assist comparison, but neither is authoritative. The visible scan controls every canonical decision.

Do not upload the source PDF to the repository.

## Volume 1-specific batching rule

For **Volume 1 alone**, process **10 complete consecutive letters per regular iteration**.

This overrides the generic five-letter batching cadence only for Volume 1.

## Current verified status

At the recorded handover boundary:

- canonical PDF coverage: **001–089 / 401**;
- canonically complete letters: **0001–0016 (16 / 110)**;
- partial letter: **none**;
- printed contents: **110 / 110 captured**;
- legacy bilingual records: **110 / 110 preserved under `volumes/volume-1/`**;
- canonical English migration: **not started / blocked**.

The completed migration commit before the Volume 1-specific handover documents was:

`e4e4a8f43581e3eeede3979dba0e8482610efce6` — `Complete Volume 1 ten-letter migration batch 0007-0016`

## Exact next activity

Begin at **PDF 090**, where the scan visibly starts:

**Letter 0017 — `கிளம்பிற்றுக்காண் தமிழச் சிங்கக் கூட்டம்!`**

Process exactly **10 complete consecutive letters: 0017 through 0026**.

For every PDF page in those ten letters:

1. inspect the actual scan directly;
2. create one canonical page file under `volumes/volume-01/pages/`;
3. preserve scan-supported Tamil exactly;
4. verify the actual letter heading, salutation, closing/sign-off and printed date;
5. create/update the canonical chapter record under `volumes/volume-01/chapters/`;
6. use the actual heading page as title authority when contents and heading differ;
7. keep all legacy files under `volumes/volume-1/` untouched.

Finish letter 0026 completely. Then inspect only enough of the next PDF page to verify the beginning of letter 0027. **Do not commit any text belonging to letter 0027.**

## Required tracking updates

After the ten letters are complete, synchronise:

- `volumes/volume-01/chapters/README.md`
- `volumes/volume-01/metadata.yml`
- `volumes/volume-01/README.md`
- `volumes/volume-01/PROGRESS.md`
- `volumes/volume-01/AUDIT.md`
- root `README.md` Volume 01 status row

Record any new source anomalies explicitly rather than silently correcting them.

## Known source notes to preserve

- PDF 039 prints page 38 and PDF 040 prints page 40; text is continuous, so printed page 39 is a pagination anomaly, not missing source text.
- Letter 0008's closing page prints the shortened date `(31-10-68)`.
- Actual letter headings control over differing contents-page title forms.

## Do not start later gates

Do not begin English migration, bilingual alignment, full-volume structural audit, second visual verification, editorial review or release work during this iteration.

The immediate goal is only the next **10-letter canonical Tamil migration batch, 0017–0026**, followed by tracking updates and a coherent commit to `main`.

---
