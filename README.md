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
| 45 | 12.03.2011–27.09.2011 | 402 | **402 / 402; structural PASS; second visual/textual-fidelity PASS; historical 243 pages / 623 spans; combined post-translation tally 243 pages / 624 spans** | **55 / 55; 3537–3591** | **55 / 55 source-checked; 5 / 55 bilingual-aligned; alignment in progress** |
| 46 | 05.10.2011–15.08.2012 | 402 | **complete; structural + second visual/textual-fidelity PASS** | **55 actual source records** | **55 / 55 verified; final release complete** |
| 47 | 19.08.2012–19.02.2013 | 401 | **complete within surviving source** | **59 records; 3681 source-incomplete** | **59 / 59 aligned/reviewed; release-ready within surviving source** |
| 48 | 20.02.2013–31.05.2013 | 402 | **complete** | **58** | **58 / 58 verified; editorial release complete** |
| 49 | 01.06.2013–10.10.2013 | 402 | **complete** | **53** | **53 / 53 verified; editorial release complete** |

## Active work — Volume 45

Volume 45 Tamil archival work is complete: **402 / 402 canonical PDF pages**, **55 / 55 source letters, 3537–3591**, structural audit **PASS**, second direct visual/textual-fidelity audit **PASS**. The historical second-pass tally is **243 corrected canonical page files / 623 correction spans**. Letter 3560 English source-check exposed one residual omission on already-corrected PDF 187; it was directly repaired from the scan, leaving **243 unique corrected pages / 624 combined scan-proven spans**.

The pilot **3537–3539 / PDF 024–049** passed and locked the English style. Ten normal drafting batches plus the final **3590–3591 / PDF 391–401** iteration are complete and source-checked. Current English drafting total: **55 / 55 source-checked**.

The first bilingual-alignment batch **3537–3541 / PDF 024–060** is now complete: **PASS — 5 / 5 aligned**, with **0 English semantic corrections** and **0 Tamil canonical corrections**. The records retain their source-checked drafting status and separately record `bilingual_alignment_status: aligned`. Editorial review and final release verification have not begun.

Current English QA totals: **55 / 55 source-checked**, **5 / 55 bilingual-aligned**, **0 / 55 editorially reviewed**, **0 / 55 final verified**.

**Exact next activity:** align **Letters 3542–3546 / PDF 061–103** as the next five-complete-letter alignment batch. Preserve Letter 3545's source anomaly `112.2006-ல்` and the source-layer exclusion of later library stamp/handwriting on Letter 3546 / PDF 102. Keep the later volume-level English editorial consistency review separate.

Volume 45 controls: [README](volumes/volume-45/README.md), [PROGRESS](volumes/volume-45/PROGRESS.md), [AUDIT](volumes/volume-45/AUDIT.md), [metadata](volumes/volume-45/metadata.yml), [translation plan](volumes/volume-45/TRANSLATION_PLAN.md), [English progress](volumes/volume-45/translations/en/PROGRESS.md), [alignment review 3537–3541](volumes/volume-45/translations/en/BILINGUAL_ALIGNMENT_REVIEW_3537_3541.md), and [translation-discovered Tamil corrections](volumes/volume-45/translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md).
