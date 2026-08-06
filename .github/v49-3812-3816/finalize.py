from pathlib import Path
import base64, bz2, hashlib, json, re, shutil

root = Path.cwd()
staging = root / '.github' / 'v49-3812-3816'
parts = sorted(staging.glob('payload.part*'))
if len(parts) != 7:
    raise SystemExit(f'Expected 7 payload parts, found {len(parts)}')
encoded = ''.join(p.read_text().strip() for p in parts)
compressed = base64.b64decode(encoded)
if hashlib.sha256(compressed).hexdigest() != '5438af4b187bef987bf782a84340025aacfa5ca5dcc5f9d09e5c8f3c5e51be83':
    raise SystemExit('Compressed payload SHA-256 mismatch')
body_json = bz2.decompress(compressed)
if hashlib.sha256(body_json).hexdigest() != '0f6a1bc998b7eafe5bedae99fcaaf909d18410691eb0c4bfc878981dc54f9e65':
    raise SystemExit('Body payload SHA-256 mismatch')
bodies = json.loads(body_json.decode('utf-8'))

translator_note = """> **Translator’s note**
>
> This translation is intended to carry Kalaignar's voice into clear, contemporary English rather than recast the letter as literary or academic prose. It preserves the source's argument, political directness, rhetorical questions, repetition, irony, factual detail, and paragraph order. Names, dates, figures, quotations, and intentional English expressions are retained. Where Tamil idiom cannot be reproduced literally without sounding unnatural, the English follows its sense and rhetorical force without adding claims absent from the source. The original Tamil is reproduced in full below the translation and remains the authoritative text. `Udanpirappē` is retained in Tamil transliteration rather than flattened into “brother,” “sister,” or “comrade.” Literally evoking “one born alongside me,” Kalaignar uses it as a distinctive address of shared identity, equality, affection, and solidarity within the movement.
"""

