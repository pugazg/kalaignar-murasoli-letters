# Volume 1 — Canonical Migration Audit

## Source intake

- Source: `Vol1.pdf`
- SHA-256: `02eda7e7bb74d6d611351319ea87bc7761df6e9c5e73cc28883940b62d1fc6df`
- Size: **244,892,260 bytes**
- PDF pages: **401**
- Printed pages stated by publisher: **400**
- Edition: **1st edition, 2022**
- Publisher: **Seethai Pathippagam**
- Usable searchable text layer: **none**

## Migration rule

The existing `volumes/volume-1/` corpus is preserved as legacy provenance. The scan controls the new canonical page layer. Existing source-corrected Tamil and English may assist comparison but cannot silently override the printed scan.

For **Volume 1 alone**, regular iterations now use **10 complete consecutive letters**, per the volume-specific instruction. This overrides the repository's normal five-letter cadence only for Volume 1. A documented final residue may be smaller.

## Iteration 1 — mandatory PDF 001–025

**Result: PASS — first-pass canonical migration complete for this scope.**

Coverage:

- PDF 001: front cover
- PDF 002: title page
- PDF 003: publication/distribution matter
- PDF 004: illustrated dedication/front matter
- PDF 005: blank page with faint show-through only
- PDF 006–014: M. K. Stalin foreword/panindurai, printed pages 5–13
- PDF 015–017: publisher preface, printed pages 14–16
- PDF 018–023: printed contents, printed pages 17–22, **110 entries**
- PDF 024–025: start of letter 0001, printed pages 23–24

Checks performed:

- one canonical Markdown page per PDF page in scope: **25 / 25**;
- page numbering and printed-page offset checked against the scan;
- front matter distinguished from library stamps/handwriting;
- printed contents preserved as printed rather than replaced by legacy actual-letter titles;
- contents entry 63 preserves its blank printed date cell;
- letter 0001 title/date/start checked against the scan;
- page-25 boundary intentionally left partial; no text from PDF 026 was imported;
- no source PDF was committed;
- no legacy bilingual file was changed;
- no English migration/translation was started.

## Iteration 2 — complete interrupted letter 0001

**Result: PASS — letter 0001 canonical boundary complete.**

Coverage:

- PDF 026 / printed 25: continuation of letter 0001;
- PDF 027 / printed 26: final body paragraphs, `அன்புள்ள,`, `மறவன்`, and printed date `(22-10-1968)`;
- PDF 028 was inspected only to verify that letter 0002 begins there; no PDF-028 text was committed in this iteration.

Checks performed:

- canonical page files added for PDF 026–027 only;
- source wording, punctuation, political comparison and rhetorical-question sequence retained;
- letter 0001 chapter boundary promoted from partial to complete;
- verified complete coverage is **PDF 024–027 / printed 23–26**;
- the printed-contents hint that letter 0002 starts at printed page 27 is independently confirmed by the visible heading on PDF 028;
- legacy bilingual files remain unchanged;
- English migration remains blocked.

## Iteration 3 — initial five-letter batch: 0002–0006

**Result: PASS — five complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0002 — `நீ விளைத்த கழனி - நீ உழைத்த உழைப்பு!`: PDF **028–031**, date **24-10-1968**;
- 0003 — `நிதானமாகப் பேசுங்கள்!`: PDF **032–035**, date **25-10-1968**;
- 0004 — `உன்னால் முடிந்ததைச் செய்து விட்டாயா?`: PDF **036–038**, date **27-10-1968**;
- 0005 — `நேர்மையும் பொறுப்பும் நீர்மேல் எழுத்தல்ல!`: PDF **039–042**, date **29-10-1968**;
- 0006 — `வெற்றி பெற்றவனே உன் வேலை என்ன?`: PDF **043–047**, date **30-10-1968**.

Checks performed:

- one canonical page file for every PDF page **028–047**: **20 / 20**;
- actual letter-start headings and closing sign-off/date pages visually checked against the scan;
- legacy source-corrected Tamil used only as migration assistance and reconciled against the visible scan;
- PDF 039 visibly prints page number 38, while PDF 040 visibly prints 40; text continues directly, so printed page number 39 is a pagination anomaly rather than missing text;
- PDF 048 inspected only to confirm that letter 0007 begins there;
- no legacy bilingual file modified; no English migration started.

## Iteration 4 — first Volume 1 ten-letter batch: 0007–0016

