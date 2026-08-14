# தொகுதி 46 — transcription batch audit log

## தொடக்க 25-பக்க batch audit

**தணிக்கை நாள்:** 2026-08-14  
**பரப்பு:** PDF பக்கங்கள் 1–25  
**மூல PDF:** `Vol46.pdf`  
**SHA-256:** `ff88d5a78a5ef4d96888ec2f5a0a3653a4f34b1bfbcb0317b5191242cc72cff9`

### செய்யப்பட்ட சோதனைகள்

1. PDF page count (`402`) மற்றும் byte size (`200631699`) பதிவு.
2. Scan cover/title page மூலம் தொகுதி எண் `46` மற்றும் `05.10.2011–15.08.2012` காலவரம்பு உறுதி.
3. PDF page 3 மூலம் சீதை பதிப்பகம், முதற் பதிப்பு 2022, அச்சுப் பக்கங்கள் 400 உறுதி.
4. முழு PDF searchable-text-layer check: 402/402 pages-லும் usable text layer இல்லை.
5. PDF 1–25 அனைத்துக்கும் uninterrupted `page-001.md`–`page-025.md` இருப்பு.
6. ஒவ்வொரு page Markdown கோப்பிலும் volume, PDF page, printed page, section, letter metadata மற்றும் transcription status front matter இருப்பு.
7. PDF 18–22 அச்சு contents rows அனைத்தும் `contents/index.md`-இல் source order-ல் பதிவு.
8. முதல் கடிதம் 3592-ன் title, salutation, paragraphs மற்றும் PDF 24–25 page boundary scan-க்கு எதிராக visual comparison.
9. PDF pages 5 and 23 blank-page descriptions scan-க்கு எதிராக உறுதி.
10. Chapter links PDF 24–25 வரிசையில் தொடர்ச்சியாக இருப்பு; letter continuation வெளிப்படையாகப் பதிவு.
11. Page-body hash comparison: இந்த batch-இல் duplicate canonical body இல்லை.
12. Unicode replacement marker (`U+FFFD`), zero-width OCR residue, தவறான page-number discontinuity மற்றும் broken internal link இல்லை.
13. PDF page 26 canonical text இந்த commit tree-இல் இல்லை என்று சரிபார்க்கப்பட்டது.
14. PDF page rotation metadata முழு source-க்கும் 0°; low-resolution render-hash scan-ல் exact duplicate rendered page இல்லை. இவை full visual audit-க்கு மாற்றாக அல்ல.

### முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected page files | 25 |
| Present page files | 25; `page-001.md`–`page-025.md` |
| PDF page 26 included | இல்லை |
| Printed contents rows | 55 |
| Complete letters | 0 |
| Partial letters | 1 — letter 3592, PDF 24–25 |
| Duplicate canonical page body | none |
| Replacement Unicode / zero-width residue | none |
| Broken internal links | none in completed range |
| Canonical pages visually compared | 25 / 25 |
| English translation | not started; blocked |

### Scan comparison-இல் செய்யப்பட்ட திருத்தங்கள் மற்றும் பாதுகாப்புகள்

- Draft transcription PDF page 25-இல் இருந்த `தொடர் அத்துமீறல்களில் / ஈடுபட்டு வருகிறார்களா` reading scan-க்கு எதிராக திருத்தப்பட்டு, source-supported `தொடர்ந்து அத்துமீறல்களில் / ஈடுபட்டு வருகின்றனர்` என canonical text அமைக்கப்பட்டது.
- PDF page 24 இறுதியின் `நிகழ்ந்` / PDF page 25 தொடக்கத்தின் `துள்ளன.` page-boundary split அமைதியாக இணைக்கப்படாமல் பாதுகாக்கப்பட்டது.
- Contents PDF page 18-இன் unusual wording `உதவாதினி ஒரு தாமதம்; உடனே விழி; தமிழா!` source-இன்படி பாதுகாக்கப்பட்டது.
- Contents PDF page 21-இல் `3637` இரண்டு முறை அச்சிடப்பட்டிருப்பதும், `3636` இல்லாததும் மாற்றமின்றிப் பதிவு செய்யப்பட்டது.
- Contents PDF page 22-இல் `3643`-க்கு அடுத்து `3647` அச்சிடப்பட்டிருப்பதும், `3644–3646` rows இல்லாததும் மாற்றப்படவில்லை.
- Mixed date formatting (`01-01-2012`, `3-2-2012`, `10-6-12`, `05-07-2012` போன்றவை) அச்சில் உள்ளபடியே contents transcription-ல் பாதுகாக்கப்பட்டது.

