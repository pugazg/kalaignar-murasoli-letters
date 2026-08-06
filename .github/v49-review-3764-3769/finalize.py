from pathlib import Path
import base64, hashlib, io, lzma, shutil, tarfile

root = Path.cwd()
staging = root / '.github' / 'v49-review-3764-3769'
parts = sorted(staging.glob('payload.part*'))
if len(parts) != 7:
    raise SystemExit(f'Expected 7 payload parts, found {len(parts)}')
encoded = ''.join(p.read_text().strip() for p in parts)
compressed = base64.b64decode(encoded)
if hashlib.sha256(compressed).hexdigest() != '8faed96c439ff61851cd0d9bbc6c620c58ff397bd411bd9276faf7955a0adf8a':
    raise SystemExit('Compressed payload SHA-256 mismatch')
payload = lzma.decompress(compressed)
if hashlib.sha256(payload).hexdigest() != 'a57e72db66b98620616cabc1e11bb26800005f22f8d565690a99dcda7fcc7b20':
    raise SystemExit('Tar payload SHA-256 mismatch')
with tarfile.open(fileobj=io.BytesIO(payload), mode='r:') as tf:
    tf.extractall(root)

volume_readme = root / 'volumes' / 'volume-49' / 'README.md'
text = volume_readme.read_text()
old = '- All **53** letters are now translated and source-checked. The next stage is full bilingual alignment review, followed by the volume-level release report.'
new = ('- All **53** letters are translated and source-checked.\n'
       '- Bilingual alignment review is complete for letters **3764–3769**: **6 verified**, **47 awaiting alignment review**. See the [review report](translations/en/BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md).\n'
       '- Next alignment batch: letters **3770–3774**.')
if old not in text:
    raise SystemExit('Volume README alignment-status target not found')
volume_readme.write_text(text.replace(old, new, 1))

for path in [
    root / '.github' / 'workflows' / 'export-v49-review-3764-3769.yml',
    root / '.github' / 'workflows' / 'finalize-v49-review-3764-3769.yml',
]:
    if path.exists():
        path.unlink()
if staging.exists():
    shutil.rmtree(staging)

letters = {
    3764: ('3764-what-was-left-out-of-the-list-of-achievements.md', 24, 31),
    3765: ('3765-i-will-work-i-will-keep-working.md', 32, 39),
    3766: ('3766-will-the-government-of-india-continue-to-sleep.md', 40, 44),
    3767: ('3767-should-there-not-be-conduct-befitting-the-office.md', 45, 51),
    3768: ('3768-it-is-among-people-like-these-that.md', 52, 56),
    3769: ('3769-some-of-the-charitable-work-carried-out-by-the-dmk.md', 57, 63),
}

def norm(text: str) -> str:
    return '\n'.join(line.rstrip() for line in text.rstrip().splitlines()) + '\n'

for no, (name, start, end) in letters.items():
    path = root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'letters' / name
    text = path.read_text()
    for needle in [
        'translation_status: "verified"',
        'bilingual_alignment_status: "verified"',
        'bilingual_alignment_report: "../BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md"',
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
    name = letters[no][0]
    text = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'letters' / name).read_text()
    if required not in text or forbidden in text:
        raise SystemExit(f'{no}: targeted correction validation failed')

index = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'README.md').read_text()
for no in letters:
    row = next((line for line in index.splitlines() if line.startswith(f'| [{no}]')), None)
    if not row or not row.endswith('| verified |'):
        raise SystemExit(f'{no}: index status not verified')
if 'BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md' not in index:
    raise SystemExit('English index lacks review report')

progress = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'PROGRESS.md').read_text()
for needle in ['- Reviewed: **6**', '- Verified: **6**', 'letters **3770–3774**']:
    if needle not in progress:
        raise SystemExit(f'Progress validation failed: {needle}')

report = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'BILINGUAL_ALIGNMENT_REVIEW_3764_3769.md').read_text()
for needle in ['Letters reviewed: **3764–3769**', 'Letters completed in this batch: **6/6**', 'Canonical Tamil changes: **0**', 'all **51** murder-list entries']:
    if needle not in report:
        raise SystemExit(f'Review report validation failed: {needle}')

volume_text = volume_readme.read_text()
for needle in ['**6 verified**', '**47 awaiting alignment review**', 'letters **3770–3774**']:
    if needle not in volume_text:
        raise SystemExit(f'Volume README validation failed: {needle}')

print('Validated bilingual alignment review for letters 3764-3769.')
