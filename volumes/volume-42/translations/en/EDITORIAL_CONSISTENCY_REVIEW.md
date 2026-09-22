# Volume 42 English Editorial Consistency Review

## Scope

- Volume: **42**
- Bilingual records reviewed as one English corpus: **64 / 64**
- Source-record identity: **3364–3376, 3154, 3378–3427**
- Canonical translated source range: **PDF 024–401**
- Source-checked before this gate: **64 / 64**
- Bilingual-aligned before this gate: **64 / 64**
- Editorial result: **PASS — 64 / 64**
- English-only consistency corrections in this pass: **2**
- Canonical Tamil changes in this pass: **0**
- New direct scan re-checks triggered in this pass: **0**

## Method

This is the separate volume-level consistency gate required after source-check drafting and complete bilingual meaning-level alignment. The review used the Volume 42 English README/index, locked `GLOSSARY.md`, all completed `BILINGUAL_ALIGNMENT_REVIEW_*.md` reports through `BILINGUAL_ALIGNMENT_REVIEW_3419_3427.md`, and all **64 aligned bilingual records**. A translation manifest does not yet exist for Volume 42; manifest creation and reconciliation remain part of the next final-release gate.

The completed alignment reviews had already compared each English record against its complete audited Tamil source. This editorial pass therefore concentrated on cross-record consistency rather than retranslating or re-adjudicating source meaning. It checked front-matter/H1 agreement, dates and source-page presentation, translator-note structure, salutations and closings, names and institutional forms, locked glossary terminology, public-language quantity style, capitalization, source-supplied English, documented source anomalies, and the presence of the complete appended Tamil.

The controlling scan remains the ultimate textual authority. No possible residual Tamil defect was exposed by this editorial pass, so no new scan comparison or Tamil canonical change was required.

## Corpus validation results

### Record and structural integrity

The English `letters/` directory contains exactly **64 source-letter records** for Volume 42, plus its directory README. The record identity remains **3364–3376, 3154, 3378–3427**; the genuine printed source number **3154** remains between 3376 and 3378 and no 3377 is invented.

Across all 64 bilingual records:

- front-matter `volume`, `letter_number`, English title, source PDF range, `translation_status: source-checked`, textual-fidelity-audit pointer and `bilingual_alignment_status: aligned` are present and coherent;
- each H1 agrees with its front-matter letter number and English title;
- the displayed source-page links agree with the front-matter PDF start/end range;
- each record contains exactly one `Translator’s note` and exactly one `## Original Tamil — மூலத் தமிழ்` appendix;
- every record retains a single ordinary closing `With affection, M.K.`;
- visible date presentation agrees with front-matter date throughout the ordinary records.

Letter **3389** remains the deliberate republication-framing exception: instead of presenting an inferred older original-letter date, it retains the Volume 42 record date and explicitly labels **Source closing date: 01 April 2009**. Letter **3401** correctly retains the source-specific salutation **Kazhagam Udanpirappē** rather than being normalised to the ordinary form.

### Locked terminology and capitalization

The locked recurring treatments remain coherent across the corpus, including **Union Government**, **State government**, **Udanpirappē**, **Tamil Eelam**, **ceasefire**, **internal reservation**, **Arunthathiyar**, **Katchatheevu**, **Classical Language**, **Sethusamudram project / Sethu project**, and **work stoppage** where the glossary defines them.

Two translated-prose capitalization inconsistencies were demonstrated and corrected:

1. Letter **3397 / PDF 232–237** used `State Government` in ordinary translated prose. Because Volume 42 locks `மாநில அரசு` as **State government**, this was corrected to **State government**.
2. Letter **3422 / PDF 374–377** used `Union government` in ordinary translated prose. Because Volume 42 locks `மத்திய அரசு` as **Union Government**, this was corrected to **Union Government**.

No `Udanpirappe`, `sub-reservation`, `inner reservation`, `Central Government`, or million/billion conversion inconsistency remained in ordinary translated prose.

### Protected source-supplied English

Genuinely printed English remains untouched even when its style differs from the corpus convention. The editorial pass specifically reconfirmed protected material including:

- Letter **3387** source-supplied English, including its printed capitalization such as `State Government`;
- Letter **3405** source-supplied *Telegraph* English;
- Letter **3408** source-supplied English with **Katcha Theevu** spelling;
- Letter **3420** two source-supplied English meeting-record extracts;
- Letter **3425** five source-supplied English discussion topics, including **Samerian** and **SriLankan**;
- Letter **3426** source-supplied **Quota and Rota**.

These protected strings were not regularised to glossary style.

### Documented source anomalies and layer distinctions

The editorial pass reconfirmed that the following remain independent source facts rather than consistency defects:

- source number **3154** between 3376 and 3378; no invented 3377;
- Letter **3392** genuine duplicated physical printing across PDF 209–212, retained in the Tamil appendix;
- Letter **3419** canonical PDF 357 source form **புறங்காந்திமடைந்து**, retained without silent normalisation;
- Letter **3425** contents-layer `திருந்தப் போகிறார்களா?` versus actual PDF 386 `திருந்தப்போகிறார்களா?`;
- Letter **3427** closes at PDF **401 / printed 400**; PDF **402** remains non-letter back-cover / portrait / publisher-contact-price material and no Letter 3428 is created.

### Quotations, rhetoric and source voice

The completed alignment phase had already verified quotations, rhetorical questions, repetition, accusation, political force, figures and source order. This editorial pass found no corpus-level convention that justified weakening, modernising, standardising or reattributing those passages. Apart from the two capitalization corrections above, no bilingual body was edited.

## Corrections applied

Exactly **2 English-only editorial consistency corrections**:

1. **Letter 3397 / PDF 232–237:** `State Government` → **`State government`** in translated prose, following the locked Volume 42 treatment of `மாநில அரசு`.
2. **Letter 3422 / PDF 374–377:** `Union government` → **`Union Government`** in translated prose, following the locked Volume 42 treatment of `மத்திய அரசு`.

Canonical Tamil changes: **0**. New scan-level corrections: **0**.

## Outcome

**PASS — Volume 42 English editorial consistency review complete for all 64 / 64 bilingual records.**

Current English QA state after synchronization:

- Source-checked: **64 / 64**
- Bilingual-aligned: **64 / 64**
- Editorially reviewed: **64 / 64 — PASS**
- Final verified for release: **0 / 64 — pending**
- Cumulative alignment corrections retained: **39**
- Editorial English-only corrections: **2**
- Editorial canonical Tamil changes: **0**

## Exact next activity

Perform the separate **Volume 42 final English release verification**. Create and reconcile `TRANSLATION_MANIFEST.csv` to exactly **64 actual source records — 3364–3376, 3154, 3378–3427**; validate unique record identity and English paths; confirm `source-checked`, `aligned` and `reviewed` state for every manifest row; verify every bilingual file and complete appended Tamil; reconfirm the source-number anomaly 3154, the 3392 duplication, the 3425 title-layer distinction, Letter 3427 ending at PDF 401 and PDF 402 as non-letter matter; create `RELEASE_REPORT.md`; then synchronize final-release status and repository controls. Do not describe Volume 42 English as FINAL RELEASE COMPLETE until that gate passes.