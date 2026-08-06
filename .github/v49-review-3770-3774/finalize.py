from pathlib import Path
import shutil

root = Path.cwd()
base = root / 'volumes' / 'volume-49' / 'translations' / 'en'
letters_dir = base / 'letters'
report_name = 'BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md'
report_rel = f'../{report_name}'

letters = {
    3770: ('3770-are-we-to-become-like-a-lizard-that-has-lost-its-tail.md', 64, 69),
    3771: ('3771-is-she-seeking-the-title-coal-heroine.md', 70, 76),
    3772: ('3772-the-rajya-sabha-election-an-analysis.md', 77, 86),
    3773: ('3773-let-us-raise-our-voice-for-people-of-every-caste-to-become-priests.md', 87, 93),
    3774: ('3774-does-tamil-not-deserve-the-right-that-hindi-has.md', 94, 100),
}

# Mark the five files verified while preserving their complete canonical Tamil sections.
for no, (filename, _start, _end) in letters.items():
    path = letters_dir / filename
    text = path.read_text()
    if 'translation_status: "source-checked"' not in text:
        raise SystemExit(f'{no}: expected source-checked status not found')
    text = text.replace('translation_status: "source-checked"', 'translation_status: "verified"', 1)
    anchor = 'translation_method: "thought-preserving, non-literary"\n'
    addition = (
        anchor
        + 'bilingual_alignment_status: "verified"\n'
        + f'bilingual_alignment_report: "{report_rel}"\n'
    )
    if anchor not in text:
        raise SystemExit(f'{no}: translation-method anchor missing')
    text = text.replace(anchor, addition, 1)
    path.write_text(text)

# Meaning-affecting corrections found in letter 3774.
path = letters_dir / letters[3774][0]
text = path.read_text()
corrections = [
    (
        'She said that her husband, Fakkeer Mydeen, had gone abroad for work;',
        'She said that her husband, Fakkeer Mydeen, had gone to Dubai for work;',
    ),
    (
        "M. C. Setalvad's successor as Attorney General, C. K. Daphtary, objected;",
        'The then Attorney General, C. K. Daphtary, objected;',
    ),
    (
        'the hearings in a large number of cases in the Madras High Court took place in Tamil.',
        'the hearings in most cases in the Madras High Court took place in Tamil.',
    ),
    (
        'Now, however, a High Court judge has denied a lawyer permission to argue in Tamil and has also stated that the Constitution does not permit arguments in Tamil.',
        'Now, however, on 3 January, a High Court judge denied a lawyer permission to argue in Tamil and also stated that the Constitution does not permit arguments in Tamil.',
    ),
    (
        "secure the President's consent for the proposal pending since the period of the DMK Government, so that Tamil may lawfully be used as a language of proceedings in the High Court in Tamil Nadu.",
        "secure the President's consent for the legal amendment pending since the period of the DMK Government, so that Tamil may lawfully be used as a language of proceedings in the High Court in Tamil Nadu.",
    ),
]
for old, new in corrections:
    if old not in text:
        raise SystemExit(f'3774: correction source wording missing: {old}')
    text = text.replace(old, new, 1)
path.write_text(text)

