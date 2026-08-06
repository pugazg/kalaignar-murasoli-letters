from pathlib import Path
import shutil

root=Path.cwd()
base=root/'volumes/volume-49/translations/en'
letters_dir=base/'letters'
letters={
3801:('3801-a-chief-minister-bent-on-holding-closing-ceremonies.md',285,291,'../BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md'),
3802:('3802-the-hogenakkal-project-and-the-muthialpet-police-station.md',292,298,'../BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md'),
3803:('3803-the-great-schemes-for-women-under-the-dmk-government.md',299,306,'../BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md'),
3804:('3804-let-us-carry-forward-the-eradication-of-superstition.md',307,313,'../BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md'),
3805:('3805-only-a-referendum-can-give-eelam-tamils-a-new-life.md',314,319,'../BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md'),
3806:('3806-justice-will-prevail-it-certainly-will.md',320,327,'../BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md'),
3807:('3807-bearing-the-sword-of-righteous-struggle-let-us-continue-on-periyars-and-annas-path.md',328,334,'../BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md'),
3808:('3808-tamil-nadu-in-the-terrifying-grip-of-murder.md',335,341,'../BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md'),
3809:('3809-you-are-lamps-to-the-home-and-workers-for-the-nation.md',342,349,'../BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md'),
3810:('3810-a-dream-seen-in-the-glare-of-publicity.md',350,357,'../BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md'),
3811:('3811-they-say-ghee-drips-from-finger-millet-listen-tamils.md',358,364,'../BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md'),
3812:('3812-many-left-uninvited-and-many-honoured-after-being-invited.md',365,374,'../BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md'),
3813:('3813-this-is-the-dmk-nurtured-by-so-many-samikkannus.md',375,379,'../BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md'),
3814:('3814-does-a-majority-government-mean-it-can-do-anything.md',380,387,'../BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md'),
3815:('3815-nothing-but-corruption-is-going-to-rise.md',388,393,'../BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md'),
3816:('3816-the-tamil-people-are-no-longer-ready-to-be-deceived.md',394,401,'../BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md')}

def norm(s): return '\n'.join(x.rstrip() for x in s.rstrip().splitlines())+'\n'
original_tamil={}
for no,(fn,start,end,report) in letters.items():
 p=letters_dir/fn; t=p.read_text()
 if 'translation_status: "source-checked"' not in t: raise SystemExit(f'{no}: expected source-checked status missing')
 original_tamil[no]=t.split('## Original Tamil — மூலத் தமிழ்\n\n',1)[1]
 t=t.replace('translation_status: "source-checked"','translation_status: "verified"',1)
 needle='translation_method: "thought-preserving, non-literary"\n'
 t=t.replace(needle,needle+'bilingual_alignment_status: "verified"\n'+f'bilingual_alignment_report: "{report}"\n',1)
 p.write_text(t)
p=letters_dir/letters[3805][0]; t=p.read_text(); old='It was unacceptable, she said, that human-rights activists who had spoken to her during the visit were later harassed by the police and military. People were increasingly being watched and intimidated, critics of the Government were attacked, and the affected communities needed both reconciliation and the means to live with dignity.'; new='It was unacceptable, she said, that human-rights activists who had spoken to her during the visit were later harassed by the police and military. Sri Lanka appeared to be in a very bad state. People were increasingly being watched and intimidated, critics of the Government were attacked, and the affected communities needed both reconciliation and the means to live with dignity.'
if old not in t: raise SystemExit('3805 correction target missing')
p.write_text(t.replace(old,new,1))
p=letters_dir/letters[3809][0]; t=p.read_text(); old='district, city, union, town, area and பேரூர் Youth Wing organisers and deputy organisers'; new='district, city, union, town, area and town-panchayat Youth Wing organisers and deputy organisers'
if old not in t: raise SystemExit('3809 correction target missing')
p.write_text(t.replace(old,new,1))
p=letters_dir/letters[3810][0]; t=p.read_text()
if t.count('Kasturirangan')!=2: raise SystemExit('3810 expected two old name forms')
t=t.replace('Kasturirangan','Kasturi Rangaiyan')
needle='- Power-generation figures, costs, investment percentages, project values and attributed statements remain source-exact and are not externally reconciled.\n'
addition='- The Tamil source prints minor spelling and spacing variants of the association president’s name (`கஸ்தூரிரங்கையன்`, `கஸ்தூரி ரங்கையன்`, `கஸ்தூரி ரெங்கையன்`); the English consistently uses **Kasturi Rangaiyan** without altering the authoritative Tamil.\n'
if needle not in t: raise SystemExit('3810 note target missing')
p.write_text(t.replace(needle,needle+addition,1))

