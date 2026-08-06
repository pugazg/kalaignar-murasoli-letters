from pathlib import Path
import ast, base64, shutil, zlib

root = Path.cwd()
base = root / "volumes" / "volume-49" / "translations" / "en"
letters_dir = base / "letters"
reports = ast.literal_eval(zlib.decompress(base64.b64decode("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")).decode())
letters = {
    3785: ("3785-let-the-womens-reservation-bill-be-passed.md", 169, 175, "../BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md"),
    3786: ("3786-is-delay-your-very-name-government-of-tamil-nadu.md", 176, 181, "../BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md"),
    3787: ("3787-august-8-gather-like-a-surging-sea-at-the-demonstration.md", 182, 188, "../BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md"),
    3788: ("3788-amartya-sen-and-the-call-he-issues.md", 189, 195, "../BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md"),
    3789: ("3789-the-cruelty-of-taking-back-even-what-was-given.md", 196, 202, "../BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md"),
    3790: ("3790-august-8-let-the-whole-world-marvel-at-the-demonstration.md", 203, 210, "../BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md"),
    3791: ("3791-heartfelt-greetings-to-the-islamic-community.md", 211, 217, "../BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md"),
    3792: ("3792-the-food-bill-our-position.md", 218, 225, "../BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md"),
    3793: ("3793-will-the-state-government-refuse-what-the-union-government-gives.md", 226, 233, "../BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md"),
    3794: ("3794-an-independence-day-speech-that-forgot-periyar-and-kamarajar.md", 234, 241, "../BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md"),
    3795: ("3795-will-india-at-least-now-understand-sri-lanka.md", 242, 248, "../BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md"),
    3796: ("3796-womens-advancement-then-and-now.md", 249, 255, "../BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md"),
    3797: ("3797-the-day-of-bidding-them-farewell-is-not-far-away.md", 256, 262, "../BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md"),
    3798: ("3798-let-us-find-a-solution-in-mother-indiras-way.md", 263, 269, "../BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md"),
    3799: ("3799-india-will-triumph-in-this-trial-too.md", 270, 276, "../BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md"),
    3800: ("3800-the-food-security-act-gain-or-loss.md", 277, 284, "../BILINGUAL_ALIGNMENT_REVIEW_3800.md"),
}

def norm(text):
    return "\n".join(line.rstrip() for line in text.rstrip().splitlines()) + "\n"

for no, (filename, start, end, report) in letters.items():
    path = letters_dir / filename
    text = path.read_text()
    if 'translation_status: "source-checked"' not in text:
        raise SystemExit(f"{no}: expected source-checked status missing")
    text = text.replace('translation_status: "source-checked"', 'translation_status: "verified"', 1)
    anchor = 'translation_method: "thought-preserving, non-literary"\n'
    if anchor not in text:
        raise SystemExit(f"{no}: translation-method anchor missing")
    text = text.replace(anchor, anchor + 'bilingual_alignment_status: "verified"\n' + f'bilingual_alignment_report: "{report}"\n', 1)
    if no == 3785:
        old = 'the Left, the Samajwadi Party and the Bahujan Samaj Party—apart from the parties of the National Democratic Alliance.'
        new = 'the Left, the Samajwadi Party and the Bahujan Samaj Party—excluding the parties of the National Democratic Alliance.'
        if old not in text:
            raise SystemExit('3785: clarification source wording missing')
        text = text.replace(old, new, 1)
    path.write_text(text)

for name, content in reports.items():
    (base / name).write_text(content)

index_path = base / "README.md"
index = index_path.read_text()
for no in letters:
    lines = index.splitlines()
    changed = False
    for i, line in enumerate(lines):
        if line.startswith(f"| [{no}]"):
            if not line.endswith("| source-checked |"):
                raise SystemExit(f"{no}: unexpected index status")
            lines[i] = line[:-len("| source-checked |")] + "| verified |"
            changed = True
            break
    if not changed:
        raise SystemExit(f"{no}: index row missing")
    index = "\n".join(lines) + ("\n" if index.endswith("\n") else "")