report = '''# Bilingual Alignment Review — Letters 3770–3774

## Scope

- Volume: **49**
- Letters reviewed: **3770–3774**
- Canonical Tamil source range: **PDF 64–100**
- Letters completed in this batch: **5/5**
- Approximate English body reviewed: **8,768 words**
- Status after review: **verified**

## Review method

Each English translation was compared directly with the complete canonical Tamil reproduced in the same bilingual file. The review checked:

1. title, salutation, closing and printed date;
2. paragraph and argumentative sequence;
3. every substantive claim and attribution;
4. quotations and reported speech;
5. names, dates, electoral arithmetic, monetary figures and institutional terms;
6. list completeness and item order;
7. wordplay, rhetorical questions, irony, repetition and political intensity; and
8. English wording that could broaden, narrow or add responsibility not present in the Tamil.

The Tamil source had already passed the scan-fidelity audit. This review made no change to any canonical Tamil page.

## Results by letter

### 3770 — *Are We to Become Like a Lizard That Has Lost Its Tail?*

- The Rajya Sabha support argument, the correspondence with Prime Minister Manmohan Singh, the Thirteenth Amendment chronology, the statements of Sri Lankan left-wing ministers and the criticism of *The Hindu* were fully aligned.
- The source-exact closing date **30 June 2016** remains preserved and explicitly documented as a printing anomaly; it was not silently changed to 2013.
- The distinction among the Sri Lankan Tamil issue, a Rajya Sabha election and a political alliance remains intact.
- No English correction was required.

### 3771 — *Is She Seeking the Title “Coal Heroine”?*

- The NLC contract-worker disputes of 1994, 2008, 2010 and 2012; the 2006 and 2013 disinvestment chronology; all percentages, dates, monetary figures, union names and quoted statements were checked.
- The central `கனி` / `கரி` wordplay and the closing theatrical idiom retain their source function without being expanded into new claims.
- The two intentional English newspaper passages were preserved.
- No English correction was required.

### 3772 — *The Rajya Sabha Election — An Analysis!*

- The complete Assembly arithmetic, party strengths, candidate changes, support negotiations and election sequence were checked.
- Historical examples from the 2004, 2007, 2008 and 1997 Rajya Sabha elections were aligned for names, seat counts, votes, dates and party responsibility.
- The reports attributed to *Dinamani*, Mukul Wasnik and V. Narayanasamy remain visibly attributed.
- No English correction was required.

### 3773 — *Let Us Raise Our Voice for People of Every Caste to Become Priests!*

- The chronology from Periyar's 1970 agitation announcement through the 1970 Act, 1972 Supreme Court judgment, later appeals, the 2006 Government Order, training centres and the 2013 Dravidar Kazhagam programme was fully aligned.
- All training-centre locations, community counts, the total of **207** trainees and the monthly **₹500** incentive were checked.
- The quotations of Periyar-era statements, Annai Maniammaiyar, the appeal made in Jagjivan Ram's presence and Agnihotram Ramanuja Thathachariar retain their speakers and rhetorical force.
- No English correction was required.

### 3774 — *Does Tamil Not Deserve the Right That Hindi Has?*

- The court case, Article 348 argument, 2001 petition, 2006 Assembly resolution, Union Government correspondence, World Classical Tamil Conference resolution and later High Court practice were aligned.
- Five English corrections were applied:
  1. restored the source's statement that Fakkeer Mydeen had gone to **Dubai**, making the printed Dubai/Saudi Arabia inconsistency visible as documented in the note;
  2. removed an unsupported reference to M. C. Setalvad and identified C. K. Daphtary only as the then Attorney General;
  3. restored the Tamil's quantifier that hearings in **most cases** took place in Tamil during the period described;
  4. restored the omitted date **3 January** for the later refusal to permit Tamil argument; and
  5. rendered the pending matter as the source's **legal amendment**, rather than the less specific “proposal”.

## Outcome

- Complete substantive coverage: **passed**
- Paragraph and argument order: **passed**
- Quotations and attribution: **passed after one correction**
- Names, dates, figures and electoral arithmetic: **passed after two corrections**
- Quantifiers and legal framing: **passed after two corrections**
- Rhetorical force and political responsibility: **passed**
- English files marked `verified`: **5**
- Canonical Tamil changes: **0**

The next bilingual alignment batch is **letters 3775–3779**.
'''
(base / report_name).write_text(report)

# Update English index statuses and alignment-report register.
index_path = base / 'README.md'
index = index_path.read_text()
for no in letters:
    lines = index.splitlines()
    changed = False
    for i, line in enumerate(lines):
        if line.startswith(f'| [{no}]'):
            if not line.endswith('| source-checked |'):
                raise SystemExit(f'{no}: unexpected index status')
            lines[i] = line[:-len('| source-checked |')] + '| verified |'
            changed = True
            break
    if not changed:
        raise SystemExit(f'{no}: index row missing')
    index = '\n'.join(lines) + ('\n' if index.endswith('\n') else '')
anchor = '- Letters **3764–3769**: substantive Tamil–English alignment completed; six files verified, with four targeted English corrections and no Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md`](BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md)\n'
entry = '- Letters **3770–3774**: substantive Tamil–English alignment completed; five files verified, with five targeted English corrections in letter 3774 and no Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md`](BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md)\n'
if anchor not in index:
    raise SystemExit('English index prior-review entry missing')
index_path.write_text(index.replace(anchor, anchor + entry, 1))

# Update progress and counts.
progress_path = base / 'PROGRESS.md'
progress = progress_path.read_text()
if '  - [ ] Letters 3770–3774' not in progress:
    raise SystemExit('Progress batch checkbox missing')
progress = progress.replace('  - [ ] Letters 3770–3774', '  - [x] Letters 3770–3774 verified', 1)
anchor = '- Letters **3764–3769** — [`BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md`](BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md): **6/6 verified**; four targeted English corrections; no Tamil-source changes.\n'
entry = '- Letters **3770–3774** — [`BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md`](BILINGUAL_ALIGNMENT_REVIEW_3770_3774.md): **5/5 verified**; five targeted English corrections; no Tamil-source changes.\n'
if anchor not in progress:
    raise SystemExit('Progress prior-review report missing')
