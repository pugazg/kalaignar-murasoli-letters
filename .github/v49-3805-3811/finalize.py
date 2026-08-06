from pathlib import Path
import base64, io, lzma, tarfile, shutil

root = Path.cwd()
staging = root / '.github' / 'v49-3805-3811'
parts = sorted(staging.glob('payload.part*'))
if not parts:
    raise SystemExit('No payload parts found')
encoded = ''.join(p.read_text().strip() for p in parts)
payload = lzma.decompress(base64.b64decode(encoded))
with tarfile.open(fileobj=io.BytesIO(payload), mode='r:') as tf:
    tf.extractall(root)

for path in [
    root / '.github' / 'workflows' / 'export-v49-3805-3811.yml',
    root / '.github' / 'workflows' / 'finalize-v49-3805-3811.yml',
]:
    if path.exists():
        path.unlink()
if staging.exists():
    shutil.rmtree(staging)

letters = {
    3805: ('3805-only-a-referendum-can-give-eelam-tamils-a-new-life.md', 314, 319),
    3806: ('3806-justice-will-prevail-it-certainly-will.md', 320, 327),
    3807: ('3807-bearing-the-sword-of-righteous-struggle-let-us-continue-on-periyars-and-annas-path.md', 328, 334),
    3808: ('3808-tamil-nadu-in-the-terrifying-grip-of-murder.md', 335, 341),
    3809: ('3809-you-are-lamps-to-the-home-and-workers-for-the-nation.md', 342, 349),
    3810: ('3810-a-dream-seen-in-the-glare-of-publicity.md', 350, 357),
    3811: ('3811-they-say-ghee-drips-from-finger-millet-listen-tamils.md', 358, 364),
}

def normalize_trailing_space(text: str) -> str:
    return '\n'.join(line.rstrip() for line in text.rstrip().splitlines()) + '\n'

for no, (name, start, end) in letters.items():
    path = root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'letters' / name
    text = path.read_text()
    expected_markers = end - start + 1
    if text.count('<!-- Source PDF page ') != expected_markers:
        raise SystemExit(f'{no}: wrong source marker count')
    if '\ufffd' in text or 'translation_status: "source-checked"' not in text:
        raise SystemExit(f'{no}: invalid translation file')
    if '## Original Tamil — மூலத் தமிழ்\n\n' not in text:
        raise SystemExit(f'{no}: original Tamil section missing')
    original = text.split('## Original Tamil — மூலத் தமிழ்\n\n', 1)[1]
    expected_parts = []
    for p in range(start, end + 1):
        src = (root / 'volumes' / 'volume-49' / 'pages' / f'page-{p}.md').read_text()
        body = src.split('---', 2)[2].lstrip('\n').rstrip()
        expected_parts.append(f'<!-- Source PDF page {p} -->\n\n{body}')
    expected = '\n\n'.join(expected_parts) + '\n'
    if normalize_trailing_space(original) != normalize_trailing_space(expected):
        raise SystemExit(f'{no}: appended Tamil does not match canonical source')

progress = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'PROGRESS.md').read_text()
for needle in ['Translated: **48**', 'Source-checked: **48**', 'letters **3812–3816**']:
    if needle not in progress:
        raise SystemExit(f'Progress validation failed: {needle}')
index = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'README.md').read_text()
for no in letters:
    if f'| [{no}]' not in index:
        raise SystemExit(f'Index validation failed for {no}')
audit = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'TEXTUAL_FIDELITY_AUDIT_3805_3811.md').read_text()
for needle in ['51/51', 'no canonical correction was required', '3805–3811']:
    if needle.lower() not in audit.lower():
        raise SystemExit(f'Audit validation failed: {needle}')
print('Validated letters 3805-3811 and metadata updates.')
