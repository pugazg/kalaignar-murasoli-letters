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

## Iteration 7 — fourth Volume 1 ten-letter batch: 0037–0046

**Result: PASS — 10 complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0037 — `நீயும் நானும் தூங்குவோமா?`: PDF **161–164**, date **17-04-1971**;
- 0038 — `இன்றே தொடங்கிடுக பணி!`: PDF **165–168**, date **18-04-1971**;
- 0039 — `“கோவை - ஒரு கனி! நீ ஒரு கிளி!”`: PDF **169–173**, date **22-04-1971**;
- 0040 — `அண்ணன்-கண்ணன் எங்கே?`: PDF **174–177**, date **23-04-1971**;
- 0041 — `நான் கேட்கும் பிச்சை!`: PDF **178–180**, date **26-05-1971**;
- 0042 — `ஜூலை 15!`: PDF **181–183**, date **10-07-1972**;
- 0043 — `பெருமை எது?`: PDF **184–186**, date **17-07-1972**;
- 0044 — `வழக்கு ஜோடனை!`: PDF **187–191**, date **22-07-1972**;
- 0045 — `மதுரை மாட்சி (1)`: PDF **192–195**, date **09-08-1972**;
- 0046 — `மதுரை மாட்சி (2)`: PDF **196–199**, date **10-08-1972**.

Checks performed and source anomalies recorded:

- one canonical page file for every PDF page **161–199**: **39 / 39**;
- all ten heading pages, salutations, closing/sign-off forms and printed dates were visually checked against the controlling scan;
- PDF 164 contains the scan-visible sentence `இறுதி வெற்றி பெறாமல், என் இனிய நண்பா! நீயும் நானும் தூங்குவோமா என்ன?`, while the legacy reading copy contains only the shortened ending `தூங்குவோமா என்ன?`; the canonical transcription follows the scan;
- PDF 165 prints the salutation `என் உடன்பிறப்பே!` without an internal space; the source form is retained rather than the legacy spacing;
- PDF 173 closes with `மு. கருணாநிதி.` including the source's final period;
- PDF 188 uses decorative markers for the eight-item accusation list; the canonical page preserves the list structure rather than flattening it into prose;
- letters 0043–0046 use the abbreviated `மு. க.` sign-off where printed; these forms are retained;
- no silent modernisation, correction, regularisation or reconstruction was applied to source-supported wording, punctuation, names, dates, quotations or typography;
- PDF 200 was inspected only enough to verify the start of 0047 — actual heading `“தாயே எட்டடி என்றால்...”`, salutation `உடன்பிறப்பே,`; no PDF-200 or letter-0047 text is committed in this batch;
- legacy bilingual files remain unchanged;
- English migration, bilingual alignment, full-volume structural audit, second visual verification, editorial review and release work remain unstarted/blocked as required.

## Iteration 8 — fifth Volume 1 ten-letter batch: 0047–0056

**Result: PASS — 10 complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0047 — `“தாயே எட்டடி என்றால்...”`: PDF **200–202**, date **29-08-1972**;
- 0048 — `பாவம்; பண்பாடு, படும் பாடு!`: PDF **203–205**, printed ending **சென்னை. / 10.10.1972**;
- 0049 — `அன்பகம்! அறிவகம்!`: PDF **206–209**, date **20-10-1972**;
- 0050 — `நமக்குப் புரியவில்லை!`: PDF **210–213**, date **21-10-1972**;
- 0051 — `அகல்விளக்கு கையில் அண்ணன் மொழி நெஞ்சில்!`: PDF **214–218**, date **23-10-1972**;
- 0052 — `பிப்ரவரி மூன்றாம் நாள் !`: PDF **219–222**, date **23-01-1973**;
- 0053 — `நட வேகமாக! நமக்கே வெற்றி!!`: PDF **223–226**, date **12-05-1973**;
- 0054 — `ஐந்தாம் ஜார்ஜா? ஆறாம் ஜார்ஜா?`: PDF **227–229**, date **13-05-1973**;
- 0055 — `“அரிதாரம் கலையும்!”`: PDF **230–232**, date **23-05-1973**;
- 0056 — `சிந்தனைக்கு!`: PDF **233–235**, date **24-05-1973**.