### பாதுகாக்கப்பட்ட source observations

- PDF page 5 blank; faint reverse-side show-through உள்ளது.
- PDF page 23 blank; contents reverse-side show-through உள்ளது.
- Title/publication/dedication pages-ல் library stamps மற்றும் handwritten library markings உள்ளன; அவை printed edition text-ஆக கலந்து எழுதப்படவில்லை.
- இந்த 1–25 batch-இல் missing, duplicated, rotated, damaged அல்லது confidently unreadable page கண்டறியப்படவில்லை.
- Full-volume missing printed-page / discontinuity assessment இன்னும் pending; இந்த batch audit அதைப் பூர்த்தி செய்ததாகக் கருதப்படாது.

---

## Interrupted-letter completion batch audit — PDF 26–29

**தணிக்கை நாள்:** 2026-08-14  
**பரப்பு:** PDF பக்கங்கள் 26–29 / அச்சுப் பக்கங்கள் 25–28  
**கடிதம்:** 3592 — `என் விருப்பத்தை வெளியிடுகிறேன்!`  
**முன் main HEAD:** `d445c800a6a052b80837aca5a0114c2d5fbfd550`

### Boundary verification

1. PDF 26 scan, PDF 25-ல் நிறுத்தப்பட்ட அதே கடிதம் 3592-ஐ தொடர்கிறது.
2. PDF 29 / printed 28-ல் கடித உரை முடிந்து `அன்புள்ள,`, `மு.க.`, `5-10-2011` என closing/date தெளிவாக உள்ளது.
3. PDF 30 scan boundary check-க்காக மட்டும் பார்க்கப்பட்டது; அது `3593. அய்யகோ! அ.தி.மு.க. ஆட்சியில் அரசு நிலம் அரோகரா!` என அடுத்த கடிதத்தைத் தொடங்குகிறது.
4. இந்த completion tree-இல் `page-030.md` உருவாக்கப்படவில்லை; PDF 30 body transcription சேர்க்கப்படவில்லை.

### Page-level fidelity audit

- `page-026.md` scan-ன் visible body-க்கு வரிவரியாக ஒப்பிடப்பட்டது.
- `page-027.md` scan-ன் visible body-க்கு வரிவரியாக ஒப்பிடப்பட்டது.
- `page-028.md` scan-ன் visible body-க்கு வரிவரியாக ஒப்பிடப்பட்டது.
- `page-029.md` scan-ன் visible body, closing மற்றும் date-க்கு வரிவரியாக ஒப்பிடப்பட்டது.
- PDF 26 இறுதி `கம்யூனிசத்திற்கு` / PDF 27 தொடக்கம் `எதிரான கொள்கையா?` என source page boundary பாதுகாக்கப்பட்டது.
- PDF 27 இறுதி `தலித்துகளுக்காக` / PDF 28 தொடக்கம் `ஒதுக்கப்பட்ட நிலத்தை...` continuation எந்த reconstruction-மும் இன்றி பாதுகாக்கப்பட்டது.
- PDF 28 இறுதி `ஏற்க மாட்டார்கள்` / PDF 29 தொடக்கம் `என்பதில்...` continuation பாதுகாக்கப்பட்டது.

### Scan comparison-இல் உறுதிசெய்யப்பட்ட readings

- PDF 26 working draft-இல் ஏற்பட்டிருக்கக்கூடிய `கம்யூனிஸ்டிற்கு` normalization தவிர்க்கப்பட்டு scan-supported **`கம்யூனிசத்திற்கு`** canonical reading பயன்படுத்தப்பட்டது.
- PDF 26-இன் source spacing **`ஆதி திராவிடர்கள்`** அப்படியே பாதுகாக்கப்பட்டது.
- PDF 28 draft reading scan-க்கு எதிராக சரிபார்க்கப்பட்டபோது source-supported **`ஏற்பாடுகள் எல்லாம் நடைபெறத் தொடங்கியதே, தற்போது`** என்பதே canonical text என உறுதிசெய்யப்பட்டது.
- PDF 28 source spelling **`கடன்ரத்து`** மற்றும் spacing **`தி.மு.க. வை`** regularise செய்யப்படவில்லை.
- PDF 29 closing/date source-இன்படி **`அன்புள்ள,` / `மு.க.` / `5-10-2011`** எனப் பதிவு செய்யப்பட்டது.

### Validation result

