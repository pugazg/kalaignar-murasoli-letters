from pathlib import Path
import base64
import re
import shutil
import tarfile
import tempfile

STAGING = Path('.github/v49-3780-3784')
WORKFLOW = Path('.github/workflows/finalize-v49-3780-3784.yml')


def must_replace(path: str | Path, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    count = text.count(old)
    if count != 1:
        raise SystemExit(
            f'Expected exactly one match in {p}; found {count} for {old!r}'
        )
    p.write_text(text.replace(old, new), encoding='utf-8')


# Reconstruct and unpack the audited translation payload.
parts = sorted(STAGING.glob('payload.part*'))
if len(parts) != 4:
    raise SystemExit(f'Expected four payload parts, found {len(parts)}')
encoded = ''.join(part.read_text(encoding='ascii').strip() for part in parts)
archive = base64.b64decode(encoded, validate=True)
work = Path(tempfile.mkdtemp(prefix='v49-3780-3784-'))
archive_path = work / 'batch.tar.gz'
archive_path.write_bytes(archive)
extract_dir = work / 'payload'
extract_dir.mkdir()
with tarfile.open(archive_path, 'r:gz') as tf:
    tf.extractall(extract_dir, filter='data')

# Scan-verified corrections to the canonical Tamil page files.
corrections = {
    'volumes/volume-49/pages/page-133.md': [
        (
            'எம்.பி.,பி.எஸ் படிப்பிற்கு அகில இந்திய அளவில் பொது',
            'எம்.பி.,பி.எஸ். படிப்பிற்கு அகில இந்திய அளவில் பொது',
        ),
    ],
    'volumes/volume-49/pages/page-134.md': [
        (
            'தமிழ்நாடு அரசு எம்பி.,பி.எஸ் படிப்பிற்கு',
            'தமிழ்நாடு அரசு எம்.பி.,பி.எஸ். படிப்பிற்கு',
        ),
        (
            'அகில இந்திய அளவில் எம்.பி.பி.எஸ். படிப்பிற்கான',
            'அகில இந்திய அளவில் எம்.பி.,பி.எஸ். படிப்பிற்கான',
        ),
    ],
    'volumes/volume-49/pages/page-142.md': [
        (
            'மார்க்சிஸ்ட் கம்யூனிஸ்ட் கட் சி, இந்தியக் கம்யூனிஸ்ட்',
            'மார்க்சிஸ்ட் கம்யூனிஸ்ட் கட்சி, இந்தியக் கம்யூனிஸ்ட்',
        ),
    ],
    'volumes/volume-49/pages/page-153.md': [
        (
            'ஆட்சியில் 1,885 கோடி ரூபாய்ச் செலவில் 4,019 சிறிய பாலங்கள்',
            'ஆட்சியில் 1,385 கோடி ரூபாய்ச் செலவில் 4,019 சிறிய பாலங்கள்',
        ),
        (
            'சாலையை முடக்கிப்போட்டு வைத்திருப்பதே, அ.தி.மு.க. ஆட்சி\nதான!',
            'சாலையை முடக்கிப்போட்டு வைத்திருப்பதே, அ.தி.மு.க. ஆட்சி\nதான்!',
        ),
    ],
    'volumes/volume-49/pages/page-156.md': [
        (
            'என்றும் உறுதிஅளித்துக் கடிதம்',
            'என்றும் உறுதியளித்துக் கடிதம்',
        ),
        (
            'தன்னாட்சி\nஉரிமைஅளிப்பது',
            'தன்னாட்சி\nஉரிமை அளிப்பது',
        ),
    ],
    'volumes/volume-49/pages/page-161.md': [
        (
            '“டெசோ” .\nஇயக்கத்தின்',
            '“டெசோ”\nஇயக்கத்தின்',
        ),
        (
            '“தமிழர் பெருந்திரள்\nஆர்ப் பாட்டம்”',
            '“தமிழர் பெருந்திரள்\nஆர்ப்பாட்டம்”',
        ),
        (
            'அதற் கான\nஅறிவிப்புகளும்',
            'அதற்கான\nஅறிவிப்புகளும்',
        ),
    ],
    'volumes/volume-49/pages/page-162.md': [
        ('என் பதைப் பற்றியும்;', 'என்பதைப் பற்றியும்;'),
    ],
    'volumes/volume-49/pages/page-164.md': [
        ('மத்தியஅரசின் விருதும்', 'மத்திய அரசின் விருதும்'),
    ],
}

for page_path, replacements in corrections.items():
    for before, after in replacements:
        must_replace(page_path, before, after)


def page_body(page: int) -> str:
    p = Path(f'volumes/volume-49/pages/page-{page:03d}.md')
    text = p.read_text(encoding='utf-8')
    match = re.match(r'^---\n.*?\n---\n(?:\n)?', text, flags=re.S)
    if not match:
        raise SystemExit(f'Front matter not found: {p}')
    return text[match.end():].rstrip()


letter_files = {
    3780: '3780-the-entrance-examination-verdict-is-opposition-necessary.md',
    3781: '3781-i-have-neither-political-rancour-nor-anguish.md',
    3782: '3782-how-long-will-they-keep-deceiving-the-people-of-this-country.md',
    3783: '3783-our-efforts-towards-the-summit-of-victory.md',
    3784: '3784-she-is-supposedly-the-pioneer-for-all-india.md',
}
ranges = {
    3780: (132, 138),
    3781: (139, 148),
    3782: (149, 155),
    3783: (156, 161),
    3784: (162, 168),
}
out_dir = Path('volumes/volume-49/translations/en/letters')
out_dir.mkdir(parents=True, exist_ok=True)

# Rebuild each Tamil section directly from the corrected canonical page files.
for letter, filename in letter_files.items():
    source_path = extract_dir / 'letters' / filename
    content = source_path.read_text(encoding='utf-8')
    start, end = ranges[letter]
    source = '\n\n'.join(
        f'<!-- Source PDF page {page} -->\n\n{page_body(page)}'
        for page in range(start, end + 1)
    )
    placeholder = '<!-- APPEND_TAMIL_FROM_SOURCE -->'
    source_marker = f'<!-- Source PDF page {start} -->'
    if content.count(placeholder) == 1:
        content = content.replace(placeholder, source)
    elif content.count(placeholder) == 0 and content.count(source_marker) == 1:
        content = content.split(source_marker, 1)[0].rstrip() + '\n\n' + source
    else:
        raise SystemExit(
            f'Expected one Tamil placeholder or one source marker in {source_path}'
        )
    (out_dir / filename).write_text(content.rstrip() + '\n', encoding='utf-8')

shutil.copy2(
    extract_dir / 'TEXTUAL_FIDELITY_AUDIT_3780_3784.md',
    'volumes/volume-49/translations/en/TEXTUAL_FIDELITY_AUDIT_3780_3784.md',
)

# Repository summaries and indexes.
must_replace(
    'README.md',
    '| 49 | 01.06.2013–10.10.2013 | 402 | 1–402 | 53 (கடிதங்கள் 3764–3816) | 16 / 53 (3764–3779) |',
    '| 49 | 01.06.2013–10.10.2013 | 402 | 1–402 | 53 (கடிதங்கள் 3764–3816) | 21 / 53 (3764–3784) |',
)

must_replace(
    'volumes/volume-49/README.md',
    '- Letters **3764–3779** have been fully translated and source-checked against Tamil PDF pages **24–131**.',
    '- Letters **3764–3784** have been fully translated and source-checked against Tamil PDF pages **24–168**.',
)
must_replace(
    'volumes/volume-49/README.md',
    '- Before translating letters **3775–3779**, every canonical Markdown page from PDF **101–131** was visually compared with its scan; all **31 pages were audited**, and eight scan-verified quotation-mark or word-boundary corrections were applied to the canonical Tamil page files.',
    '- Before translating letters **3775–3779**, every canonical Markdown page from PDF **101–131** was visually compared with its scan; all **31 pages were audited**, and eight scan-verified quotation-mark or word-boundary corrections were applied to the canonical Tamil page files.\n- Before translating letters **3780–3784**, every canonical Markdown page from PDF **132–168** was visually compared with its scan; all **37 pages were audited**, and thirteen scan-verified punctuation, numeral, word-boundary or omitted-character corrections were applied to the canonical Tamil page files.',
)
must_replace(
    'volumes/volume-49/README.md',
    '- Next five-letter iteration: **3780–3784**.',
    '- Next five-letter iteration: **3785–3789**.',
)

index_path = Path('volumes/volume-49/translations/en/README.md')
index = index_path.read_text(encoding='utf-8')
old_pending = '| 3780–3816 | — | — | pending |'
rows = '\n'.join(
    [
        '| [3780](letters/3780-the-entrance-examination-verdict-is-opposition-necessary.md) | The Entrance-Examination Verdict — Is Opposition Necessary? | 23 July 2013 | source-checked |',
        '| [3781](letters/3781-i-have-neither-political-rancour-nor-anguish.md) | I Have Neither Political Rancour nor Anguish! | 24 July 2013 | source-checked |',
        '| [3782](letters/3782-how-long-will-they-keep-deceiving-the-people-of-this-country.md) | How Long Will They Keep Deceiving the People of This Country! | 26 July 2013 | source-checked |',
        '| [3783](letters/3783-our-efforts-towards-the-summit-of-victory.md) | Our Efforts Towards the Summit of Victory! | 27 July 2013 | source-checked |',
        '| [3784](letters/3784-she-is-supposedly-the-pioneer-for-all-india.md) | She Is Supposedly the Pioneer for All India! | 29 July 2013 | source-checked |',
        '| 3785–3816 | — | — | pending |',
    ]
)
if index.count(old_pending) != 1:
    raise SystemExit('Pending index row not found exactly once')
index = index.replace(old_pending, rows)
audit_anchor = '- Letters 3775–3779: **31/31 pages audited; eight canonical quotation/word-boundary artefacts corrected** — [`TEXTUAL_FIDELITY_AUDIT_3775_3779.md`](TEXTUAL_FIDELITY_AUDIT_3775_3779.md)'
audit_new = (
    audit_anchor
    + '\n- Letters 3780–3784: **37/37 pages audited; thirteen canonical punctuation, numeral, word-boundary or omitted-character artefacts corrected** — [`TEXTUAL_FIDELITY_AUDIT_3780_3784.md`](TEXTUAL_FIDELITY_AUDIT_3780_3784.md)'
)
if index.count(audit_anchor) != 1:
    raise SystemExit('Audit anchor missing from English index')
index_path.write_text(index.replace(audit_anchor, audit_new), encoding='utf-8')

must_replace(
    'volumes/volume-49/translations/en/PROGRESS.md',
    '- [x] Letters 3775–3779 translated and source-checked\n- [ ] Letters 3780–3816',
    '- [x] Letters 3775–3779 translated and source-checked\n- [x] Letters 3780–3784 translated and source-checked\n- [ ] Letters 3785–3816',
)
must_replace(
    'volumes/volume-49/translations/en/PROGRESS.md',
    '- Canonical pages **101–131** visually compared against their scans: **31/31 audited**.\n  - [`TEXTUAL_FIDELITY_AUDIT_3775_3779.md`](TEXTUAL_FIDELITY_AUDIT_3775_3779.md)\n  - Eight quotation-mark or word-boundary transcription artefacts were corrected before translation.',
    '- Canonical pages **101–131** visually compared against their scans: **31/31 audited**.\n  - [`TEXTUAL_FIDELITY_AUDIT_3775_3779.md`](TEXTUAL_FIDELITY_AUDIT_3775_3779.md)\n  - Eight quotation-mark or word-boundary transcription artefacts were corrected before translation.\n- Canonical pages **132–168** visually compared against their scans: **37/37 audited**.\n  - [`TEXTUAL_FIDELITY_AUDIT_3780_3784.md`](TEXTUAL_FIDELITY_AUDIT_3780_3784.md)\n  - Thirteen punctuation, numeral, word-boundary or omitted-character transcription artefacts were corrected before translation.',
)
must_replace(
    'volumes/volume-49/translations/en/PROGRESS.md',
    '- Translated: **16**',
    '- Translated: **21**',
)
must_replace(
    'volumes/volume-49/translations/en/PROGRESS.md',
    '- Source-checked: **16**',
    '- Source-checked: **21**',
)
must_replace(
    'volumes/volume-49/translations/en/PROGRESS.md',
    'Translate and source-check letters **3780–3784** using the locked five-letter workflow, including visual scan comparison of every corresponding Tamil Markdown page before translation.',
    'Translate and source-check letters **3785–3789** using the locked five-letter workflow, including visual scan comparison of every corresponding Tamil Markdown page before translation.',
)

glossary_path = Path('volumes/volume-49/translations/en/GLOSSARY.md')
glossary = glossary_path.read_text(encoding='utf-8')
glossary_rows = '\n'.join(
    [
        "| பொது நுழைவுத் தேர்வு | **nationwide common entrance examination** | approved | Uses the source's 2013 terminology; the later acronym NEET is not inserted where absent. |",
        '| +2 | **Plus Two** | approved | Familiar Indian term for the Higher Secondary examination and its marks. |',
        '| 110வது விதி | **Rule 110** | approved | Tamil Nadu Legislative Assembly procedure for a ministerial statement without an immediate debate. |',
        '| சம்பா சாகுபடி | **samba cultivation** | approved | Long-duration paddy season in the Cauvery Delta. |',
        '| காவேரி நடுவர் மன்றம் | **Cauvery Water Disputes Tribunal** | approved | Full institutional name on first contextual reference; Tribunal thereafter. |',
    ]
)
if 'பொது நுழைவுத் தேர்வு' not in glossary:
    glossary = glossary.rstrip() + '\n' + glossary_rows + '\n'
glossary_path.write_text(glossary, encoding='utf-8')

# Validate the finished bilingual files and canonical corrections.
expected_markers = {3780: 7, 3781: 10, 3782: 7, 3783: 6, 3784: 7}
for letter, filename in letter_files.items():
    p = out_dir / filename
    text = p.read_text(encoding='utf-8')
    if '<!-- APPEND_TAMIL_FROM_SOURCE -->' in text:
        raise SystemExit(f'Unresolved Tamil marker in {p}')
    if '## Original Tamil — மூலத் தமிழ்' not in text:
        raise SystemExit(f'Missing Tamil section in {p}')
    if text.count('<!-- Source PDF page ') != expected_markers[letter]:
        raise SystemExit(f'Wrong page-marker count in {p}')
    if 'translation_status: "source-checked"' not in text:
        raise SystemExit(f'Wrong translation status in {p}')

for page_path, replacements in corrections.items():
    text = Path(page_path).read_text(encoding='utf-8')
    for before, after in replacements:
        if before in text or after not in text:
            raise SystemExit(f'Canonical correction validation failed in {page_path}')

# Remove all one-use staging material before the final commit.
shutil.rmtree(STAGING)
if WORKFLOW.exists():
    WORKFLOW.unlink()
shutil.rmtree(work)
