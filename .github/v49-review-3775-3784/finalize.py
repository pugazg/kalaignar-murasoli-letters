from pathlib import Path
import shutil

root = Path.cwd()
base = root / 'volumes' / 'volume-49' / 'translations' / 'en'
letters_dir = base / 'letters'
staging = root / '.github' / 'v49-review-3775-3784'

letters = {
    3775: ('3775-long-live-the-fame-of-perunthalaivar-kamarajar.md', 101, 106, '../BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md'),
    3776: ('3776-our-journey-continues-without-faltering.md', 107, 113, '../BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md'),
    3777: ('3777-a-graceful-hair-knot-a-fragrant-screw-pine-flower-they-say.md', 114, 119, '../BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md'),
    3778: ('3778-katchatheevu-and-the-trash-question.md', 120, 126, '../BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md'),
    3779: ('3779-the-height-of-danger-foreign-direct-investment.md', 127, 131, '../BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md'),
    3780: ('3780-the-entrance-examination-verdict-is-opposition-necessary.md', 132, 138, '../BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md'),
    3781: ('3781-i-have-neither-political-rancour-nor-anguish.md', 139, 148, '../BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md'),
    3782: ('3782-how-long-will-they-keep-deceiving-the-people-of-this-country.md', 149, 155, '../BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md'),
    3783: ('3783-our-efforts-towards-the-summit-of-victory.md', 156, 161, '../BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md'),
    3784: ('3784-she-is-supposedly-the-pioneer-for-all-india.md', 162, 168, '../BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md'),
}

# Mark all ten letters verified and attach the appropriate batch report.
for no, (filename, _start, _end, report) in letters.items():
    path = letters_dir / filename
    text = path.read_text()
    if 'translation_status: "source-checked"' not in text:
        raise SystemExit(f'{no}: expected source-checked status not found')
    text = text.replace('translation_status: "source-checked"', 'translation_status: "verified"', 1)
    anchor = 'translation_method: "thought-preserving, non-literary"\n'
    addition = anchor + 'bilingual_alignment_status: "verified"\n' + f'bilingual_alignment_report: "{report}"\n'
    if anchor not in text:
        raise SystemExit(f'{no}: translation-method anchor missing')
    text = text.replace(anchor, addition, 1)
    path.write_text(text)

# Meaning-affecting corrections found through direct Tamil–English comparison.
corrections = {
    3777: [
        (
            'the pressure of the workers’ indefinite struggle might have compelled the Union Government',
            'the pressure of the workers’ indefinite hunger strike might have compelled the Union Government',
        ),
    ],
    3780: [
        ('Justice Vikramajit Sen delivered the majority judgment.', 'Justice Vikramajit Singh delivered the majority judgment.'),
        ('Chief Justice Altamas Kabir and Justice Vikramajit Sen had expressed the view', 'Chief Justice Altamas Kabir and Justice Vikramajit Singh had expressed the view'),
    ],
    3782: [
        ('had been delayed because of land acquisition.', 'had been delayed because of land encroachment.'),
    ],
}
for no, pairs in corrections.items():
    path = letters_dir / letters[no][0]
    text = path.read_text()
    for old, new in pairs:
        if old not in text:
            raise SystemExit(f'{no}: correction source wording missing: {old}')
        text = text.replace(old, new, 1)
    path.write_text(text)

# Explain the source-form name retained in letter 3780.
path_3780 = letters_dir / letters[3780][0]
text_3780 = path_3780.read_text()
note_anchor = '4. Three punctuation artefacts in the medical-degree abbreviation on PDF pages 133–134 were corrected after visual comparison with the scans.\n'
note_line = '5. The canonical Tamil source prints the judge’s name as **Vikramajit Singh**. The English now retains that source form rather than silently substituting another spelling.\n'
if note_anchor not in text_3780:
    raise SystemExit('3780: translator-note anchor missing')
text_3780 = text_3780.replace(note_anchor, note_anchor + note_line, 1)
path_3780.write_text(text_3780)

