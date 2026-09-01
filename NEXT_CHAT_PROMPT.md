# Next Chat Prompt — Continue Murasoli Letters Volume 43

Continue the Kalaignar Murasoli Letters archival project directly in:

`pugazg/kalaignar-murasoli-letters`

Branch: `main`

Controlling source PDF:

`TVA_BOK_0065828_கலைஞரின்_கடிதங்கள்_தொகுதி_43.pdf`

## Live-main rule for a fresh chat

**Fetch live `main` first and treat it as authoritative.** If `main` has advanced beyond any checkpoint copied into a prompt, preserve the newer durable state and continue from it. Do not reset or overwrite later completed work.

Before changing anything, read the repository processing guides, `PROJECT_HANDOVER.md`, this `NEXT_CHAT_PROMPT.md`, and the controls for the active source/volume.

## Volume 43 durable boundary

- Printed pages: **400**
- Physical PDF pages: **402**
- Source SHA-256: `53607130844a56b7b65b7dc5451031a33690c867e81c5ffab6e9b70958fdaf35`
- Source inventory: **56 records, 3428–3483**
- Date span: **01.11.2009–17.07.2010**
- Printed contents: **PDF 018–022**
- Canonical Tamil pages: **PDF 001–103 / 402**
- Completed Tamil letters: **11 / 56 — 3428–3438**
- English translation: **blocked pending Tamil gates**

Latest completed boundaries:

- **3434** — PDF 070–075 — 18-11-2009
- **3435** — PDF 076–086 — 26-11-2009
- **3436** — PDF 087–092 — 28-11-2009
- **3437** — PDF 093–098 — 30-11-2009
- **3438** — PDF 099–103 — 4-12-2009

Documented contents/actual-title discrepancies must remain source-layer specific:

- 3430: printed contents differs from actual PDF 040 title.
- 3435: contents `முடிந்த தொடாக்கதை; முடியாத வரலாறு!`; PDF 076 `முடிந்த தொடர்கதை; முடியாத வரலாறு!`.
- 3438: contents `ஊனமுற்றோரின் ஊன்று கோலாகக் கழக அரசு!`; PDF 099 `ஊனமுற்றோரின் ஊன்றுகோலாகக் கழக அரசு!`.

Printed contents Letter 3467 has a blank date cell; preserve it as blank until the source letter itself is reached and verified.

PDF **104 / printed page 103** begins Letter **3439 — `குளிர் தருவென; தரு நிழலெனக் கோவையில் மாநாடு!`**.

## Exact next activity

Transcribe the next **five complete Volume 43 source records, Letters 3439–3443**, beginning at **PDF 104 / printed page 103**. Determine each closing/date boundary directly from the scan, create the corresponding canonical page and chapter records, synchronize contents/metadata/progress/audit/README controls, and stop before Letter 3444. Do not start English translation.

Before any mutation, recheck live `main`, preserve concurrent work, prefer a validated atomic commit, use a normal fast-forward with `force: false`, and verify parent → new HEAD changed-file scope.
