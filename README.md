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

### இயல்பான transcription வரிசை

1. புதிய தொகுதியில் முதலில் **PDF 001–025** மட்டும்.
2. பக்கம் 25 கடிதத்தின் நடுவில் முடிந்தால், அடுத்த commit-ல் பக்கம் 26 முதல் அதே கடிதத்தை முடித்தல்.
3. அதன் பின்னர் இயல்பாக **ஐந்து முழுமையான தொடர்ச்சியான கடிதங்கள் = ஒரு atomic commit**.
4. ஒவ்வொரு iteration-க்கும் scan comparison, ஐந்து chapter records, structural updates, batch audit மற்றும் exact next-page/letter record கட்டாயம்.
5. ஆறாவது கடிதத்தின் ஒரு பகுதியை ஐந்து-letter iteration-ல் சேர்க்கக் கூடாது.
6. முழுத் Tamil volume audit முடியும் முன் English translation தொடங்காது.

Volume 49 reference implementation ஆகும்; ஆனால் ஒவ்வொரு பழைய தொகுதியின் அச்சு அமைப்பு, கடித எண்ணிக்கை, தேதி, மொழிநடை மற்றும் scan quality தனியாகச் சரிபார்க்கப்பட வேண்டும்.

## தற்போதைய நிலை

| தொகுதி | காலவரம்பு | PDF பக்கங்கள் | மின்னாக்கப்பட்ட PDF பக்கங்கள் | முழுமையான கடிதங்கள் | English translation |
|---|---|---:|---:|---:|---:|
| 47 | 19.08.2012–19.02.2013 | 401 | 1–96 | 11 (கடிதங்கள் 3647–3657) | not started; blocked pending Tamil audit |
| 48 | 20.02.2013–31.05.2013 | 402 | 1–325 | 46 (கடிதங்கள் 3706–3751) | not started; blocked pending Tamil audit |
| 49 | 01.06.2013–10.10.2013 | 402 | 1–402 | 53 (கடிதங்கள் 3764–3816) | 53 / 53 verified; editorial release complete |

தொகுதி 47-இன் தற்போதைய நிலைக்கு [Volume 47 README](volumes/volume-47/README.md) மற்றும் [iteration audit](volumes/volume-47/AUDIT.md) பார்க்கவும்.

தொகுதி 48-இன் தற்போதைய நிலைக்கு [Volume 48 README](volumes/volume-48/README.md) மற்றும் [iteration audit](volumes/volume-48/AUDIT.md) பார்க்கவும்.

தொகுதி 49-இன் audit விவரங்களுக்கு [முழுத் தொகுதி தணிக்கை அறிக்கை](volumes/volume-49/AUDIT.md) பார்க்கவும்.

English translation முறைக்கு [Translation Plan](volumes/volume-49/TRANSLATION_PLAN.md) மற்றும் [Volume 49 English Index](volumes/volume-49/translations/en/README.md) பார்க்கவும்.