report_3775_3779 = '''# Bilingual Alignment Review — Letters 3775–3779

## Scope

- Volume: **49**
- Letters reviewed: **3775–3779**
- Canonical Tamil source range: **PDF 101–131**
- Letters completed in this batch: **5/5**
- Approximate English body reviewed: **6,998 words**
- Status after review: **verified**

## Review method

Each English translation was compared directly with the complete canonical Tamil reproduced in the same bilingual file. The review checked:

1. title, salutation, closing and date;
2. paragraph and argumentative sequence;
3. every substantive claim and attribution;
4. quotations, poems, reported speech and intentional English passages;
5. names, dates, counts, monetary figures, percentages and institutional terms;
6. lists, chronology and item order;
7. wordplay, rhetorical questions, irony, repetition and political intensity; and
8. English wording that could broaden, narrow or alter a source claim.

The Tamil pages had already passed the scan-fidelity audit. This review made no change to any canonical Tamil page.

## Results by letter

### 3775 — *Long Live the Fame of Perunthalaivar Kamarajar!*

- The public memorials, Government measures, personal recollections, wedding episode, Ooty accommodation episode and funeral arrangements were aligned in sequence.
- The complete 1976 poem was checked for imagery, honorifics, emotional movement and named historical figures.
- Dates, place names, institutional names and the concluding statement of political atonement remain complete.
- No English correction was required.

### 3776 — *Our Journey Continues Without Faltering!*

- The formation of TESO, the district-by-district 1985 arrest totals, the 1985–86 demonstrations and conferences, and the organisations and leaders named at Madurai were checked.
- The 2012–13 TESO meetings, resolutions, protests, court action and August 8 mobilisation were aligned for dates, locations, participants and political purpose.
- The distinction between reported allegations, adopted resolutions and Kalaignar's own position remains intact.
- No English correction was required.

### 3777 — *A Graceful Hair-Knot, a Fragrant Screw-Pine Flower, They Say!!*

- The 2006 and 2013 NLC disinvestment chronology, letters, union actions, percentages, rupee figures and SEBI framing were checked.
- One correction restored the source's specific reference to the workers’ **indefinite hunger strike**, rather than the less precise “indefinite struggle”.
- The closing proverb and the political contrast between withdrawal of the sale and purchase by State public-sector institutions remain source-faithful.

### 3778 — *Katchatheevu and the “Trash” Question!*

- The 1974 agreement chronology, all-party meeting, Prime Ministerial letter, parliamentary interventions, Assembly resolution and later Supreme Court cases were aligned.
- Jayalalithaa's quoted 1994 English sentence, the TESO resolution, dates and political attributions were preserved without converting allegations into independent fact.
- The `Katchatheevu` / `கச்சடா` wordplay and final butter-versus-lime idiom retain their rhetorical functions.
- No English correction was required.

### 3779 — *The Height of Danger: Foreign Direct Investment!*

- Every sectoral percentage, approval route, BSNL profit-and-loss figure, country comparison and institutional response was checked.
- The distinction between the Government's stated economic rationale and Kalaignar's security, public-sector and side-effect arguments remains clear.
- The *Tirukkural* medical analogy, parliamentary-process criticism and final DMK opposition were fully aligned.
- No English correction was required.

## Outcome

- Complete substantive coverage: **passed**
- Paragraph, poem and argument order: **passed**
- Quotations and attribution: **passed**
- Names, dates, figures, percentages and lists: **passed**
- Rhetorical force and political responsibility: **passed**
- English files marked `verified`: **5**
- Targeted English corrections: **1**
- Canonical Tamil changes: **0**

The following bilingual alignment batch is **letters 3780–3784**.
'''
(base / 'BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md').write_text(report_3775_3779)