letters = {
    3812: {
        'tamil_title': 'அழைக்காமல் பலரையும், அழைத்துப் பலரையும்?',
        'english_title': 'Many Left Uninvited—and Many “Honoured” after Being Invited?',
        'date_iso': '2013-09-28', 'date_long': '28 September 2013',
        'pdf_start': 365, 'pdf_end': 374, 'printed_start': 364, 'printed_end': 373,
        'chapter': '3812-azhaikkaamal-palaraiyum-azhaiththup-palaraiyum.md',
        'filename': '3812-many-left-uninvited-and-many-honoured-after-being-invited.md',
        'notes': [
            'Press reports and attributed comments are translated as printed and remain claims made in the source; they have not been independently reconciled or adjudicated.',
            'The Pattukkottai Kalyanasundaram song passage is rendered for meaning and rhetorical force rather than metre.',
            'The source terms `protocol`, “Fourth Estate,” publication names, film titles and movement/cinema honorifics are retained where their historical texture matters.',
        ],
    },
    3813: {
        'tamil_title': 'எத்தனை சாமிக்கண்ணுகள் வளர்த்த கழகமிது!',
        'english_title': 'This Is the DMK Nurtured by So Many Samikkannus!',
        'date_iso': '2013-09-30', 'date_long': '30 September 2013',
        'pdf_start': 375, 'pdf_end': 379, 'printed_start': 374, 'printed_end': 378,
        'chapter': '3813-eththanai-saamikkannugal-valarththa-kazhagamithu.md',
        'filename': '3813-this-is-the-dmk-nurtured-by-so-many-samikkannus.md',
        'notes': [
            'Samikkannu’s written account is preserved as a first-person block quotation.',
            'Community descriptions, family details and the account of the 2009 fire are translated exactly as presented in the source, without outside supplementation.',
            'Established movement honorifics such as `Perasiriyar` and the banyan-tree image are retained rather than flattened into generic institutional prose.',
        ],
    },
    3814: {
        'tamil_title': '“மெஜாரிட்டி” ஆட்சி என்றால் எதுவும் செய்யலாமோ?',
        'english_title': 'Does a “Majority” Government Mean It Can Do Anything?',
        'date_iso': '2013-10-08', 'date_long': '8 October 2013',
        'pdf_start': 380, 'pdf_end': 387, 'printed_start': 379, 'printed_end': 386,
        'chapter': '3814-mejaarity-aatchi-endraal-ethuvum-seyyalaamo.md',
        'filename': '3814-does-a-majority-government-mean-it-can-do-anything.md',
        'notes': [
            'Crime statistics, legal allegations, promotion disputes and the case chronology are translated as presented in the source and are not independently adjudicated here.',
            'The English rule names `Tamil Nadu Police Service Rules` and `Tamil Nadu Police Subordinate Service Rules` remain exactly as printed in the authoritative Tamil section.',
            'Administrative ranks and Indian legal terms such as writ petition, writ appeal and contempt petition are rendered in their established English forms.',
        ],
    },
    3815: {
        'tamil_title': 'ஊழலைத் தவிர வேறு எதுவும் உயரப் போவதில்லை!',
        'english_title': 'Nothing but Corruption Is Going to Rise!',
        'date_iso': '2013-10-09', 'date_long': '9 October 2013',
        'pdf_start': 388, 'pdf_end': 393, 'printed_start': 387, 'printed_end': 392,
        'chapter': '3815-oozhalai-thavira-veru-ethuvum-uyarap-povathillai.md',
        'filename': '3815-nothing-but-corruption-is-going-to-rise.md',
        'notes': [
            'Paddy prices, production-cost calculations, cultivation areas, beneficiary and loan figures are translated source-exactly without numerical reconciliation.',
            'The verse attributed to Avvai Piratti is rendered for sense and for the concluding rhetorical contrast, not as a metrical literary translation.',
            'Agricultural and scheme names are kept in familiar Indian English where a generic substitute would erase the source context.',
        ],
    },
    3816: {
        'tamil_title': 'இனியும் தமிழினம் ஏமாறத் தயாராக இல்லை!',
        'english_title': 'The Tamil People Are No Longer Ready to Be Deceived!',
        'date_iso': '2013-10-10', 'date_long': '10 October 2013',
        'pdf_start': 394, 'pdf_end': 401, 'printed_start': 393, 'printed_end': 400,
        'chapter': '3816-iniyum-thamizhinam-emaara-thayaaraaga-illai.md',
        'filename': '3816-the-tamil-people-are-no-longer-ready-to-be-deceived.md',
        'notes': [
            'Institutional titles, announced project values, dates and financial figures are translated as printed and are not reconciled with later records.',
            'The source’s achievement list is preserved as a list; its argumentative framing and repeated rhetorical questions remain Kalaignar’s own.',
            'Terms including Tamil Thai Vazhthu, the five Tamil landscapes, Tolkāppiya Poonga and the Central Institute of Classical Tamil retain their historical and cultural specificity.',
        ],
    },
}

def page_body(p: int) -> str:
    text = (root / 'volumes' / 'volume-49' / 'pages' / f'page-{p}.md').read_text()
    parts = text.split('---', 2)
    if len(parts) != 3:
        raise SystemExit(f'Unexpected page format: {p}')
    return parts[2].lstrip('\n').rstrip()

