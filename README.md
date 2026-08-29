# கலைஞரின் முரசொலி கடிதங்கள் — பக்கவாரி மின்னாக்கம்

இந்த repository, **கலைஞரின் கடிதங்கள்** தொகுதிகளை PDF பக்க வரிசை மாறாமல் Markdown வடிவில் மின்னாக்குவதற்கானது.

- ஒவ்வொரு PDF பக்கமும் தனி Markdown கோப்பாகச் சேமிக்கப்படும்.
- உள்ளடக்க அட்டவணை தனியாகப் பாதுகாக்கப்படும்.
- ஒவ்வொரு கடிதத்திற்கும் `chapters/` கட்டமைப்பு பதிவு இருக்கும்.
- அச்சுப் பிழைகள், source anomalies, punctuation, figures மற்றும் physical boundaries அமைதியாகத் திருத்தப்படாது.
- English bilingual records source-audited canonical Tamil-இலிருந்து உருவாக்கப்படும்; translation/alignment source-ஐ outside knowledge கொண்டு silently correct செய்யக் கூடாது.

## தொகுதிகள் 1–48 — முதன்மை செயல்முறை

- [Master Processing Guide — Volumes 1–48](VOLUME_PROCESSING_GUIDE.md)
- [Mandatory Volume Transcription Batching Policy](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md)
- [Quick Tamil Transcription Rules](TRANSCRIPTION_GUIDE.md)
- [Future Volume Work Guidelines](FUTURE_VOLUME_WORK_GUIDELINES.md)
- [Project Handover](PROJECT_HANDOVER.md)
- [Current Continuation Prompt](NEXT_CHAT_PROMPT.md)
- [Reusable Prompt — Start or Continue the Next Volume](START_NEXT_MURASOLI_VOLUME_PROMPT.md)

`VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, and `TRANSCRIPTION_GUIDE.md` are controlling repository policies.

## தற்போதைய நிலை

| தொகுதி | காலவரம்பு | PDF பக்கங்கள் | Tamil archival status | முழுமையான கடிதங்கள் | English translation |
|---|---|---:|---|---:|---|
| 01 | 22.10.1968–01.12.1974 | 401 | **401 / 401; structural + visual/textual-fidelity PASS** | **110 / 110** | **110 / 110 FINAL RELEASE COMPLETE** |
| 45 | 12.03.2011–27.09.2011 | 402 | **402 / 402; structural PASS; second visual/textual-fidelity PASS; historical 243 pages / 623 spans; combined post-translation tally 243 pages / 624 spans** | **55 / 55; 3537–3591** | **55 / 55 source-checked; 50 / 55 bilingual-aligned; alignment in progress** |
| 46 | 05.10.2011–15.08.2012 | 402 | **complete; structural + second visual/textual-fidelity PASS** | **55 actual source records** | **55 / 55 verified; final release complete** |
| 47 | 19.08.2012–19.02.2013 | 401 | **complete within surviving source** | **59 records; 3681 source-incomplete** | **59 / 59 aligned/reviewed; release-ready within surviving source** |
| 48 | 20.02.2013–31.05.2013 | 402 | **complete** | **58** | **58 / 58 verified; editorial release complete** |
| 49 | 01.06.2013–10.10.2013 | 402 | **complete** | **53** | **53 / 53 verified; editorial release complete** |

## Active work — Volume 45

Volume 45 Tamil archival work is complete: **402 / 402 canonical PDF pages**, **55 / 55 source letters, 3537–3591**, structural audit **PASS**, second direct visual/textual-fidelity audit **PASS**. The historical second-pass tally is **243 corrected canonical page files / 623 correction spans**. Letter 3560 English source-check exposed one residual omission on already-corrected PDF 187; it was directly repaired from the scan, leaving **243 unique corrected pages / 624 combined scan-proven spans**.

English main drafting is complete at **55 / 55 source-checked**. Ten bilingual alignment batches are complete through **3582–3586 / PDF 338–369**. The tenth batch passed **5 / 5**, with **1 English-only correction** and **0 Tamil changes**.

During Letter 3583 alignment, direct scan re-check confirmed that the physical PDF 348→349 source reads `வாக்க` / `எதிரிகளை`. The earlier English “class enemies” silently supplied an unprinted normalization, so the aligned English now conservatively uses **“enemies.”** Canonical Tamil remains unchanged. Letter 3582's Thai/Chithirai/Tamil-New-Year claims remain source-specific, and Letter 3586 retains the scan-proven title `கழக அரசு கடைப்பிடித்த வழியில் காத்திடுக மூவர் உயிர்!`.

Current English QA totals: **55 / 55 source-checked**, **50 / 55 bilingual-aligned**, **0 / 55 editorially reviewed**, **0 / 55 final verified**.

**Exact next activity:** complete the **final bilingual-alignment batch, Letters 3587–3591 / PDF 370–401**. After all five pass and alignment reaches **55 / 55**, the separate volume-level English editorial consistency review becomes the next gate; do not merge it into the alignment iteration.

Volume 45 controls: [README](volumes/volume-45/README.md), [PROGRESS](volumes/volume-45/PROGRESS.md), [AUDIT](volumes/volume-45/AUDIT.md), [metadata](volumes/volume-45/metadata.yml), [translation plan](volumes/volume-45/TRANSLATION_PLAN.md), [English progress](volumes/volume-45/translations/en/PROGRESS.md), [latest alignment review](volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3582_3586.md), [alignment status sidecars](volumes/volume-45/translations/en/alignment-status/README.md), and [translation-discovered Tamil corrections](volumes/volume-45/translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md).