report_3780_3784 = '''# Bilingual Alignment Review — Letters 3780–3784

## Scope

- Volume: **49**
- Letters reviewed: **3780–3784**
- Canonical Tamil source range: **PDF 132–168**
- Letters completed in this batch: **5/5**
- Approximate English body reviewed: **8,604 words**
- Status after review: **verified**

## Review method

Each English translation was compared directly with the complete canonical Tamil reproduced in the same bilingual file. The review checked:

1. title, salutation, closing and date;
2. paragraph and argumentative sequence;
3. every substantive claim and attribution;
4. court judgments, Government correspondence, newspaper quotations and reported speech;
5. names, dates, counts, monetary figures, percentages and institutional terms;
6. legal, electoral, agricultural and budgetary chronology;
7. rhetorical questions, irony, repetition and political intensity; and
8. English wording that could broaden, narrow or alter responsibility or causation.

The Tamil pages had already passed the scan-fidelity audit. This review made no change to any canonical Tamil page.

## Results by letter

### 3780 — *The Entrance-Examination Verdict — Is Opposition Necessary?*

- The three-judge decision, the 2010–13 litigation chronology, Union and State positions, reservation argument, 115 petitions and quoted correspondence were fully aligned.
- Two English occurrences of the judge's name were changed from **Vikramajit Sen** to the canonical Tamil source form **Vikramajit Singh**; a source-form note was added so that the archival wording is not silently normalised.
- The source does not use the later acronym NEET, and the English continues not to insert it.

### 3781 — *I Have Neither Political Rancour nor Anguish!*

- The 2006 NLC chronology was checked across newspaper reports, letters, union decisions, strike dates, party statements and the Union Government's withdrawal.
- All leaders, organisations, dates, quotations, advertisement counts and the final *Tirukkural* were aligned.
- The distinction between the Chief Minister's claim, Kalaignar's documentary rebuttal and reported third-party praise remains clear.
- No English correction was required.

### 3782 — *How Long Will They Keep Deceiving the People of This Country!*

- Budget allocations, Rule 110 announcements, road lengths, bridge counts, departmental figures, comparative DMK–AIADMK statistics and quoted newspaper passages were checked.
- One correction restored `நில ஆக்கிரமிப்பு` as **land encroachment**, replacing the incorrect “land acquisition”.
- The repeated-announcement argument, “old toddy in a new pot” analogy and *Malaikkallan* refrain retain their source sequence and force.

### 3783 — *Our Efforts Towards the Summit of Victory!*

- The Prime Minister's letters to Kalaignar, the Chief Minister and Sitaram Yechury; the Tamil National Alliance meeting; the Indo–Sri Lanka Accord; and the TESO resolution were aligned.
- The quoted Clause 2.14 English sentence, Thirteenth Amendment argument, referendum position and August 8 leadership assignments were checked in full.
- No English correction was required.

### 3784 — *She Is Supposedly the Pioneer for All India!*

- The kuruvai–samba chronology, Mettur opening and closing dates, food-production figure, Cauvery Tribunal chronology, Assembly and Cabinet decisions, and quoted English statements were aligned.
- The distinctions among the Supreme Court's direction, the Chief Minister's public claim and Kalaignar's rebuttal remain intact.
- The childbirth metaphor, “I am the song; I am the emotion” allusion and sequence of rhetorical questions preserve their political function.
- No English correction was required.

## Outcome

- Complete substantive coverage: **passed**
- Paragraph and argument order: **passed**
- Quotations, judgments and attribution: **passed after one source-name correction**
- Names, dates, figures, percentages and chronology: **passed**
- Legal and factual terminology: **passed after one correction**
- Rhetorical force and political responsibility: **passed**
- English files marked `verified`: **5**
- Targeted English corrections: **2**
- Canonical Tamil changes: **0**

The next bilingual alignment batch is **letters 3785–3789**.
'''
(base / 'BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md').write_text(report_3780_3784)

# Update the English index statuses and review-report list.
index_path = base / 'README.md'
index = index_path.read_text()
for no in letters:
    lines = index.splitlines()
    changed = False
    for i, line in enumerate(lines):
        if line.startswith(f'| [{no}]'):
            if not line.endswith('| source-checked |'):
                raise SystemExit(f'{no}: unexpected English-index status')
            lines[i] = line[:-len('| source-checked |')] + '| verified |'
            changed = True
            break
    if not changed:
        raise SystemExit(f'{no}: English-index row missing')
    index = '\n'.join(lines) + ('\n' if index.endswith('\n') else '')
review_anchor = '- Letters **3770–3774**: substantive Tamil–English alignment completed; five files verified, with five targeted English corrections in letter 3774 and no Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md`](BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md)\n'
review_addition = (
    review_anchor
    + '- Letters **3775–3779**: substantive Tamil–English alignment completed; five files verified, with one targeted English correction and no Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md`](BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md)\n'
    + '- Letters **3780–3784**: substantive Tamil–English alignment completed; five files verified, with two targeted English corrections and no Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md`](BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md)\n'
)
if review_anchor not in index:
    raise SystemExit('English-index review anchor missing')
index = index.replace(review_anchor, review_addition, 1)
index_path.write_text(index)

# Update progress.
progress_path = base / 'PROGRESS.md'
progress = progress_path.read_text()
replacements = [
    ('  - [ ] Letters 3775–3779\n', '  - [x] Letters 3775–3779 verified\n'),
    ('  - [ ] Letters 3780–3784\n', '  - [x] Letters 3780–3784 verified\n'),
    (
        '- Letters **3770–3774** — [`BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md`](BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md): **5/5 verified**; five targeted English corrections; no Tamil-source changes.\n',
        '- Letters **3770–3774** — [`BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md`](BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md): **5/5 verified**; five targeted English corrections; no Tamil-source changes.\n'
        '- Letters **3775–3779** — [`BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md`](BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md): **5/5 verified**; one targeted English correction; no Tamil-source changes.\n'
        '- Letters **3780–3784** — [`BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md`](BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md): **5/5 verified**; two targeted English corrections; no Tamil-source changes.\n',
    ),
    ('- Reviewed: **11**', '- Reviewed: **21**'),
    ('- Verified: **11**', '- Verified: **21**'),
    (
        'Continue the bilingual alignment review with letters **3775–3779**. After all 53 letters are verified, conduct the volume-level English editorial consistency pass and prepare the release report.',
        'Continue the bilingual alignment review with letters **3785–3789**. After all 53 letters are verified, conduct the volume-level English editorial consistency pass and prepare the release report.',
    ),
]
for old, new in replacements:
    if old not in progress:
        raise SystemExit(f'Progress target missing: {old}')
    progress = progress.replace(old, new, 1)
progress_path.write_text(progress)