progress = progress.replace(anchor, anchor + entry, 1)
progress = progress.replace('- Reviewed: **6**', '- Reviewed: **11**', 1)
progress = progress.replace('- Verified: **6**', '- Verified: **11**', 1)
progress = progress.replace('Continue the bilingual alignment review with letters **3770–3774**.', 'Continue the bilingual alignment review with letters **3775–3779**.', 1)
progress_path.write_text(progress)

# Update volume-level summary.
volume_path = root / 'volumes' / 'volume-49' / 'README.md'
volume = volume_path.read_text()
old = ('- Bilingual alignment review is complete for letters **3764–3769**: **6 verified**, **47 awaiting alignment review**. See the [review report](translations/en/BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md).\n'
       '- Next alignment batch: letters **3770–3774**.')
new = ('- Bilingual alignment review is complete through letter **3774**: **11 verified**, **42 awaiting alignment review**. See the [review reports](translations/en/README.md#bilingual-alignment-reviews).\n'
       '- Next alignment batch: letters **3775–3779**.')
if old not in volume:
    raise SystemExit('Volume README alignment-status target not found')
volume_path.write_text(volume.replace(old, new, 1))

# Remove every one-use workflow and copied finalizer from the final main tree.
for path in [
    root / '.github' / 'workflows' / 'export-v49-review-3770-3774.yml',
    root / '.github' / 'workflows' / 'finalize-v49-review-3770-3774.yml',
]:
    if path.exists():
        path.unlink()
staging = root / '.github' / 'v49-review-3770-3774'
if staging.exists():
    shutil.rmtree(staging)

# Validation: statuses, source markers and exact canonical Tamil preservation.
def norm(value: str) -> str:
    return '\n'.join(line.rstrip() for line in value.rstrip().splitlines()) + '\n'

for no, (filename, start, end) in letters.items():
    path = letters_dir / filename
    text = path.read_text()
    for needle in [
        'translation_status: "verified"',
        'bilingual_alignment_status: "verified"',
        f'bilingual_alignment_report: "{report_rel}"',
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
    for page_no in range(start, end + 1):
        page = (root / 'volumes' / 'volume-49' / 'pages' / f'page-{page_no:03d}.md').read_text()
        body = page.split('---', 2)[2].lstrip('\n').rstrip()
        expected_parts.append(f'<!-- Source PDF page {page_no:03d} -->\n\n{body}')
    marker = f'<!-- Source PDF page {start:03d} -->'
    if marker not in original:
        raise SystemExit(f'{no}: first source marker missing')
    actual_pages = original[original.index(marker):]
    expected = '\n\n'.join(expected_parts) + '\n'
    if norm(actual_pages) != norm(expected):
        raise SystemExit(f'{no}: Tamil source no longer matches canonical pages')

text3774 = (letters_dir / letters[3774][0]).read_text()
for needle in [
    'had gone to Dubai for work',
    'The then Attorney General, C. K. Daphtary',
    'the hearings in most cases in the Madras High Court took place in Tamil',
    'on 3 January, a High Court judge denied',
    "President's consent for the legal amendment pending",
]:
    if needle not in text3774:
        raise SystemExit(f'3774: corrected wording missing: {needle}')
for stale in [
    'had gone abroad for work',
    "M. C. Setalvad's successor",
    'hearings in a large number of cases',
    'consent for the proposal pending since',
]:
    if stale in text3774:
        raise SystemExit(f'3774: stale wording remains: {stale}')

index = index_path.read_text()
for no in letters:
    row = next((line for line in index.splitlines() if line.startswith(f'| [{no}]')), None)
    if not row or not row.endswith('| verified |'):
        raise SystemExit(f'{no}: index status not verified')
if report_name not in index:
    raise SystemExit('English index lacks new review report')

progress = progress_path.read_text()
for needle in ['  - [x] Letters 3770–3774 verified', '- Reviewed: **11**', '- Verified: **11**', 'letters **3775–3779**', report_name]:
    if needle not in progress:
        raise SystemExit(f'Progress validation failed: {needle}')

report_text = (base / report_name).read_text()
for needle in ['Letters reviewed: **3770–3774**', 'Letters completed in this batch: **5/5**', 'Approximate English body reviewed: **8,768 words**', 'Five English corrections were applied', 'Canonical Tamil changes: **0**']:
    if needle not in report_text:
        raise SystemExit(f'Review report validation failed: {needle}')

volume = volume_path.read_text()
for needle in ['**11 verified**', '**42 awaiting alignment review**', 'letters **3775–3779**']:
    if needle not in volume:
        raise SystemExit(f'Volume README validation failed: {needle}')

print('Validated bilingual alignment review for letters 3770-3774.')
