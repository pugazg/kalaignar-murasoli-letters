# கலைஞரின் முரசொலி கடிதங்கள் — பக்கவாரி மின்னாக்கம்

இந்த repository, **கலைஞரின் கடிதங்கள்** தொகுதிகளை PDF பக்க வரிசை மாறாமல் Markdown வடிவில் மின்னாக்குவதற்கானது.

- ஒவ்வொரு PDF பக்கமும் தனி Markdown கோப்பாகச் சேமிக்கப்படும்.
- உள்ளடக்க அட்டவணை தனியாகப் பாதுகாக்கப்படும்.
- ஒவ்வொரு கடிதத்திற்கும் `chapters/` கட்டமைப்பு பதிவு இருக்கும்.
- அச்சுப் பிழைகள், source anomalies, punctuation, figures மற்றும் physical boundaries அமைதியாகத் திருத்தப்படாது.
- English bilingual records source-audited canonical Tamil-இலிருந்து உருவாக்கப்படும்; translation source-ஐ outside knowledge கொண்டு silently correct செய்யக் கூடாது.

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
| 45 | 12.03.2011–27.09.2011 | 402 | **402 / 402; structural PASS; second visual/textual-fidelity PASS; historical 243 pages / 623 spans; combined post-translation tally 243 pages / 624 spans** | **55 / 55; 3537–3591** | **IN PROGRESS — 3537–3579 source-checked (43 / 55); next 3580–3584** |
| 46 | 05.10.2011–15.08.2012 | 402 | **complete; structural + second visual/textual-fidelity PASS** | **55 actual source records** | **55 / 55 verified; final release complete** |
| 47 | 19.08.2012–19.02.2013 | 401 | **complete within surviving source** | **59 records; 3681 source-incomplete** | **59 / 59 aligned/reviewed; release-ready within surviving source** |
| 48 | 20.02.2013–31.05.2013 | 402 | **complete** | **58** | **58 / 58 verified; editorial release complete** |
| 49 | 01.06.2013–10.10.2013 | 402 | **complete** | **53** | **53 / 53 verified; editorial release complete** |

## Active work — Volume 45

Volume 45 Tamil archival work is complete: **402 / 402 canonical PDF pages**, **55 / 55 source letters, 3537–3591**, structural audit **PASS**, second direct visual/textual-fidelity audit **PASS**. The historical second-pass tally is **243 corrected canonical page files / 623 correction spans**. Letter 3560 English source-check exposed one residual omission on already-corrected PDF 187; it was directly repaired from the scan, leaving **243 unique corrected pages / 624 combined scan-proven spans**.

The pilot **3537–3539 / PDF 024–049** passed and locked the English style. Eight normal drafting batches through **3575–3579 / PDF 275–319** are complete and source-checked. Current English total: **43 / 55 draft-translated and source-checked**, **0 / 55 bilingual-aligned**, **0 / 55 final verified**.

The latest batch preserves Letter 3575's genuine contents/start punctuation difference, Letter 3576's scan-proven `பாரீர்!` title, PDF 290 `18-5-2001`, the complete Letter 3577 law-and-order catalogue, Letter 3578's Housing Board/Jaffer Sait material, and Letter 3579's complete budget figures and printed English passages. No Tamil canonical change was required in 3575–3579.

**Exact next activity:** translate **Letters 3580–3584 / PDF 320–357** as the next normal five-complete-letter English drafting batch, source-check each complete draft, trigger direct scan re-verification if another Tamil discrepancy appears, and keep bilingual alignment as a later distinct QA gate.

Volume 45 controls: [README](volumes/volume-45/README.md), [PROGRESS](volumes/volume-45/PROGRESS.md), [AUDIT](volumes/volume-45/AUDIT.md), [metadata](volumes/volume-45/metadata.yml), [translation plan](volumes/volume-45/TRANSLATION_PLAN.md), [English progress](volumes/volume-45/translations/en/PROGRESS.md), [translation-discovered Tamil corrections](volumes/volume-45/translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md), and [3575–3579 source check](volumes/volume-45/translations/en/DRAFT_SOURCE_CHECK_3575_3579.md).