| சோதனை | முடிவு |
|---|---|
| New canonical page files | 4; `page-026.md`–`page-029.md` |
| Completed canonical range | `page-001.md`–`page-029.md` |
| PDF page 30 body included | இல்லை |
| Letter 3592 | complete; PDF 24–29 / printed 23–28 |
| Complete letters total | 1 |
| Partial letter after this commit | none |
| Source-incomplete gap in letter 3592 | none observed |
| New pages visually compared | 4 / 4 |
| Replacement Unicode / zero-width residue | none |
| Duplicate canonical page body | none in completed 1–29 range |
| Internal links | valid in updated Volume 46 control/chapter files |
| English translation | not started; blocked |

---

## Post-completion zoom fidelity correction — PDF 26–28

**தணிக்கை நாள்:** 2026-08-14  
**பரப்பு:** Letter 3592 canonical PDF pages 26–28  
**முன் completion commit:** `4f606a836fe89e42b5c41beea7f2b91946182ee8`

Follow-up high-magnification scan review identified six source-fidelity corrections before beginning the first regular five-letter batch:

- PDF 26: `அறியாத செய்திகள்?` → scan-supported `அறியாத செய்திகளா?`.
- PDF 27: `மக்ஸிம் கார்க்கி` → scan-supported `மாக்ஸிம் கார்க்கி`.
- PDF 27: `இருந்திருப்பேனேயானால்` → scan-supported `இருந்திருப்பேனே யானால்`.
- PDF 27: `உள்ளாட்சிமன்றத்` → scan-supported `உள்ளாட்சி மன்றத்`.
- PDF 27: `தண்ணீர்கூட கொடுக்காமல்` → scan-supported `தண்ணீர்கூடக் கொடுக்காமல்`.
- PDF 28: `சிவசுப்ரமணியம்` → scan-supported `சிவசுப்பிரமணியம்`.

The corrections change no letter boundary, printed/PDF page mapping, closing, signature, date, or completion status. PDF 29 required no correction. Letter 3592 remains complete at PDF 24–29 / printed 23–28.

---

## First regular five-letter batch audit — letters 3593–3597 / PDF 30–63

**தணிக்கை நாள்:** 2026-08-14  
**பரப்பு:** PDF பக்கங்கள் **30–63** / அச்சுப் பக்கங்கள் **29–62**  
**கடிதங்கள்:** **3593–3597**  
**batch தொடக்க main HEAD:** `4f606a836fe89e42b5c41beea7f2b91946182ee8`  
**final-tree rebuild parent after concurrent fidelity correction:** `e0b166e482da0ed39c65b2423d0cde384ba3299e`

### Boundary verification

1. **3593** PDF 30 / printed 29-ல் தொடங்கி PDF 36 / printed 35-ல் `அன்புள்ள, / மு.க. / 10-10-2011` என முடிகிறது.
2. **3594** PDF 37 / printed 36-ல் தொடங்கி PDF 44 / printed 43-ல் `அன்புள்ள, / மு.க. / 30-10-2011` என முடிகிறது; தேதிக்குப் பின் அச்சிடப்பட்ட parenthetical குறிப்பு source body-யாகப் பாதுகாக்கப்பட்டது.
3. **3595** PDF 45 / printed 44-ல் தொடங்கி PDF 49 / printed 48-ல் `அன்புள்ள, / மு.க. / 31-10-2011` என முடிகிறது.
4. **3596** PDF 50 / printed 49-ல் தொடங்கி PDF 56 / printed 55-ல் `அன்புள்ள, / மு.க. / 1-11-2011` என முடிகிறது.
5. **3597** PDF 57 / printed 56-ல் தொடங்கி PDF 63 / printed 62-ல் `அன்புள்ள, / மு.க. / 4-11-2011` என முடிகிறது.
6. PDF **64** boundary check-க்காக மட்டும் visually inspected செய்யப்பட்டது; அது **3598 — `என் உடன்பிறப்புகள் ஏமாற மாட்டார்கள்!`** என தொடங்குகிறது. `page-064.md` இந்த batch-ல் உருவாக்கப்படவில்லை.

### Visual comparison / scan-proven corrections

