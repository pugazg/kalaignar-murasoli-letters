# NEXT CHAT PROMPT — Volume 41 / normal five-letter batch 3307–3311

Continue directly in `pugazg/kalaignar-murasoli-letters`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable current state

Controlling source: `TVA_BOK_0065825_கலைஞரின்_கடிதங்கள்_தொகுதி_41.pdf`

- source SHA-256: `950eeb8c97d1cd6b8ab6c4cfd47739264c1223c0f34ba1f0da85c41f90ef3418`
- source extent: **402 physical PDF pages / 400 printed pages**
- canonical first-pass coverage: **PDF 001–033 / 402**
- contents: **58 / 58 rows transcribed — 3306–3363**
- Letter **3306**: **COMPLETE — PDF 024–033 / printed 23–32**
- actual closing/date: **அன்புள்ள, மு.க. — 25-11-2007**
- Letter **3307 — உறவு வேலி உறுதிப்பட வாரீர் திருநெல்வேலி!** begins **PDF 034 / printed 33**
- completed letters: **1 / 58**
- partial letters: **0**
- English remains blocked

## Read first

1. `VOLUME_PROCESSING_GUIDE.md`
2. `VOLUME_TRANSCRIPTION_BATCHING_POLICY.md`
3. `TRANSCRIPTION_GUIDE.md`
4. `volumes/volume-41/AUDIT.md`
5. `volumes/volume-41/PROGRESS.md`
6. `volumes/volume-41/contents/index.md`
7. `volumes/volume-41/chapters/README.md`

Refetch live `main` before editing and immediately before commit.

## Exact activity

Process the first normal **five-letter** transcription iteration:

**3307, 3308, 3309, 3310, 3311**

Start at **PDF 034 / printed 33**.

For each record:

- verify actual source title separately from the contents title;
- transcribe every physical page exactly from scan;
- preserve source spelling, punctuation, quotations, figures and page boundaries;
- verify closing/signature/date;
- create a chapter record only after actual boundaries are established;
- do not infer the next boundary from contents alone.

Stop after the verified end of **Letter 3311**. Do not begin Letter 3312 in the same commit.

Update all applicable Volume 41 and root control documents atomically. English remains blocked.

Commit message should state the actual completed letter range and PDF page span.
