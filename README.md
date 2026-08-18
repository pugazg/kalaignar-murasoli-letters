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
- ஒவ்வொரு translation batch-க்கும் முன், தொடர்புடைய ஒவ்வொரு Markdown பக்கமும் அதன் PDF scan-உடன் visually compared செய்து textual-fidelity audit செய்யப்படும்.

## தொகுதிகள் 1–48 — முதன்மை செயல்முறை

மீதமுள்ள 48 PDF தொகுதிகளுக்கான source intake, folder structure, page transcription, contents/chapter preservation, Tamil audit, English translation, bilingual alignment, editorial review, manifest, release validation மற்றும் Git hygiene ஆகிய முழு வழிமுறைகளுக்கு:

- [Master Processing Guide — Volumes 1–48](VOLUME_PROCESSING_GUIDE.md)
- [Mandatory Volume Transcription Batching Policy](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md)
- [Quick Tamil Transcription Rules](TRANSCRIPTION_GUIDE.md)
- [Future Volume Work Guidelines](FUTURE_VOLUME_WORK_GUIDELINES.md)
- [Project Handover](PROJECT_HANDOVER.md)
- [Reusable Prompt — Start or Continue the Next Volume](START_NEXT_MURASOLI_VOLUME_PROMPT.md)

`VOLUME_PROCESSING_GUIDE.md`, `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`, மற்றும் `TRANSCRIPTION_GUIDE.md` ஆகியவை controlling repository policies. புதிய future-work documents அவற்றை operational continuation / handover நோக்கில் ஒருங்கிணைக்கின்றன; conflict ஏற்பட்டால் controlling policies முன்னுரிமை பெறும்.

### இயல்பான transcription வரிசை

1. புதிய தொகுதியில் முதலில் **PDF 001–025** மட்டும்.
2. பக்கம் 25 கடிதத்தின் நடுவில் முடிந்தால், அடுத்த commit-ல் பக்கம் 26 முதல் அதே கடிதத்தை முடித்தல்.
3. அதன் பின்னர் இயல்பாக **ஐந்து முழுமையான தொடர்ச்சியான கடிதங்கள் = ஒரு atomic commit**.
4. ஒவ்வொரு iteration-க்கும் scan comparison, chapter records, structural updates, batch audit மற்றும் exact next-page/letter record கட்டாயம்.
5. இயல்பான ஐந்து-letter batch-ஐ விட பெரிய scope explicit user approval-உடன் மட்டுமே பயன்படுத்தப்படும்; documented end-of-volume/source exception-ல் smaller batch பயன்படுத்தலாம்.
6. முழுத் Tamil volume audit முடியும் முன் English translation தொடங்காது.

**Volume 1-specific override:** Volume 01 canonical migration/review work uses **10 complete consecutive letters per regular iteration**. The user explicitly approved one expanded **20-letter** iteration for letters **0057–0076**. This does not permanently change the regular Volume 1 cadence; later regular work returns to 10 letters unless separately instructed.

Volume 49 reference implementation ஆகும்; ஆனால் ஒவ்வொரு பழைய தொகுதியின் அச்சு அமைப்பு, கடித எண்ணிக்கை, தேதி, மொழிநடை மற்றும் scan quality தனியாகச் சரிபார்க்கப்பட வேண்டும்.

## தற்போதைய நிலை

| தொகுதி | காலவரம்பு | PDF பக்கங்கள் | மின்னாக்கப்பட்ட PDF பக்கங்கள் | முழுமையான கடிதங்கள் | English translation |
|---|---|---:|---:|---:|---:|
| 01 | 22.10.1968–01.12.1974 | 401 | **1–401 canonical transcription complete; full-volume Tamil structural audit PASS; full 401-page visual/textual-fidelity audit PASS** | **110 / 110 complete; 0001–0110; printed pagination skips number 39 while text remains continuous** | **legacy 110 bilingual records preserved under `volume-1`; canonical English migration/source-checking complete — 110 / 110; bilingual alignment COMPLETE — 110 / 110 PASS; 4 cumulative alignment-driven prose/quotation corrections; volume-level English editorial consistency is next** |
| 46 | 05.10.2011–15.08.2012 | 402 | **1–402 complete; structural audit + second visual/textual-fidelity verification complete** | **55 actual source records**; source numbering omits 3636 and 3644–3646 and prints 3637 twice | **55 / 55 verified; editorial review + 55-row manifest + final release report complete** |
| 47 | 19.08.2012–19.02.2013 | 401 | **1–401 complete; Tamil structural/fidelity gates complete** | **59 records; 3681 source-incomplete because printed page 252 is absent** | **59 / 59 bilingual-aligned; editorial review + manifest + final release report complete; release-ready within surviving source** |
| 48 | 20.02.2013–31.05.2013 | 402 | 1–402 | 58 (கடிதங்கள் 3706–3763) | **58 / 58 verified; editorial release complete** |
| 49 | 01.06.2013–10.10.2013 | 402 | 1–402 | 53 (கடிதங்கள் 3764–3816) | **53 / 53 verified; editorial release complete** |

தொகுதி 01 canonical migration நிலைக்கு [Volume 01 README](volumes/volume-01/README.md), [full-volume structural audit](volumes/volume-01/FULL_VOLUME_STRUCTURAL_AUDIT.md), [full-volume textual-fidelity audit](volumes/volume-01/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md), [English migration progress](volumes/volume-01/translations/en/PROGRESS.md), [bilingual alignment progress](volumes/volume-01/translations/en/alignment/PROGRESS.md), [alignment manifest](volumes/volume-01/translations/en/alignment/ALIGNMENT_MANIFEST.csv), [second-pass fidelity reports](volumes/volume-01/translations/en/) மற்றும் [legacy migration audit](volumes/volume-1/MIGRATION_AUDIT.md) பார்க்கவும். பழைய `volumes/volume-1/` bilingual/audit material provenance ஆக மாற்றமின்றி பாதுகாக்கப்படுகிறது.

தொகுதி 46-இன் தற்போதைய நிலைக்கு [Volume 46 README](volumes/volume-46/README.md), [full-volume Tamil audit](volumes/volume-46/AUDIT.md), [English workspace](volumes/volume-46/translations/en/README.md), [translation manifest](volumes/volume-46/translations/en/TRANSLATION_MANIFEST.csv), மற்றும் [final release report](volumes/volume-46/translations/en/RELEASE_REPORT.md) பார்க்கவும்.

தொகுதி 47-இன் தற்போதைய நிலைக்கு [Volume 47 README](volumes/volume-47/README.md), [full-volume Tamil structural audit](volumes/volume-47/AUDIT.md), [English translation progress](volumes/volume-47/translations/en/PROGRESS.md) மற்றும் final release records பார்க்கவும்.

தொகுதி 48-இன் தற்போதைய நிலைக்கு [Volume 48 README](volumes/volume-48/README.md) மற்றும் [iteration audit](volumes/volume-48/AUDIT.md) பார்க்கவும்.

தொகுதி 49-இன் audit விவரங்களுக்கு [முழுத் தொகுதி தணிக்கை அறிக்கை](volumes/volume-49/AUDIT.md) பார்க்கவும்.

English translation முறைக்கு Volume 47-க்கு [Translation Plan](volumes/volume-47/TRANSLATION_PLAN.md) மற்றும் Volume 49 reference implementation-க்கு [Translation Plan](volumes/volume-49/TRANSLATION_PLAN.md) பார்க்கவும்.