**Result: PASS — 10 complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0007 — `தோற்ற முயலே! முன்போல சுறுசுறுப்பாக இரு!`: PDF **048–053**, date **31-10-1968**;
- 0008 — `“தீராதி தீரர்- தேசீய மகிபர்- பராக்! பராக்!”`: PDF **054–057**, date printed **31-10-68**;
- 0009 — `வீரனே! வெற்றி என்றைக்கும் உன் பக்கம்தான்!`: PDF **058–062**, date **01-11-1968**;
- 0010 — `பாவி கெடுத்தானே; பலே சாப்பாட்டை!`: PDF **063–066**, date **02-11-1968**;
- 0011 — `தென்றல்- தெம்பாங்கு- தேன்கீதம்!`: PDF **067–069**, date **06-11-1968**;
- 0012 — `“பூப்போட்ட கிளாசிலே போட்டய்யா ஒண்ணரை!”`: PDF **070–072**, date **07-11-1968**;
- 0013 — `மேயர் தேர்தல் நேரம் - நிலை - நேர்த்தியான முடிவு!`: PDF **073–077**, date **09-11-1968**;
- 0014 — `‘பகைமரம்’ தழைக்க விடோம்!`: PDF **078–081**, date **11-11-1968**;
- 0015 — `நம்பிக்கையில்லாத் தீர்மானம் - நாடாளுமன்ற நிகழ்ச்சி!`: PDF **082–085**, date **14-11-1968**;
- 0016 — `யார் அந்த உணவு அமைச்சர்?`: PDF **086–089**, date **16-11-1968**.

Checks performed:

- one canonical page file for every PDF page **048–089**: **42 / 42**;
- all ten letter starts and all ten closing/sign-off/date boundaries visually checked against the scan;
- actual letter headings control over contents-page forms; notably 0008 and 0012 retain their scan headings rather than silently adopting contents variants;
- source-shortened date `(31-10-68)` on 0008 preserved at page level;
- source wording, rhetorical sequences, lists, quotations, emphases and sign-off forms retained;
- legacy source-corrected Tamil used only as migration assistance and checked against the visible scan in this scope;
- PDF 090 inspected only to verify that letter 0017 begins there; no PDF-090 text committed in this iteration;
- legacy bilingual files remain unchanged;
- English migration remains blocked.

## Iteration 5 — second Volume 1 ten-letter batch: 0017–0026

**Result: PASS — 10 complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0017 — `கிளம்பிற்றுக்காண் தமிழச் சிங்கக் கூட்டம்!`: PDF **090–093**, date **18-11-1968**;
- 0018 — `கழுதையும் - பன்றியும்!`: PDF **094–096**, date **22-11-1968**;
- 0019 — `“பசுத்தோல் வேங்கை பாராய்!”`: PDF **097–100**, date **25-11-1968**;
- 0020 — `“தமிழ்த்தாயே அவர்களை மன்னித்துவிடு!”`: PDF **101–104**, date **26-11-1968**;
- 0021 — `‘தமிழ் நாடு’ ஒரு முழு விளக்கம்!`: PDF **105–116**, date **28-11-1968**;
- 0022 — `கண்கள் திறக்க ஒரு கதை!`: PDF **117–118**, date **02-12-1968**;
- 0023 — `பரிதாபப்படுகிறேன்!`: PDF **119**, date **05-12-1968**;
- 0024 — `“அரசியல் மோசடியாம் - அறிவிக்கிறார்; ஆழ்வப் பிறவி!”`: PDF **120–122**, date **07-12-1968**;
- 0025 — `இந்தியும் மொரார்ஜி தேசாயும்!`: PDF **123–124**, date **09-12-1968**;
- 0026 — `தகுந்த பாடம் தரவேண்டாமா?`: PDF **125–126**, date **20-12-1968**.

Checks performed and source anomalies recorded:

- one canonical page file for every PDF page **090–126**: **37 / 37**;
- all ten heading pages, salutations, closing/sign-off forms and printed dates visually checked against the controlling scan;
- actual heading-page title controls over the contents variant for 0024; canonical title retains `ஆழ்வப் பிறவி`;
- PDF 095 deliberately suppresses words with printed ellipses around `சேலையிலே`; the omission marks are preserved and no wording is reconstructed;
- PDF 099 contains substantial scan-visible text that is absent from the legacy Tamil reading copy, including Anna's `ரத்தத்தின் ரத்தம் / சதையின் சதை` response and the Morarji/Hindi passage; canonical transcription follows the scan, not the legacy record;
- PDF 101 has a library stamp and handwritten accession/notation marks over/above the heading; these are non-authorial and omitted;
- PDF 109 prints `(?)` after `பொய்யா`; it is retained;
- PDF 113 prints `கண்யம்`; it is retained rather than normalised;
- PDF 115 repeats `தமிழ் நாடா?` before `மெட்ராஸ் ஸ்டேட்டா?`; the repetition is retained;
- PDF 119 contains an unmatched opening parenthesis after `திரியும்போது-`; it is retained as printed;
- PDF 123 and PDF 125 contain source-leading hyphens before `துணைப் பிரதமர்` and `ஷாவின்`; they are retained;
- PDF 124 prints `வில்லையா?`; it is retained;
- no silent modernisation, regularisation or reconstruction was applied to source-supported unusual forms;
- PDF 127 was inspected only enough to verify the start of 0027 — `காட்சி காண அல்ல - களம் காண!`; no PDF-127 text is committed in this batch;
- legacy bilingual files remain unchanged;
- English migration, bilingual alignment, full-volume structural audit, second visual verification, editorial review and release work remain unstarted/blocked as required.