letters_dir = root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'letters'
letters_dir.mkdir(parents=True, exist_ok=True)
for no, d in letters.items():
    body = bodies[str(no)].strip()
    if not body.endswith('**M. K.**'):
        raise SystemExit(f'{no}: unexpected body ending')
    body += f'\n{d["date_long"]}'
    original = '\n\n'.join(
        f'<!-- Source PDF page {p} -->\n\n{page_body(p)}'
        for p in range(d['pdf_start'], d['pdf_end'] + 1)
    ) + '\n'
    notes = '\n'.join(f'- {note}' for note in d['notes'])
    tamil_yaml = d['tamil_title'].replace('"', '\\"')
    english_yaml = d['english_title'].replace('"', '\\"')
    content = f'''---
volume: 49
letter_number: {no}
tamil_title: "{tamil_yaml}"
english_title: "{english_yaml}"
date: {d['date_iso']}
source_pdf_page_start: {d['pdf_start']}
source_pdf_page_end: {d['pdf_end']}
source_printed_page_start: {d['printed_start']}
source_printed_page_end: {d['printed_end']}
translation_status: "source-checked"
translation_method: "thought-preserving, non-literary"
source_textual_fidelity_audit: "visual-scan-verified"
---

# {no}. {d['english_title']}

{translator_note}
**Tamil source:** [Letter {no}](../../../chapters/{d['chapter']})

**Source pages:** [PDF {d['pdf_start']}](../../../pages/page-{d['pdf_start']}.md)–[PDF {d['pdf_end']}](../../../pages/page-{d['pdf_end']}.md)

**Textual-fidelity audit:** Complete — every canonical Tamil Markdown page from PDF {d['pdf_start']} through PDF {d['pdf_end']} was visually compared with its scan before translation; no canonical correction was required.

**Date:** {d['date_long']}

{body}

## Source notes

{notes}

## Original Tamil — மூலத் தமிழ்

{original}'''
    (letters_dir / d['filename']).write_text(content)

# Audit report.
audit = """# Textual-Fidelity Audit — Letters 3812–3816

## Scope

- Volume: **49**
- Letters: **3812–3816**
- Canonical Tamil Markdown pages: **PDF 365–401**
- Total letter pages visually compared with scans: **37/37**
- PDF page **402** is the back cover and is outside these letters.
- Method: every canonical letter page was compared with its corresponding rendered PDF scan before translation. Titles, letter numbers, paragraph order, quoted reports, verse passages, lists, legal and institutional English expressions, figures, punctuation, signatures, dates and page boundaries were checked.

## Result

- All **37** letter pages were inspected.
- No paragraph or passage was missing.
- The canonical Markdown matched the visible scans closely enough that **no canonical correction was required** in this batch.
- Printed irregularities and historical source forms were retained rather than silently modernised or repaired.

## Source-exact features retained

- PDF page 367 retains the printed space before the semicolon in `அதுமாத்திரமல்ல ;`.
- PDF page 373 retains the printed space before the semicolon in `பாவம் ;`.
- PDF page 374 preserves the closing ironic form `“பெருமைப்படுத்தி”(?)`.
- PDF page 376 preserves the printed date form `27-9-2013 ந்தேதி`.
- PDF page 383 retains the original English legal names `Tamil Nadu Police Service Rules` and `Tamil Nadu Police Subordinate Service Rules`.
- PDF page 393 preserves the printed question mark at the end of the Avvai verse: `குடி உயர கோன் உயரும்?`.
- PDF page 398 retains the source’s visibly irregular closing quotation mark in the reference to `தமிழ்த் தாய்ப் பூங்கா“`.
- PDF page 399 preserves the achievement sequence as separate unbulleted printed lines; the English renders it as a list for readable structural equivalence.
- PDF page 400 retains the English loanword `“ஸ்டிக்கர்”`.
- Press quotations, crime reports, legal allegations, project values, agricultural figures, beneficiary counts, dates and financial amounts are translated as presented, without outside fact-correction or numerical reconciliation.

## Translation assembly

Each English file contains:

1. the standard Translator’s note;
2. a complete thought-preserving English translation;
3. letter-specific source notes; and
4. the full canonical Tamil text, divided by original PDF page.

This audit establishes **source-checked** status for letters **3812–3816** and completes the source-checked first translation pass for all **53** letters in Volume 49. Full bilingual line-by-line editorial review remains a later, separate stage.
"""
(root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'TEXTUAL_FIDELITY_AUDIT_3812_3816.md').write_text(audit)

