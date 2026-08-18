# Volume 1 — Canonical Migration Progress

- [x] Migration audit completed against existing legacy Volume 1 corpus
- [x] Controlling `Vol1.pdf` verified: 401 PDF pages, 400 printed pages
- [x] Canonical Tamil page/letter migration complete: **401 / 401 pages; 110 / 110 letters**
- [x] Full-volume Tamil structural audit — **PASS**
- [x] Second visual/textual-fidelity verification — **PASS; PDF 001–401 / 401 complete**
- [x] Legacy English record migration and source checking — **complete; 0001–0110 / 110 source-checked**
- [x] Bilingual alignment — **complete; 0001–0110 / 110 reviewed and PASS**
- [x] Volume-level editorial consistency review — **complete; 110 / 110 PASS**
- [ ] Translation manifest and final English release report

## Current boundary

- Canonical page files: **401 / 401**
- Printed contents entries: **110 / 110**
- Canonically complete letters: **110 / 110** (`0001–0110`)
- Letter coverage: PDF **024–400**; PDF 401 is non-letter back cover
- Tamil structural audit: **PASS**
- Full second visual/textual-fidelity verification: **PASS — PDF 001–401 / 401**
- Cumulative scan-proven corrections: **159 canonical pages / 274 spans**
- Letter 0063 remains undated because no date is printed in the source
- Printed pagination skips number 39 between PDF 039 and PDF 040 while text remains continuous
- Contents/heading variants remain literal, including 0109 contents `அவள் ஒரு தொடற்கதை!` versus actual heading `அவள் ஒரு தொடர்கதை!`
- Legacy bilingual records preserved unchanged: **110 / 110** under `../volume-1/`
- Canonical English records: **110 / 110 source-checked**
- Bilingual-aligned canonical English records: **110 / 110 — PASS**
- Editorially reviewed canonical English records: **110 / 110 — PASS**
- Alignment-driven English prose/quotation corrections: **4** — 0014, 0043, 0058, 0059
- Additional English prose/quotation corrections in editorial pass: **0**
- Verified/release-certified canonical English records: **0 / 110** pending final release gate

## English QA records

Bilingual alignment closes in [`translations/en/alignment/PROGRESS.md`](translations/en/alignment/PROGRESS.md) and [`translations/en/alignment/ALIGNMENT_MANIFEST.csv`](translations/en/alignment/ALIGNMENT_MANIFEST.csv). The completed volume-level English editorial pass is recorded in [`translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`](translations/en/EDITORIAL_CONSISTENCY_REVIEW.md).

The editorial review found no source-aligned English prose/quotation change requiring a canonical record rewrite. It documented the inherited migration-format variation across 0001–0040, 0041–0060 and 0061–0110 and left source-check-era frontmatter untouched where changing it would be bookkeeping-only churn.

## High-value source controls retained

- 0002 complete Kamaraj Deepavali quotation; 0010 **Runner Cup**; 0028 printed date **28-12-1968**; 0036 unexpanded **C. P. C.**; 0048 printed `சென்னை. / 10.10.1972`; 0054 figure **6908**; 0058 date **29-05-1973**; 0063 undated; 0068 scan-controlled Bharathidasan verse; 0070 printed English judicial quotation verbatim.
- 0076–0080 preserve Sixth Finance Commission structure, Periyar analogies/self-critique, `பாடி வீடுகள்` and `கொள்கை மலர்கள்` imagery.
- 0081–0090 preserve state-autonomy, Pongal, labour, railway-strike, birthday and organisational imagery.
- 0091–0100 preserve celebration/work, betrayal/state-autonomy, Kamaraj/*Navasakthi*/*Dinamani*, police-family lullaby, `மாம்பழ மங்கை`, paired 1799/1972 dates, `முப்பெரும் விழா`, `இரட்டைக்குழல் துப்பாக்கி`, Murasoli Selvam and *Kalingattuparani* material.
- 0101–0110 preserve the five slogans, N. V. N. passage, hunger report, *Kalki* arguments, industrial data, `ஆட்சி / மாட்சி`, Jayaprakash satire, actual 0109 heading/opaque wording and the full 1949 quotation through PDF 400.

## Exact next task

Prepare the **final translation manifest and English release report**. Inventory exactly one canonical English record for each letter **0001–0110**, validate unique letter IDs and file paths, title/date/source-page agreement, complete Tamil appendices, source-check/alignment/editorial completion and all documented anomalies, then synchronize Volume 1/root release status.

Do not modify the legacy `volumes/volume-1/` tree or bulk-rewrite canonical records solely to change source-check-era status fields.