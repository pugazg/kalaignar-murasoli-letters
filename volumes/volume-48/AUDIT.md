# தொகுதி 48 — முழுத் தமிழ் கட்டமைப்பு தணிக்கை

**தணிக்கை நாள்:** 2026-08-08  
**மூல PDF:** `Vol48.pdf`  
**பதிவு செய்யப்பட்ட SHA-256:** `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c`  
**PDF பக்கங்கள்:** 402  
**அச்சுப் பக்கங்கள்:** 400  
**கடிதங்கள்:** 58 — 3706–3763

## முடிவு

**Full-volume Tamil structural audit: PASS.**

இந்தத் தணிக்கை முழுத் தொகுதியின் page/letter/chapter/index கட்டமைப்பு ஒருமைப்பாட்டைச் சரிபார்க்கிறது. இது தனியான எழுத்து-எழுத்து second visual / textual-fidelity audit அல்ல. அந்த audit தற்போது PDF **1–192** வரை முடிந்துள்ளது; PDF **193–402** இன்னும் source-check செய்யப்பட வேண்டும்.

## Fresh source verification

- Local authoritative source `/mnt/data/Vol48(1).pdf` மீண்டும் கணக்கிடப்பட்டது.
- SHA-256: `1f7258b06857fadf3958dc3e9e19eee1ac602e66277d907351701225fcb1bb4c` — repository metadata-வுடன் exact match.
- PDF page count: `402` — repository metadata-வுடன் exact match.
- File size: `214390300` bytes — repository metadata-வுடன் exact match.

## கட்டமைப்பு சோதனைகள்

1. ஆரம்ப batch audit `page-001.md`–`page-025.md` தொடர்ச்சியைச் சரிபார்த்தது; பிந்தைய transcription iteration audits மற்றும் இறுதி remainder audit வழியாக canonical range `page-001.md`–`page-402.md` வரை இடைவெளியின்றி முடிக்கப்பட்டுள்ளது.
2. Canonical page mapping:
   - PDF 1–17 — front/publisher matter
   - PDF 18–22 — printed contents
   - PDF 23 — blank page with faint show-through
   - PDF 24–400 — letters 3706–3763
   - PDF 401 — printed page 400; running header/page number only, otherwise blank with faint show-through
   - PDF 402 — back cover
3. Printed contents identify exactly **58 letters**, and the chapter register contains the same consecutive letter-number range **3706–3763**.
4. Letter-number continuity check: `3763 - 3706 + 1 = 58`; no undocumented letter-number gap exists.
5. Reconciled letter boundaries cover PDF **24–400** continuously, without an undocumented gap or overlap. Each iteration verified the first page, closing/date page and next-letter boundary before integration.
6. Chapter records link to the canonical page sequence rather than duplicating letter text. Previous/next navigation was reconciled at each iteration boundary.
7. `contents/index.md` preserves the wording and date formatting printed in the contents pages; chapter records preserve the wording printed at the actual letter start.
8. The known title discrepancy for letter 3749 remains intentionally preserved: the contents row prints `கலைஞர் தொடர்கடிதம்-3`, while the actual start page/chapter title prints `கலைஞர் தொடர் கடிதம்-3`.
9. The earlier scan-proven letter-3743 contents/title correction from `கழகத்தே` to `கழுதையே` remains recorded and propagated consistently.
10. Batch audits checked new page bodies for duplication, missing bodies, replacement Unicode and zero-width characters. A fresh repository search found no replacement character `�` and no zero-width-space match.
11. Intentional Latin/English passages were retained on the relevant pages rather than normalised away; examples include legal/court quotations, NASA material, Maduravoyal English reporting, reservation-judgment text and the English passages in the final Hogenakkal letters.
12. Covers, contents, blanks and final back-cover material are represented as canonical page files; no PDF page is intentionally omitted.

## Counts

| Check | Result |
|---|---|
| Source PDF pages | 402 |
| Canonical Markdown range | `page-001.md`–`page-402.md` |
| Front/contents/blank before letters | PDF 1–23 |
| Letter-page span | PDF 24–400 |
| Final non-letter material | PDF 401–402 |
| Printed contents rows | 58 |
| Chapter records | 58 |
| Letter-number range | 3706–3763 |
| Complete letters | 58 |
| Structural gaps/overlaps | none detected |
| Replacement Unicode `�` | none found |
| Full-volume structural audit | **PASS** |

## Preserved source anomalies / distinctions

- PDF 23 is blank with faint reverse-side show-through.
- Letter 3749 contents/start-page subtitle spacing differs and is preserved separately.
- Letter 3743's earlier derived `கழகத்தே` reading was corrected to scan-proven `கழுதையே`.
- Source-specific malformed or unusual English/Tamil forms are not silently regularised; the final-letter scan-visible `By injectinga` is one recorded example.
- PDF 401 is effectively blank except for its running header/page number and faint show-through.
- PDF 402 is the back cover with portrait, publisher/contact information, QR indication, `GO 2300` and `ரூ.300`.

## Verification still pending

The **second visual / textual-fidelity audit** remains separate. Current source-checked coverage is PDF **1–192**, covering the front matter and letters **3706–3730**.

The latest batch, letters **3726–3730 / PDF 162–192**, directly compared **31/31 pages** and passed after **7 scan-proven corrections on 6 canonical pages**: PDF **166, 172, 187, 188, 191 and 192**. These corrections address source-visible word spacing, sentence punctuation, a semicolon/colon discrepancy, a joined word, a year suffix, and an unbalanced quotation that had previously been silently closed.

The next audit batch begins with **3731 — “தலித்” மக்கள் தெரிந்து கொள்வதற்காக!**, PDF **193** / printed page **192**, and runs through letter **3735 / PDF 219**.

English translation remains blocked until the relevant canonical Tamil pages pass that scan-based textual-fidelity gate.

## Final transcription iteration record

The final user-authorised remainder exception completed letters 3762–3763 at PDF 387–400 and preserved PDF 401–402 back matter. That iteration was visually compared page by page before integration. This full-volume audit supersedes the earlier `AUDIT.md` status only at the **structural** level; it does not claim character-level source verification beyond PDF 192.
