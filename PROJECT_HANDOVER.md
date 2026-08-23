# Project Handover — Kalaignar Murasoli Letters

**Repository:** `pugazg/kalaignar-murasoli-letters`  
**Primary branch:** `main`  
**Handover date:** 2026-08-23

This document is the current project-level handover for continuing the multi-volume Kalaignar Murasoli Letters archive in a new chat/window or with another worker.

It should be read together with:

1. [`VOLUME_PROCESSING_GUIDE.md`](VOLUME_PROCESSING_GUIDE.md)
2. [`VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md)
3. [`TRANSCRIPTION_GUIDE.md`](TRANSCRIPTION_GUIDE.md)
4. [`FUTURE_VOLUME_WORK_GUIDELINES.md`](FUTURE_VOLUME_WORK_GUIDELINES.md)
5. [`START_NEXT_MURASOLI_VOLUME_PROMPT.md`](START_NEXT_MURASOLI_VOLUME_PROMPT.md)

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
- Second full-volume visual/textual-fidelity verification: **IN PROGRESS — PDF 001–010 verified**
- Second-pass corrections so far: **5 canonical page files**
- English translation: **blocked** until the second visual/textual-fidelity gate passes

The complete Tamil transcription sequence is durable, and the structural audit has passed. The current work is the independent second direct scan comparison of every canonical page.

Second-pass corrections so far:

- PDF 002 — `சீதா பதிப்பகம்` → scan-printed `சீதை பதிப்பகம்`.
- PDF 003 — Tamil publisher `சீதா பதிப்பகம்` → scan-printed `சீதை பதிப்பகம்`.
- PDF 008 — `எடுத்துச் இயம்பியவர்கள்` → scan-printed `எடுத்து இயம்பியவர்கள்`.
- PDF 009 — `ஏற்பாடித் தொகுத்துச் சொல்லவும்` → scan-printed `ஏற்றபடி தொகுத்துச் சொல்லவும்`.
- PDF 010 — `பேரறுமை` → scan-printed `பேரருமை`.

PDF 001, 004–007 passed without canonical text correction. PDF 005 is a no-printed-text page whose faint show-through remains correctly excluded.

The live second-pass log is:

- [`volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md)

**Exact next activity:** resume the second full-volume visual/textual-fidelity verification at **PDF 011 / printed page 10**, continue sequential direct scan comparison, record PASS/corrections, and do **not** start English translation until all **402** pages have passed this gate.

Authoritative continuation files:

- [`volumes/volume-45/README.md`](volumes/volume-45/README.md)
- [`volumes/volume-45/PROGRESS.md`](volumes/volume-45/PROGRESS.md)
- [`volumes/volume-45/AUDIT.md`](volumes/volume-45/AUDIT.md)
- [`volumes/volume-45/FULL_VOLUME_STRUCTURAL_AUDIT.md`](volumes/volume-45/FULL_VOLUME_STRUCTURAL_AUDIT.md)
- [`volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md`](volumes/volume-45/FULL_VOLUME_TEXTUAL_FIDELITY_AUDIT.md)
- [`volumes/volume-45/metadata.yml`](volumes/volume-45/metadata.yml)
- [`volumes/volume-45/contents/index.md`](volumes/volume-45/contents/index.md)
- [`volumes/volume-45/chapters/README.md`](volumes/volume-45/chapters/README.md)

Do not restart Volume 45 transcription from an earlier boundary.

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

## 4. Mandatory new-volume startup

For a new attached volume: read all controlling root guides and this handover; inspect the repository for existing work; verify the volume number from the scan; record source metadata only when supported; inspect contents and source anomalies; use OCR/text layers only as aids; do not commit the source PDF unless explicitly instructed; and continue existing target-volume work rather than duplicating it.

---

## 5. Tamil transcription rules

First new-volume transcription commit is PDF 001–025 exactly. If PDF 25 interrupts a letter, the next commit starts at PDF 26 and completes that letter first. Default subsequent iteration is five complete consecutive actual source letters. One canonical Markdown file is kept per PDF page, and every accepted page/title/boundary/closing/date must ultimately be supported by the scan. Contents, chapter records/index, metadata, progress, audit and README are maintained with each completed iteration.

---

## 6. Keep Tamil QA stages distinct

1. iteration/batch audit;
2. full-volume Tamil structural audit;
3. second visual verification;
4. translation textual-fidelity audit.

English translation remains blocked until the required Tamil gates pass. A later English concern does not justify changing canonical Tamil unless fresh direct scan comparison proves the Tamil transcription itself is wrong.

---

## 7. Source anomalies and gaps

If printed text appears wrong or inconsistent, preserve and document it. Do not repair duplicate/skipped numbers, unusual dates, contents/title differences, malformed English, or inconsistent figures using outside knowledge. If the controlling PDF genuinely omits material, mark the record source-incomplete and do not reconstruct it.

---

## 8. English translation/release handoff

Translate from audited canonical Tamil in clear contemporary English while preserving thought order, political force, irony, rhetorical questions, repetition, quotations, names, dates, figures, units, source-supplied English, anomalies and source gaps. Retain the complete available audited Tamil under `Original Tamil — மூலத் தமிழ்` in every bilingual record.

Default future-volume translation flow: three-letter pilot → bilingual pilot review → lock volume conventions → five actual source records per translation batch → separate bilingual alignment gate → full-volume editorial consistency review → manifest → final release report.

---

## 9. Git/concurrency discipline

Work on `main` as requested; never force-push routine work; recheck `main` before writes when concurrency is possible; preserve unrelated concurrent changes; keep iteration scope explicit; remove temporary artefacts; and verify the resulting repository tree before claiming completion.

---

## 10. Meaning of “Proceed with next activity”

Inspect the current durable target-volume state, identify the next already-defined gate/batch, execute it directly, and report completed source/page scope, QA result, commit SHA where applicable, current counts/status and exact next activity. Do not ask the user to choose among routine next steps.

---

## 11. Clean interruption/handoff rule

At any interruption, the repository itself must contain the exact completed page/letter range, anomalies/gaps, audit state, translation state and next PDF page/letter. The chat must never be the sole place where critical archival state exists.

For Volume 45, transcription and the full-volume structural audit are complete. The second full-volume visual/textual-fidelity audit is verified through **PDF 010**. Resume at **PDF 011 / printed page 10** unless a later committed repository update moves that boundary.