addition = """- Letters **3785–3789**: substantive Tamil–English alignment completed; five files verified, with one targeted English clarification and no Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md`](BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md)
- Letters **3790–3794**: substantive Tamil–English alignment completed; five files verified with no English or Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md`](BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md)
- Letters **3795–3799**: substantive Tamil–English alignment completed; five files verified with no English or Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md`](BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md)
- Letter **3800**: substantive Tamil–English alignment completed; one file verified with no English or Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3800.md`](BILINGUAL_ALIGNMENT_REVIEW_3800.md)

"""
anchor = "## Translation policy\n"
if anchor not in index:
    raise SystemExit("English index translation-policy anchor missing")
index_path.write_text(index.replace(anchor, addition + anchor, 1))

progress_path = base / "PROGRESS.md"
progress = progress_path.read_text()
replacements = [
    ("  - [ ] Letters 3785–3789", "  - [x] Letters 3785–3789 verified"),
    ("  - [ ] Letters 3790–3794", "  - [x] Letters 3790–3794 verified"),
    ("  - [ ] Letters 3795–3799", "  - [x] Letters 3795–3799 verified"),
    ("  - [ ] Letters 3800–3804", "  - [ ] Letters 3800–3804\n    - [x] Letter 3800 verified\n    - [ ] Letters 3801–3804"),
    ("- Reviewed: **21**", "- Reviewed: **37**"),
    ("- Verified: **21**", "- Verified: **37**"),
    ("Continue the bilingual alignment review with letters **3785–3789**. After all 53 letters are verified, conduct the volume-level English editorial consistency pass and prepare the release report.", "Continue the bilingual alignment review with letters **3801–3804**. After all 53 letters are verified, conduct the volume-level English editorial consistency pass and prepare the release report."),
]
for old, new in replacements:
    if old not in progress:
        raise SystemExit(f"Progress target missing: {old}")
    progress = progress.replace(old, new, 1)
report_add = """- Letters **3785–3789** — [`BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md`](BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md): **5/5 verified**; one targeted English clarification; no Tamil-source changes.
- Letters **3790–3794** — [`BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md`](BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md): **5/5 verified**; no English or Tamil-source changes.
- Letters **3795–3799** — [`BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md`](BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md): **5/5 verified**; no English or Tamil-source changes.
- Letter **3800** — [`BILINGUAL_ALIGNMENT_REVIEW_3800.md`](BILINGUAL_ALIGNMENT_REVIEW_3800.md): **1/1 verified**; no English or Tamil-source changes.

"""
counts_anchor = "## Counts\n"
if counts_anchor not in progress:
    raise SystemExit("Progress counts anchor missing")
progress_path.write_text(progress.replace(counts_anchor, report_add + counts_anchor, 1))

volume_path = root / "volumes" / "volume-49" / "README.md"
volume = volume_path.read_text()
old = '- Bilingual alignment review is complete through letter **3784**: **21 verified**, **32 awaiting alignment review**. See the [review reports](translations/en/README.md#bilingual-alignment-reviews).\n- Next alignment batch: letters **3785–3789**.'
new = '- Bilingual alignment review is complete through letter **3800**: **37 verified**, **16 awaiting alignment review**. See the [review reports](translations/en/README.md#bilingual-alignment-reviews).\n- Next alignment batch: letters **3801–3804**.'
if old not in volume:
    raise SystemExit("Volume README status target missing")
volume_path.write_text(volume.replace(old, new, 1))

