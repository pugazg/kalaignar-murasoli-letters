# தொகுதி 46 — தொடக்க 25-பக்க batch audit

**தணிக்கை நாள்:** 2026-08-14  
**பரப்பு:** PDF பக்கங்கள் 1–25  
**மூல PDF:** `Vol46.pdf`  
**SHA-256:** `ff88d5a78a5ef4d96888ec2f5a0a3653a4f34b1bfbcb0317b5191242cc72cff9`

## செய்யப்பட்ட சோதனைகள்

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

## முடிவு

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

## Scan comparison-இல் செய்யப்பட்ட திருத்தங்கள் மற்றும் பாதுகாப்புகள்

- Draft transcription PDF page 25-இல் இருந்த `தொடர் அத்துமீறல்களில் / ஈடுபட்டு வருகிறார்களா` reading scan-க்கு எதிராக திருத்தப்பட்டு, source-supported `தொடர்ந்து அத்துமீறல்களில் / ஈடுபட்டு வருகின்றனர்` என canonical text அமைக்கப்பட்டது.
- PDF page 24 இறுதியின் `நிகழ்ந்` / PDF page 25 தொடக்கத்தின் `துள்ளன.` page-boundary split அமைதியாக இணைக்கப்படாமல் பாதுகாக்கப்பட்டது.
- Contents PDF page 18-இன் unusual wording `உதவாதினி ஒரு தாமதம்; உடனே விழி; தமிழா!` source-இன்படி பாதுகாக்கப்பட்டது.
- Contents PDF page 21-இல் `3637` இரண்டு முறை அச்சிடப்பட்டிருப்பதும், `3636` இல்லாததும் மாற்றமின்றிப் பதிவு செய்யப்பட்டது.
- Contents PDF page 22-இல் `3643`-க்கு அடுத்து `3647` அச்சிடப்பட்டிருப்பதும், `3644–3646` rows இல்லாததும் மாற்றப்படவில்லை.
- Mixed date formatting (`01-01-2012`, `3-2-2012`, `10-6-12`, `05-07-2012` போன்றவை) அச்சில் உள்ளபடியே contents transcription-ல் பாதுகாக்கப்பட்டது.

## பாதுகாக்கப்பட்ட source observations

- PDF page 5 blank; faint reverse-side show-through உள்ளது.
- PDF page 23 blank; contents reverse-side show-through உள்ளது.
- Title/publication/dedication pages-ல் library stamps மற்றும் handwritten library markings உள்ளன; அவை printed edition text-ஆக கலந்து எழுதப்படவில்லை.
- இந்த 1–25 batch-இல் missing, duplicated, rotated, damaged அல்லது confidently unreadable page கண்டறியப்படவில்லை.
- Full-volume missing printed-page / discontinuity assessment இன்னும் pending; இந்த batch audit அதைப் பூர்த்தி செய்ததாகக் கருதப்படாது.

## Pending

இந்த அறிக்கை ஒரு **iteration/batch audit** மட்டுமே. Full-volume Tamil structural audit, later second visual verification, மற்றும் translation textual-fidelity audit ஆகியவை தனித்தனி gates. Letter 3592 PDF page 25-இல் incomplete. English translation unlock ஆகவில்லை.
