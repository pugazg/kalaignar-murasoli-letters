# Volume 42 — Full-Volume Tamil Structural Audit

**Audit date:** 2026-09-20  
**Scope:** canonical PDF records **001–402**, actual source records **3364–3376, 3154, 3378–3427**  
**Result:** **PASS — structural gate complete**

## Authority and scope

This audit checks the internal structure of the completed first-pass Tamil source archive. The controlling scan remains the highest textual authority. This structural gate does **not** substitute for the required second full-volume direct visual/textual-fidelity verification.

No source wording was normalized, reconstructed or silently corrected during this audit. Any issue requiring fresh visual judgment belongs to the second visual/textual-fidelity gate.

## Source identity

- Controlling source: `TVA_BOK_0065826_கலைஞரின்_கடிதங்கள்_தொகுதி_42.pdf`
- Source SHA-256: `43f9b51fd3765144f707cce535cc9ed39892f911a126c3c3c005173a1efc1676`
- Source byte size: **232,174,916**
- Physical PDF page count: **402**
- Printed page count: **400**
- Visible date span: **31.01.2009–30.10.2009**
- Printed contents inventory: **64 rows**
- Searchable text layer: **none usable; scan images control transcription**

The source identity above was rechecked from the controlling attachment during this audit. `pdfinfo` reports **402** physical pages and the byte size agrees with repository metadata.

## Physical page inventory

- The live Git tree is non-truncated and contains exactly **402** canonical numbered page files: `page-001.md` through `page-402.md`.
- No canonical page number is missing and no numbered page outside **001–402** is registered.
- PDF **001–003** retain Volume 42-local front-cover/title/publication data.
- PDF **004–017** were structurally represented under the series front-matter policy at structural-audit time. The subsequent second fidelity pass proved PDF **004** is a Volume 42-local wording difference and converted it to a local transcription; PDF **005–017** remain direct-verified shared-series reference records. This does not alter the structural page inventory.
- Printed contents occupy PDF **018–022**.
- PDF **023 / printed 22** is correctly classified as a blank page after the contents.
- Letter-bearing canonical coverage is continuous from PDF **024 / printed 23** through PDF **401 / printed 400**.
- PDF **402** is correctly preserved as non-letter back-cover / portrait / publisher-contact-price material.
- No Letter **3428** is created in Volume 42.

## Printed contents and source-record inventory

- `contents/index.md` contains exactly **64** printed source rows.
- The exact record order is:
  - **3364–3376**
  - **3154**
  - **3378–3427**
- This exactly matches the 64 chapter-record numbers.
- The source-number anomaly is preserved: both the printed contents and actual heading at **PDF 092 / printed 91** show **3154** between 3376 and 3378.
- There is **no source record 3377** at that position and no 3377 chapter file is invented.
- `partial_letter` remains null; source-incomplete record count remains **0**.

## Chapter and page-link reconciliation

- The chapter tree contains exactly **64** chapter files plus `chapters/README.md`.
- Every printed source row has exactly one corresponding chapter file; there are no missing or extra chapter numbers.
- Every chapter's recorded PDF start/end and printed start/end reconcile with the next printed-contents boundary.
- Every chapter links the complete consecutive canonical page range for its record.
- The union of all 64 chapter ranges is exactly **PDF 024–401**, comprising **378 unique letter-bearing physical pages**.
- There is **no chapter-range gap and no chapter-range overlap**.
- Chapter files link canonical pages rather than duplicating complete Tamil source bodies.

## Verified source anomalies preserved

### Source-number anomaly — 3154

The contents and actual source heading at PDF **092 / printed 91** both print **3154** between 3376 and 3378. This is retained as source truth; no 3377 is inferred.

### Letter 3392 — genuine duplicated printed body

Letter **3392 — `பூச்சாண்டிப் பொம்மை?`** spans PDF **209–212**. The first printed copy closes at the top of PDF 211, after which the title and body begin again and continue through PDF 212, closing a second time. Canonical pages preserve both physical source copies; the structural audit does not deduplicate them.

### Letter 3388 — title/subtitle layout

Printed contents shows `அந்த நினைவுக்கு ஒரு நன்றி!! (கலைஞர் கவிதைக் கடிதம்)` inline. Actual PDF **187** prints the main heading `அந்த நினைவுக்கு ஒரு நன்றி!!` and then the separate subtitle `(கலைஞர் கவிதைக் கடிதம்)`. The chapter record explicitly preserves this source-layer layout distinction via its main title, `record_type`, and source note. This is a layout distinction, not a missing-text defect.

### Letter 3425 — genuine contents/actual-title spacing difference

Printed contents uses `வருந்தப் போகிறார்களா - இனியேனும் திருந்தப் போகிறார்களா?`, while actual PDF **386** uses joined `திருந்தப்போகிறார்களா?`. Each source layer remains independently preserved and the chapter record documents the difference.

### Volume ending

Letter **3427 — `மேலும் பயன்படுகின்ற சந்திப்பு!`** closes on PDF **401 / printed 400** with `அன்புள்ள, மு.க.` and date **30-10-2009**. PDF **402** is non-letter matter and does not create a new source record.