# Root README.
path = root / 'README.md'
text = path.read_text()
text = text.replace('| 49 | 01.06.2013–10.10.2013 | 402 | 1–402 | 53 (கடிதங்கள் 3764–3816) | 48 / 53 (3764–3811) |',
                    '| 49 | 01.06.2013–10.10.2013 | 402 | 1–402 | 53 (கடிதங்கள் 3764–3816) | 53 / 53 (3764–3816) |')
path.write_text(text)

# Volume README.
path = root / 'volumes' / 'volume-49' / 'README.md'
text = path.read_text()
text = text.replace('Letters **3764–3811** have been fully translated and source-checked against Tamil PDF pages **24–364**.',
                    'Letters **3764–3816** have been fully translated and source-checked against Tamil PDF pages **24–401**.')
anchor = '- Before translating letters **3805–3811**, every canonical Markdown page from PDF **314–364** was visually compared with its scan; all **51 pages matched**, and no canonical correction was required.\n'
if anchor not in text:
    raise SystemExit('Volume README insertion anchor missing')
text = text.replace(anchor, anchor + '- Before translating letters **3812–3816**, every canonical Markdown page from PDF **365–401** was visually compared with its scan; all **37 letter pages matched**, and no canonical correction was required. PDF page **402** is the back cover and falls outside the letters.\n')
text = text.replace('- Final five-letter iteration: **3812–3816**.', '- All **53** letters are now translated and source-checked. The next stage is full bilingual alignment review, followed by the volume-level release report.')
path.write_text(text)

# Progress.
path = root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'PROGRESS.md'
text = path.read_text()
text = text.replace('- [ ] Letters 3812–3816', '- [x] Letters 3812–3816 translated and source-checked')
anchor = '- Canonical pages **314–364** visually compared against their scans: **51/51 matched**.\n  - [`TEXTUAL_FIDELITY_AUDIT_3805_3811.md`](TEXTUAL_FIDELITY_AUDIT_3805_3811.md)\n  - No canonical correction was required; visibly printed irregularities were retained source-exact.\n'
if anchor not in text:
    raise SystemExit('Progress insertion anchor missing')
text = text.replace(anchor, anchor + '- Canonical pages **365–401** visually compared against their scans: **37/37 matched**.\n  - [`TEXTUAL_FIDELITY_AUDIT_3812_3816.md`](TEXTUAL_FIDELITY_AUDIT_3812_3816.md)\n  - No canonical correction was required; visibly printed irregularities were retained source-exact. PDF page 402 is the back cover.\n')
text = text.replace('- Translated: **48**', '- Translated: **53**').replace('- Source-checked: **48**', '- Source-checked: **53**')
text = re.sub(r'## Next iteration\n\n.*\Z', '## Next stage\n\nConduct the full bilingual alignment review across letters **3764–3816**, followed by the volume-level English release report.\n', text, flags=re.S)
path.write_text(text)

# English index.
path = root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'README.md'
text = path.read_text()
rows = '\n'.join(f"| [{no}](letters/{d['filename']}) | {d['english_title']} | {d['date_long']} | source-checked |" for no, d in letters.items())
if '| 3812–3816 | — | — | pending |' not in text:
    raise SystemExit('English index pending row missing')
text = text.replace('| 3812–3816 | — | — | pending |', rows)
anchor = '- Letters 3805–3811: **51/51 pages matched; no canonical correction required** — [`TEXTUAL_FIDELITY_AUDIT_3805_3811.md`](TEXTUAL_FIDELITY_AUDIT_3805_3811.md)\n'
if anchor not in text:
    raise SystemExit('English index audit anchor missing')
text = text.replace(anchor, anchor + '- Letters 3812–3816: **37/37 letter pages matched; no canonical correction required** — [`TEXTUAL_FIDELITY_AUDIT_3812_3816.md`](TEXTUAL_FIDELITY_AUDIT_3812_3816.md)\n')
path.write_text(text)

