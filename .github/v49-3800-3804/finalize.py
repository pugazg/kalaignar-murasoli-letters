from pathlib import Path
import base64, io, lzma, tarfile, shutil

root = Path.cwd()
staging = root / '.github' / 'v49-3800-3804'
parts = sorted(staging.glob('payload.part*'))
if not parts:
    raise SystemExit('No payload parts found')
encoded = ''.join(p.read_text().strip() for p in parts)
payload = lzma.decompress(base64.b64decode(encoded))
with tarfile.open(fileobj=io.BytesIO(payload), mode='r:') as tf:
    tf.extractall(root)

# Remove every one-use workflow and staging artifact from the final tree.
for path in [
    root / '.github' / 'workflows' / 'export-v49-3800-3804.yml',
    root / '.github' / 'workflows' / 'finalize-v49-3800-3804.yml',
]:
    if path.exists():
        path.unlink()
if staging.exists():
    shutil.rmtree(staging)

letters = {
    3800: ('3800-the-food-security-act-gain-or-loss.md', 277, 284),
    3801: ('3801-a-chief-minister-bent-on-holding-closing-ceremonies.md', 285, 291),
    3802: ('3802-the-hogenakkal-project-and-the-muthialpet-police-station.md', 292, 298),
    3803: ('3803-the-great-schemes-for-women-under-the-dmk-government.md', 299, 306),
    3804: ('3804-let-us-carry-forward-the-eradication-of-superstition.md', 307, 313),
}
for no, (name, start, end) in letters.items():
    path = root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'letters' / name
    text = path.read_text()
    expected_markers = end - start + 1
    if text.count('<!-- Source PDF page ') != expected_markers:
        raise SystemExit(f'{no}: wrong source marker count')
    if '\ufffd' in text or 'translation_status: "source-checked"' not in text:
        raise SystemExit(f'{no}: invalid translation file')
    original = text.split('## Original Tamil — மூலத் தமிழ்\n\n', 1)[1]
    expected_parts = []
    for p in range(start, end + 1):
        src = (root / 'volumes' / 'volume-49' / 'pages' / f'page-{p}.md').read_text()
        body = src.split('---', 2)[2].lstrip('\n').rstrip()
        expected_parts.append(f'<!-- Source PDF page {p} -->\n\n{body}')
    expected = '\n\n'.join(expected_parts) + '\n'
    if original != expected:
        raise SystemExit(f'{no}: appended Tamil is not canonical')

progress = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'PROGRESS.md').read_text()
for needle in ['Translated: **41**', 'Source-checked: **41**', 'letters **3805–3809**']:
    if needle not in progress:
        raise SystemExit(f'Progress validation failed: {needle}')
print('Validated letters 3800-3804 and metadata updates.')
