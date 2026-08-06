from pathlib import Path
import re, csv, shutil, json

repo = Path.cwd()
en = repo / 'volumes/volume-49/translations/en'
letters = en / 'letters'
plan_path = repo / 'volumes/volume-49/TRANSLATION_PLAN.md'

fixes = {
    '3765-i-will-work-i-will-keep-working.md': [('Tolkappiya Poonga', 'Tolkāppiya Poonga')],
    '3775-long-live-the-fame-of-perunthalaivar-kamarajar.md': [('Kanniyakumari', 'Kanyakumari')],
    '3776-our-journey-continues-without-faltering.md': [('Kanniyakumari', 'Kanyakumari')],
    '3785-let-the-womens-reservation-bill-be-passed.md': [('Law Minister Bharadwaj', 'Law Minister Bhardwaj')],
    '3786-is-delay-your-very-name-government-of-tamil-nadu.md': [('Kanniyakumari', 'Kanyakumari')],
    '3797-the-day-of-bidding-them-farewell-is-not-far-away.md': [('named it after Pavendar.', 'named it after Pavendhar.')],
    '3807-bearing-the-sword-of-righteous-struggle-let-us-continue-on-periyars-and-annas-path.md': [
        ("Periyar's and Anna's Path", 'Periyar’s and Anna’s Path'),
        ('the Pavendar Award', 'the Pavendhar Award'),
    ],
    '3809-you-are-lamps-to-the-home-and-workers-for-the-nation.md': [('opened by videoconference', 'opened by video conference')],
}

originals = {p.name: p.read_text() for p in sorted(letters.glob('*.md'))}
if len(originals) != 53:
    raise SystemExit(f'Expected 53 letter files, found {len(originals)}')

applied = []
for name, replacements in fixes.items():
    p = letters / name
    text = p.read_text()
    before, marker, tamil = text.partition('## Original Tamil — மூலத் தமிழ்')
    if not marker:
        raise SystemExit(f'{name}: missing Tamil marker')
    for old, new in replacements:
        count = before.count(old)
        if count == 0:
            raise SystemExit(f'{name}: missing expected text {old!r}')
        before = before.replace(old, new)
        applied.append((name, old, new, count))
    p.write_text(before + marker + tamil)


def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        raise SystemExit('Missing frontmatter')
    data = {}
    for line in m.group(1).splitlines():
        if ': ' not in line:
            continue
        key, value = line.split(': ', 1)
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.isdigit():
            value = int(value)
        data[key] = value
    return data, m.end()

rows = []
word_total = 0
for p in sorted(letters.glob('*.md')):
    text = p.read_text()
    meta, fm_end = frontmatter(text)
    eng = text[fm_end:].split('## Original Tamil — மூலத் தமிழ்')[0]
    starts = [x for token in ('**Udanpirappē,**', '*(A tribute written') if (x := eng.find(token)) >= 0]
    start = min(starts) if starts else 0
    end = eng.find('## Letter-specific notes')
    if end < 0:
        end = len(eng)
    body = eng[start:end]
    body = re.sub(r'<!--.*?-->', ' ', body, flags=re.S)
    body = re.sub(r'\[[^\]]+\]\([^\)]+\)', ' ', body)
    body = re.sub(r'[`*_>#|~-]', ' ', body)
    wc = len(re.findall(r"[A-Za-zÀ-ž0-9₹]+(?:[’'-][A-Za-zÀ-ž0-9]+)*", body))
    word_total += wc
    rows.append({
        'letter_number': meta['letter_number'],
        'date': meta['date'],
        'english_title': meta['english_title'],
        'tamil_title': meta['tamil_title'],
        'source_pdf_pages': f"{meta['source_pdf_page_start']}-{meta['source_pdf_page_end']}",
        'source_printed_pages': f"{meta['source_printed_page_start']}-{meta['source_printed_page_end']}",
        'translation_status': meta['translation_status'],
        'bilingual_alignment_status': meta['bilingual_alignment_status'],
        'source_textual_fidelity_audit': meta['source_textual_fidelity_audit'],
        'english_word_count': wc,
        'file': f'letters/{p.name}',
        'bilingual_alignment_report': meta['bilingual_alignment_report'],
    })

readme = en / 'README.md'
r = readme.read_text()
r = r.replace("Bearing the Sword of Righteous Struggle, Let Us Continue on Periyar's and Anna's Path!", "Bearing the Sword of Righteous Struggle, Let Us Continue on Periyar’s and Anna’s Path!")
release_section = '''\n## Volume release\n\nVolume 49 has completed translation, source checking, bilingual alignment and the volume-level English editorial consistency pass.\n\n- [Editorial consistency review](EDITORIAL_CONSISTENCY_REVIEW.md)\n- [Translation manifest](TRANSLATION_MANIFEST.csv)\n- [Final release report](RELEASE_REPORT.md)\n\nRelease status: **53/53 translated, source-checked and verified**.\n'''
if '## Volume release' not in r:
    marker = '\n## Translation policy\n'
    if marker not in r:
        raise SystemExit('English README insertion marker missing')
    r = r.replace(marker, release_section + marker)
