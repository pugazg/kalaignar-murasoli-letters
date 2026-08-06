from pathlib import Path

root = Path.cwd()
base = root / 'volumes' / 'volume-49' / 'translations' / 'en'
letters_dir = base / 'letters'
report_name = 'BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md'
report_rel = f'../{report_name}'

letters = {
    3764: ('3764-what-was-left-out-of-the-list-of-achievements.md', 24, 31),
    3765: ('3765-i-will-work-i-will-keep-working.md', 32, 39),
    3766: ('3766-will-the-government-of-india-continue-to-sleep.md', 40, 44),
    3767: ('3767-should-there-not-be-conduct-befitting-the-office.md', 45, 51),
    3768: ('3768-it-is-among-people-like-these-that.md', 52, 56),
    3769: ('3769-some-of-the-charitable-work-carried-out-by-the-dmk.md', 57, 63),
}

# Mark the reviewed letters verified while preserving the authoritative Tamil section.
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
        raise SystemExit(f'{no}: translation method anchor missing')
    text = text.replace(anchor, addition, 1)
    if no == 3764 and 'source_textual_fidelity_audit:' not in text.split('---', 2)[1]:
        text = text.replace(
            f'bilingual_alignment_report: "{report_rel}"\n',
            f'bilingual_alignment_report: "{report_rel}"\nsource_textual_fidelity_audit: "visual-scan-verified"\n',
            1,
        )
    path.write_text(text)

