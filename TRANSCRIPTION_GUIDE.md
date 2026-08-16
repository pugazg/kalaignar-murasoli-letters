# மின்னாக்க வழிமுறை

இந்தச் சுருக்க வழிமுறையுடன் [Volume Transcription Batching Policy](VOLUME_TRANSCRIPTION_BATCHING_POLICY.md) கட்டாயமாகப் பின்பற்றப்பட வேண்டும். Batch அளவு குறித்து வேறுபாடு இருந்தால், அந்த policy முன்னுரிமை பெறும்.

1. **ஒரு PDF பக்கம் = ஒரு Markdown கோப்பு.** கோப்பு பெயர் `page-001.md` போன்ற பூஜ்யம் நிரப்பிய எண்ணாக இருக்கும்.
2. YAML front matter-ல் தொகுதி எண், PDF பக்கம், அச்சுப் பக்கம், பகுதி, கடித எண்/தேதி ஆகியவை பதிவு செய்யப்படும்.
3. மூலத் தமிழின் சொல் வடிவம், நிறுத்தக்குறி, தலைப்பு, மேற்கோள் மற்றும் பத்தி வரிசை இயன்றவரை பாதுகாக்கப்படும்.
4. தெளிவாகத் தெரியாத எழுத்து ஊகிக்கப்படாது. தேவைப்பட்டால் `[தெளிவில்லை]` எனப் பதிவு செய்யப்படும்.
5. மூல நூலில் உள்ள பிழை தானாகச் சரிசெய்யப்படாது. `source_note` அல்லது குறிப்பில் அது சுட்டப்படும்.
6. புகைப்படம், முத்திரை, கையெழுத்து, வெற்றுப் பக்கம் போன்றவை சதுரக் குறிக்குள் உண்மையாகத் தெரியும் அளவுக்கே விவரிக்கப்படும்.
7. `first-pass-reviewed` என்பது உரை பக்கப் படத்துடன் ஒருமுறை ஒப்பிடப்பட்டதைக் குறிக்கும்; இது இறுதி scholarly அல்லது character-by-character verification அல்ல.
8. கடிதம்/அத்தியாயக் கோப்புகள் canonical உரையை நகலெடுக்காமல், சம்பந்தப்பட்ட பக்கக் கோப்புகளைக் காலவரிசையில் இணைக்கும்.
9. ஒவ்வொரு புதிய தொகுதியின் முதல் commit **PDF பக்கங்கள் 001–025** மட்டுமே கொண்டிருக்க வேண்டும்.
10. PDF பக்கம் 25 ஒரு கடிதத்தின் நடுவில் முடிந்தால், அந்த இடத்திலேயே நிறுத்தி `partial` எனத் தெளிவாகப் பதிவு செய்ய வேண்டும்; அடுத்த commit PDF பக்கம் 26-இல் தொடங்கி அதே கடிதத்தை முதலில் முடிக்க வேண்டும்.
11. அந்த interrupted letter முடிந்தபின், இயல்பான transcription iteration என்பது **ஐந்து முழுமையான தொடர்ச்சியான கடிதங்கள் = ஒரு atomic commit** ஆகும்.
12. ஐந்து கடிதங்களும் அவற்றின் verified closing/date page வரை முழுமையாக முடிந்த பின்னரே iteration commit செய்யப்படும்; ஆறாவது கடிதத்தின் ஒரு பகுதியை சேர்க்கக் கூடாது.
13. குறைவான அல்லது அதிகமான letter batch user approval அல்லது policy-ல் குறிப்பிடப்பட்ட documented exception இல்லாமல் செய்யப்படாது.
14. ஒவ்வொரு iteration-லும் புதிய page files மட்டுமல்லாமல் `contents/index.md`, ஐந்து chapter files, `chapters/README.md`, `PROGRESS.md`, `metadata.yml`, `AUDIT.md`, மற்றும் தேவையான volume `README.md` ஆகியவை புதுப்பிக்கப்பட வேண்டும்.
15. ஒவ்வொரு புதிய அல்லது திருத்தப்பட்ட Markdown பக்கமும் commit-க்கு முன் அதன் scan-உடன் visually compared செய்யப்பட வேண்டும். OCR ஒருபோதும் இறுதி ஆதாரம் அல்ல.
16. PDF page boundary-ல் சொல் இரண்டாகப் பிரிந்திருந்தால், canonical page files-ல் அந்தப் பிரிவு அப்படியே பாதுகாக்கப்பட வேண்டும்; அமைதியாக ஒன்றிணைக்கக் கூடாது.
17. Contents title மற்றும் actual letter-start title வேறுபட்டால், இரண்டையும் தத்தம் source-இன்படி பாதுகாத்து வேறுபாட்டைக் குறிப்பிட வேண்டும்.
18. Iteration audit, full-volume structural audit, second visual verification, translation textual-fidelity audit ஆகியவை தனித்தனி நிலைகள்; ஒன்றை மற்றொன்றாகக் குறிக்கக் கூடாது.
19. முழு Tamil volume transcription மற்றும் full-volume audit முடியும் முன் English translation தொடங்கப்படாது. Translation batch தொடங்குவதற்கு முன் அதன் ஒவ்வொரு Tamil page-க்கும் scan-based textual-fidelity audit கட்டாயம்.
20. ஒவ்வொரு commit report-லும் ஐந்து letter numbers/titles, committed PDF/printed range, audit result, commit SHA, மற்றும் exact next PDF page/letter குறிப்பிடப்பட வேண்டும்.
