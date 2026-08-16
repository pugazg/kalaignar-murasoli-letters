# Volume 1 — Canonical Migration Audit

## Source intake

- Source: `Vol1.pdf`
- SHA-256: `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`
- Size: **244,892,260 bytes**
- PDF pages: **401**
- Printed pages stated by publisher: **400**
- Edition: **1st edition, 2022**
- Publisher: **Seethai Pathippagam**
- Usable searchable text layer: **none**

## Migration rule

The existing `volumes/volume-1/` corpus is preserved as legacy provenance. The scan controls the new canonical page layer. Existing source-corrected Tamil and English may assist comparison but cannot silently override the printed scan.

## Iteration 1 — mandatory PDF 001–025

**Result: PASS — first-pass canonical migration complete for this scope.**

Coverage:

- PDF 001: front cover
- PDF 002: title page
- PDF 003: publication/distribution matter
- PDF 004: illustrated dedication/front matter
- PDF 005: blank page with faint show-through only
- PDF 006–014: M. K. Stalin foreword/panindurai, printed pages 5–13
- PDF 015–017: publisher preface, printed pages 14–16
- PDF 018–023: printed contents, printed pages 17–22, **110 entries**
- PDF 024–025: start of letter 0001, printed pages 23–24

Checks performed:

- one canonical Markdown page per PDF page in scope: **25 / 25**;
- page numbering and printed-page offset checked against the scan;
- front matter distinguished from library stamps/handwriting;
- printed contents preserved as printed rather than replaced by legacy actual-letter titles;
- contents entry 63 preserves its blank printed date cell;
- letter 0001 title/date/start checked against the scan;
- page-25 boundary intentionally left partial; no text from PDF 026 was imported;
- no source PDF was committed;
- no legacy bilingual file was changed;
- no English migration/translation was started.

## Iteration 2 — complete interrupted letter 0001

**Result: PASS — letter 0001 canonical boundary complete.**

Coverage:

- PDF 026 / printed 25: continuation of letter 0001;
- PDF 027 / printed 26: final body paragraphs, `அன்புள்ள,`, `மறவன்`, and printed date `(22-10-1968)`;
- PDF 028 was inspected only to verify that letter 0002 begins there; no PDF-028 text was committed in this iteration.

Checks performed:

- canonical page files added for PDF 026–027 only;
- source wording, punctuation, political comparison and rhetorical-question sequence retained;
- letter 0001 chapter boundary promoted from partial to complete;
- verified complete coverage is **PDF 024–027 / printed 23–26**;
- the printed-contents hint that letter 0002 starts at printed page 27 is now independently confirmed by the visible heading on PDF 028;
- legacy bilingual files remain unchanged;
- English migration remains blocked.

## Iteration 3 — first regular five-letter batch: 0002–0006

**Result: PASS — five complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0002 — `நீ விளைத்த கழனி - நீ உழைத்த உழைப்பு!`: PDF **028–031**, date **24-10-1968**;
- 0003 — `நிதானமாகப் பேசுங்கள்!`: PDF **032–035**, date **25-10-1968**;
- 0004 — `உன்னால் முடிந்ததைச் செய்து விட்டாயா?`: PDF **036–038**, date **27-10-1968**;
- 0005 — `நேர்மையும் பொறுப்பும் நீர்மேல் எழுத்தல்ல!`: PDF **039–042**, date **29-10-1968**;
- 0006 — `வெற்றி பெற்றவனே உன் வேலை என்ன?`: PDF **043–047**, date **30-10-1968**.

Checks performed:

- one canonical page file for every PDF page **028–047**: **20 / 20**;
- actual letter-start headings and closing sign-off/date pages visually checked against the scan;
- legacy source-corrected Tamil was used only as migration assistance and reconciled against the visible scan in this scope;
- source-specific wording, rhetorical questions, repeated imperatives, quotations, names, figures and sign-off forms retained;
- letter 0004's closing uses `இங்ஙனம்`; letter 0005's closing uses `தங்கள் தம்பி`; other sign-off forms remain as printed;
- PDF 039 visibly prints page number 38, while PDF 040 visibly prints 40; the sentence continues directly across the boundary, so printed page number 39 is documented as a pagination anomaly rather than missing text;
- PDF 048 was inspected only to confirm that letter 0007 begins there; no PDF-048 text was committed;
- no source PDF was committed;
- no legacy bilingual file was modified;
- no English migration was started.

## Current boundary

Canonical PDF coverage is **001–047 / 401**. Letters **0001–0006** are canonically complete. The next activity begins at PDF 048 and follows the normal five-complete-letter rule for letters **0007–0011**, stopping before letter 0012.

These migration iterations are first-pass visual transcription gates. They are **not** the later full-volume structural audit, second visual verification, or translation textual-fidelity audit.
