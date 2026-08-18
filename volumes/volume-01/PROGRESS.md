# Volume 1 — Canonical Migration Progress

- [x] Migration audit completed against existing legacy Volume 1 corpus
- [x] Controlling `Vol1.pdf` verified: 401 PDF pages, 400 printed pages
- [x] Canonical Tamil page/letter migration complete: **401 / 401 pages; 110 / 110 letters**
- [x] Full-volume Tamil structural audit — **PASS**
- [x] Second visual/textual-fidelity verification — **PASS; PDF 001–401 / 401 complete**
- [x] Legacy English record migration and source checking — **complete; 0001–0110 / 110 source-checked**
- [ ] Bilingual alignment — **in progress; 0001–0090 / 90 reviewed and PASS**
- [ ] Volume-level editorial consistency review
- [ ] Translation manifest and final release report

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
- Bilingual-aligned canonical English records: **90 / 110**
- Completed bilingual-alignment range: **0001–0090**
- Alignment-driven English prose/quotation corrections: **4** — 0014, 0043, 0058, 0059
- Verified canonical English records: **0 / 110**
- Editorially reviewed canonical English records: **0 / 110**

## Alignment reports

Reports are complete through [`translations/en/alignment/ALIGNMENT_0081_0090.md`](translations/en/alignment/ALIGNMENT_0081_0090.md). The authoritative record-level ledger is [`translations/en/alignment/ALIGNMENT_MANIFEST.csv`](translations/en/alignment/ALIGNMENT_MANIFEST.csv); current boundary is in [`translations/en/alignment/PROGRESS.md`](translations/en/alignment/PROGRESS.md).

The **0081–0090** batch passed with no English prose/quotation correction. It reconfirmed state-autonomy/Rajamannar material, Pongal imagery, election/cadre rhetoric, budget imagery, internal-election rose imagery, May Day labour history, railway-strike Centre/State asymmetry, birthday-fund redirection, organisational lamp/pearls/balance imagery and the summer/cyclone/Tamil–Malayali violence/Kamaraj sequence.

## High-value source controls retained across migration

- 0002 complete Kamaraj Deepavali quotation; 0010 **Runner Cup**; 0028 printed date **28-12-1968**; 0036 unexpanded **C. P. C.**; 0048 printed `சென்னை. / 10.10.1972`; 0054 figure **6908**; 0058 date **29-05-1973**; 0063 undated; 0068 scan-controlled Bharathidasan verse; 0070 printed English judicial quotation verbatim.
- 0076–0080 preserve Sixth Finance Commission structure, Periyar analogies/self-critique, `பாடி வீடுகள்` and `கொள்கை மலர்கள்` imagery.
- 0081–0090 preserve state-autonomy, Pongal, labour, railway-strike, birthday and organisational imagery.
- 0091–0100 preserve celebration/work, betrayal/state-autonomy, Kamaraj/*Navasakthi*/*Dinamani*, police-family lullaby, `மாம்பழ மங்கை`, paired 1799/1972 dates, `முப்பெரும் விழா`, `இரட்டைக்குழல் துப்பாக்கி`, Murasoli Selvam and *Kalingattuparani* material.
- 0101–0110 preserve the five slogans, N. V. N. passage, hunger report, *Kalki* arguments, industrial data, `ஆட்சி / மாட்சி`, Jayaprakash satire, actual 0109 heading/opaque wording and the full 1949 quotation through PDF 400.

## Exact next task

Continue bilingual alignment with **0091–0100**, source PDF / printed pages **326–358**. Compare English directly with complete canonical Tamil, correct only demonstrable correspondence errors, create `translations/en/alignment/ALIGNMENT_0091_0100.md`, append the manifest, and advance to **100 / 110** only after all ten pass.

Keep volume-level editorial consistency, final translation manifest, release report and release declaration blocked until bilingual alignment is complete.