# Glossary.
path = root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'GLOSSARY.md'
text = path.read_text().rstrip() + '\n'
new_rows = [
    '| நான்காவது எஸ்டேட் | **Fourth Estate** | approved | Established democratic metaphor for the press; retained in letter 3812. |',
    '| பணிமூப்பு / சீனியாரிட்டி | **seniority** | approved | Administrative ordering by length of service, especially in promotion disputes. |',
    '| ரிட் / ரிட் அப்பீல் | **writ / writ appeal** | approved | Established Indian legal terms retained in the police-promotion litigation. |',
    '| உழவர் சந்தை | **Uzhavar Sandhai** / **farmers’ market** | approved | Direct farmer-to-consumer market scheme; Tamil scheme name may be retained on first reference. |',
    '| ஐந்திணை | **the five Tamil landscapes** | approved | Kurinji, mullai, marutham, neithal and paalai; ecological-poetic classification used in Sangam literature. |',
    '| தமிழ்த்தாய் வாழ்த்து | **Tamil Thai Vazhthu** | approved | Official invocation to Mother Tamil; title retained rather than reduced to a generic “Tamil anthem”. |',
    '| வட்டெழுத்து | **Vatteluttu** | approved | Historical rounded script used for Tamil and related languages. |',
]
for row in new_rows:
    key = row.split('|')[1].strip()
    if key not in text:
        text += row + '\n'
path.write_text(text)

# Remove every one-use workflow and staging artifact from the final tree.
for path in [
    root / '.github' / 'workflows' / 'export-v49-3812-3816.yml',
    root / '.github' / 'workflows' / 'finalize-v49-3812-3816.yml',
]:
    if path.exists():
        path.unlink()
if staging.exists():
    shutil.rmtree(staging)

# Final validation.
def normalise(text: str) -> str:
    return '\n'.join(line.rstrip() for line in text.rstrip().splitlines()) + '\n'
for no, d in letters.items():
    path = letters_dir / d['filename']
    text = path.read_text()
    if text.count('<!-- Source PDF page ') != d['pdf_end'] - d['pdf_start'] + 1:
        raise SystemExit(f'{no}: wrong source marker count')
    if '\ufffd' in text or 'translation_status: "source-checked"' not in text:
        raise SystemExit(f'{no}: invalid translation file')
    original = text.split('## Original Tamil — மூலத் தமிழ்\n\n', 1)[1]
    expected = '\n\n'.join(f'<!-- Source PDF page {p} -->\n\n{page_body(p)}' for p in range(d['pdf_start'], d['pdf_end'] + 1)) + '\n'
    if normalise(original) != normalise(expected):
        raise SystemExit(f'{no}: appended Tamil mismatch')
progress = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'PROGRESS.md').read_text()
for needle in ['Translated: **53**', 'Source-checked: **53**', 'full bilingual alignment review']:
    if needle.lower() not in progress.lower():
        raise SystemExit(f'Progress validation failed: {needle}')
index = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'README.md').read_text()
for no in letters:
    if f'| [{no}]' not in index:
        raise SystemExit(f'Index validation failed for {no}')
audit_text = (root / 'volumes' / 'volume-49' / 'translations' / 'en' / 'TEXTUAL_FIDELITY_AUDIT_3812_3816.md').read_text()
for needle in ['37/37', 'no canonical correction was required', 'all **53** letters']:
    if needle.lower() not in audit_text.lower():
        raise SystemExit(f'Audit validation failed: {needle}')
if '53 / 53 (3764–3816)' not in (root / 'README.md').read_text():
    raise SystemExit('Root README completion count missing')
if not (root / 'volumes' / 'volume-49' / 'pages' / 'page-402.md').exists():
    raise SystemExit('Back cover page unexpectedly missing')
print('Validated final letters 3812-3816 and completed all 53 Volume 49 translations.')
