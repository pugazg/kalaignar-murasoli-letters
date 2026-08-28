# கலைஞரின் முரசொலி கடிதங்கள் — பக்கவாரி மின்னாக்கம்

இந்த repository, **கலைஞரின் கடிதங்கள்** தொகுதிகளை PDF பக்க வரிசை மாறாமல் Markdown வடிவில் மின்னாக்குவதற்கானது.

## அடைவு அமைப்பு

```text
volumes/
  volume-49/
    README.md
    metadata.yml
    contents/index.md
    chapters/
    pages/
    translations/en/
```

- ஒவ்வொரு PDF பக்கமும் தனி Markdown கோப்பாகச் சேமிக்கப்படும்.
- நூலின் உள்ளடக்க அட்டவணை (`contents/index.md`) தனியாகப் பாதுகாக்கப்படும்.
- ஒவ்வொரு கடிதம்/அத்தியாயத்திற்கும் `chapters/` அடைவில் கட்டமைப்பு பதிவு இருக்கும்.
- அச்சுப் பிழைகள் அமைதியாகத் திருத்தப்படாது; மூலத்தில் இருப்பதுபோலப் பதிவு செய்து குறிப்பு சேர்க்கப்படும்.
- English translations தெளிவான, non-literary முறையில் Kalaignar-ன் சிந்தனை, வாத வரிசை, அரசியல் விமர்சனம் மற்றும் rhetorical questions-ஐப் பாதுகாக்கும்.
- English bilingual records source-audited canonical Tamil-இலிருந்து உருவாக்கப்பட வேண்டும்; source anomaly வெளியறிவால் silently corrected செய்யப்படாது.

## தொகுதிகள் 1–48 — முதன்மை செயல்முறை

- [Master Processing Guide — Volumes 1–48](VOLUME_PROCESSING_GUIDE.md)
- [Mandatory Volume Transcription Batching Policy](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md)
- [Quick Tamil Transcription Rules](TRANSCRIPTION_GUIDE.md)
- [Future Volume Work Guidelines](FUTURE_VOLUME_WORK_GUIDELINES.md)
- [Project Handover](PROJECT_HANDOVER.md)
- [Current Continuation Prompt](NEXT_CHAT_PROMPT.md)
- [Reusable Prompt — Start or Continue the Next Volume](START_NEXT_MURASOLI_VOLUME_PROMPT.md)

`VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, மற்றும் `TRANSCRIPTION_GUIDE.md` controlling repository policies. Conflict ஏற்பட்டால் அவை முன்னுரிமை பெறும்.

### இயல்பான Tamil transcription வரிசை

1. புதிய தொகுதியில் முதலில் **PDF 001–025** மட்டும்.
2. பக்கம் 25 கடிதத்தின் நடுவில் முடிந்தால், அடுத்த commit-ல் அதே கடிதத்தை முடித்தல்.
3. அதன் பின்னர் இயல்பாக **ஐந்து முழுமையான தொடர்ச்சியான கடிதங்கள் = ஒரு atomic commit**.
4. ஒவ்வொரு iteration-க்கும் scan comparison, chapter records, structural updates, batch audit மற்றும் exact next-page/letter record கட்டாயம்.
5. முழுத் Tamil volume audit முடியும் முன் English translation தொடங்காது.

**Volume 1-specific override:** Volume 01 canonical migration/review work used 10 complete consecutive letters per regular iteration, with one explicitly approved 20-letter batch. அந்த override மற்ற volumes-க்கு தானாக பொருந்தாது.

Volume 49 principal English/reference implementation; Volume 46 source-anomaly/bilingual reference; Volume 47 completed surviving-source alignment/release reference. ஒவ்வொரு volume-இன் source facts தனியாகப் பாதுகாக்கப்பட வேண்டும்.

## தற்போதைய நிலை

| தொகுதி | காலவரம்பு | PDF பக்கங்கள் | Tamil archival status | முழுமையான கடிதங்கள் | English translation |
|---|---|---:|---|---:|---|
| 01 | 22.10.1968–01.12.1974 | 401 | **401 / 401; structural + visual/textual-fidelity PASS** | **110 / 110** | **110 / 110 FINAL RELEASE COMPLETE** |
| 45 | 12.03.2011–27.09.2011 | 402 | **402 / 402; structural PASS; second visual/textual-fidelity PASS; historical 243 pages / 623 spans; combined post-translation tally 243 pages / 624 spans** | **55 / 55; 3537–3591** | **IN PROGRESS — 3537–3564 source-checked (28 / 55); next 3565–3569** |
| 46 | 05.10.2011–15.08.2012 | 402 | **complete; structural + second visual/textual-fidelity PASS** | **55 actual source records** | **55 / 55 verified; final release complete** |
| 47 | 19.08.2012–19.02.2013 | 401 | **complete within surviving source** | **59 records; 3681 source-incomplete** | **59 / 59 aligned/reviewed; release-ready within surviving source** |
| 48 | 20.02.2013–31.05.2013 | 402 | **complete** | **58** | **58 / 58 verified; editorial release complete** |
| 49 | 01.06.2013–10.10.2013 | 402 | **complete** | **53** | **53 / 53 verified; editorial release complete** |

## Active work — Volume 45

Volume 45 Tamil archival work is complete: **402 / 402 canonical PDF pages**, **55 / 55 source letters, 3537–3591**, structural audit **PASS**, second direct visual/textual-fidelity audit **PASS**. The historical second-pass tally is **243 corrected canonical page files / 623 correction spans**. During Letter 3560 English source-check, a residual omission on already-corrected PDF 187 was re-rendered and repaired directly from the scan; the unique corrected-page count remains **243** and the combined scan-proven correction tally is now **624 spans**. Letter 3591 closes at PDF 401 / printed page 400 on `27-9-2011`; PDF 402 is back-cover/publisher matter. The Letter 3576 control-layer `பார்!` reading was withdrawn in favor of scan-proven `பாரீர்!`; the genuine Letter 3575 contents/start punctuation difference remains.

English translation began only after the full Tamil gate was durably verified. The pilot **3537–3539 / PDF 024–049** passed and locked the style. Five normal drafting batches — **3540–3544 / PDF 050–088**, **3545–3549 / PDF 089–122**, **3550–3554 / PDF 123–154**, **3555–3559 / PDF 155–180**, and **3560–3564 / PDF 181–217** — are complete and source-checked. Current English total: **28 / 55 draft-translated and source-checked**, **0 / 55 bilingual-aligned**, **0 / 55 final verified**.

The 3560–3564 source check preserves source-specific material rather than repairing it from outside knowledge, including the scan-restored PDF 187 Wall Street Journal/Oxford Analytica passage, the complete Classical Tamil awards/history sequence, the full Pazha. Nedumaran prison letter, the autobiographical/financial/donation chronology, source `ஒகனேக்கல்`, and PDF 217 `011ஆம் ஆண்டு`.

**Exact next activity:** translate **Letters 3565–3569 / PDF 218–248** as the next normal five-complete-letter English drafting batch, source-check each draft against its full audited canonical Tamil, trigger direct scan re-verification if another Tamil discrepancy appears, and keep bilingual alignment as a later distinct QA gate.

Volume 45 controls: [README](volumes/volume-45/README.md), [PROGRESS](volumes/volume-45/PROGRESS.md), [AUDIT](volumes/volume-45/AUDIT.md), [structural audit](volumes/volume-45/FULL_VOLUME_STRUCTURAL_AUDIT.md), [textual-fidelity audit](volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md), [metadata](volumes/volume-45/metadata.yml), [translation plan](volumes/volume-45/TRANSLATION_PLAN.md), [English progress](volumes/volume-45/translations/en/PROGRESS.md), [translation-discovered Tamil corrections](volumes/volume-45/translations/en/TRANSLATION_DISCOVERED_TAMIL_CORRECTIONS.md), and [3560–3564 source check](volumes/volume-45/translations/en/DRAFT_SOURCE_CHECK_3560_3564.md).

தொகுதி 01 final release நிலைக்கு [Volume 01 README](volumes/volume-01/README.md) மற்றும் அதன் English release controls பார்க்கவும்.

தொகுதி 46-க்கு [Volume 46 README](volumes/volume-46/README.md) மற்றும் English release workspace பார்க்கவும்.

தொகுதி 47-க்கு [Volume 47 README](volumes/volume-47/README.md), [Translation Plan](volumes/volume-47/TRANSLATION_PLAN.md) மற்றும் English release controls பார்க்கவும்.

தொகுதி 48-க்கு [Volume 48 README](volumes/volume-48/README.md) பார்க்கவும்.

தொகுதி 49-க்கு [Volume 49 Audit](volumes/volume-49/AUDIT.md), [Translation Plan](volumes/volume-49/TRANSLATION_PLAN.md) மற்றும் English reference implementation பார்க்கவும்.
