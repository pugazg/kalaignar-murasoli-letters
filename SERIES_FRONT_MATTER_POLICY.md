# Series Front Matter Reuse Policy — Volumes 1–54

**Status:** Mandatory optimization policy for the recurring front-matter block in the 54-volume Seethai Pathippagam series.

## Why this exists

PDF pages **001–017** are the recurring series front-matter zone. Re-transcribing the same foreword/publisher material volume after volume is unnecessary work and increases the chance of transcription drift.

However, the repository must **not** assume that all 17 pages are byte-for-byte or text-for-text identical.

Live repository comparison already shows two important caveats:

- PDF **001–003** carry volume-specific data such as volume number, date span, title-page details and publication metadata.
- The recurring publisher material can have edition/state wording variants. For example, existing canonical page 015 records include both `வெளியிடவுள்ள` and `வெளியாகியுள்ள` in different volume trees.

Therefore the rule is **reuse after visual verification**, not blind omission.

## Shared-reference rule

For a newly processed volume in this series:

1. Still create one page file for every physical PDF page, including PDF **001–017**.
2. **Do not repeat the full body transcription** of PDF 001–017 when the page has been visually verified as matching the approved shared/reference content.
3. PDF **001–003** must still capture all volume-specific fields visible in that volume:
   - volume number;
   - visible date span;
   - title-page volume/date line;
   - publisher/edition/year;
   - printed page count;
   - price/code or other volume-specific publication data when present;
   - library stamps/handwriting only as non-source notes.
4. For PDF **004–017**, compare each page directly with the shared reference before using a reference-only page file.
5. Current shared comparison reference for the recurring front matter is the fully verified Volume 43 canonical set:
   - `volumes/volume-43/pages/page-004.md` through `page-017.md`.
6. If a page matches the shared reference in printed source text, the target-volume page file may contain only:
   - normal YAML/page metadata;
   - `transcription_status: "shared-series-front-matter-verified"`;
   - `shared_front_matter_ref: "volumes/volume-43/pages/page-NNN.md"`;
   - a short note that the printed source text was visually checked and matches the shared reference;
   - any target-volume-specific stamp/annotation note.
7. If **any printed wording, punctuation, date, figure, line, heading, or layout-relevant text differs**, do **not** use a reference-only stub. Transcribe that page locally in full and record the variance.
8. Never treat OCR equality, filename similarity or assumed series uniformity as verification. The scan controls.
9. This reuse rule applies only to the recurring front-matter zone **PDF 001–017**. Contents pages and all later pages are transcribed normally.
10. Existing released volumes do not need to be rewritten merely to adopt this policy.

## Batching effect

The mandatory first batch remains **PDF 001–025 exactly**.

For that commit:

- PDF 001–017: verify under this shared-front-matter policy; use reference-only page files where allowed, and local full transcription only for deviations/volume-specific text that must be preserved.
- PDF 018–025: transcribe normally and completely from the target scan.
- If PDF 025 interrupts a letter, the existing partial-letter rule still applies.

This optimization changes **how repeated front matter is represented**, not the requirement that every physical source page has a canonical repository page record.
