# Volume 1 — Full-Volume Tamil Structural Audit

**Audit date:** 2026-08-17  
**Scope:** canonical PDF records **001–401**, printed contents **110 entries**, canonical letters **0001–0110**  
**Result:** **PASS — structural gate complete after documentation-only corrections**

## Authority and scope

This audit checks the internal structure of the completed first-pass Tamil canonical migration. The supplied Volume 1 scan remains the controlling source. This is a structural gate only; it does **not** replace the required second visual/textual-fidelity comparison of every canonical page against the scan.

The legacy `../volume-1/` bilingual corpus is provenance/migration input and was not edited by this audit.

## Page-layer checks

- The canonical `pages/` tree contains exactly the sequential records `page-001.md` through `page-401.md`; no page number is skipped or duplicated and no unexpected page record is present.
- PDF **001–023** is front matter / contents material before the first letter.
- Letter 0001 begins on PDF **024**.
- Canonical letter coverage is continuous from PDF **024** through PDF **400**.
- Letter 0110 closes on PDF **400** with the source date `(01-12-1974)`.
- PDF **401** is correctly classified as a non-letter colour back cover / publisher advertisement.

## Chapter-layer checks

- The canonical `chapters/` tree contains exactly **110 numbered chapter records**, `0001` through `0110`, plus the chapter register README.
- The chapter register accounts for all letters continuously from 0001 to 0110.
- The registered PDF ranges are contiguous from **024–400**: every next letter starts immediately after the previous letter ends; no letter-range gap or overlap was found.
- All 110 chapter records are marked complete and there is no partial canonical letter.

## Printed-contents mapping

- `contents/index.md` preserves **110 printed entries**, numbered 1–110.
- Every printed-content entry maps by letter number to one canonical chapter record.
- Printed-content wording is preserved as printed and is not silently rewritten to match later heading pages.
- Actual heading pages continue to control canonical chapter titles where the contents wording differs. Confirmed examples include:
  - 0008 — contents wording differs from the actual `“தீராதி தீரர்- தேசீய மகிபர்- பராக்! பராக்!”` heading;
  - 0012 — the actual heading ends with `!`, while the contents uses `?`;
  - 0024 — actual heading uses `ஆழ்வப் பிறவி`, while the contents prints `ஆழ்வப்பிறவி`;
  - 0109 — contents prints `அவள் ஒரு தொடற்கதை!`, while PDF 392 actually heads the letter `அவள் ஒரு தொடர்கதை!`.

## Date and pagination exceptions

- Letter **0063 — `“கிலுகிலுப்பை!”`** remains deliberately undated: the printed contents date cell is blank and the canonical chapter record has `letter_date: null`. No date is inferred.
- Letter **0028** retains the scan-printed closing date **28-12-1968**, which controls over conflicting legacy metadata.
- PDF **039** prints page **38** and PDF **040** prints page **40**. The sentence continues across the boundary, so printed page number 39 is recorded as a source-pagination anomaly rather than treated as missing text.

## Documentation corrections made by this audit

The structural data itself passed. Two stale migration-era notes were corrected so that repository documentation matches the completed canonical state:

1. `contents/index.md` no longer says that only letter 0001 has a verified canonical start; it now records that all 110 canonical boundaries have been verified.
2. `chapters/README.md` no longer describes later letter boundaries as unverified future work; it now records the completed 0001–0110 chapter mapping and structural-audit result.

No canonical Tamil page body, letter boundary, title, date, sign-off or source transcription required alteration in this structural audit.

## Gate result

**PASS.** The full-volume Tamil structural audit is complete for Volume 1.

Still blocked / pending:

- second visual/textual-fidelity verification against the controlling scan;
- canonical English migration/source checking;
- bilingual alignment;
- editorial consistency review;
- translation manifest and final release work.

English migration must not begin until the second visual/textual-fidelity gate is complete.
