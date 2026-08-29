# Next Chat Prompt — Continue Murasoli Letters Volume 44

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Attach the controlling source PDF again when starting a fresh chat:

`TVA_BOK_0065830_கலைஞரின்_கடிதங்கள்_தொகுதி_44.pdf`

## Durable boundary

**Volume 44 source intake is complete; Tamil transcription has not started.**

- Scan-confirmed volume: **44**
- PDF pages: **400**
- Source SHA-256: `573d65d7b7d3a8e3cc158b7f91af3a9382ac90ea1eaa37e8c0022b5a64dc747d`
- Date span printed on cover/title: **18.07.2010–11.03.2011**
- Printed contents: PDF **018–022**
- Provisional source inventory: **53 records, 3484–3536**
- Canonical pages: **0 / 400**
- Completed letters: **0**
- English translation: **blocked**

PDF 024 begins letter 3484 at printed page 23, and PDF 025 continues that letter.

## Exact next activity

Execute the mandatory first transcription batch **PDF pages 001–025 exactly**:

1. create `volumes/volume-44/pages/page-001.md` through `page-025.md`;
2. visually compare every new page with the controlling scan;
3. preserve covers, publisher matter, foreword/publisher text, contents, blanks and letter text without silent normalization;
4. transcribe printed contents PDF 018–022 exactly into the canonical page files and update `contents/index.md`;
5. create/update the 3484 chapter record as `partial`;
6. update `chapters/README.md`, `metadata.yml`, `PROGRESS.md`, `AUDIT.md`, volume `README.md`, and any applicable root status;
7. stop exactly at PDF 025 — do not include PDF 026;
8. commit the batch atomically with message `Transcribe Volume 44 PDF pages 001-025`.

After that commit, the next activity is to begin at PDF 026 and finish letter 3484 before regular five-complete-letter transcription iterations.

Before changing anything, fetch live `main`, read the controlling guides and target-volume durable files, and preserve any concurrent unrelated changes. The scan is the highest textual authority; OCR and contents are aids only.