Checks performed and source anomalies recorded:

- one canonical page file for every PDF page **200–235**: **36 / 36**;
- all ten heading pages, salutations, closing/date boundaries and source emphasis were visually checked against the controlling scan;
- letter 0048's text itself says the AIADMK had existed eight years, while PDF 205 ends with `சென்னை.` / `10.10.1972`; the printed evidence is retained as-is and no unsupported later composition date is inferred;
- PDF 209 visibly underlines `நினைவூட்டினேன்.`; the canonical page uses underline markup to retain the source emphasis;
- PDF 211 prints `ஆட்டுச்சந்தைக்கு அருகாமையில்!`, while the legacy Tamil reading copy gives `ஸ்பென்சருக்கு அருகாமையில்!`; the canonical page follows the scan;
- PDF 213 visibly prints the unusual joined form `வேண்டும்”மென்கிறார்.`; it is retained without regularisation;
- PDF 214 sets the letter 0051 title on two lines, and PDFs 215–218 contain source-visible bold emphasis; the canonical page layer retains that structure;
- PDFs 219–222 preserve source-visible emphasis and the lineated Anna-praise sequence in letter 0052;
- PDF 219 prints the heading `பிப்ரவரி மூன்றாம் நாள் !` with a space before the exclamation mark and later prints `வரையில்- அப்போதுகூட என் உடன்பிறப்பாம்`; these source forms are retained;
- PDF 226 preserves the source-visible bold closing exhortations in letter 0053;
- PDF 228 prints `(6908) ஆறாயிரத்துத்தொள்ளாயிரத்து எட்டு`; the unusual joined wording is retained rather than replaced by the legacy reading copy's spaced form;
- PDF 232 prints the closing rhetorical passage in bold; that emphasis is retained;
- source-supported spacing, punctuation, abbreviations and sign-off forms are preserved, including abbreviated `மு. க.` where printed;
- PDF 236 was inspected only enough to verify the start of 0057 — actual heading `“பிறந்த நாள் வேண்டுகோள்!”`, salutation `உடன்பிறப்பே,`; no PDF-236 or letter-0057 text is committed in this batch;
- legacy bilingual files remain unchanged;
- English migration, bilingual alignment, full-volume structural audit, second visual verification, editorial review and release work remain unstarted/blocked as required.

## Iteration 9 — user-approved expanded Volume 1 batch: 0057–0076

**Result: PASS — 20 complete consecutive source letters migrated.**

The user explicitly requested letters **0057–0076** in one activity. This is a one-time expansion beyond the regular Volume 1 ten-letter cadence and is documented here rather than silently changing the standing rule.

Coverage and verified boundaries:

- 0057 — `“பிறந்த நாள் வேண்டுகோள்!”`: PDF **236–238**, date **28-05-1973**;
- 0058 — `“நடக்கின்ற ஆச்சரியம்!”`: PDF **239–240**, date **29-05-1973**;
- 0059 — `இதுதான் உலகம்!`: PDF **241–245**, date **30-05-1973**;
- 0060 — `“கண்ணீர் மடல்!”`: PDF **246–249**, date **02-06-1973**;
- 0061 — `“ஒழுங்கான கணக்கு!”`: PDF **250–252**, date **15-06-1973**;
- 0062 — `உண்மை! உண்மை!!`: PDF **253–255**, date **24-06-1973**;
- 0063 — `“கிலுகிலுப்பை!”`: PDF **256–259**, **no date printed in source**;
- 0064 — `பதவி-துறவி!`: PDF **260–262**, date **02-07-1973**;
- 0065 — `உன் பெயர் எங்கே?`: PDF **263–265**, date **23-07-1973**;
- 0066 — `“அண்ணன் எழுதிய மடல்!”`: PDF **266–268**, date **02-10-1973**;
- 0067 — `நடக்கட்டும் நாடகம்!`: PDF **269–270**, date **29-11-1973**;
- 0068 — `“டெல்லி லாயத்தில்!”`: PDF **271–272**, date **03-12-1973**;
- 0069 — `படையெடுப்பு பலிக்குமா?`: PDF **273–274**, date **07-12-1973**;
- 0070 — `உணரச் செய்வோம்!`: PDF **275–276**, date **11-12-1973**;
- 0071 — `காலக் கருவூலம்!`: PDF **277–278**, date **12-12-1973**;
- 0072 — `ஒன்று சொல்க!`: PDF **279–280**, date **13-12-1973**;
- 0073 — `புன்னகையும் பெருமூச்சும்!`: PDF **281–282**, date **15-12-1973**;
- 0074 — `குறள் மறவோம்!`: PDF **283–284**, date **16-12-1973**;
- 0075 — `உன் எதிரே!`: PDF **285–286**, date **18-12-1973**;
- 0076 — `தட்டிக் கேட்கலாமா?`: PDF **287–288**, date **20-12-1973**.

