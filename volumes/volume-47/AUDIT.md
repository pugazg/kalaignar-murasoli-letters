# தொகுதி 47 — full-volume Tamil structural audit

**தணிக்கை நாள்:** 2026-08-12  
**முழு canonical பரப்பு:** PDF பக்கங்கள் 1–401  
**இறுதி transcription iteration:** PDF/printed பக்கங்கள் 345–400; கடிதங்கள் 3698–3705; PDF 401 பின்அட்டை  
**மூல PDF:** `Vol47.pdf`  
**SHA-256:** `4c151357a822a8855e553de080b311d35934e9d844c81aff168b811cd8fd8558`

## Final batch scope

பயனர் முன்பு **15 letters in each batch** என larger-batch scope-ஐ வெளிப்படையாக ஒப்புதல் அளித்தார். 3697 முடிந்தபின் தொகுதியில் எட்டு கடிதங்களே மீதமிருந்ததால், இறுதி iteration **3698–3705** என்ற எட்டு கடிதங்களையும் PDF/printed **345–400** வரை ஒரே atomic batch-ஆக முடிக்கிறது. PDF **401** ஒரு letter page அல்ல; source-இன் பின்அட்டை என்பதால் one-page/one-Markdown விதிப்படி அதுவும் இந்த final source-completion commit-இல் சேர்க்கப்படுகிறது.

## Full-volume structural checks

1. மூலக் கோப்பு SHA-256 `4c151357a822a8855e553de080b311d35934e9d844c81aff168b811cd8fd8558`, byte size `199112671`, page count **401** என மீண்டும் உறுதி செய்யப்பட்டது.
2. Canonical filename range `page-001.md`–`page-401.md` முழுமையாக இருக்க வேண்டும் என்ற invariant prior iteration audits + final pages மூலம் உறுதி செய்யப்பட்டது; புதிய range **345–401**-இல் 57 files உள்ளன.
3. PDF 18–22 printed contents-இல் உள்ள **59** letter records **3647–3705** அனைத்தும் contents register-இல் உள்ளன.
4. Chapter records மொத்தம் **59**: **58 complete** (3647–3680, 3682–3705) + **1 source-incomplete** (3681).
5. Source-incomplete 3681: PDF 249–252 / printed 248–251 available; printed page **252** source PDF-இல் இல்லை. காணாமற்போன continuation, closing, date ஊகிக்கப்படவில்லை.
6. Letter 3682 PDF/printed 253–254-இல் தெளிவாகத் தொடங்கி முடிகிறது; source gap-க்குப் பிறகு PDF/printed page numbering மீண்டும் ஒன்றாகிறது.
7. Prior batch audits-இல் verified boundaries 3647–3697 carry forward செய்யப்பட்டன; final batch 3698–3705-க்கு ஒவ்வொரு start, body continuity, closing `அன்புள்ள, மு.க.` மற்றும் printed date rendered scan-உடன் ஒப்பிடப்பட்டது.
8. Final verified ranges: 3698 = 345–351; 3699 = 352–358; 3700 = 359–365; 3701 = 366–371; 3702 = 372–377; 3703 = 378–383; 3704 = 384–393; 3705 = 394–400.
9. PDF **401** பின்அட்டை: colour portrait, `1924 - 2018`, publisher/contact block, QR code, `GO 2300`, `ரூ.300`; letter content இல்லை.
10. Final 57 page front-matter records-ல் PDF number/file number agreement; PDF 345–400-க்கு printed page = PDF page; PDF 401-க்கு `printed_page: null`.
11. Final-range canonical bodies duplicate hash check — duplicate இல்லை.
12. Final page/structural files replacement Unicode (`U+FFFD`) check — இல்லை.
13. Final page/structural files Unicode format / zero-width residue check — இல்லை.
14. New chapter page links 345–400, previous/next navigation, contents links மற்றும் chapter-index links synthetic repository path set-க்கு எதிராகச் சரிபார்க்கப்பட்டன.
15. Contents title versus actual heading discrepancies 3663 மற்றும் 3674 தத்தம் source context-இல் மாற்றமின்றிப் பாதுகாக்கப்பட்டுள்ளன.
16. Volume 48 மற்றும் Volume 49 release-state files இந்த final Volume 47 commit-இல் மாற்றப்படக்கூடாது.
17. English translation files உருவாக்கப்படவில்லை; translation status `not-started` ஆகவே உள்ளது.

## முடிவு

| சோதனை | முடிவு |
|---|---|
| Source PDF pages | 401 |
| Canonical expected range | `page-001.md`–`page-401.md` |
| Canonical source coverage | complete for all 401 PDF pages |
| Printed contents rows | 59 — letters 3647–3705 |
| Chapter records | 59 |
| Complete letters | 58 — 3647–3680, 3682–3705 |
| Source-incomplete letters | 1 — 3681 |
| Ordinary partial letters | 0 |
| Source missing printed pages | 1 — printed page 252 |
| Final new canonical pages | 57 — PDF 345–401 |
| Final new letter records | 8 — 3698–3705 |
| Final new complete letters | 8 |
| Duplicate final-range body | none detected |
| Replacement Unicode | none detected |
| Zero-width / format residue | none detected |
| Final pages visually compared | 57/57 |
| Full-volume Tamil structural audit | complete for available source |
| Second visual verification | pending |
| English translation | not started |

## Final batch scan-proven preservation notes

- Letter 3698 preserves source dates, figures and political/economic wording without normalisation.
- Letter 3699 preserves Eelam-related quoted correspondence and reader-response names/locations as printed.
- Letter 3700 preserves the long English `The Hindu` passage and the source's `விஸ்வரூபம்` litigation chronology.
- Letter 3701 preserves `(Elevated Highway)`, printed English headline/quotation and Chennai Port–Maduravoyal project dates/figures.
- Letter 3702 preserves the new Secretariat chronology, court references and source form `“ஜெயா”`.
- Letter 3703 preserves power-project dates, megawatt/rupee figures, `(எம்.ஓ.யூ.)` and `(SEZ)` source forms.
- Letter 3704 preserves Cauvery chronology, `205 டி.எம்.சி.`, `(CauveryAuthority)` and `Karunanidhi Scores Diplomatic Victory` quotation without silent correction.
- Letter 3705 preserves the printed violence-case list, death-penalty/legal references, names, dates and quotations; no external source was used to supplement the text.
- Final visual comparison also corrected draft readings against the scan, including PDF 374 `திரிபுரா ஆளுநர்`, PDF 396 `மாதர் சங்கம்`, PDF 397 `பண்பாட்டுக்கும்`, PDF 399 `தூக்கிலேறிட`, and PDF 401 `அட்டை : ஜெ.ஜெ டிசைன்ஸ்`; these scan-proven forms control the canonical files.

## Source gap — printed page 252

The source defect remains unchanged and explicit: PDF 252 is printed page 251 and ends letter 3681 mid-sentence after `அடிப்படையான வேளாண்மை, வணிகம், சிறுதொழில் மற்றும்`. The next PDF page is printed page 253 and begins letter 3682. Printed page 252 is not present in this only PDF/edition. No reconstruction is present in canonical Tamil.

## Audit-level limitation / next gate

இந்த report **full-volume Tamil structural audit** ஆகும். இது later **second visual verification** அல்லது translationக்கு முன் செய்ய வேண்டிய **textual-fidelity audit** அல்ல. அந்த இரு verification நிலைகளும் தனியாக pending. English translation தொடங்கப்படவில்லை.
