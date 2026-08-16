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

For **Volume 1 alone**, regular iterations now use **10 complete consecutive letters**, per the volume-specific instruction. This overrides the repository's normal five-letter cadence only for Volume 1. A documented final residue may be smaller.

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
- the printed-contents hint that letter 0002 starts at printed page 27 is independently confirmed by the visible heading on PDF 028;
- legacy bilingual files remain unchanged;
- English migration remains blocked.

## Iteration 3 — initial five-letter batch: 0002–0006

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
- legacy source-corrected Tamil used only as migration assistance and reconciled against the visible scan;
- PDF 039 visibly prints page number 38, while PDF 040 visibly prints 40; text continues directly, so printed page number 39 is a pagination anomaly rather than missing text;
- PDF 048 inspected only to confirm that letter 0007 begins there;
- no legacy bilingual file modified; no English migration started.

## Iteration 4 — first Volume 1 ten-letter batch: 0007–0016

**Result: PASS — 10 complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0007 — `தோற்ற முயலே! முன்போல சுறுசுறுப்பாக இரு!`: PDF **048–053**, date **31-10-1968**;
- 0008 — `“தீராதி தீரர்- தேசீய மகிபர்- பராக்! பராக்!”`: PDF **054–057**, date printed **31-10-68**;
- 0009 — `வீரனே! வெற்றி என்றைக்கும் உன் பக்கம்தான்!`: PDF **058–062**, date **01-11-1968**;
- 0010 — `பாவி கெடுத்தானே; பலே சாப்பாட்டை!`: PDF **063–066**, date **02-11-1968**;
- 0011 — `தென்றல்- தெம்பாங்கு- தேன்கீதம்!`: PDF **067–069**, date **06-11-1968**;
- 0012 — `“பூப்போட்ட கிளாசிலே போட்டய்யா ஒண்ணரை!”`: PDF **070–072**, date **07-11-1968**;
- 0013 — `மேயர் தேர்தல் நேரம் - நிலை - நேர்த்தியான முடிவு!`: PDF **073–077**, date **09-11-1968**;
- 0014 — `‘பகைமரம்’ தழைக்க விடோம்!`: PDF **078–081**, date **11-11-1968**;
- 0015 — `நம்பிக்கையில்லாத் தீர்மானம் - நாடாளுமன்ற நிகழ்ச்சி!`: PDF **082–085**, date **14-11-1968**;
- 0016 — `யார் அந்த உணவு அமைச்சர்?`: PDF **086–089**, date **16-11-1968**.

Checks performed:

- one canonical page file for every PDF page **048–089**: **42 / 42**;
- all ten letter starts and all ten closing/sign-off/date boundaries visually checked against the scan;
- actual letter headings control over contents-page forms; notably 0008 and 0012 retain their scan headings rather than silently adopting contents variants;
- source-shortened date `(31-10-68)` on 0008 preserved at page level;
- source wording, rhetorical sequences, lists, quotations, emphases and sign-off forms retained;
- legacy source-corrected Tamil used only as migration assistance and checked against the visible scan in this scope;
- PDF 090 inspected only to verify that letter 0017 begins there; no PDF-090 text committed in this iteration;
- legacy bilingual files remain unchanged;
- English migration remains blocked.

## Current boundary

Canonical PDF coverage is **001–089 / 401**. Letters **0001–0016** are canonically complete. The next activity begins at PDF 090 and follows the Volume 1-specific **10-letter** rule for letters **0017–0026**, stopping before letter 0027.

These migration iterations are first-pass visual transcription gates. They are **not** the later full-volume structural audit, second visual verification, or translation textual-fidelity audit.