## Cross-file synchronization

The completed first-pass state reconciles as:

- physical PDF pages: **402 / 402**
- canonical numbered page files: **402 / 402**
- printed contents rows: **64 / 64**
- actual source records: **64 / 64**
- record order: **3364–3376, 3154, 3378–3427**
- letter-bearing canonical range: **PDF 024–401**
- non-letter terminal page: **PDF 402**
- partial records: **0**
- source-incomplete records: **0**

The page tree, contents register, chapter tree, metadata, progress records and batch-audit history are structurally consistent with this state.

## Repository and link hygiene

- All numbered canonical page filenames follow the zero-padded `page-NNN.md` convention.
- The page tree contains **402 unique blobs** and no exact duplicate canonical page-file blob.
- Repository code searches found no **U+FFFD** replacement character and no **U+200B / U+200C / U+200D / U+FEFF** residue under `volumes/volume-42`.
- No unexpected OCR/render/temp/export image or PDF artifact is committed under the Volume 42 tree.
- The chapter tree contains exactly the expected 64 record numbers and no Letter 3428 chapter.
- The English area remains scaffolding-only; translation is still blocked.

## Structural corrections made by this gate

No canonical Tamil source body, letter boundary, title, date or page mapping required a deterministic structural correction.

One metadata completion was made: the previously null `source_sha256` field is populated with the SHA-256 of the controlling PDF verified during this audit.

## Gate result

**PASS.** The full-volume Tamil structural audit is complete for Volume 42.

Current Tamil gate state:

- first-pass canonical source coverage: **PASS — PDF 001–402 / 402**
- full-volume structural audit: **PASS**
- second full-volume direct visual/textual-fidelity verification: **IN PROGRESS — PDF 001–218 / 402 verified**
- English translation: **BLOCKED**

## Post-structural fidelity note — 2026-09-20

- Second-pass Batch 1 directly verified PDF **001–023**. It exposed a textual/source-policy defect not visible to the structural gate: PDF **004** prints Volume 42-local `அம்மாவுக்கு...`, not the Volume 43 shared-reference `அண்ணாவுக்கு...`. PDF 004 is now local; PDF 005–017 remain shared references. PDF 003 was also expanded from a selective summary to the complete printed publication-details page.
- Second-pass Batch 2 directly verified Letters **3364–3368 / PDF 024–049** and corrected canonical pages **026, 029, 034, 036, 037, 044 and 046**. The major semantic repair is PDF 044 `உத்தரவாதம் அளிக்கக்கூடிய`; no structural range/title/date change resulted.
- Second-pass Batch 3 directly verified Letters **3369–3373 / PDF 050–073** and corrected canonical pages **053, 058, 060, 061 and 063**. Major repairs restore PDF 060 `ஒரு கலவரத்தைத் தூண்டி விட முடியாதா?`, PDF 061 `அறிக்கையாக்கியிருக்கிறேன்`, and PDF 063 `டெல்லி மருத்துவரும்`; no structural range/title/date change resulted.
- Second-pass Batch 4 directly verified source records **3374, 3375, 3376, 3154 and 3378 / PDF 074–105** and applied **21 scan-proven corrections across 12 canonical pages — 074, 075, 076, 077, 079, 080, 081, 083, 087, 090, 102 and 103**. The source-number anomaly **3154** remains unchanged; no structural range, title, date, boundary or contents-row change resulted.
- Second-pass Batch 5 directly verified source records **3379–3383 / PDF 106–149** and applied **28 scan-proven corrections across 19 canonical pages — 109, 111, 112, 116, 118, 119, 120, 122, 124, 126, 127, 128, 129, 132, 143, 144, 145, 146 and 147**. No structural range, title, date, boundary or contents-row change resulted.
- Second-pass Batch 6 directly verified source records **3384–3388 / PDF 150–190** and applied **17 scan-proven textual corrections plus 1 physical page-boundary restoration across 10 canonical pages — 151, 154, 157, 158, 162, 167, 179, 184, 187 and 188**. The restored PDF 157→158 continuation changes only canonical physical-page placement, not any letter boundary, title, date, contents row or total record/page count. Letter 3388 retains its scan-verified main-title/subtitle layout.
- Second-pass Batch 7 directly verified source records **3389–3393 / PDF 191–218** and applied **6 scan-proven textual corrections plus 7 paragraph-structure restorations across 7 canonical pages — 195, 196, 209, 215, 216, 217 and 218**. These changes preserve the same five letter ranges, dates and source record counts; Letter 3392's genuine duplicated printed body across PDF 209–212 remains intact.

Structural counts/ranges remain unchanged.

## Exact next activity

Continue the separate **second full-volume direct visual/textual-fidelity verification with 3394–3398 / PDF 219–241**, stopping before PDF 242.

Compare the canonical Tamil against the controlling scan directly, preserve the verified **3154** source-number anomaly and all physical page boundaries, record every scan-proven correction, and do **not** begin English translation until the full second-pass fidelity gate is complete.
