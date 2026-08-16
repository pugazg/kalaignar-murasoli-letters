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

## Current boundary

Canonical PDF coverage is **001–027 / 401**. Letter **0001 — `“ஜாக்குலின்கள்”`** is complete. The next activity starts at PDF 028 and follows the normal five-complete-letter rule for letters **0002–0006**, stopping before letter 0007.

These migration iterations are first-pass visual transcription gates. They are **not** the later full-volume structural audit, second visual verification, or translation textual-fidelity audit.