# Update the volume-level status summary.
volume_path = root / 'volumes' / 'volume-49' / 'README.md'
volume = volume_path.read_text()
old_volume = (
    '- Bilingual alignment review is complete through letter **3774**: **11 verified**, **42 awaiting alignment review**. See the [review reports](translations/en/README.md#bilingual-alignment-reviews).\n'
    '- Next alignment batch: letters **3775–3779**.'
)
new_volume = (
    '- Bilingual alignment review is complete through letter **3784**: **21 verified**, **32 awaiting alignment review**. See the [review reports](translations/en/README.md#bilingual-alignment-reviews).\n'
    '- Next alignment batch: letters **3785–3789**.'
)
if old_volume not in volume:
    raise SystemExit('Volume README status target missing')
volume_path.write_text(volume.replace(old_volume, new_volume, 1))

# Validate metadata, source markers and exact preservation of canonical Tamil.
def norm(text: str) -> str:
    return '\n'.join(line.rstrip() for line in text.rstrip().splitlines()) + '\n'

for no, (filename, start, end, report) in letters.items():
    path = letters_dir / filename
    text = path.read_text()
    for needle in [
        'translation_status: "verified"',
        'bilingual_alignment_status: "verified"',
        f'bilingual_alignment_report: "{report}"',
        '## Original Tamil — மூலத் தமிழ்\n\n',
    ]:
        if needle not in text:
            raise SystemExit(f'{no}: missing {needle}')
    if text.count('<!-- Source PDF page ') != end - start + 1:
        raise SystemExit(f'{no}: wrong source-marker count')
    if '\ufffd' in text:
        raise SystemExit(f'{no}: replacement character found')
    original = text.split('## Original Tamil — மூலத் தமிழ்\n\n', 1)[1]
    expected_parts = []
    for pageno in range(start, end + 1):
        src = (root / 'volumes' / 'volume-49' / 'pages' / f'page-{pageno:03d}.md').read_text()
        body = src.split('---', 2)[2].lstrip('\n').rstrip()
        expected_parts.append(f'<!-- Source PDF page {pageno:03d} -->\n\n{body}')
    marker = f'<!-- Source PDF page {start:03d} -->'
    if marker not in original:
        raise SystemExit(f'{no}: first source marker missing')
    actual_pages = original[original.index(marker):]
    expected = '\n\n'.join(expected_parts) + '\n'
    if norm(actual_pages) != norm(expected):
        raise SystemExit(f'{no}: Tamil source no longer matches canonical pages')

text_3777 = (letters_dir / letters[3777][0]).read_text()
if 'workers’ indefinite hunger strike' not in text_3777 or 'workers’ indefinite struggle' in text_3777:
    raise SystemExit('3777 hunger-strike correction failed')
text_3780 = path_3780.read_text()
if text_3780.count('Vikramajit Singh') < 3 or 'Vikramajit Sen' in text_3780:
    raise SystemExit('3780 source-name alignment failed')
if 'canonical Tamil source prints the judge’s name as **Vikramajit Singh**' not in text_3780:
    raise SystemExit('3780 source-name note missing')
text_3782 = (letters_dir / letters[3782][0]).read_text()
if 'delayed because of land encroachment.' not in text_3782 or 'delayed because of land acquisition.' in text_3782:
    raise SystemExit('3782 land-encroachment correction failed')

for report_path, required in [
    (base / 'BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md', ['Letters reviewed: **3775–3779**', 'Letters completed in this batch: **5/5**', 'Targeted English corrections: **1**', 'Canonical Tamil changes: **0**']),
    (base / 'BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md', ['Letters reviewed: **3780–3784**', 'Letters completed in this batch: **5/5**', 'Targeted English corrections: **2**', 'Canonical Tamil changes: **0**']),
]:
    report_text = report_path.read_text()
    for needle in required:
        if needle not in report_text:
            raise SystemExit(f'{report_path.name}: missing {needle}')

index = index_path.read_text()
for no in letters:
    row = next((line for line in index.splitlines() if line.startswith(f'| [{no}]')), None)
    if not row or not row.endswith('| verified |'):
        raise SystemExit(f'{no}: English-index status not verified')
progress = progress_path.read_text()
for needle in ['- [x] Letters 3775–3779 verified', '- [x] Letters 3780–3784 verified', '- Reviewed: **21**', '- Verified: **21**', 'letters **3785–3789**']:
    if needle not in progress:
        raise SystemExit(f'Progress validation failed: {needle}')
volume = volume_path.read_text()
for needle in ['through letter **3784**', '**21 verified**', '**32 awaiting alignment review**', 'letters **3785–3789**']:
    if needle not in volume:
        raise SystemExit(f'Volume README validation failed: {needle}')

if staging.exists():
    shutil.rmtree(staging)
print('Validated bilingual alignment review for letters 3775-3784.')