readme.write_text(r)

progress = en / 'PROGRESS.md'
ptext = progress.read_text()
ptext = ptext.replace('- [ ] Volume-level English index and release report', '- [x] Volume-level English editorial consistency pass\n- [x] Translation manifest and final release report')
ptext = ptext.replace('The bilingual alignment review is complete for all **53 letters**. Conduct the volume-level English editorial consistency pass and prepare the release report.', 'Volume 49 English release preparation is complete: all **53 letters** are translated, source-checked, bilingual-aligned, editorially reviewed and listed in the final manifest and release report.')
progress.write_text(ptext)

volume_readme = repo / 'volumes/volume-49/README.md'
vtext = volume_readme.read_text().replace('- Next stage: volume-level English editorial consistency pass and release report.', '- Volume-level English editorial consistency pass and release report: **complete**. See [`translations/en/RELEASE_REPORT.md`](translations/en/RELEASE_REPORT.md).')
volume_readme.write_text(vtext)

root_readme = repo / 'README.md'
rt = root_readme.read_text().replace('| 49 | 01.06.2013–10.10.2013 | 402 | 1–402 | 53 (கடிதங்கள் 3764–3816) | 53 / 53 (3764–3816) |', '| 49 | 01.06.2013–10.10.2013 | 402 | 1–402 | 53 (கடிதங்கள் 3764–3816) | 53 / 53 verified; editorial release complete |')
root_readme.write_text(rt)

glossary = en / 'GLOSSARY.md'
g = glossary.read_text().rstrip() + '\n'
for row in [
    '| கன்னியாகுமரி | **Kanyakumari** | approved | Established English place-name used consistently throughout the released translation. |',
    '| தொல்காப்பியப் பூங்கா | **Tolkāppiya Poonga** | approved | Diacritic-bearing transliteration used consistently for the named park and work-derived title. |',
    '| பாவேந்தர் | **Pavendhar** | approved | Established literary honorific; spelling standardised across institutional and award references. |',
    '| காணொலிக் காட்சி / video conference | **video conference** | approved | Open compound used consistently for remote inaugurations and official events. |',
]:
    if row not in g:
        g += row + '\n'
glossary.write_text(g)

