# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-28

This document is the current project-level handover for continuing the multi-volume Kalaignar Murasoli Letters archive in a new chat/window or with another worker.

It should be read together with:

1. [`VOLUME_PROCESSING_GUIDE.md`](VOLUME_PROCESSING_GUIDE.md)
2. [`VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md)
3. [`TRANSCRIPTION_GUIDE.md`](TRANSCRIPTION_GUIDE.md)
4. [`FUTURE_VOLUME_WORK_GUIDELINES.md`](FUTURE_VOLUME_WORK_GUIDELINES.md)
5. [`NEXT_CHAT_PROMPT.md`](NEXT_CHAT_PROMPT.md)

If these documents conflict, the mandatory repository processing/batching/transcription guides take precedence.

---

## 1. Project purpose

The repository preserves Kalaignar’s Murasoli letters as a page-faithful archival corpus and, where completed, as verified bilingual Tamil–English records.

> **The source scan controls.**

OCR, contents pages, another edition, outside historical knowledge, English translations and inferred chronology may help identify questions, but none may silently override what is printed in the controlling scan. Historical wording, source errors, numbering anomalies, punctuation, quoted material, political rhetoric, English text and missing-source conditions are preserved and documented.

---

## 2. Current active work — Volume 45

Volume 45 is the current active workstream.

- Controlling source: `TVA_BOK_0065831_கலைஞரின்_கடிதங்கள்_தொகுதி_45.pdf`
- Source PDF pages: **402**
- Visible source date range: **12.03.2011–27.09.2011**
- Canonical Tamil page coverage: **001–402 / 402 — complete**
- Completed actual source-letter records: **55 / 55**
- Completed source-letter range: **3537–3591**
- Last source letter: **3591**
- Letter 3591 closing boundary: **PDF 401 / printed page 400**
- Letter 3591 closing date: **27-9-2011**
- PDF 402: non-letter back cover / portrait / publisher-information matter
- Full-volume Tamil structural audit: **PASS**
- Second full-volume visual/textual-fidelity verification: **IN PROGRESS — PDF 001–385 verified**
- Second-pass corrections so far: **227 canonical page files / 605 correction spans**
- User-approved routine second-pass iteration size: **25 consecutive PDF pages**; only final **PDF 386–402** remains
- English translation: **BLOCKED** until the second visual/textual-fidelity gate passes

### Latest durable checkpoint

Live `main` at handover creation is:

`c429c45dd96297e2bc6a21d002b91723e4c70f04`

Commit message:

`Verify Volume 45 second fidelity PDF 361-385`

Treat live GitHub state as authoritative if `main` has advanced after this handover was written.

The latest completed iteration is **PDF 361–385 / printed pages 360–384**. PDF 361–364, 366–376 and 385 passed unchanged. Scan-proven corrections were made on PDF 365 and 377–384: **9 corrected page files / 13 correction spans**.

Important corrections include restoration of `சந்தித்தபோது` on PDF 365; removal of spurious zero-width OCR contamination from PDF 377–384; restoration of `அதன் மூலமாக`, `கல்வியிலேயே` and `தன்மையோடு` on PDF 377; and source spacing `பாரா முகத்தால்` on PDF 382. Zero-width cleanup removes transcription/OCR contamination only and must not be treated as normalization of source language.

Confirmed source anomalies and non-edition material remain handled conservatively. Examples already documented in the repository include PDF 088 `ஒப்பங்கள்` / `மணலை ஜலித்து`, PDF 098 `112.2006-ல்`, scan-printed March 2010 dates on PDF 116, PDF 127 `தனிச்சையாக`, PDF 170 `பொக்கம்`, PDF 176 `10ந்தேதியன்று`, PDF 177 `முஜா கி தீன்`, PDF 217 `011ஆம் ஆண்டு`, PDF 233 `பொத்தம் 31 கேள்விகளில் 22 1 கேள்விகள்`, PDF 248 `என்னருந் தமிழ் மக்களுக்குக்`, PDF 259 `16-10-1999ந்தேதி`, and PDF 290 `18-5-2001`. Later library stamp/handwriting on PDF 102 remains excluded from edition text. Do not normalize these from outside knowledge.

Direct scan verification at PDF 284 resolved the Letter 3576 contents/start-title question in favor of `பாரீர்!`. The genuine Letter 3575 source-context difference remains: contents `அந்த நாள் முதல் இந்த நாள் வரையில்...!` versus letter-start `அந்த நாள் முதல் இந்த நாள் வரையில்....!`.

### Exact next activity

Resume at **PDF 386 / printed page 385** and complete the final **PDF 386–402** end-of-volume second-pass iteration in one go.

For each page:

1. visually compare the canonical Markdown against the controlling scan;
2. treat the rendered scan as textual authority;
3. use OCR/text extraction only for navigation or candidate detection, never to decide a reading;
4. preserve spelling, punctuation, spacing, figures, English text, source anomalies and physical page boundaries exactly as printed;
5. exclude later stamps/handwriting/show-through;
6. record PASS or scan-proven corrections;
7. update corrected canonical page files only where the scan proves a discrepancy.

After PDF 402:

- reconcile corrected-page and correction-span counts;
- update `PROGRESS.md`, `metadata.yml`, Volume 45 `README.md`, `AUDIT.md`, `FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`, `FULL_VOLUME_STRUCTURAL_AUDIT.md`, root `README.md`, this handover, and `NEXT_CHAT_PROMPT.md` as appropriate;
- make the final batch atomic where technically possible;
- verify the resulting live `main` commit/tree before claiming completion;
- only after all **402 / 402** pages pass may the second Tamil visual/textual-fidelity gate be marked **PASS**.

**Do not begin English translation merely because PDF 386–402 has been inspected. First make the 402-page gate durable in GitHub and verify it.** After that, use the repository’s translation plan/reference conventions to determine the next translation activity.

Authoritative continuation files:

- [`volumes/volume-45/README.md`](volumes/volume-45/README.md)
- [`volumes/volume-45/PROGRESS.md`](volumes/volume-45/PROGRESS.md)
- [`volumes/volume-45/AUDIT.md`](volumes/volume-45/AUDIT.md)
- [`volumes/volume-45/FULL_VOLUME_STRUCTURAL_AUDIT.md`](volumes/volume-45/FULL_VOLUME_STRUCTURAL_AUDIT.md)
- [`volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md)
- [`volumes/volume-45/metadata.yml`](volumes/volume-45/metadata.yml)
- [`volumes/volume-45/contents/index.md`](volumes/volume-45/contents/index.md)
- [`volumes/volume-45/chapters/README.md`](volumes/volume-45/chapters/README.md)