reports={
'BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md':'''# Bilingual Alignment Review — Letters 3801–3804

## Scope
- Volume: **49**
- Letters reviewed: **3801–3804**
- Canonical Tamil source range: **PDF 285–313**
- Letters completed in this batch: **4/4**
- Approximate English body reviewed: **5,798 words**
- Status after review: **verified**

## Review method
Each English translation was compared directly with the complete canonical Tamil reproduced in the same bilingual file. The review checked paragraph and argumentative order, newspaper and court quotations, names, dates, project costs, beneficiary and scheme figures, constitutional wording, attribution, irony and rhetorical force. The Tamil pages had already matched their scans; no canonical Tamil page was changed.

## Results by letter
### 3801 — *A Chief Minister Bent on Holding Closing Ceremonies!*
The Maduravoyal–Port elevated-road chronology, NHAI proceedings, protest details, project and land figures, and the catalogue of projects alleged to have been obstructed or closed were aligned. English newspaper passages and legal claims remain visibly attributed and source-exact. No English correction was required.

### 3802 — *The Hogenakkal Project and the Muthialpet Police Station!*
The Hogenakkal project chronology, DMK-period implementation account, completion claims, video-conference inauguration and the Muthialpet police-station episode were checked in full. Dates, percentages, costs, names and quoted statements retain their source framing. No English correction was required.

### 3803 — *The Great Schemes for Women under the DMK Government!*
The marriage-assistance announcement and the full comparison with DMK schemes for women were aligned for scheme names, eligibility, beneficiary counts, financial totals and sequence. No English correction was required.

### 3804 — *Let Us Carry Forward the Eradication of Superstition!*
The Maharashtra ordinance, Narendra Dabholkar’s murder, the chronology of the anti-superstition campaign, reported incidents and constitutional-duty argument were aligned. The unusual printed constitutional-article form remains documented rather than silently regularised. No English correction was required.

## Outcome
- Complete substantive coverage: **passed**
- Paragraph and argument order: **passed**
- Quotations and attribution: **passed**
- Names, dates, figures and chronology: **passed**
- English files marked `verified`: **4**
- Targeted English corrections: **0**
- Canonical Tamil changes: **0**

The next reviewed group in the final block is **letters 3805–3811**.
''',
'BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md':'''# Bilingual Alignment Review — Letters 3805–3811

## Scope
- Volume: **49**
- Letters reviewed: **3805–3811**
- Canonical Tamil source range: **PDF 314–364**
- Letters completed in this batch: **7/7**
- Approximate English body reviewed: **10,605 words**
- Status after review: **verified**

## Review method
Each English translation was compared directly with the complete canonical Tamil reproduced in the same bilingual file. The review checked paragraph order, United Nations and court statements, political and legal chronology, names, dates, crime and power-generation figures, organisational terminology, quotations, source anomalies, rhetorical questions and responsibility. The Tamil pages had already matched their scans; no canonical Tamil page was changed.

## Results by letter
### 3805 — *Only a Referendum Can Give Eelam Tamils a New Life!*
Navanethem Pillay’s Sri Lanka visit, attributed findings, the UN Human Rights Council timetable and referendum argument were aligned. One omitted source sentence was restored: **“Sri Lanka appeared to be in a very bad state.”** The intentional English statement remains source-exact.

### 3806 — *Justice Will Prevail; It Certainly Will!*
The Bengaluru disproportionate-assets case, prosecutor changes, applications, retirement chronology and attributed motives were aligned without treating allegations as adjudicated fact. No English correction was required.

### 3807 — *Bearing the Sword of Righteous Struggle, Let Us Continue on Periyar's and Anna's Path!*
The Mupperum Vizha anniversaries, Anna’s recollections of Periyar, movement history, invitation passages and final image were checked. No English correction was required.

### 3808 — *Tamil Nadu in the Terrifying Grip of Murder!*
The sequence of reported murders, robberies and other incidents; names, locations, dates and newspaper attributions; and the law-and-order rebuttal were aligned. No English correction was required.

### 3809 — *You Are Lamps to the Home and Workers for the Nation!*
The Youth Wing resolutions, campaign period, organisational responsibilities and district arrangements were aligned. The untranslated term `பேரூர்` was corrected to **town-panchayat** in the English organisational list.

### 3810 — *A Dream Seen in the Glare of Publicity!*
Wind-power figures, purchase prices, association and official statements, solar-project claims and court directions were checked. The English now consistently uses **Kasturi Rangaiyan** for the Tamil source’s three minor printed name variants, which are documented in a note.

### 3811 — *They Say Ghee Drips from Finger Millet; Listen, Tamils!*
The National Integration Council speech, “park of peace” claim, law-and-order incidents, minority-welfare history and concluding metaphor were aligned. No English correction was required.

## Outcome
- Complete substantive coverage: **passed after one restored sentence**
- Paragraph and argument order: **passed**
- Quotations and attribution: **passed**
- Names and terminology: **passed after two corrections**
- Dates, figures and chronology: **passed**
- English files marked `verified`: **7**
- Targeted English corrections: **3**
- Canonical Tamil changes: **0**

The final reviewed group is **letters 3812–3816**.
''',
'BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md':'''# Bilingual Alignment Review — Letters 3812–3816

## Scope
- Volume: **49**
- Letters reviewed: **3812–3816**
- Canonical Tamil source range: **PDF 365–401**
- Letters completed in this batch: **5/5**
- Approximate English body reviewed: **9,295 words**
- Status after review: **verified**

## Review method
Each English translation was compared directly with the complete canonical Tamil reproduced in the same bilingual file. The review checked paragraph and list order, press quotations, names, dates, awards and invitations, police-service and court chronology, agricultural figures, schemes, Tamil institutions, wordplay, sarcasm and political attribution. The Tamil letter pages had already matched their scans; no canonical Tamil page was changed.

## Results by letter
### 3812 — *Many Left Uninvited—and Many “Honoured” after Being Invited?*
The cinema-centenary programme, award order, invitation exclusions, treatment of artists and press commentary were aligned. No English correction was required.

### 3813 — *This Is the DMK Nurtured by So Many Samikkannus!*
Kalaignar’s routine, the meeting with centenarian volunteer Samikkannu, his movement history, family details and concluding tribute were aligned. No English correction was required.

### 3814 — *Does a “Majority” Government Mean It Can Do Anything?*
Crime reports, gutka and TASMAC criticism, STF promotions, Government Orders, writ proceedings, contempt allegations, vacancies and the fourteen-DSP case were checked in full. No English correction was required.

### 3815 — *Nothing but Corruption Is Going to Rise!*
Paddy and sugarcane prices, crop-loan totals, welfare-board assistance, farmers’ demands, irrigation conditions and comparisons were aligned. The Avvai verse and its rhetorical application remain intact. No English correction was required.

### 3816 — *The Tamil People Are No Longer Ready to Be Deceived!*
The Tirukkural gallery, Tamil cultural centre, Tolkāppiyar chair, Tamil Thai statue and park announcements were aligned with the earlier announcements and initiatives cited. The full achievements list and repeated questions were checked. No English correction was required.

## Outcome
- Complete substantive coverage: **passed**
- Paragraph, quotation and list order: **passed**
- Names, dates, figures and legal chronology: **passed**
- Source anomalies and attribution: **passed**
- English files marked `verified`: **5**
- Targeted English corrections: **0**
- Canonical Tamil changes: **0**

With this group, the bilingual alignment review is complete for all **53 letters (3764–3816)** in Volume 49.
'''}
for name,text in reports.items(): (base/name).write_text(text)
p=base/'README.md'; t=p.read_text(); lines=t.splitlines()
for no in range(3801,3817):
 for i,line in enumerate(lines):
  if line.startswith(f'| [{no}]'):
   if not line.endswith('| source-checked |'): raise SystemExit(f'{no}: index status unexpected')
   lines[i]=line[:-len('| source-checked |')]+'| verified |'; break
 else: raise SystemExit(f'{no}: index row missing')