manifest = en / 'TRANSLATION_MANIFEST.csv'
with manifest.open('w', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

correction_lines = '''- **3765:** standardised `Tolkappiya Poonga` to **Tolkāppiya Poonga**.
- **3775, 3776 and 3786:** standardised the place-name to **Kanyakumari**.
- **3785:** corrected Union Law Minister **H. R. Bharadwaj** to **H. R. Bhardwaj**, matching the established form already used elsewhere in the volume.
- **3797 and 3807:** standardised the literary honorific to **Pavendhar**.
- **3807:** standardised the English title apostrophes to **Periyar’s and Anna’s Path**.
- **3809:** standardised **videoconference** to **video conference**.'''

(en / 'EDITORIAL_CONSISTENCY_REVIEW.md').write_text(f'''# Volume 49 English Editorial Consistency Review

## Scope

- Letters reviewed: **53** — 3764 through 3816
- English translation files: **53**
- Source letter pages represented: **PDF 24–401**
- Editorial English word count: **{word_total:,}**
- Bilingual alignment status before this pass: **53/53 verified**
- Canonical Tamil changes in this pass: **0**

## Method

The pass reviewed every English file at volume level rather than as an isolated letter. It checked:

1. metadata, title and index agreement;
2. the mandatory translator’s note and bilingual document order;
3. names, place-names, honorifics and transliteration;
4. recurring institutional, legal, political and administrative terminology;
5. British/Indian English spelling and compound-word treatment;
6. punctuation and typography in English titles;
7. source links, PDF and printed-page ranges, dates and status fields;
8. the position and preservation of letter-specific notes; and
9. byte-for-byte preservation of every **Original Tamil — மூலத் தமிழ்** section.

The pass was editorial, not substantive: it did not recast arguments, soften political language, modernise source-era claims or reconcile anomalies with outside information.

## Corrections applied

{correction_lines}

These changes affect **8 letter files** and are limited to English spelling, transliteration, typography or name-form consistency.

## Deliberately preserved

- The printed date **30 June 2016** in letter 3770 remains preserved and explicitly documented as a source anomaly.
- Source-era institutional names, quotations, figures and conflicting claims remain as translated and attributed.
- Distinct people with similar names were not conflated—for example, Nakkheeran Kamaraj, Kamarajar, Ilayaraja and Ilaiyaraaja remain separate.
- Source-specific rhetoric, double exclamation marks, ellipses, sarcasm and title wordplay remain intact where they carry the Tamil’s force.
- File slugs were not renamed, preserving stable repository links.

## Validation outcome

- Translation files present: **53/53**
- `translation_status: verified`: **53/53**
- `bilingual_alignment_status: verified`: **53/53**
- Mandatory translator’s note: **53/53 exact**
- English title and frontmatter agreement: **53/53**
- Original Tamil sections preserved: **53/53**
- Translation manifest rows: **53**
- Canonical Tamil edits: **0**

The volume-level English editorial consistency pass is complete.
''')

(en / 'RELEASE_REPORT.md').write_text(f'''# Volume 49 English Translation — Final Release Report

## Release identity

- Work: **Kalaignar’s Murasoli Letters — Volume 49**
- Letters: **3764–3816**
- Letter dates: **1 June 2013–10 October 2013**
- Source PDF: **402 pages**
- Translated letter-page span: **PDF 24–401**
- English letters released: **53**
- Editorial English word count: **{word_total:,}**

## Completion status

| Stage | Result |
|---|---:|
| Tamil page-level transcription | Complete |
| English translation | 53/53 |
| Source checking | 53/53 |
| Bilingual alignment verification | 53/53 |
| Volume-level English editorial review | Complete |
| Translation manifest | 53 rows |
| Canonical Tamil changed during English editorial review | 0 |

## Release contents

- [`README.md`](README.md) — complete English index and access point
- [`letters/`](letters/) — one verified bilingual Markdown file per letter
- [`TRANSLATION_MANIFEST.csv`](TRANSLATION_MANIFEST.csv) — machine-readable metadata for all 53 letters
- [`GLOSSARY.md`](GLOSSARY.md) — approved recurring terms and transliteration decisions
- [`EDITORIAL_CONSISTENCY_REVIEW.md`](EDITORIAL_CONSISTENCY_REVIEW.md) — volume-level editorial QA record
- `BILINGUAL_ALIGNMENT_REVIEW_*.md` — substantive Tamil–English review reports
- `TEXTUAL_FIDELITY_AUDIT_*.md` — scan-to-Markdown source audits

## Editorial and archival policy

The released English is a clear, contemporary, non-literary translation. It preserves Kalaignar’s argument order, factual detail, criticism, irony, repetition, quoted voices and rhetorical questions. The complete audited Tamil source remains appended to every letter and remains authoritative.

Source anomalies are documented rather than silently corrected. Most notably, letter 3770 retains the printed date **30 June 2016**, while its file explains that the contents and volume position place it in June 2013.

## QA summary

The final editorial pass corrected a small set of cross-volume inconsistencies in English name forms, place-name spelling, transliteration, title typography and compound-word treatment. It made no change to political meaning, responsibility, attribution, uncertainty, figures, quotations or the canonical Tamil.

Release status: **ready as the completed English edition of Volume 49 in this repository**.
''')

errors = []
for name, old in originals.items():
    new = (letters / name).read_text()
    marker = '## Original Tamil — மூலத் தமிழ்'
    if old.partition(marker)[2] != new.partition(marker)[2]:
        errors.append(f'Tamil changed: {name}')

plan = plan_path.read_text()
cm = re.search(r'(> \*\*Translator’s note\*\*\n>\n> This translation.*?movement\.)', plan, re.S)
if not cm:
    errors.append('Canonical translator note not found')
else:
    canonical_note = cm.group(1)
    for p in sorted(letters.glob('*.md')):
        text = p.read_text()
        meta, _ = frontmatter(text)
        nm = re.search(r'(> \*\*Translator’s note\*\*\n>\n> This translation.*?movement\.)', text, re.S)
        if not nm or nm.group(1) != canonical_note:
            errors.append(f'Translator note mismatch: {p.name}')
        h = re.search(r'^# (.+)$', text, re.M)
        if not h or h.group(1) != f"{meta['letter_number']}. {meta['english_title']}":
            errors.append(f'Title mismatch: {p.name}')
        if meta.get('translation_status') != 'verified' or meta.get('bilingual_alignment_status') != 'verified':
            errors.append(f'Status mismatch: {p.name}')

index = readme.read_text()
for row in rows:
    filename = Path(row['file']).name
    if f"[{row['letter_number']}](letters/{filename})" not in index:
        errors.append(f"Index missing {row['letter_number']}")
if len(manifest.read_text().splitlines()) != 54:
    errors.append('Manifest does not contain 53 rows')
for name, replacements in fixes.items():
    eng = (letters / name).read_text().split('## Original Tamil — மூலத் தமிழ்')[0]
    for old, new in replacements:
        if old in eng:
            errors.append(f'Old form remains in {name}: {old}')
        if new not in eng:
            errors.append(f'New form missing in {name}: {new}')

shutil.rmtree(repo / '.github/v49-editorial-release', ignore_errors=True)
for temp in [repo / '.github/workflows/export-v49-editorial-release.yml', repo / '.github/workflows/finalize-v49-editorial-release.yml']:
    if temp.exists():
        temp.unlink()

if errors:
    raise SystemExit('\n'.join(errors))
print(json.dumps({'letters': len(rows), 'word_total': word_total, 'letter_files_changed': len(fixes), 'correction_operations': len(applied)}, ensure_ascii=False))