Do not restart Volume 45 transcription or re-run already durable second-pass ranges without scan evidence requiring a correction.

---

## 3. Completed reference volumes

### Volume 01

Volume 01 is fully released: **401 / 401** canonical pages, **110 / 110** source records, full-volume Tamil structural audit PASS, full 401-page visual/textual-fidelity audit PASS, and **110 / 110** final bilingual release records. Its approved volume-specific batching overrides must not be carried into other volumes without explicit approval.

### Volume 46

Volume 46 is fully complete through English release: **402 / 402** canonical pages, **55 actual source records**, **55 / 55** verified bilingual records, editorial consistency review, 55-row manifest and final release report complete. It remains the key reference for preserving source-number anomalies: no 3636; two distinct records numbered 3637; no 3644–3646.

### Volume 47

Volume 47 is release-ready within the surviving source: **59 / 59** bilingual aligned, final manifest/report complete, with Letter **3681** explicitly source-incomplete because printed page 252 is absent from the sole available PDF. Do not reconstruct that missing page without new source evidence and explicit approval.

### Volumes 48 and 49

Volumes 48 and 49 are completed English references. Volume 49 remains the principal structural/quality reference implementation; never copy its volume-specific facts into another volume.

---

## 4. Mandatory startup / source rules

Before changing repository state in a fresh chat:

1. fetch live `main` and treat it as authoritative;
2. read the controlling root guides completely;
3. read this handover and `NEXT_CHAT_PROMPT.md` completely;
4. read the active Volume 45 continuation/audit files listed above;
5. inspect the attached controlling PDF/rendered pages directly;
6. never infer an unseen source reading from OCR or outside knowledge.

The scan is the highest authority. Do not silently normalize spelling, punctuation, spacing, dates, figures, repetitions, anomalies, English text or physical page boundaries.

---

## 5. Tamil transcription / QA rules

For ordinary new-volume transcription, follow `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`. Volume 45 is no longer in initial transcription: canonical transcription and structural audit are complete.

**Volume 45 second-pass override:** the user approved **25 consecutive PDF pages per visual/textual-fidelity iteration**. The only remaining second-pass scope is the documented end-of-volume exception: **17 pages, PDF 386–402**.

Keep QA stages distinct:

1. iteration/batch audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. translation textual-fidelity/alignment audit.

English remains blocked until stage 3 is durably PASS.

---

## 6. Source anomalies and gaps

If printed text appears wrong or inconsistent, preserve and document it. Do not repair duplicate/skipped numbers, unusual dates, contents/title differences, malformed English or inconsistent figures using outside knowledge.

If the controlling PDF genuinely omits material, mark the record source-incomplete, preserve surviving text only, do not reconstruct or guess missing continuation/closing/date/signature, and carry the gap consistently through archival and translation records.

---

## 7. English translation/release handoff

Once the second Tamil gate is durably PASS, translate from audited canonical Tamil in clear contemporary English while preserving thought order, political force, irony, rhetorical questions, repetition, quotations, names, dates, figures, units, source-supplied English, anomalies and source gaps. Retain complete audited Tamil under `Original Tamil — மூலத் தமிழ்` in every bilingual record.

Use completed reference volumes and any Volume 45 translation plan already in the live repository. Do not invent a new translation convention when a documented repository convention exists.

---

## 8. Git/concurrency discipline

- Work on `main` as requested.
- Never force-push routine work.
- Recheck live `main` immediately before mutation.
- Preserve unrelated concurrent changes.
- Keep iteration scope explicit.
- Prefer one atomic commit for the declared final batch where technically possible.
- Remove temporary OCR/render/export/workflow artifacts from the final repository tree.
- Compare/verify the resulting tree before moving `main` and fetch live `main` afterward.

---

## 9. Meaning of “Proceed with next activity”

Inspect current durable state, identify the next already-defined gate/batch, execute it directly, and report completed scope, QA result, commit SHA, current counts/status and exact next activity. Do not ask the user to choose among routine next steps.

---

## 10. Clean interruption/handoff rule

The repository must contain the exact completed page/letter range, anomalies/gaps, audit state, translation state and next activity. The chat must never be the sole place where critical archival state exists.

At this handover boundary, the second Volume 45 visual/textual-fidelity audit is durable through **PDF 385 / 402**. The exact next source page is **PDF 386 / printed page 385**, and the exact remaining second-pass scope is **PDF 386–402**.