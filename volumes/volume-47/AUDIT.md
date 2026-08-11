# தொகுதி 47 — five-letter transcription iteration audit

**தணிக்கை நாள்:** 2026-08-11  
**மொத்தப் பரப்பு:** PDF பக்கங்கள் 1–161  
**இந்த iteration:** PDF பக்கங்கள் 128–161; கடிதங்கள் 3663–3667  
**மூல PDF:** `Vol47.pdf`  
**SHA-256:** `4c151357a822a8855e553de080b311d35934e9d844c81aff168b811cd8fd8558`

## செய்யப்பட்ட சோதனைகள்

1. PDF 1–161 அனைத்துக்கும் uninterrupted `page-001.md`–`page-161.md` canonical range இருப்பு.
2. புதிய canonical pages 128–161 ஒவ்வொன்றும் rendered scan-உடன் visual comparison.
3. கடிதங்கள் 3663–3667 அனைத்துக்கும் title, address, body, closing, signature, printed date மற்றும் next-letter boundary verification.
4. ஐந்து chapter records, chapter index, contents boundaries, metadata, progress மற்றும் volume/root status agreement.
5. புதிய 34 page files-க்கு front-matter/page-number/printed-page/letter mapping validation.
6. Duplicate canonical body, replacement Unicode (`U+FFFD`) மற்றும் completed-range broken-link checks.
7. PDF page 162 visually inspected; கடிதம் 3668 அங்கே தொடங்குவது உறுதி செய்யப்பட்டது. Page 162 இந்த iteration-இல் சேர்க்கப்படவில்லை.
8. Volume 48 release files இந்த iteration-இல் மாற்றப்படவில்லை.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Expected canonical page range | `page-001.md`–`page-161.md` |
| Continuity | no gap through PDF 161 |
| New pages in this iteration | 34 — PDF 128–161 |
| New complete letters | 5 — letters 3663–3667 |
| Total complete letters | 21 — letters 3647–3667 |
| Partial letters | 0 |
| Printed contents rows | 59 — letters 3647–3705 |
| New chapter records | 5 |
| Duplicate new page body | none detected |
| Replacement Unicode | none detected |
| Broken internal links | none detected in completed range |
| New canonical pages visually compared | 34/34 |
| Next boundary | letter 3668 starts PDF 162 / printed 161 |

## Scan-proven readings and preservation decisions

- OCR batch attempts did not produce a usable result; rendered page images controlled the canonical text throughout this iteration.
- Printed contents row 3663 reads `நெஞ்சைத் துளைத்திடும் கொடுமை இது!`, while the actual heading on PDF page 128 reads `நெஞ்சைத் துளைத்திடும் தொடர்கதை இது!`. The contents wording remains in `contents/index.md`; the actual heading controls the page and chapter records.
- Letter 3663 preserves source forms including `காப்பக்கிரகம்`, `தக்கதிருத்தம்` and the quoted material on the 1970 archar law without silent modernisation.
- Letter 3664 preserves the Sethu Samudram committee history, the numbered 13-point sequence, distances/cost figures, and source-specific forms such as `சரி. ஜான்கூடே`, `செல்லவடிவம்`, `பனிரெண்டு`, `பொருளாதாரரீதியாக` and `வாய்ப்பிரசாதமாக`.
- Letter 3665 preserves printed `(?)` markers, source-specific wording, and the English headlines `Palanimanickam’s spat with Baalu comes out in open` and `Two DMK Leaders locked in turf battle - Baalu,Palanimanickam Spar Over Rail Projects`.
- Letter 3666 preserves the source wording around Sri Lankan Tamil displacement, the war memorial/museum description and the `டெசோ` resolution references; source anomalies were not silently corrected.
- Letter 3667 preserves power-project dates, costs and capacities, the total `7798` MW figure, and the source `(?)` marker. PDF page 157 genuinely prints both a malformed paragraph and a following clearer paragraph; both are retained rather than treating one as an OCR duplicate.
- PDF page 162 was inspected only to establish the next boundary and was not transcribed or included in this iteration.

## பாதுகாக்கப்பட்ட source observations

- PDF page 5 is blank with faint reverse-side show-through.
- PDF page 23 is blank with faint reverse-side contents show-through.
- Library stamps and handwritten library markings appear on title/publication/dedication pages and remain factual descriptions only.
- No missing, duplicated, rotated, damaged or illegible source page was observed in PDF 1–161.

## Audit-level limitation

This is an **iteration/batch audit** and first visual comparison, not the full-volume Tamil structural audit, not the later character-by-character second visual verification, and not the mandatory textual-fidelity audit that unlocks translation. English translation remains blocked.
