# தொகுதி 49 — முழுத் தொகுதி தணிக்கை

**தணிக்கை நாள்:** 2026-08-04  
**தணிக்கை செய்யப்பட்ட நிலை:** `first-pass-complete`  
**மூல PDF:** `TVA_BOK_0065839_கலைஞரின்_கடிதங்கள்_தொகுதி_49.pdf`  
**மூல SHA-256:** `02a7b94a67497bbc39b4664eb232caf6b6c52d3c3367a722a85f943501749dfd`

## தணிக்கையின் பரப்பு

இந்த audit, தொகுதி 49-இன் முழு repository-யையும் பின்வரும் அடுக்குகளில் சோதித்தது:

1. PDF மற்றும் repository பக்க எண்ணிக்கை / தொடர்ச்சி
2. ஒவ்வொரு page Markdown கோப்பின் front matter
3. கடித எண், தலைப்பு, தேதி, அச்சுப் பக்கம் மற்றும் PDF பக்க வரம்பு
4. உள்ளடக்க அட்டவணை, chapter index மற்றும் chapter navigation இணக்கத்தன்மை
5. 53 கடிதங்களின் தொடக்கப் பக்கங்களை மூலப் படத்துடன் visual comparison
6. 53 கடிதங்களின் இறுதிப் பக்கங்களில் கையொப்பம் / தேதி / சிறப்பு முடிவு visual comparison
7. அனைத்து letter pages-க்கும் image-ink-density எதிர் transcription-length completeness scan
8. completeness scan-இல் மிகப் பெரிய 20 outlier பக்கங்களுக்கு fresh independent OCR comparison
9. Latin / English உரை உள்ள 44 பக்கங்களுக்கு fresh independent OCR cross-check
10. Unicode control / replacement character, duplicate body மற்றும் file duplication scan

## முடிவுகள்

| சோதனை | முடிவு |
|---|---|
| PDF பக்கங்கள் | 402 |
| page Markdown கோப்புகள் | 402; `page-001.md` முதல் `page-402.md` வரை இடைவெளியின்றி உள்ளன |
| கடிதப் பக்கங்கள் | PDF 24–401; 378 பக்கங்கள் |
| கடிதங்கள் | 53; 3764–3816 இடைவெளியின்றி உள்ளன |
| chapter கோப்புகள் | 53; ஒவ்வொரு கடிதத்திற்கும் ஒன்று |
| chapter page links | அனைத்து வரம்புகளும் தொடர்ச்சியாகவும் சரியாகவும் உள்ளன |
| contents rows | 53; தலைப்பு மற்றும் தொடக்க அச்சுப் பக்கங்கள் chapter metadata-ஐப் பொருந்துகின்றன |
| duplicate page body | எதுவும் இல்லை |
| invalid / replacement Unicode | எதுவும் இல்லை |
| மூல PDF hash | metadata-வில் உள்ள SHA-256-ஐப் பொருந்துகிறது |
| title-page visual check | 53 / 53 பொருந்தின |
| ending-page visual check | 53 / 53 பொருந்தின |
| completeness correlation | image ink density மற்றும் text length இடையே `0.969` |
| 20 completeness outliers | normalized fresh-OCR agreement `98.4%–99.5%`; missing passage கண்டறியப்படவில்லை |
| 44 Latin / English pages | fresh OCR cross-check செய்யப்பட்டது; missing passage கண்டறியப்படவில்லை |

## சிறப்பு குறிப்புகள்

- கடிதம் **3775** வழக்கமான `அன்புள்ள, மு.க.` கையொப்பத்துடன் முடியவில்லை. மூலத்தில் `***` மற்றும் `16-07-2013` தேதி மட்டுமே உள்ளது; repository அதையே பாதுகாக்கிறது.
- கடிதம் **3770**-இன் மூல தேதி `30-6-2016`. தொகுதியின் 2013 காலவரம்புடன் முரண்பட்டாலும், source typo மாற்றப்படவில்லை.
- பக்கம் 189-இல் காணப்படும் `Goverflouisleiro` என்ற அசாதாரண Latin string மூல அச்சிலேயே இருப்பது visual check மூலம் உறுதிசெய்யப்பட்டது; அது அமைதியாகத் திருத்தப்படவில்லை.
- பக்கம் 402 பின் அட்டையாகவும், PDF பக்கம் 23 வெற்றுப் பக்கமாகவும் சரியாகப் பதிவு செய்யப்பட்டுள்ளன.

## இந்த audit-இல் செய்யப்பட்ட திருத்தங்கள்

- `metadata.yml`-இல் இருந்த பழைய `transcription_page_range: "1-31"` மற்றும் `in-progress` நிலை புதுப்பிக்கப்பட்டது.
- கடிதங்கள் 3764–3774 chapter பதிவுகளில் தேதி label ஒரே வடிவில் அமைக்கப்பட்டது.
- கடிதங்கள் 3767, 3768, 3770–3774-இன் chapter display dates மூல அச்சின் zero-padding-ஐ அப்படியே பிரதிபலிக்கத் திருத்தப்பட்டன.
- இந்த audit அறிக்கை மற்றும் முன்னேற்றப் பதிவு சேர்க்கப்பட்டது.
- audit செய்ய உருவாக்கப்பட்ட temporary export files repository-யிலிருந்து அகற்றப்பட்டன.

## மீதமுள்ள தனிப் பணி

இந்த full-volume audit, structure, metadata, source boundaries, titles, endings மற்றும் automated completeness-ஐ முழுமையாகச் சோதித்துள்ளது. இருப்பினும் **ஒவ்வொரு உட்பக்கத்தின் ஒவ்வொரு எழுத்தையும் மூல scan-க்கு எதிராக மனிதர் character-by-character பார்க்கும் தனி second visual-verification pass** இன்னும் pending ஆகும்.