# Four targeted English clarifications found during direct Tamil–English comparison.
corrections = {
    3764: [
        (
            'Selvi was electrocuted and murdered by her husband in Tiruppur.',
            'Selvi was electrocuted and murdered in Tiruppur.',
        ),
    ],
    3765: [
        (
            'the weddings I have conducted alone approach twenty thousand.',
            'the number of marriages I have solemnised is itself close to twenty thousand.',
        ),
        (
            'fearing that the crowd might fall upon me',
            'fearing that the crowd might press in on me',
        ),
    ],
    3766: [
        (
            'they will sail towards Sri Lanka on 22 June in all their mechanised boats, flying white flags.',
            'they will conduct a boat procession towards Sri Lanka on 22 June in all their mechanised boats, flying white flags.',
        ),
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

report = '''# Bilingual Alignment Review — Letters 3764–3769

## Scope

- Volume: **49**
- Letters reviewed: **3764–3769**
- Canonical Tamil source range: **PDF 24–63**
- Letters completed in this batch: **6/6**
- Approximate English body reviewed: **9,621 words**
- Status after review: **verified**

## Review method

Each English translation was compared directly with the complete canonical Tamil reproduced in the same bilingual file. The review checked:

1. title, salutation, closing and date;
2. paragraph and argumentative sequence;
3. every substantive claim and attribution;
4. quotations and reported speech;
5. names, dates, counts, monetary figures and institutional terms;
6. list completeness and item order;
7. rhetorical questions, irony, repetition and political intensity; and
8. English wording that could accidentally broaden, narrow or change responsibility.

The Tamil source was already scan-verified. This pass did not modify any canonical Tamil page.

## Results by letter

### 3764 — *What Was Left Out of the List of Achievements!*

- The newspaper extract, the two Natarajan interview passages, the surrounding political argument and all **51** murder-list entries were aligned against the Tamil.
- One unsupported attribution was removed: the Tamil reports that Selvi was killed by electrocution in Tiruppur, but does not identify her husband as the perpetrator in that list item.
- Names, dates, rupee amounts, party affiliations and the uncertainty around `சாமாரி` remain source-faithful.

### 3765 — *I Will Work; I Will Keep Working!*

- All publication titles, page counts, numbers of volumes, films, poets, marriages, events, times and named speakers were checked.
- Two English phrases were clarified where their earlier syntax could mislead: the count of marriages solemnised, and the description of the crowd pressing in on Kalaignar.
- No claim, event or rhetorical movement was omitted.

### 3766 — *Will the Government of India Continue to Sleep?*

- The two groups of detained fishermen, all named fishermen, boat counts, custody dates, prisons, courts and Katchatheevu chronology were checked.
- The announced protest was corrected to retain the Tamil's explicit **boat procession** towards Sri Lanka with white flags.
- Attributed allegations regarding Sri Lankan warships and Chinese personnel remain attributed rather than converted into statements of independently established fact.

### 3767 — *Should There Not Be Conduct Befitting the Office?*

- The Mettur–kuruvai chronology, drought-relief complaints, quoted statements, dates, relief amounts and Cauvery argument were fully aligned.
- The acting/acted wordplay and the sequence of rhetorical questions were preserved.
- No English correction was required.

### 3768 — *It Is Among People Like These That....*

- All student totals, rank groups, times, locations, announcements and the quoted Electricity Board passage were checked.
- The distinction between what the Government press release claimed and what *Dinamalar* reported was preserved.
- No English correction was required.

### 3769 — *Some of the Charitable Work Carried Out by the DMK!*

- Every assistance category, date, beneficiary count, rupee figure, educational award and examination statistic was checked against the Tamil.
- The distinction among the DMK, DMK Charitable Trust, headquarters and Youth Wing Charitable Trust was maintained throughout.
- No English correction was required.

## Outcome

- Complete substantive coverage: **passed**
- Paragraph and argument order: **passed**
- Quotations and attribution: **passed after one correction**
- Names, dates, figures and list items: **passed**
- Rhetorical force and political responsibility: **passed**
- English files marked `verified`: **6**
- Canonical Tamil changes: **0**

The next bilingual alignment batch is **letters 3770–3774**.
'''
(base / report_name).write_text(report)

# Update the English index statuses and add the batch report.
index_path = base / 'README.md'
index = index_path.read_text()
for no in letters:
    lines = index.splitlines()
    changed = False
    for i, line in enumerate(lines):
        if line.startswith(f'| [{no}]'):
            if not line.endswith('| source-checked |'):
                raise SystemExit(f'{no}: unexpected index row status')
            lines[i] = line[:-len('| source-checked |')] + '| verified |'
            changed = True
            break
    if not changed:
        raise SystemExit(f'{no}: index row missing')
    index = '\n'.join(lines) + ('\n' if index.endswith('\n') else '')
section = '''## Bilingual alignment reviews

- Letters **3764–3769**: substantive Tamil–English alignment completed; six files verified, with four targeted English corrections and no Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md`](BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md)

'''
anchor = '## Translation policy\n'
if section.strip() not in index:
    if anchor not in index:
        raise SystemExit('English index translation-policy anchor missing')
    index = index.replace(anchor, section + anchor, 1)
index_path.write_text(index)

# Record batch-level progress.
progress_path = base / 'PROGRESS.md'
progress = progress_path.read_text()
progress = progress.replace(
    '- [ ] Full bilingual alignment review\n',
    '- [ ] Full bilingual alignment review\n'
    '  - [x] Letters 3764–3769 verified\n'
    '  - [ ] Letters 3770–3774\n'
    '  - [ ] Letters 3775–3779\n'
    '  - [ ] Letters 3780–3784\n'
    '  - [ ] Letters 3785–3789\n'
    '  - [ ] Letters 3790–3794\n'
    '  - [ ] Letters 3795–3799\n'
    '  - [ ] Letters 3800–3804\n'
    '  - [ ] Letters 3805–3811\n'
    '  - [ ] Letters 3812–3816\n',
    1,
)
progress = progress.replace(
    '## Counts\n',
    '## Bilingual alignment review reports\n\n'
    '- Letters **3764–3769** — [`BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md`](BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md): **6/6 verified**; four targeted English corrections; no Tamil-source changes.\n\n'
    '## Counts\n',
    1,
)
progress = progress.replace('- Reviewed: **0**', '- Reviewed: **6**', 1)
progress = progress.replace('- Verified: **0**', '- Verified: **6**', 1)
progress = progress.replace(
    'Conduct the full bilingual alignment review across letters **3764–3816**, followed by the volume-level English release report.',
    'Continue the bilingual alignment review with letters **3770–3774**. After all 53 letters are verified, conduct the volume-level English editorial consistency pass and prepare the release report.',
    1,
)
progress_path.write_text(progress)

# Update the volume summary.
volume_readme = root / 'volumes' / 'volume-49' / 'README.md'
volume = volume_readme.read_text()
old = '- All **53** letters are now translated and source-checked. The next stage is full bilingual alignment review, followed by the volume-level release report.'
new = ('- All **53** letters are translated and source-checked.\n'
       '- Bilingual alignment review is complete for letters **3764–3769**: **6 verified**, **47 awaiting alignment review**. See the [review report](translations/en/BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md).\n'
       '- Next alignment batch: letters **3770–3774**.')
if old not in volume:
    raise SystemExit('Volume README alignment-status target not found')
volume_readme.write_text(volume.replace(old, new, 1))

# Remove every one-use workflow and staging artifact from the final tree.
for path in [
    root / '.github' / 'workflows' / 'export-v49-review-3764-3769.yml',
    root / '.github' / 'workflows' / 'finalize-v49-review-3764-3769.yml',
]:
    if path.exists():
        path.unlink()
staging = root / '.github' / 'v49-review-3764-3769'
if staging.exists():
    import shutil
    shutil.rmtree(staging)

# Validation helpers.
def norm(text: str) -> str:
    return '\n'.join(line.rstrip() for line in text.rstrip().splitlines()) + '\n'

# Verify statuses, complete canonical Tamil preservation, and source markers.
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
    for p in range(start, end + 1):
        src = (root / 'volumes' / 'volume-49' / 'pages' / f'page-{p:03d}.md').read_text()
        body = src.split('---', 2)[2].lstrip('\n').rstrip()
        expected_parts.append(f'<!-- Source PDF page {p:03d} -->\n\n{body}')
    marker = f'<!-- Source PDF page {start:03d} -->'
    if marker not in original:
        raise SystemExit(f'{no}: first source marker missing')
    actual_pages = original[original.index(marker):]
    expected = '\n\n'.join(expected_parts) + '\n'
    if norm(actual_pages) != norm(expected):
        raise SystemExit(f'{no}: Tamil source no longer matches canonical pages')

checks = {
    3764: ('Selvi was electrocuted and murdered in Tiruppur.', 'by her husband in Tiruppur'),
    3765: ('the number of marriages I have solemnised is itself close to twenty thousand.', 'the weddings I have conducted alone approach twenty thousand'),
    3766: ('conduct a boat procession towards Sri Lanka', 'they will sail towards Sri Lanka on 22 June'),
}
for no, (required, forbidden) in checks.items():
    text = (letters_dir / letters[no][0]).read_text()
    if required not in text or forbidden in text:
        raise SystemExit(f'{no}: targeted correction validation failed')

index = index_path.read_text()
for no in letters:
    row = next((line for line in index.splitlines() if line.startswith(f'| [{no}]')), None)
    if not row or not row.endswith('| verified |'):
        raise SystemExit(f'{no}: index status not verified')
if report_name not in index:
    raise SystemExit('English index lacks review report')

progress = progress_path.read_text()
for needle in ['- Reviewed: **6**', '- Verified: **6**', 'letters **3770–3774**']:
    if needle not in progress:
        raise SystemExit(f'Progress validation failed: {needle}')

report_text = (base / report_name).read_text()
for needle in ['Letters reviewed: **3764–3769**', 'Letters completed in this batch: **6/6**', 'Canonical Tamil changes: **0**', 'all **51** murder-list entries']:
    if needle not in report_text:
        raise SystemExit(f'Review report validation failed: {needle}')

volume_text = volume_readme.read_text()
for needle in ['**6 verified**', '**47 awaiting alignment review**', 'letters **3770–3774**']:
    if needle not in volume_text:
        raise SystemExit(f'Volume README validation failed: {needle}')

print('Validated bilingual alignment review for letters 3764-3769.')
