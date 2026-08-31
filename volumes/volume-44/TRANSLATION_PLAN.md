# Volume 44 — English Translation Plan

**Status:** main translation drafting/source-check complete — **53 / 53 records source-checked, Letters 3484–3536 / PDF 024–399**. Bilingual alignment is in progress — **5 / 53 aligned, Letters 3484–3488 / PDF 024–066**.

All required Tamil gates passed before English work began. English drafting/source-check completed the pilot and ten regular batches through Letter 3536 with **0 canonical Tamil changes** during the regular batches.

The first bilingual alignment batch **3484–3488 / PDF 024–066** is now synchronized and PASS. It required one English punctuation-only correction in Letter 3487 / PDF 051 (`indefinitely.` → `indefinitely?`) to preserve the audited Tamil source punctuation. Canonical Tamil changes during this alignment batch: **0**.

Durable QA records:

- [`translations/en/PILOT_REVIEW_3484_3486.md`](translations/en/PILOT_REVIEW_3484_3486.md)
- [`translations/en/BILINGUAL_ALIGNMENT_REVIEW_3484_3488.md`](translations/en/BILINGUAL_ALIGNMENT_REVIEW_3484_3488.md)
- [`translations/en/BATCH_SOURCE_CHECK_3487_3491.md`](translations/en/BATCH_SOURCE_CHECK_3487_3491.md)
- [`translations/en/BATCH_SOURCE_CHECK_3492_3496.md`](translations/en/BATCH_SOURCE_CHECK_3492_3496.md)
- [`translations/en/BATCH_SOURCE_CHECK_3497_3501.md`](translations/en/BATCH_SOURCE_CHECK_3497_3501.md)
- [`translations/en/BATCH_SOURCE_CHECK_3502_3506.md`](translations/en/BATCH_SOURCE_CHECK_3502_3506.md)
- [`translations/en/BATCH_SOURCE_CHECK_3507_3511.md`](translations/en/BATCH_SOURCE_CHECK_3507_3511.md)
- [`translations/en/BATCH_SOURCE_CHECK_3512_3516.md`](translations/en/BATCH_SOURCE_CHECK_3512_3516.md)
- [`translations/en/BATCH_SOURCE_CHECK_3517_3521.md`](translations/en/BATCH_SOURCE_CHECK_3517_3521.md)
- [`translations/en/BATCH_SOURCE_CHECK_3522_3526.md`](translations/en/BATCH_SOURCE_CHECK_3522_3526.md)
- [`translations/en/BATCH_SOURCE_CHECK_3527_3531.md`](translations/en/BATCH_SOURCE_CHECK_3527_3531.md)
- [`translations/en/BATCH_SOURCE_CHECK_3532_3536.md`](translations/en/BATCH_SOURCE_CHECK_3532_3536.md)
- [`translations/en/GLOSSARY.md`](translations/en/GLOSSARY.md)
- [`translations/en/TRANSLATION_MANIFEST.csv`](translations/en/TRANSLATION_MANIFEST.csv)

## Locked Volume 44 policy

- Preserve Kalaignar’s thought and argument order, political directness, irony, accusation, repetition and rhetorical questions.
- Retain `Udanpirappē` for the standard characteristic salutation when supported by the source.
- Use `With affection, M.K.` where the source has the standard `அன்புள்ள, மு.க.` closing.
- Retain public-language units such as `lakh` and `crore`.
- Use source-supported party/government, reservation, legal, employment and period-specific social/community terminology consistently with the locked glossary.
- Preserve genuinely printed source English verbatim where it functions as source wording.
- Preserve source anomalies and source gaps rather than repairing them; explicitly surface internally opaque audited text when necessary.
- Keep historical, legal and political claims source-framed and do not silently reconcile them from outside knowledge.
- Keep figures, dates, lists, statutory references, quotations and continuation/conclusion markers in source order.
- Every bilingual record must include the complete available audited Tamil under `## Original Tamil — மூலத் தமிழ்`.
- The audited canonical Tamil is the immediate translation/alignment source; OCR, contents wording and outside knowledge may not silently override it.

## Phase 3 — bilingual alignment

Follow the five-record alignment method already proven in Volume 45. Each alignment batch must:

1. compare each complete English record against its complete audited Tamil source, including the reproduced Tamil appendix in physical page order;
2. check title, salutation, closing/date, paragraph and argument sequence, complete substantive coverage, figures/units, names/institutions, quotations, source English, rhetoric, repetition, continuation/conclusion markers and documented anomalies;
3. apply only English corrections needed for meaning-level alignment;
4. change canonical Tamil only if a suspected Tamil defect is rechecked against the controlling scan and proven;
5. create a durable `BILINGUAL_ALIGNMENT_REVIEW_<start>_<end>.md` report;
6. mark the reviewed records and manifest rows aligned while retaining `translation_status: source-checked`; and
7. keep the later volume-level English editorial consistency review and final release verification separate.

## Exact next activity

Align **Letters 3489–3493 / PDF 067–098** as the second five-record bilingual-alignment batch. Create `translations/en/BILINGUAL_ALIGNMENT_REVIEW_3489_3493.md`, update the five English records/manifest/progress/index and relevant Volume/root controls, and stop after Letter 3493. Do **not** begin 3494, editorial review or final release verification in the same activity.