Checks performed and source anomalies recorded:

- one canonical page file for every PDF page **236–288**: **53 / 53**;
- all twenty actual heading pages, salutations, continuation pages and closing boundaries were visually inspected against the controlling scan;
- letter 0063 has no date printed either in the contents date cell or at its closing on PDF 259; canonical `letter_date` is therefore `null` and no date is inferred;
- PDF 252 prints `என் நெஞ்சும் கல்லாகவில்லை!`, while the legacy reading copy uses `என் நெஞ்சம்`; canonical transcription follows the scan;
- PDF 258 visibly emphasizes `தொண்டர்களை மதிக்காதவர்களை மதிக்காதவன் நான் என்பதை நீ அறிவாய்!`; the emphasis is represented in the canonical page layer;
- PDF 259 closes letter 0063 with `அன்புள்ள, / மு. க.` and no date;
- PDF 270 visibly underlines `ஊரையடித்து உலையிலே போடுபவர்கள்.-`; the underline and unusual terminal punctuation are retained;
- PDFs 271–272 preserve Bharathidasan verse lineation and source hyphenation rather than silently adopting the legacy reading copy's spacing; PDF 272 prints `எழுச்சிமிகு` and visually emphasizes `“கனைக்கும் உரிமை”`;
- PDF 274 prints the newspaper phrase `யூனியன் சர்க்கார் இலாக்காக்களில் காகிதப் பஞ்சம்`; the source's doubled `க்` form controls over the legacy reading copy;
- PDF 276 contains the English judicial quotation beginning `That the dead body found, in the reservoir`; source punctuation and wording are preserved verbatim;
- PDF 277 preserves the printed mixed Tamil-English `Becosules - B-Complex`, `Capsules`, `கேப்ஸூல்ஸ்-Capsules-` sequence and the ingredient list, including printed `Pyridoxime`;
- PDFs 279–280 preserve the source lineation/hyphenation of the Bharathidasan poem, including `காண்-தோள்கள்`, `காண்-கிளம்பிற்றுகாண்`, and `கூட்டம்-`;
- PDFs 283–284 preserve the Kural quotation as a two-line unit;
- PDF 286 preserves the lineated closing exhortations in letter 0075;
- PDF 289 was inspected only enough to verify the next boundary: actual heading `77. பெரியாரின் வெற்றி!`, salutation `உடன்பிறப்பே,`; no PDF-289 or letter-0077 text is committed in this iteration;
- no silent modernisation, correction, regularisation or reconstruction was applied to source-supported spelling, spacing, punctuation, English text, quotations, or typography;
- legacy bilingual files remain unchanged;
- English migration, bilingual alignment, full-volume structural audit, second visual verification, editorial review and release work remain blocked/unstarted as required.

## Iteration 10 — sixth regular Volume 1 ten-letter batch: 0077–0086

