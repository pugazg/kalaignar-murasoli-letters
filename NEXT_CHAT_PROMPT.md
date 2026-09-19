# NEXT CHAT PROMPT — Volume 42 / first transcription batch PDF 001–025

Continue directly in `pugazg/kalaignar-murasoli-letters`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Mandatory startup

Read completely:

1. `VOLUME_PROCESSING_GUIDE.md`
2. `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
3. `TRANSCRIPTION_GUIDE.md`
4. `FUTURE_VOLUME_WORK_GUIDELINES.md`
5. `PROJECT_HANDOVER.md`
6. this `NEXT_CHAT_PROMPT.md`
7. `volumes/volume-42/README.md`
8. `volumes/volume-42/metadata.yml`
9. `volumes/volume-42/PROGRESS.md`
10. `volumes/volume-42/AUDIT.md`
11. `volumes/volume-42/contents/index.md`
12. `volumes/volume-42/chapters/README.md`
13. `volumes/volume-42/TRANSLATION_PLAN.md`

Controlling attachment: `TVA_BOK_0065826_கலைஞரின்_கடிதங்கள்_தொகுதி_42.pdf`.

## Durable source-intake state

- Scan-confirmed volume: **42**.
- Visible cover/title date span: **31.01.2009–30.10.2009**.
- Publisher: **Seethai Pathippagam**.
- Edition: **1st edition 2022**.
- Publication states **400 printed pages**.
- Controlling PDF has **402 physical PDF pages**. The earlier 150-page view was only a preview-layer limit.
- No usable parsed/searchable text layer is available; the rendered scan controls.
- Printed contents are PDF **018–022**.
- Printed contents provisionally contain **64 rows** over nominal span **3364–3427**.
- Contents visibly print **3154** between **3376** and **3378**; preserve this exact source anomaly. Do not renumber it silently.
- Letter **3364** begins PDF **024 / printed page 23**.
- PDF **025** remains inside Letter 3364.
- Canonical Tamil transcription: **not started**.
- English translation: **blocked**.

## Exact next activity — mandatory first batch

Transcribe **exactly PDF pages 001–025** and commit atomically with message:

`Transcribe Volume 42 PDF pages 001-025`

Requirements:

- create `pages/page-001.md` through `pages/page-025.md`;
- include covers, publication matter, foreword/publisher matter, contents, blank/show-through pages and letter text without omission;
- visually compare all 25 Markdown pages directly with the scan;
- preserve printed spelling, punctuation, figures, English/Latin text, stamps/annotations distinctions and page boundaries;
- fully transcribe printed contents PDF 018–022 exactly as printed;
- preserve the printed `3154` contents row as printed rather than normalising it;
- create/update Letter **3364** chapter metadata from PDF 024 onward;
- because PDF 25 interrupts 3364, set it **partial**, do not invent `pdf_page_end`, and state that continuation begins at PDF 26;
- update `contents/index.md`, `chapters/README.md`, `metadata.yml`, `PROGRESS.md`, `AUDIT.md`, and volume/root controls as applicable;
- do not begin PDF 26 in this commit;
- do not begin English translation.

After this commit, the next activity is the special continuation commit beginning at **PDF 026** and ending only when Letter **3364** reaches its verified closing/date page.
