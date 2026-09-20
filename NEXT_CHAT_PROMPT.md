# NEXT CHAT PROMPT — Volume 42 / full-volume Tamil structural audit

Continue directly in `pugazg/kalaignar-murasoli-letters`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable state

- Controlling source: `TVA_BOK_0065826_கலைஞரின்_கடிதங்கள்_தொகுதி_42.pdf`
- Source extent: **402 physical PDF pages / 400 printed pages**.
- First-pass canonical coverage: **PDF 001–402 / 402 COMPLETE**.
- Printed contents: **64 / 64 rows transcribed**.
- Completed actual source records: **64 — 3364–3376, 3154, 3378–3427**.
- Partial records: **0**.
- Source-incomplete records: **0**.
- English translation: **blocked**.
- Full-volume Tamil structural audit: **NOT STARTED**.
- Second full-volume direct visual/textual-fidelity verification: **pending**.

## Verified source facts that must remain intact

1. **Numbering anomaly:** printed contents and actual PDF **092 / printed 91** both print **3154** between 3376 and 3378. **Do not invent 3377.**
2. **Letter 3392 duplication:** the printed source genuinely repeats the title/body across PDF 209–212; both physical copies are preserved.
3. **Letter 3425 title-layer difference:** printed contents uses `திருந்தப் போகிறார்களா?`, while actual PDF **386** uses joined `திருந்தப்போகிறார்களா?`. Preserve both source layers independently.
4. **Volume ending:** Letter **3427** closes on PDF **401 / printed 400** with date **30-10-2009**.
5. PDF **402** is non-letter back-cover / portrait / publisher-contact-price material.
6. **No Letter 3428 exists in Volume 42**; Volume 43 begins separately.

## Exact next activity — full-volume Tamil structural audit

Read `VOLUME_PROCESSING_GUIDE.md`, `TRANSCRIPTION_GUIDE.md`, `SERIES_FRONT_MATTER_POLICY.md`, Volume 42 `metadata.yml`, `PROGRESS.md`, `AUDIT.md`, `contents/index.md`, `chapters/README.md`, and the current page/chapter tree before changing anything.

Audit **PDF 001–402 / 402** structurally. Verify:

- exactly one canonical `pages/page-NNN.md` record for every PDF page 001–402;
- no missing, duplicate or extra page-number files;
- front matter, publisher matter, contents, blank/non-letter pages, letters and back cover are structurally classified correctly;
- shared-front-matter records PDF 001–017 remain valid under `SERIES_FRONT_MATTER_POLICY.md`;
- printed contents count is **64 / 64**;
- actual source-record count is **64**;
- actual record sequence is **3364–3376, 3154, 3378–3427**;
- every chapter file maps to its canonical page range with no overlap/gap except documented non-letter matter;
- every letter start/end, printed-page range, date and closing/signature page structurally reconciles;
- Letter 3392 duplication is preserved, not deduplicated;
- Letter 3425 contents/actual-title distinction is documented consistently;
- Letter 3427 ends at PDF 401 / printed 400;
- PDF 402 remains non-letter and no 3428 is created;
- no accidental duplicate canonical body, invalid/replacement Unicode, zero-width OCR residue, broken chapter/page links or large structural omissions;
- metadata, progress, audit, volume README, root README and handover all agree.

If the structural audit passes, record a durable **FULL-VOLUME STRUCTURAL AUDIT — PASS** and update all applicable controls atomically.

Do **not** claim second visual/textual-fidelity PASS and do **not** start English translation. The exact following gate after structural PASS is the **second full-volume direct visual/textual-fidelity verification**.

Suggested commit message:

`Audit Volume 42 full Tamil structure — PDF pages 001-402`