- PDF 30–63-இன் **34/34** canonical page bodies source scans-க்கு எதிராக visually compared செய்யப்பட்டன.
- PDF 39-ல் date **`11-5-1999`** scan-க்கு எதிராக உறுதிசெய்யப்பட்டது; printed English quotation capitalization/wording source-இன்படி பாதுகாக்கப்பட்டது.
- PDF 43-ல் scan-supported பெயர் **`சோழநம்பியார்`** மற்றும் wording **`தூக்குத் தண்டனையிலிருந்து`** canonical-ல் அமைக்கப்பட்டது.
- PDF 45 actual title **`உதவாதினி ஒரு தாமதம்; உடனே விழி; தமிழா!`** scan-இன்படி உறுதிசெய்யப்பட்டது.
- PDF 47-இன் புறநானூறு பாடல் தனியாக high-resolution scan-க்கு எதிராக line-by-line checked செய்யப்பட்டது; OCR-induced letter substitutions நீக்கப்பட்டன.
- PDF 49 இறுதி exhortation source-ல் **`உதவாதினி ஒரு தாமதம்; உடனே விழி; தமிழ!`** என அச்சிடப்பட்டுள்ளது. Heading/contents-இன் `தமிழா!` வடிவத்துடன் force-match செய்யப்படவில்லை.
- PDF 50-ல் OCR-generated malformed Unicode readings scan-க்கு எதிராக `கட்சியினர்`, `உறுப்பினர்` என source-supported glyphs-ஆக சரிசெய்யப்பட்டன.
- PDF 52-ல் `அதில்` மற்றும் `அளித்ததால்தான்`; PDF 54-ல் **`16 ஓட்டு`** scan-க்கு எதிராக உறுதிசெய்யப்பட்டன.
- PDF 58-ல் `நான்`, `மருத்துவப் பல்கலைக்`, `வெங்கட்ராமன் பல்கலைக்` readings scan-க்கு எதிராக திருத்தப்பட்டன.
- PDF 60-ல் running header OCR residue canonical body-யிலிருந்து நீக்கப்பட்டு, source-supported `என்றமைத்திடும் வகையில்` reading பாதுகாக்கப்பட்டது.
- PDF 63 bullet list, closing மற்றும் date scan-க்கு எதிராக உறுதிசெய்யப்பட்டன.

### Preserved source-specific forms / anomalies

- 3595: heading/contents `தமிழா!`, final exhortation `தமிழ!` — இரண்டும் source-supported; anomaly documented, not normalized.
- 3596: source-specific **`25ந்தேதி`** wording மற்றும் PDF 53 unusual name **`அய்ரசி`** மாற்றப்படவில்லை.
- 3594 PDF 44 post-date parenthetical note letter body-யிலிருந்து நீக்கப்படவில்லை.
- Mixed spacing around abbreviations, dates, punctuation and source quotation forms silently regularise செய்யப்படவில்லை.
- இந்த PDF 30–63 batch-இல் genuinely missing, duplicated, rotated, damaged அல்லது confidently illegible source page எதுவும் காணப்படவில்லை.

### Validation result

| சோதனை | முடிவு |
|---|---|
| New canonical page files | 34; `page-030.md`–`page-063.md` |
| Completed canonical range | `page-001.md`–`page-063.md` |
| Complete letters in this batch | exactly 5 — 3593, 3594, 3595, 3596, 3597 |
| Complete letters cumulative | 6 — 3592–3597 |
| Partial letter after batch | none |
| PDF page 64 canonical body included | இல்லை |
| New pages visually compared | 34 / 34 |
| Replacement Unicode (`U+FFFD`) | none |
| Zero-width / format-control residue | none |
| Duplicate canonical body | none in new 30–63 batch |
| Chapter navigation | verified for 3592–3597 |
| English translation | not started; blocked |

---

## Post-batch source-fidelity correction — PDF 60, 61, 63

**தணிக்கை நாள்:** 2026-08-14  
**பரப்பு:** Letter 3597 canonical PDF pages 60, 61 and 63  
**முன் regular-batch commit:** `697b205c835735c0ce0c0da7e048b7135498773c`

Follow-up magnified scan review found four transcription-level fidelity corrections. These do not change any letter boundary, date, title, closing, page mapping or completion status:

- PDF 60: `அம்பேத்கர்` → scan-supported **`அம்பேத்கார்`**.
- PDF 61: `சின்னங்கள் தான்!` → scan-supported **`சின்னங்கள்தான்!`**.
- PDF 61: `உயர்த்துவதற் காக` → scan-supported **`உயர்த்துவதற்காக`**.
- PDF 63: restored the source-printed dash in **`தொடங்கப்பட்ட -`** immediately before the bullet list.

The affected pages were rechecked directly against magnified source scans. Letter 3597 remains complete at PDF 57–63 / printed 56–62. The next canonical page remains PDF 64, letter 3598.

## Pending

இந்த audit log இன்னும் **iteration/batch audit** மட்டுமே. PDF 64–402 transcription, full-volume Tamil structural audit, second visual verification மற்றும் translation textual-fidelity gates pending. English translation unlock ஆகவில்லை.
