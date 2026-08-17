# Volume 1 — Full-Volume Visual/Textual Fidelity Audit

## Controlling source

`Vol1.pdf` is the controlling source for this canonical migration.

- PDF pages: **401**
- Printed pages represented: **400**
- Letter text: PDF **024–400**
- Non-letter back cover: PDF **401**

## Result

**PASS — second visual/textual-fidelity verification complete for PDF 001–401 / 401.**

Every canonical Markdown page was compared directly against the corresponding scan page. Scan-proven corrections were applied only where the canonical first-pass record differed from source-supported wording, spacing, punctuation, lineation, or visible emphasis. No silent modernization, normalization, reconstruction, or inferred correction was permitted.

### Cumulative correction count

- Canonical pages corrected during second pass: **159**
- Scan-proven correction spans: **274**
- Canonical page coverage verified: **401 / 401**
- Canonical letter coverage verified: **110 / 110 — letters 0001–0110**

## Range reports

The second pass was recorded in consecutive audit ranges:

- `TEXTUAL_FIDELITY_AUDIT_001_025.md`
- `TEXTUAL_FIDELITY_AUDIT_026_050.md`
- `TEXTUAL_FIDELITY_AUDIT_051_075.md`
- `TEXTUAL_FIDELITY_AUDIT_076_100.md`
- `TEXTUAL_FIDELITY_AUDIT_101_125.md`
- `TEXTUAL_FIDELITY_AUDIT_126_150.md`
- `TEXTUAL_FIDELITY_AUDIT_151_175.md`
- `TEXTUAL_FIDELITY_AUDIT_176_200.md`
- `TEXTUAL_FIDELITY_AUDIT_201_225.md`
- `TEXTUAL_FIDELITY_AUDIT_226_250.md`
- `TEXTUAL_FIDELITY_AUDIT_251_275.md`
- `TEXTUAL_FIDELITY_AUDIT_276_300.md`
- `TEXTUAL_FIDELITY_AUDIT_301_325.md`
- `TEXTUAL_FIDELITY_AUDIT_326_350.md`
- `TEXTUAL_FIDELITY_AUDIT_351_375.md`
- `TEXTUAL_FIDELITY_AUDIT_376_400.md`
- `TEXTUAL_FIDELITY_AUDIT_401.md`

These range reports are stored under `translations/en/` because the fidelity gate controls readiness for canonical English migration; they audit the Tamil canonical source pages rather than the English translation.

## Source-specific findings retained

- Printed page number **39** is skipped between PDF 039 and PDF 040 while the text remains continuous; this is preserved as a source-pagination anomaly rather than treated as missing content.
- Letter **0063** has no printed date; no date has been inferred.
- Printed contents wording is preserved independently from actual heading-page wording. In particular, letter 0109 appears in contents as `அவள் ஒரு தொடற்கதை!`, while PDF 392 actually heads the letter `அவள் ஒரு தொடர்கதை!`.
- The source varies opening-address forms such as `உடன்பிறப்பே` and `உடன் பிறப்பே`, as well as comma/exclamation punctuation. Those scan-supported forms are preserved rather than normalized.
- PDF 401 is a non-letter colour back cover and was separately verified against its canonical descriptive record.

## Gate decision

The required Tamil structural audit and full 401-page visual/textual-fidelity audit are both complete and PASS.

**Canonical English migration and source checking may now begin.** The preserved legacy bilingual records under `../volume-1/` may be used as drafts/evidence, but they do not override the verified canonical Tamil source or the controlling scan.
