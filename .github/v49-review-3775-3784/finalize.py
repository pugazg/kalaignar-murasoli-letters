from pathlib import Path
import base64, hashlib, io, lzma, shutil, tarfile

root = Path.cwd()
staging = root / '.github' / 'v49-review-3775-3784'
parts = sorted(staging.glob('payload.part*'))
if len(parts) != 3:
    raise SystemExit(f'Expected 3 payload parts, found {len(parts)}')
encoded = ''.join(p.read_text().strip() for p in parts)
compressed = base64.b64decode(encoded)
if hashlib.sha256(compressed).hexdigest() != '3d15685cb9761a33ec4cfe08038cccc2537dd542297ec7b8555e558be789a437':
    raise SystemExit('Compressed payload SHA-256 mismatch')
payload = lzma.decompress(compressed)
if hashlib.sha256(payload).hexdigest() != '3bd26cfde5cdfa4bba3c5e3dc5c7eb69c354f8dc5937e6fe95825385e8363df5':
    raise SystemExit('Tar payload SHA-256 mismatch')
with tarfile.open(fileobj=io.BytesIO(payload), mode='r:') as tf:
    for member in tf.getmembers():
        dest = (root / member.name).resolve()
        if root.resolve() not in dest.parents and dest != root.resolve():
            raise SystemExit(f'Unsafe tar path: {member.name}')
    tf.extractall(root)

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

base = root / 'volumes' / 'volume-49' / 'translations' / 'en'
letters_dir = base / 'letters'

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

t3777 = (letters_dir / letters[3777][0]).read_text()
if 'workers’ indefinite hunger strike' not in t3777 or 'workers’ indefinite struggle' in t3777:
    raise SystemExit('3777 hunger-strike correction failed')
t3780 = (letters_dir / letters[3780][0]).read_text()
if t3780.count('Vikramajit Singh') < 3 or 'Vikramajit Sen' in t3780:
    raise SystemExit('3780 source-name alignment failed')
if 'canonical Tamil source prints the judge’s name as **Vikramajit Singh**' not in t3780:
    raise SystemExit('3780 source-name note missing')
t3782 = (letters_dir / letters[3782][0]).read_text()
if 'delayed because of land encroachment.' not in t3782 or 'delayed because of land acquisition.' in t3782:
    raise SystemExit('3782 land-encroachment correction failed')

r1 = (base / 'BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md').read_text()
for needle in ['Letters reviewed: **3775–3779**', 'Letters completed in this batch: **5/5**', 'Targeted English corrections: **1**', 'Canonical Tamil changes: **0**']:
    if needle not in r1:
        raise SystemExit(f'3775-3779 report missing: {needle}')
r2 = (base / 'BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md').read_text()
for needle in ['Letters reviewed: **3780–3784**', 'Letters completed in this batch: **5/5**', 'Targeted English corrections: **2**', 'Canonical Tamil changes: **0**']:
    if needle not in r2:
        raise SystemExit(f'3780-3784 report missing: {needle}')

index = (base / 'README.md').read_text()
for no in letters:
    row = next((line for line in index.splitlines() if line.startswith(f'| [{no}]')), None)
    if not row or not row.endswith('| verified |'):
        raise SystemExit(f'{no}: English index status not verified')
for report_name in ['BILINGUAL_ALIGNMENT_REVIEW_3775_3779.md', 'BILINGUAL_ALIGNMENT_REVIEW_3780_3784.md']:
    if report_name not in index:
        raise SystemExit(f'Index lacks {report_name}')

progress = (base / 'PROGRESS.md').read_text()
for needle in ['- [x] Letters 3775–3779 verified', '- [x] Letters 3780–3784 verified', '- Reviewed: **21**', '- Verified: **21**', 'letters **3785–3789**']:
    if needle not in progress:
        raise SystemExit(f'Progress validation failed: {needle}')

volume = (root / 'volumes' / 'volume-49' / 'README.md').read_text()
for needle in ['through letter **3784**', '**21 verified**', '**32 awaiting alignment review**', 'letters **3785–3789**']:
    if needle not in volume:
        raise SystemExit(f'Volume README validation failed: {needle}')

if staging.exists():
    shutil.rmtree(staging)
print('Validated bilingual alignment review for letters 3775-3784.')
