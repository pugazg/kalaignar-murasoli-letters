# Volume 1 — Canonical Migration Progress

- [x] Migration audit completed against existing legacy Volume 1 corpus
- [x] Controlling `Vol1.pdf` verified: 401 PDF pages, 400 printed pages
- [x] New canonical `volumes/volume-01/` scaffold established
- [x] Canonical Tamil page/letter migration complete: **401 / 401 pages; 110 / 110 letters**
- [x] Full-volume Tamil structural audit — **PASS**
- [x] Second visual/textual-fidelity verification — **PASS; PDF 001–401 / 401 complete**
- [x] Legacy English record migration and source checking — **complete; 0001–0110 / 110 source-checked**
- [ ] Bilingual alignment — **in progress; 0001–0050 / 50 reviewed and PASS**
- [ ] Volume-level editorial consistency review
- [ ] Translation manifest and final release report

## Current boundary

- Canonical page files: **401 / 401**
- Printed contents entries captured: **110 / 110**
- Canonically completed letters: **110 / 110**
- Completed canonical letter range: **0001–0110**
- Partial canonical letter: **none**
- Canonical letter coverage: **PDF 024–400**; PDF 401 is non-letter back cover
- Full-volume Tamil structural audit: **PASS — complete**; report: [`FULL_VOLUME_STRUCTURAL_AUDIT.md`](FULL_VOLUME_STRUCTURAL_AUDIT.md)
- Full-volume second visual/textual-fidelity verification: **PASS — PDF 001–401 / 401 complete**; closure report: [`FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md)
- Cumulative second-pass corrections: **159 canonical pages / 274 spans**
- Letters **0001–0110** have complete second-pass source-page coverage
- Source-pagination anomaly: printed page number **39** is skipped between PDF 039 and PDF 040, with continuous text
- Letter 0063 has no printed date and remains undated rather than inferred
- Printed-contents wording remains literal where it differs from actual heading pages; letter 0109 contents `அவள் ஒரு தொடற்கதை!` differs from actual PDF-392 heading `அவள் ஒரு தொடர்கதை!`
- Legacy bilingual records preserved unchanged: **110 / 110** under `../volume-1/`
- Canonically migrated English records: **110 / 110**
- Canonically source-checked English records: **110 / 110**
- Completed canonical English range: **0001–0110**
- Bilingual-aligned canonical English records: **50 / 110**
- Completed bilingual-alignment range: **0001–0050**
- Alignment-driven English prose corrections: **2** — letters 0014 and 0043
- Verified canonical English records: **0 / 110**
- Editorially reviewed canonical English records: **0 / 110**

## English source-check reports

- [`translations/en/SOURCE_CHECK_0001_0010.md`](translations/en/SOURCE_CHECK_0001_0010.md)
- [`translations/en/SOURCE_CHECK_0011_0020.md`](translations/en/SOURCE_CHECK_0011_0020.md)
- [`translations/en/SOURCE_CHECK_0021_0030.md`](translations/en/SOURCE_CHECK_0021_0030.md)
- [`translations/en/SOURCE_CHECK_0031_0040.md`](translations/en/SOURCE_CHECK_0031_0040.md)
- [`translations/en/SOURCE_CHECK_0041_0050.md`](translations/en/SOURCE_CHECK_0041_0050.md)
- [`translations/en/SOURCE_CHECK_0051_0060.md`](translations/en/SOURCE_CHECK_0051_0060.md)
- [`translations/en/SOURCE_CHECK_0061_0070.md`](translations/en/SOURCE_CHECK_0061_0070.md)
- [`translations/en/SOURCE_CHECK_0071_0080.md`](translations/en/SOURCE_CHECK_0071_0080.md)
- [`translations/en/SOURCE_CHECK_0081_0090.md`](translations/en/SOURCE_CHECK_0081_0090.md)
- [`translations/en/SOURCE_CHECK_0091_0100.md`](translations/en/SOURCE_CHECK_0091_0100.md)
- [`translations/en/SOURCE_CHECK_0101_0110.md`](translations/en/SOURCE_CHECK_0101_0110.md)

## Bilingual-alignment reports

- [`translations/en/alignment/ALIGNMENT_0001_0010.md`](translations/en/alignment/ALIGNMENT_0001_0010.md) — **PASS**, 0 English prose corrections
- [`translations/en/alignment/ALIGNMENT_0011_0020.md`](translations/en/alignment/ALIGNMENT_0011_0020.md) — **PASS after 1 English prose correction**
- [`translations/en/alignment/ALIGNMENT_0021_0030.md`](translations/en/alignment/ALIGNMENT_0021_0030.md) — **PASS**, 0 English prose corrections
- [`translations/en/alignment/ALIGNMENT_0031_0040.md`](translations/en/alignment/ALIGNMENT_0031_0040.md) — **PASS**, 0 English prose corrections
- [`translations/en/alignment/ALIGNMENT_0041_0050.md`](translations/en/alignment/ALIGNMENT_0041_0050.md) — **PASS after 1 English prose correction**
- [`translations/en/alignment/ALIGNMENT_MANIFEST.csv`](translations/en/alignment/ALIGNMENT_MANIFEST.csv) — authoritative record-level alignment ledger
- [`translations/en/alignment/PROGRESS.md`](translations/en/alignment/PROGRESS.md) — active alignment boundary

Alignment corrections so far:

- **0014** — preserves Tamil's separation of political swagger from the separately stronger armed-violence condemnation.
- **0043** — Tamil `ஒன்று மட்டும் மறவாதே` is now correctly rendered **“Do not forget this one thing:”** rather than the earlier opposite imperative **“Forget only this one thing:”**.

The **0041–0050** alignment batch otherwise required no English prose correction. Controls reconfirmed include the Beggars' Rehabilitation Fund appeal; anti-violence sequence; complete Indira Congress accusation list; Madurai conference material; `நாடு + அகம் = நாடகம்`; printed `சென்னை. / 10.10.1972` and **25 of 33** in 0048; Anna's 1961 reply; and *Navasakthi* chronology/figures.

## High-value source controls retained across migration

- Letter 0002 restores the complete Kamaraj Deepavali quotation from scan-verified PDF 030.
- Letter 0010 follows scan-supported `ரன்னர்` / **Runner Cup**, not stale legacy `Rainer`.
- Letter 0018 preserves deliberate censorship without reconstruction; 0019 restores scan-visible material absent from the legacy reading copy; 0020 excludes non-authorial library marks.
- Letter 0028 preserves the source-printed date **28-12-1968** despite conflicting legacy metadata.
- Letter 0036 retains `சி. பி. சி.` / `C. P. C.` without speculative expansion; 0037 follows scan title `தூங்குவோமா?`.
- Letter 0048 preserves printed `சென்னை. / 10.10.1972` without inferring another composition date.
- Letter 0054 follows source figure **6908**; 0058 follows source date **29-05-1973**.
- Letter 0063 remains undated; 0068 preserves scan-controlled Bharathidasan verse forms; 0070 reproduces the printed English judicial quotation verbatim.
- Letters 0076–0080 preserve the Sixth Finance Commission structure, Periyar analogies/self-critique, `பாடி வீடுகள்` martial image and `கொள்கை மலர்கள்` victory-garland image.
- Letters 0081–0090 preserve state-autonomy, Pongal, labour, railway-strike, birthday and organisational imagery.
- Letters 0091–0100 preserve celebrations, betrayal/state-autonomy arguments, Kamaraj/*Navasakthi*/*Dinamani* passages, police-family lullaby, `மாம்பழ மங்கை`, paired 1799/1972 dates, `முப்பெரும் விழா`, `இரட்டைக்குழல் துப்பாக்கி`, Murasoli Selvam context and *Kalingattuparani* sequence.
- Letters 0101–0110 preserve the five great slogans, N. V. N. emotional passage, hunger-report sequence, *Kalki* arguments, industrial data, `ஆட்சி / மாட்சி`, Jayaprakash satire, actual PDF-392 title `அவள் ஒரு தொடர்கதை!`, opaque `நமப்பார்வதி பதேக்கள்!`, and the full 1949 *கயிற்றில் தொங்கிய கணபதி* quotation through PDF 400.

All canonical English records **0001–0110** contain the full canonical Tamil witness. The dedicated alignment ledger records which records have passed bilingual alignment. No aligned record is thereby promoted to `verified` or editorially reviewed status.

## Source-check gate closure

The **canonical English migration/source-check gate is complete at 110 / 110**.

## Exact next task

Continue the dedicated bilingual-alignment review with canonical English letters **0051–0060**, source PDF / printed pages **214–249**. Compare English directly with the complete canonical Tamil witness, correct only demonstrable correspondence/alignment errors, create `translations/en/alignment/ALIGNMENT_0051_0060.md`, append the record-level results to the alignment manifest, and advance alignment progress to **60 / 110** only after all ten records pass.

Keep volume-level editorial consistency, final translation manifest, release report and release declaration blocked until bilingual alignment is complete.