**Result: PASS — 10 complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0077 — `பெரியாரின் வெற்றி!`: PDF **289–290**, date **26-12-1973**;
- 0078 — `நம்மை வென்றாரா?`: PDF **291–292**, date **28-12-1973**;
- 0079 — `இருபதாயிரம் பாடி வீடுகள்!`: PDF **293–295**, date **01-01-1974**;
- 0080 — `கொள்கை மலர்கள்`: PDF **296–297**, date **04-01-1974**;
- 0081 — `தெள்ளிய ஆலின் சிறு பழத்தொரு விதை!`: PDF **298–300**, date **10-01-1974**;
- 0082 — `பொங்கல் உறுதி!`: PDF **301**, date **14-01-1974**;
- 0083 — `காண வருகிறேன் உன்னை!`: PDF **302–304**, date **11-02-1974**;
- 0084 — `‘தொய்வு இல்லை! தொடர்க பயணம்!’`: PDF **305–307**, date **05-03-1974**;
- 0085 — `“எல்லா மலர்களும் ரோஜா மலர்களே!”`: PDF **308–309**, date **19-03-1974**;
- 0086 — `மே தின வாழ்த்து!`: PDF **310–312**, date **01-05-1974**.

Checks performed and source anomalies recorded:

- one canonical page file for every PDF page **289–312**: **24 / 24**;
- all ten heading pages, salutations, continuation pages, sign-offs and printed dates were visually checked against the controlling scan;
- PDF 294 prints `அறை கூவல்`, `நியாய நெஞ்சும்`, and the closing form `வலிப்பு நோய் ஆவான்...`; these scan forms control over the legacy reading copy;
- PDF 297 prints `தன்னலமற்ற-கண்ணயராத` without spaces around the hyphen;
- PDF 299 prints `சட்டம் பயின்றோர்-அரசியல்`, `எங்கள் களைப்பையெல்லாம்`, and `மாநிலத்தில் சுயாட்சி-மத்தியிலே கூட்டாட்சி`; PDF 300 prints `ராஜ மன்னார்` and `செழியன்-மாறன்`;
- PDF 301 prints `“நல்லவர்”(?)களுக்கும்` without inserted spaces;
- PDF 302 uses decorative three-dot markers for its five campaign-summary lines; PDF 303 visually emphasizes repeated `ஊழல்` forms and prints `உழைப்புக்கு சொந்தக்காரனாகிய`;
- PDF 304 preserves the source lineation of `வீரனே! / தீரனே! / வெற்றிச் சரிதம் / படைக்கும் என் / அன்பு உடன்பிறப்பே!`;
- PDFs 306–307 preserve source punctuation and hyphenation including `வீட்டு விளக்கு-வீதி`, `தாண்டுகிறது-`, `கடாட்சத்தால்!-`, and `இவைகளைத் தான்`; source-visible bold scheme and closing passages are represented in Markdown;
- PDFs 308–309 preserve the bold election passages, `மேலவை-மாநிலங்கள்`, the lineated principle block, and `மலர்கள் தான்`;
- PDFs 310–312 preserve mixed source hyphenation including `மேடைகளில்-ஏடுகளில்`, `பொறுப்பு-முதலீட்டில்`, `அரசுத்துறையில்- குறிப்பாக`, and `மத்திய-மாநில`; PDF 312 prints a colon after `தடைப்பட்டன`;
- PDF 313 was inspected only enough to verify the next boundary: actual heading `87. ‘நமது நிலை’!`, salutation `உடன்பிறப்பே,`; no PDF-313 or letter-0087 text is committed in this iteration;
- no silent modernisation, correction, regularisation or reconstruction was applied to source-supported spelling, spacing, punctuation, emphasis or typography;
- legacy bilingual files remain unchanged;
- English migration, bilingual alignment, full-volume structural audit, second visual verification, editorial review and release work remain blocked/unstarted as required.

## Iteration 11 — seventh regular Volume 1 ten-letter batch: 0087–0096

**Result: PASS — 10 complete consecutive source letters migrated.**

Coverage and verified boundaries:

- 0087 — `‘நமது நிலை’!`: PDF **313–315**, date **10-05-1974**;
- 0088 — `என் பிறந்த நாளில்...!`: PDF **316–318**, date **15-05-1974**;
- 0089 — `“மறவாதே!”`: PDF **319–321**, date **18-05-1974**;
- 0090 — `கோடையிலே...!`: PDF **322–325**, date **05-06-1974**;
- 0091 — `நமது விழாக்கள்!`: PDF **326–327**, date **16-06-1974**;
- 0092 — `பயணம் தொடரட்டும்!`: PDF **328–329**, date **23-06-1974**;
- 0093 — `பிறந்த நாள் விழாவும் மறந்த சில விவரங்களும்!`: PDF **330–334**, date **28-07-1974**;
- 0094 — `நேரமும் நினைப்பும்!`: PDF **335–338**, date **04-08-1974**;
- 0095 — `‘மாம்பழ மங்கை!’`: PDF **339–342**, date **11-08-1974**;
- 0096 — `அதே தேதிகள்!`: PDF **343–344**, date **01-09-1974**.

