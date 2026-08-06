from pathlib import Path
import base64, hashlib, io, lzma, shutil, tarfile

root = Path.cwd()
staging = root / '.github' / 'v49-3812-3816'
parts = sorted(staging.glob('payload.part*'))
if len(parts) != 19:
    raise SystemExit(f'Expected 19 payload parts, found {len(parts)}')
encoded = ''.join(p.read_text().strip() for p in parts)
compressed = base64.b64decode(encoded)
expected_xz_sha = 'c72e2c0c68f138fd889c36ea45c97fc6292a2e07f656c622f1ebf003b4706d3b'
if hashlib.sha256(compressed).hexdigest() != expected_xz_sha:
    raise SystemExit('Compressed payload SHA-256 mismatch')
payload = lzma.decompress(compressed)
if hashlib.sha256(payload).hexdigest() != 'e2cd99428d4a2ab3860cc6a2794851979632fbe9ccf4d128b3910ba839bdc4f2':
    raise SystemExit('Tar payload SHA-256 mismatch')
with tarfile.open(fileobj=io.BytesIO(payload), mode='r:') as tf:
    tf.extractall(root)

# Remove every one-use workflow and staging artifact from the final tree.
for path in [
    root / '.github' / 'workflows' / 'export-v49-3812-3816.yml',
    root / '.github' / 'workflows' / 'finalize-v49-3812-3816.yml',
]:
    if path.exists():
        path.unlink()
if staging.exists():
    shutil.rmtree(staging)

letters = {
    3812: ('3812-many-left-uninvited-and-many-honoured-after-being-invited.md', 365, 374),
    3813: ('3813-this-is-the-dmk-nurtured-by-so-many-samikkannus.md', 375, 379),
    3814: ('3814-does-a-majority-government-mean-it-can-do-anything.md', 380, 387),
    3815: ('3815-nothing-but-corruption-is-going-to-rise.md', 388, 393),
    3816: ('3816-the-tamil-people-are-no-longer-ready-to-be-deceived.md', 394, 401),
}

def normalize_trailing_space(text: str) -> str:
    return '\n'.join(line.rstrip() for line in text.rstrip().splitlines()) + '\n'

for no, (name, start, end) in letters.items():
    path = root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'letters' / name
    if not path.exists():
        raise SystemExit(f'{no}: translation file missing')
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
for needle in ['Translated: **53**', 'Source-checked: **53**', 'full bilingual alignment review']:
    if needle.lower() not in progress.lower():
        raise SystemExit(f'Progress validation failed: {needle}')
index = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'README.md').read_text()
for no in letters:
    if f'| [{no}]' not in index:
        raise SystemExit(f'Index validation failed for {no}')
audit = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'TEXTUAL_FIDELITY_AUDIT_3812_3816.md').read_text()
for needle in ['37/37', 'no canonical correction was required', 'all **53** letters']:
    if needle.lower() not in audit.lower():
        raise SystemExit(f'Audit validation failed: {needle}')
root_readme = (root / 'README.md').read_text()
if '53 / 53 (3764–3816)' not in root_readme:
    raise SystemExit('Root README completion count missing')
if (root / 'volumes' / 'volume-49' / 'pages' / 'page-402.md').exists() is False:
    raise SystemExit('Back cover page unexpectedly missing')
print('Validated final letters 3812-3816 and completed Volume 49 translation metadata.')
