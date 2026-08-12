# தொகுதி 47 — 15-letter transcription iteration audit

**தணிக்கை நாள்:** 2026-08-12  
**மொத்த canonical பரப்பு:** PDF பக்கங்கள் 1–344  
**இந்த iteration:** PDF/printed பக்கங்கள் 255–344; கடிதங்கள் 3683–3697  
**மூல PDF:** `Vol47.pdf`  
**SHA-256:** `4c151357a822a8855e553de080b311d35934e9d844c81aff168b811cd8fd8558`

## Batch-size exception

Repository default policy ஐந்து complete letters per normal iteration என்கிறது; larger batch user explicit approval இருந்தால் அனுமதிக்கப்படுகிறது. பயனர் **“15 letters in each batch”** என வெளிப்படையாக scope மாற்றத்தை ஒப்புதல் அளித்ததால், இந்த iteration **3683–3697** என்ற 15 complete consecutive letters-ஐ ஒரே atomic batch-ஆகப் பதிவு செய்கிறது.

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–344 அனைத்துக்கும் uninterrupted canonical filename range `page-001.md`–`page-344.md` இருப்பு.
2. புதிய canonical pages **255–344**, மொத்தம் **90**, ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. கடிதங்கள் 3683–3697 அனைத்திற்கும் letter-start heading, salutation, body continuity, closing `அன்புள்ள, மு.க.`, printed date மற்றும் exact end boundary verification.
4. Verified letter ranges: 3683 = 255–259; 3684 = 260–264; 3685 = 265–270; 3686 = 271–276; 3687 = 277–282; 3688 = 283–288; 3689 = 289–295; 3690 = 296–301; 3691 = 302–306; 3692 = 307–312; 3693 = 313–319; 3694 = 320–326; 3695 = 327–332; 3696 = 333–339; 3697 = 340–344.
5. Exactly **15** new chapter records உருவாக்கப்பட்டன; previous letter 3682 next navigation புதிய 3683 chapter-க்கு மாற்றப்பட்டது.
6. `contents/index.md`, `chapters/README.md`, `metadata.yml`, `PROGRESS.md`, Volume 47 `README.md` மற்றும் root `README.md` range/count agreement checked.
7. New page front matter-ல் PDF page = printed page for 255–344; letter-number/date/title mappings verified.
8. Duplicate canonical body, replacement Unicode (`U+FFFD`), zero-width residue மற்றும் new-range internal-link targets checked.
9. Existing source-incomplete letter 3681 மற்றும் missing printed page 252 record மாற்றமின்றி carry forward செய்யப்பட்டது.
10. Existing contents-vs-heading discrepancies for 3663 and 3674 remain preserved without reconciliation.
11. PDF **345** visually inspected only to establish that letter **3698** starts there; `page-345.md` இந்த iteration-இல் உருவாக்கப்படவில்லை, 3698 body சேர்க்கப்படவில்லை.
12. Volume 48 மற்றும் Volume 49 release-state files இந்த iteration-இல் மாற்றப்படவில்லை.
13. English translation files உருவாக்கப்படவில்லை; translation gate remains blocked.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page range | `page-001.md`–`page-344.md` |
| PDF filename continuity | no gap through PDF 344 |
| New canonical pages | 90 — PDF/printed 255–344 |
| New letter records | 15 — letters 3683–3697 |
| New complete letters | 15 |
| Total complete letters | 50 — 3647–3680 and 3682–3697 |
| Source-incomplete letters | 1 — 3681 |
| Source missing printed pages | 1 — printed page 252 |
| Ordinary partial letters | 0 |
| Printed contents rows | 59 — letters 3647–3705 |
| Duplicate new page body | none detected |
| Replacement Unicode | none detected |
| Zero-width residue | none detected |
| New canonical pages visually compared | 90/90 |
| Next boundary | letter 3698 starts PDF 345 / printed 345 |

## Scan-proven readings and preservation decisions

- Letter 3690 preserves the printed quotation containing `“மைனாரிட்டி” தி.மு.க. அரசு ராஜினாமா செய்ய வேண்டும்`.
- Letter 3693 preserves printed constitutional/statutory references including `அரசியல் சாசனச் சட்டப்பிரிவு 348`, `348 (1)` and `1963ஆம் ஆண்டு ஆட்சி மொழிச் சட்டப் பிரிவு 7`.
- Letter 3694 preserves intentional English `(Street House)` on PDF 322.
- Letter 3695 preserves the printed English sentence `(The State also took courageous decisions under my leadership to raise power tariffs after ten years)` on PDF 327 and the printed `(?)` marker on PDF 332.
- Letter 3696 preserves its long quoted passage and the printed Thirukkural quotation forms on PDF 339 rather than silently normalising them.
- Letter 3697 preserves the quoted Rizana Nafeek petition, names, ages, dates and times exactly as transcribed from the scan, ending with printed date `21-1-2013`.
- Printed contents row 3663 versus actual PDF 128 heading and printed contents row 3674 versus actual PDF 203 heading remain separately preserved as previously audited.

## Source gap — printed page 252

The earlier source defect remains unchanged: PDF 252 carries printed page 251 and letter 3681 ends there mid-sentence; the next source page is PDF 253 / printed page 253 and begins letter 3682. Printed page 252 is absent from the only available PDF/edition. No missing continuation, closing or date has been reconstructed.

## Audit-level limitation

This remains an **iteration/batch audit** and first visual comparison of the available scan pages. It is not the full-volume Tamil structural audit, not the later character-by-character second visual verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