Checks performed and source anomalies recorded:

- one canonical page file for every PDF page **313–344**: **32 / 32**;
- all ten actual heading pages, page boundaries, sign-offs and printed dates were visually checked against the controlling scan;
- PDF 313 prints the salutation `உடன் பிறப்பே,` with an internal space and carries a source-bold railway-worker demand block; PDFs 314–315 preserve the bold negotiation/settlement passages;
- PDF 315 prints `இது தான் நமது ஆசை` with `இது தான்` separated, and later `உடன் பிறப்பே!` with an internal space; the legacy joined forms are not substituted;
- PDFs 316–318 preserve the source-bold three-fund list, the lineated `கவியரங்கம் / பாட்டரங்கம் / கலையரங்கம் / கூத்தரங்கம்` sequence, the bold request to stop extravagant birthday functions, and the lineation around `கழகக் குரல்`;
- PDFs 319–321 preserve source no-space hyphenation around the movement-destruction sequence, `தியாகநோக்கும்`, the bold organisational-unity passage, and the closing `சிந்தாமல் சிதறாமல்`;
- PDFs 322–325 preserve source no-space hyphenation including `தமிழர்-மலையாளிகள்`, the arrest/legal-action sequence, the bold `அலைஓசை` passage, the quoted `தி.மு.க.-அ.தி.மு.க.` form, `காமராசரின்`, and the lineated closing counter-question;
- PDFs 326–327 preserve scan forms including `எதுபற்றிக்`, `நமது உடன் பிறப்புகளும்`, and the dated September festival sequence with source hyphenation;
- PDF 329 prints `வீழட்டும்`, `துண்டாடப் பட்டது`, and later `சில உடன் பிறப்புக்கள்`; these scan forms control over the legacy reading copy;
- PDFs 330–334 preserve dense source no-space hyphenation, the lineated `கேலி / கிண்டல் / ஏசல் / ஏளனம் / ஏகடியம்` block, the contrasting `அவன் - இவன்` / `அவன்-இவன்` forms, and the two `தினமணி` quotations;
- PDFs 335–338 preserve the `உதய சூரியன்` lullaby lineation, source no-space hyphenation, and the bold prohibition-song/accusation blocks;
- PDF 340 prints `“மாம்பழ மங்கை”` with double quotation marks, `இதோ...மங்கையே` without an inserted space after the ellipsis, and a source-bold newspaper quotation;
- PDF 342 prints `பகுத்தறிவு வாதிகளின்` with a space; the legacy joined form is not substituted;
- letter 0096 begins on PDF 343 without a salutation after its heading; PDFs 343–344 preserve the bold opening account, source no-space hyphenation, the bold `1799ஆம் ஆண்டு...` line, and the bold 1972 parallel;
- PDF 345 was inspected only enough to verify the next boundary: actual heading `97. இன்றே தயாராகு!`, salutation `உடன்பிறப்பே,`; no PDF-345 or letter-0097 text is committed in this iteration;
- no silent modernisation, correction, regularisation or reconstruction was applied to source-supported spelling, spacing, punctuation, emphasis, quotations or typography;
- legacy bilingual files remain unchanged;
- English migration, bilingual alignment, full-volume structural audit, second visual verification, editorial review and release work remain blocked/unstarted as required.

## Current boundary

Canonical PDF coverage is **001–344 / 401**. Letters **0001–0096** are canonically complete, with no partial letter. The next regular Volume 1 migration activity begins at PDF **345** with letter **0097 — `இன்றே தயாராகு!`** and follows the standing **10-letter** rule for letters **0097–0106**, stopping before letter 0107.

These migration iterations are first-pass visual transcription gates. They are **not** the later full-volume structural audit, second visual verification, or translation textual-fidelity audit.
