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

Volume 45 remains the current active workstream, but its Tamil transcription and Tamil QA gates are now complete.

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
- Second full-volume visual/textual-fidelity verification: **PASS — PDF 001–402 / 402**
- Final second-pass cumulative corrections: **243 canonical page files / 623 correction spans**
- English translation: **UNBLOCKED BY TAMIL QA; NOT STARTED**

### Final Tamil fidelity checkpoint

The final end-of-volume iteration covered **PDF 386–402 / printed pages 385–400 plus the back cover**. All 17 pages were visually compared directly against the controlling scan.

- PDF 386–401: systematic spurious zero-width OCR characters removed.
- PDF 388: additionally restored source spacing `பொறியியல் தொழில் நுட்பவியல்`.
- PDF 389: additionally restored source punctuation `காரணம், அவர்கள்`.
- PDF 390: Letter 3589 closing/signature/date `19-9-2011` verified.
- PDF 396: Letter 3590 closing/signature/date `24-9-2011` verified.
- PDF 397: Letter 3591 title/opening verified.
- PDF 399: printed `21-3-2002` date in the quoted earlier letter preserved.
- PDF 401: Letter 3591 closing/signature/date `27-9-2011` verified.
- PDF 402: back-cover portrait, publisher/address/price matter and QR-code presence verified; later handwriting excluded from edition text.

Final iteration result: **16 corrected canonical page files / 18 correction spans; 1 page passed unchanged**.

The earlier Letter 3576 control-layer `பார்!` reading is withdrawn. Direct scan verification establishes `உலகப் புகழ் உத்தமத் தமிழச்சி, பாரீர்!` in both contents and the actual letter start. The genuine Letter 3575 source-context punctuation difference remains: contents `அந்த நாள் முதல் இந்த நாள் வரையில்...!` versus letter-start `அந்த நாள் முதல் இந்த நாள் வரையில்....!`.

Confirmed printed anomalies remain preserved and must not be normalized from outside knowledge. Examples already documented include PDF 088 `ஒப்பங்கள்`, PDF 098 `112.2006-ல்`, PDF 170 `பொக்கம்`, PDF 176 `10ந்தேதியன்று`, PDF 177 `முஜா கி தீன்`, PDF 217 `011ஆம் ஆண்டு`, PDF 233 `பொத்தம் 31 கேள்விகளில் 22 1 கேள்விகள்`, PDF 248 `என்னருந் தமிழ் மக்களுக்குக்`, PDF 259 `16-10-1999ந்தேதி`, and PDF 290 `18-5-2001`. Later library stamp/handwriting on PDF 102 remains excluded from edition text.

### Exact next activity

After confirming that the final Tamil fidelity checkpoint is the live `main` state, inspect the current Volume 47 and Volume 49 translation plans/reference implementation and initialize the Volume 45 English translation workspace and pilot according to repository policy.

Do not invent a Volume 45 translation convention when a documented repository convention exists. Translation must use the audited canonical Tamil as source and preserve source-specific anomalies, figures, punctuation, quotations, political force, rhetorical questions and surviving source boundaries.

Authoritative Volume 45 files now include:

- [`volumes/volume-45/README.md`](volumes/volume-45/README.md)
- [`volumes/volume-45/PROGRESS.md`](volumes/volume-45/PROGRESS.md)
- [`volumes/volume-45/AUDIT.md`](volumes/volume-45/AUDIT.md)
- [`volumes/volume-45/FULL_VOLUME_STRUCTURAL_AUDIT.md`](volumes/volume-45/FULL_VOLUME_STRUCTURAL_AUDIT.md)
- [`volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md)
- [`volumes/volume-45/metadata.yml`](volumes/volume-45/metadata.yml)
- [`volumes/volume-45/contents/index.md`](volumes/volume-45/contents/index.md)
- [`volumes/volume-45/chapters/README.md`](volumes/volume-45/chapters/README.md)

Do not restart Volume 45 Tamil transcription or re-run already durable visual/textual-fidelity ranges unless direct scan evidence requires a specific correction.

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
5. never infer an unseen source reading from OCR or outside knowledge.

The scan is the highest authority. Do not silently normalize spelling, punctuation, spacing, dates, figures, repetitions, anomalies, English text or physical page boundaries.

---

## 5. Tamil transcription / QA rules

For ordinary new-volume transcription, follow `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`. Volume 45 Tamil transcription, structural audit and second full-volume visual/textual-fidelity verification are now complete.

Keep QA stages distinct:

1. iteration/batch audit;
2. full-volume Tamil structural audit;
3. second full-volume direct visual/textual-fidelity verification;
4. translation textual-fidelity/alignment audit.

For Volume 45, stages 1–3 are complete and stage 4 has not begun.

---

## 6. Source anomalies and gaps

If printed text appears wrong or inconsistent, preserve and document it. Do not repair duplicate/skipped numbers, unusual dates, contents/title differences, malformed English or inconsistent figures using outside knowledge.

If the controlling PDF genuinely omits material, mark the record source-incomplete, preserve surviving text only, do not reconstruct or guess missing continuation/closing/date/signature, and carry the gap consistently through archival and translation records.

---

## 7. English translation/release handoff

Volume 45 English translation may now begin because both Tamil QA gates are durably PASS once this checkpoint is verified on live `main`.

Translate from audited canonical Tamil in clear contemporary English while preserving thought order, political force, irony, rhetorical questions, repetition, quotations, names, dates, figures, units, source-supplied English, anomalies and source gaps. Retain complete audited Tamil under `Original Tamil — மூலத் தமிழ்` in every bilingual record.

Use completed reference volumes and the live translation plans. Do not invent a new translation convention when a documented repository convention exists.

---

## 8. Git/concurrency discipline

- Work on `main` as requested.
- Never force-push routine work.
- Recheck live `main` immediately before mutation.
- Preserve unrelated concurrent changes.
- Keep iteration scope explicit.
- Prefer one atomic commit for a declared batch where technically possible.
- Remove temporary OCR/render/export/workflow artifacts from the final repository tree.
- Compare/verify the resulting tree before moving `main` and fetch live `main` afterward.

---

## 9. Meaning of “Proceed with next activity”

Inspect current durable state, identify the next already-defined gate/batch, execute it directly, and report completed scope, QA result, commit SHA, current counts/status and exact next activity. Do not ask the user to choose among routine next steps.

---

## 10. Clean interruption/handoff rule

The repository must contain the exact completed page/letter range, anomalies/gaps, audit state, translation state and next activity. The chat must never be the sole place where critical archival state exists.

At this handover boundary, the Volume 45 Tamil archival layer is complete: **402 / 402 canonical pages, 55 / 55 source letters, structural audit PASS, second direct visual/textual-fidelity audit PASS, 243 corrected page files / 623 correction spans**. The next workstream is Volume 45 English translation initialization/pilot after live-main verification of this final Tamil checkpoint.