for no, (filename, start, end, report) in letters.items():
    text = (letters_dir / filename).read_text()
    for needle in ['translation_status: "verified"', 'bilingual_alignment_status: "verified"', f'bilingual_alignment_report: "{report}"', '## Original Tamil — மூலத் தமிழ்\n\n']:
        if needle not in text:
            raise SystemExit(f"{no}: missing {needle}")
    if text.count('<!-- Source PDF page ') != end - start + 1:
        raise SystemExit(f"{no}: wrong source-marker count")
    if '\ufffd' in text:
        raise SystemExit(f"{no}: replacement character found")
    original = text.split('## Original Tamil — மூலத் தமிழ்\n\n', 1)[1]
    expected_parts = []
    for pageno in range(start, end + 1):
        source = (root / 'volumes' / 'volume-49' / 'pages' / f'page-{pageno:03d}.md').read_text()
        body = source.split('---', 2)[2].lstrip('\n').rstrip()
        expected_parts.append(f'<!-- Source PDF page {pageno:03d} -->\n\n{body}')
    marker = f'<!-- Source PDF page {start:03d} -->'
    actual_pages = original[original.index(marker):]
    expected = '\n\n'.join(expected_parts) + '\n'
    if norm(actual_pages) != norm(expected):
        raise SystemExit(f"{no}: Tamil source differs from canonical pages")

t3785 = (letters_dir / letters[3785][0]).read_text()
if '—excluding the parties of the National Democratic Alliance.' not in t3785 or '—apart from the parties of the National Democratic Alliance.' in t3785:
    raise SystemExit("3785: NDA-exclusion clarification validation failed")

report_checks = {
    'BILINGUAL_ALIGNMENT_REVIEW_3785_3789.md': ['Letters reviewed: **3785–3789**', 'Letters completed in this batch: **5/5**', 'Targeted English corrections: **1**', 'Canonical Tamil changes: **0**'],
    'BILINGUAL_ALIGNMENT_REVIEW_3790_3794.md': ['Letters reviewed: **3790–3794**', 'Letters completed in this batch: **5/5**', 'Targeted English corrections: **0**', 'Canonical Tamil changes: **0**'],
    'BILINGUAL_ALIGNMENT_REVIEW_3795_3799.md': ['Letters reviewed: **3795–3799**', 'Letters completed in this batch: **5/5**', 'Targeted English corrections: **0**', 'Canonical Tamil changes: **0**'],
    'BILINGUAL_ALIGNMENT_REVIEW_3800.md': ['Letter reviewed: **3800**', 'Letters completed in this batch: **1/1**', 'Targeted English corrections: **0**', 'Canonical Tamil changes: **0**'],
}
for name, needles in report_checks.items():
    text = (base / name).read_text()
    for needle in needles:
        if needle not in text:
            raise SystemExit(f"{name}: missing {needle}")

index = index_path.read_text()
for no in letters:
    row = next((line for line in index.splitlines() if line.startswith(f"| [{no}]")), None)
    if not row or not row.endswith("| verified |"):
        raise SystemExit(f"{no}: index status not verified")
if sum(1 for line in index.splitlines() if line.endswith("| verified |")) != 37:
    raise SystemExit("English index does not have exactly 37 verified rows")

progress = progress_path.read_text()
for needle in ['- [x] Letters 3785–3789 verified', '- [x] Letters 3790–3794 verified', '- [x] Letters 3795–3799 verified', '- [x] Letter 3800 verified', '- [ ] Letters 3801–3804', '- Reviewed: **37**', '- Verified: **37**', 'letters **3801–3804**']:
    if needle not in progress:
        raise SystemExit(f"Progress validation failed: {needle}")
volume = volume_path.read_text()
for needle in ['through letter **3800**', '**37 verified**', '**16 awaiting alignment review**', 'letters **3801–3804**']:
    if needle not in volume:
        raise SystemExit(f"Volume README validation failed: {needle}")

staging = root / '.github' / 'v49-review-3785-3800'
if staging.exists():
    shutil.rmtree(staging)
for workflow in [root / '.github/workflows/export-v49-review-3785-3800.yml', root / '.github/workflows/finalize-v49-review-3785-3800.yml']:
    if workflow.exists():
        workflow.unlink()

print('Validated bilingual alignment review for letters 3785-3800.')
