# Volume 1 — Project Handover

## Repository

`pugazg/kalaignar-murasoli-letters`

Work on `main`.

## Active work

Canonical migration of **Murasoli Letters — Volume 1** into:

`volumes/volume-01/`

The earlier tree:

`volumes/volume-1/`

contains the legacy 110 bilingual records. It must remain preserved and unchanged unless a later, explicitly authorised migration gate requires work there.

## Controlling source

The controlling source is the supplied **`Vol1.pdf` scan**.

Repository intake records:

- SHA-256: `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`
- size: 244,892,260 bytes
- PDF pages: 401
- printed pages stated by publisher: 400
- edition: first edition, 2022
- publisher: Seethai Pathippagam
- usable searchable text layer: none

The scan controls all canonical Tamil transcription and metadata decisions.

## Mandatory startup for a new chat

Before making any change, read these files completely:

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

Then inspect the current `main` state and verify that no later Volume 1 work has already been committed.

## Current canonical status

As of the handover creation point:

- canonical PDF pages: **89 / 401**
- canonical coverage: **PDF 001–089**
- printed contents captured: **110 / 110 entries**
- canonically complete letters: **16 / 110**
- completed letter range: **0001–0016**
- partial canonical letter: **none**
- canonical letter-body coverage: **PDF 024–089**
- legacy bilingual records preserved: **110 / 110**
- canonically migrated/verified English records: **0 / 110**
- full-volume Tamil structural audit: not started
- second visual/textual-fidelity verification: not started
- English migration/alignment: blocked

The latest completed migration commit before these handover documents was:

`e4e4a8f43581e3eeede3979dba0e8482610efce6` — `Complete Volume 1 ten-letter migration batch 0007-0016`

## Completed work

### Initial intake and front matter

- canonical `volumes/volume-01/` scaffold created;
- PDF 001–025 first-pass reviewed;
- front matter and publisher matter migrated;
- printed contents PDF 018–023 transcribed with all 110 entries;
- Letter 0001 correctly started at PDF 024 and completed through PDF 027.

### Initial regular batch

Letters **0002–0006** migrated from PDF **028–047**.

### Volume 1 batching override

The user explicitly instructed that **Volume 1 alone uses 10 letters per regular iteration**. That rule is now recorded in `VOLUME1_MIGRATION_GUIDELINES.md`, `PROGRESS.md` and `AUDIT.md`.

### First 10-letter batch

Letters **0007–0016** migrated from PDF **048–089**:

- 0007 — `தோற்ற முயலே! முன்போல சுறுசுறுப்பாக இரு!` — PDF 048–053 — 31-10-1968
- 0008 — `“தீராதி தீரர்- தேசீய மகிபர்- பராக்! பராக்!”` — PDF 054–057 — printed `(31-10-68)`
- 0009 — `வீரனே! வெற்றி என்றைக்கும் உன் பக்கம்தான்!` — PDF 058–062 — 01-11-1968
- 0010 — `பாவி கெடுத்தானே; பலே சாப்பாட்டை!` — PDF 063–066 — 02-11-1968
- 0011 — `தென்றல்- தெம்பாங்கு- தேன்கீதம்!` — PDF 067–069 — 06-11-1968
- 0012 — `“பூப்போட்ட கிளாசிலே போட்டய்யா ஒண்ணரை!”` — PDF 070–072 — 07-11-1968
- 0013 — `மேயர் தேர்தல் நேரம் - நிலை - நேர்த்தியான முடிவு!` — PDF 073–077 — 09-11-1968
- 0014 — `‘பகைமரம்’ தழைக்க விடோம்!` — PDF 078–081 — 11-11-1968
- 0015 — `நம்பிக்கையில்லாத் தீர்மானம் - நாடாளுமன்ற நிகழ்ச்சி!` — PDF 082–085 — 14-11-1968
- 0016 — `யார் அந்த உணவு அமைச்சர்?` — PDF 086–089 — 16-11-1968

All 42 PDF pages in this batch were represented by canonical page files and all ten start/end boundaries were visually checked.

## Known source/migration notes

1. **Printed page 39 anomaly:** PDF 039 visibly prints page 38 and PDF 040 prints page 40, while the text continues normally. Treat this as a source pagination anomaly, not a missing-text gap.
2. **Letter 0008 shortened date:** closing page prints `(31-10-68)`; preserve it at page level.
3. **Contents versus heading variants:** actual letter heading pages control canonical titles where they differ from contents entries.
4. Legacy Tamil/English may assist migration, but may never silently override the scan.
5. Do not commit the source PDF.

## Exact next task

Begin at **PDF 090**, which visibly starts:

**0017 — `கிளம்பிற்றுக்காண் தமிழச் சிங்கக் கூட்டம்!`**

Process exactly **10 complete consecutive letters: 0017–0026**.

For each letter:

- inspect every scan page directly;
- create one canonical Markdown page per PDF page;
- preserve scan-supported Tamil wording and punctuation;
- verify heading, salutation, closing/sign-off and date;
- create/update the corresponding chapter record;
- keep the legacy `volumes/volume-1/` corpus untouched.

After completing letter 0026, inspect only enough of the following PDF page to confirm where letter 0027 begins. **Do not commit any text from letter 0027.**

Then synchronise:

- `chapters/README.md`
- `metadata.yml`
- `README.md`
- `PROGRESS.md`
- `AUDIT.md`
- root `README.md` Volume 01 status row

and commit the complete 10-letter iteration to `main`.

## Gates that remain blocked

Do not begin these yet:

- full-volume Tamil structural audit;
- second visual/textual-fidelity verification;
- canonical English migration/source checking;
- bilingual alignment;
- editorial consistency review;
- translation manifest;
- final release report.

Those follow only after the canonical Tamil page migration reaches 401/401 and the repository-level workflow permits them.