t='\n'.join(lines)+'\n'
anchor='- Letter **3800**: substantive Tamil–English alignment completed; one file verified with no English or Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3800.md`](BILINGUAL_ALIGNMENT_REVIEW_3800.md)\n'
addition='''- Letters **3801–3804**: substantive Tamil–English alignment completed; four files verified with no English or Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md`](BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md)
- Letters **3805–3811**: substantive Tamil–English alignment completed; seven files verified with three targeted English corrections and no Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md`](BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md)
- Letters **3812–3816**: substantive Tamil–English alignment completed; five files verified with no English or Tamil-source changes — [`BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md`](BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md)

All **53 letters** in Volume 49 have completed substantive bilingual alignment and are marked **verified**.
'''
if anchor not in t: raise SystemExit('index anchor missing')
p.write_text(t.replace(anchor,anchor+addition,1))
p=base/'PROGRESS.md'; t=p.read_text().replace('- [ ] Full bilingual alignment review','- [x] Full bilingual alignment review',1)
old='  - [ ] Letters 3800–3804\n    - [x] Letter 3800 verified\n    - [ ] Letters 3801–3804\n  - [ ] Letters 3805–3811\n  - [ ] Letters 3812–3816'
new='  - [x] Letters 3800–3804 verified\n  - [x] Letters 3805–3811 verified\n  - [x] Letters 3812–3816 verified'
if old not in t: raise SystemExit('progress checklist target missing')
t=t.replace(old,new,1)
anchor='- Letter **3800** — [`BILINGUAL_ALIGNMENT_REVIEW_3800.md`](BILINGUAL_ALIGNMENT_REVIEW_3800.md): **1/1 verified**; no English or Tamil-source changes.\n'
add='''- Letters **3801–3804** — [`BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md`](BILINGUAL_ALIGNMENT_REVIEW_3801_3804.md): **4/4 verified**; no English or Tamil-source changes.
- Letters **3805–3811** — [`BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md`](BILINGUAL_ALIGNMENT_REVIEW_3805_3811.md): **7/7 verified**; three targeted English corrections; no Tamil-source changes.
- Letters **3812–3816** — [`BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md`](BILINGUAL_ALIGNMENT_REVIEW_3812_3816.md): **5/5 verified**; no English or Tamil-source changes.
'''
if anchor not in t: raise SystemExit('progress report anchor missing')
t=t.replace(anchor,anchor+add,1).replace('- Reviewed: **37**','- Reviewed: **53**',1).replace('- Verified: **37**','- Verified: **53**',1)
t=t.replace('Continue the bilingual alignment review with letters **3801–3804**. After all 53 letters are verified, conduct the volume-level English editorial consistency pass and prepare the release report.','The bilingual alignment review is complete for all **53 letters**. Conduct the volume-level English editorial consistency pass and prepare the release report.',1)
p.write_text(t)
p=root/'volumes/volume-49/README.md'; t=p.read_text(); old='- Bilingual alignment review is complete through letter **3800**: **37 verified**, **16 awaiting alignment review**. See the [review reports](translations/en/README.md#bilingual-alignment-reviews).\n- Next alignment batch: letters **3801–3804**.\n'; new='- Bilingual alignment review is complete for letters **3764–3816**: **53 verified**, **0 awaiting alignment review**. See the [review reports](translations/en/README.md#bilingual-alignment-reviews).\n- Next stage: volume-level English editorial consistency pass and release report.\n'
if old not in t: raise SystemExit('volume status target missing')
p.write_text(t.replace(old,new,1))
for no,(fn,start,end,report) in letters.items():
 t=(letters_dir/fn).read_text()
 if t.split('## Original Tamil — மூலத் தமிழ்\n\n',1)[1] != original_tamil[no]: raise SystemExit(f'{no}: Tamil section changed')
 if t.count('<!-- Source PDF page ') != end-start+1: raise SystemExit(f'{no}: marker count')
 expected=[]
 for pg in range(start,end+1):
  s=(root/f'volumes/volume-49/pages/page-{pg:03d}.md').read_text().split('---',2)[2].lstrip('\n').rstrip()
  expected.append(f'<!-- Source PDF page {pg:03d} -->\n\n{s}')
 actual=t.split('## Original Tamil — மூலத் தமிழ்\n\n',1)[1]
 marker=f'<!-- Source PDF page {start:03d} -->'; actual=actual[actual.index(marker):]
 if norm(actual)!=norm('\n\n'.join(expected)+'\n'): raise SystemExit(f'{no}: canonical mismatch')
 for n in ['translation_status: "verified"','bilingual_alignment_status: "verified"',f'bilingual_alignment_report: "{report}"']:
  if n not in t: raise SystemExit(f'{no}: metadata missing')
if 'Sri Lanka appeared to be in a very bad state.' not in (letters_dir/letters[3805][0]).read_text(): raise SystemExit('3805 failed')
if 'town-panchayat Youth Wing organisers' not in (letters_dir/letters[3809][0]).read_text(): raise SystemExit('3809 failed')
body=(letters_dir/letters[3810][0]).read_text().split('## Source notes',1)[0]
if body.count('Kasturi Rangaiyan')!=3 or 'Kasturirangan' in body: raise SystemExit('3810 failed')
progress=(base/'PROGRESS.md').read_text()
for n in ['- [x] Full bilingual alignment review','- Reviewed: **53**','- Verified: **53**','volume-level English editorial consistency pass']:
 if n not in progress: raise SystemExit(f'progress missing {n}')
staging=root/'.github/v49-review-3801-3816'
if staging.exists(): shutil.rmtree(staging)
print('Validated final bilingual alignment review for letters 3801-3816; all 53 letters verified.')