## Iteration 6 — third Volume 1 ten-letter batch: 0027–0036

**Result: PASS — 10 complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0027 — `காட்சி காண அல்ல - களம் காண!`: PDF **127–128**, date **26-12-1968**;
- 0028 — `வெண்மணிச் சம்பவம் ஒரு விளக்கம்!`: PDF **129–131**, date **28-12-1968**;
- 0029 — `காங்கிரஸ் வெற்றியும் இந்தித் திணிப்பும்!`: PDF **132–133**, date **11-01-1969**;
- 0030 — `பாழடைந்த மண்டபமும் வெளவால்களும்!`: PDF **134–135**, date **17-01-1969**;
- 0031 — `வேங்கை போடும் வெள்ளாடு வேடம்!`: PDF **136–140**, date **18-01-1969**;
- 0032 — `காமராஜரின் கடற்கரைப் பேச்சின் பொருள் என்ன?`: PDF **141–142**, date **28-01-1969**;
- 0033 — `தெளிந்திடும் நீரோடை!`: PDF **143–147**, date **01-01-1971**;
- 0034 — `வென்றிட வேறு யாருளர்?`: PDF **148–151**, date **07-01-1971**;
- 0035 — `உனக்காக விழித்திருப்போம்!`: PDF **152–155**, date **10-01-1971**;
- 0036 — `“கிழச் சிங்கம், கிளறிய நெஞ்சம்!”`: PDF **156–160**, date **16-04-1971**.

Checks performed and source anomalies recorded:

- one canonical page file for every PDF page **127–160**: **34 / 34**;
- all ten heading pages, salutations, closing/sign-off forms and printed dates were visually checked against the controlling scan;
- letter 0028 closes on PDF 131 with the source-printed date `(28-12-1968)`; a conflicting legacy metadata value is not propagated into the canonical layer;
- PDF 137 prints the unusual punctuation `ஜனநாயக உரிமைகளை(!)`; it is retained;
- PDF 144 contains a substantial scan-visible 1938 anti-Hindi movement passage that is absent from the legacy Tamil reading copy; canonical transcription follows the scan, including the source's references to Periyar, தாளமுத்து, நடராசன், Anna's imprisonment, and the `தமிழர் படை` sequence;
- PDF 149 prints `எட்டு நாட்களுக்கு முன்பு`; the legacy reading copy's `ஏழெட்டு நாட்களுக்கு முன்பு` is not substituted;
- PDF 155 uses decorative diamond list markers and PDF 158 uses three-dot list markers; their list structure is retained in the canonical page layer;
- letters 0033–0035 address `அண்ணா,` and close `தம்பி, / மு. கருணாநிதி.`; letter 0036 begins `உடன் பிறப்பே!` and closes `அன்புள்ள, / மு. கருணாநிதி`, preserving the source-visible transition away from the earlier `மறவன்` sign-off;
- PDF 160 prints no final period after `மு. கருணாநிதி`; the source form is retained;
- no silent modernisation, correction, regularisation or reconstruction was applied to source-supported wording, punctuation, dates or typography;
- PDF 161 was inspected only enough to verify the start of 0037 — `நீயும் நானும் தூங்குவோமா?`; no PDF-161 text is committed in this batch;
- legacy bilingual files remain unchanged;
- English migration, bilingual alignment, full-volume structural audit, second visual verification, editorial review and release work remain unstarted/blocked as required.

## Current boundary

Canonical PDF coverage is **001–160 / 401**. Letters **0001–0036** are canonically complete, with no partial letter. The next regular Volume 1 migration activity begins at PDF 161 with letter 0037 and follows the Volume 1-specific **10-letter** rule for letters **0037–0046**, stopping before letter 0047.

These migration iterations are first-pass visual transcription gates. They are **not** the later full-volume structural audit, second visual verification, or translation textual-fidelity audit.
