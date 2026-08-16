#!/usr/bin/env python3
"""Group Volume 1 page JSON into candidate chapter/letter folders.

This local-output adaptation of the Volume 54 letter splitter reads page JSON
directly from the correction stage. It removes running headers and bare page
numbers before reassembling consecutive pages into numbered chapters/letters.

What defines a letter (validated against Volume 54):
  START  a numbered heading — "4016. <title, often wrapping two lines>" —
         followed within a few lines by the salutation "உடன்பிறப்பே,".
         (Volume 54 uses the singular salutation; the serial number is a
         GLOBAL sequence across all 54 volumes, so it makes a durable id.)
         A salutation with no readable number still starts a letter
         (number recorded as null; flagged in the report).
  END    the sign-off block — "அன்புள்ள," / "மு.க." — usually followed by a
         date (dd-mm-yyyy). That trailing date is the letter's date.
  NOISE  running page headers ("தலைவர் கலைஞர் NN", "NN கலைஞரின் கடிதங்கள்"),
         bare page numbers, and table-of-contents pages are stripped/skipped.

Output chapter schema (one folder per heading):
    <output>/<id>_<Tamil heading>/chapter.md
    <output>/<id>_<Tamil heading>/chapter.json
    <output>/<id>_<Tamil heading>/images/page_XXXX.png

The JSON keeps source page ids for audit. The readable Markdown does not include
running page headers or standalone page numbers.

JSON schema:
    { id, collection: "murasoli-letter", volume, number, date | null,
      title: {en, ta}, salutation, pages: [page ids], paragraphs[], ocrStatus }
plus letters index appended into public/data/murasoli/letters-index.json.

Usage:
    python3 group_chapters.py --volume 50 \
        --pages-dir processed/vol50/ocr/03_corrected_v4/text \
        --output processed/vol50/ocr/04_chapters
"""
import argparse, glob, json, os, re, shutil, unicodedata
from pathlib import Path

PAGES_DIR = "public/data/murasoli/text"
PUB_LETTERS_DIR = "public/data/murasoli/letters"
PUB_LETTERS_INDEX = "public/data/murasoli/letters-index.json"
ARCHIVE_DIR = "archive"

# --- patterns (tolerant of OCR noise) ---------------------------------------
# ZWNJ/ZWSP and the Tamil pulli sequences OCR sprinkles around; normalise first.
ZW = re.compile(r"[​‌‍]")

# Volume 1 uses printed letter numbers 1 through 100.
HEAD = re.compile(r"^\s*(\d{1,3})\s*[.،]\s*(.*)$")

# Salutation — singular form used in Vol 54; keep the plural as a fallback for
# earlier volumes ("உடன்பிறப்புகளே", "...புக்களே") and allow stray spaces.
SALUT = re.compile(
    r"(?:"
    r"உடன்\s*பிறப்(?:பே|புக?\s*களே|புக்களே)|"
    r"அன்பு\s+நண்பா|பழைய\s+நண்ப(?:ா|னே)|"
    r"ஆருயிர்த்?\s+தோழா|அன்புத்?\s+தோழா|"
    r"அன்பின்\s+ஊற்றே|நண்பா|தம்பி"
    r")\s*[,!]?"
)

# Sign-off: "அன்புள்ள," then "மு.க." (OCR may space the dots), then a date.
# OCR routinely drops the pulli in the sign-off: அன்புள்ள / அனபுள்ள / அன்புளள /
# அனபுளள all occur in V54. The optional pulli marks make the regex catch them all.
SIGNOFF = re.compile(
    r"அன்?புள்?ள\s*[,.]?\s*(?:\n\s*)?"
    r"(?:மு\s*\.?\s*க\s*\.?|மறவன்|நண்பன்)"
)
COMPACT_SIGNOFF = re.compile(r"^\s*மு\s*\.?\s*க\s*\.?\s*$")
# trailing stray digit tolerated: "24-6-20168" → 2016
DATE = re.compile(r"\b(\d{1,2})\s*[.\-/]\s*(\d{1,2})\s*[.\-/]\s*(\d{4})\d?\b")

# Running headers glued INTO body lines by the OCR (page header merged with the
# first paragraph line). Always accompanied by junk — latin fragments, garbled
# page numbers ("தலைவர் கலைஞர் IPSS", "] 83", "1 6டு கலைஞரின் கடிதங்கள்") —
# which is what distinguishes them from genuine prose mentions.
INLINE_HEADERS = [
    # "...தலைவர் கலைஞர் <junk>" — கலைஞர் itself is often garbled (கலைஞார்,
    # கலைஞா, or reduced to bare "கலை" with latin junk); page numbers may be
    # Tamil digits ("0௫"). Junk = up to 3 short latin/digit/bracket tokens.
    re.compile(r"\s*தலைவர்?\s*கலை(?:ஞார்|ஞர்|ஞாா்|ஞா|ஞ)?\s*(?:[A-Za-z0-9\[\]|.௦-௯]{1,5}\s*){0,3}(?=\s|$)"),
    re.compile(r"\s*தலைவர்?\s*கலைஞர்\s*[இடுஉர]\s*(?=\s|$)"),
    # "<junk> கலைஞரின் கடிதங்கள் ..." at/near line start
    re.compile(r"(?:^|(?<=\s))(?:[A-Za-z0-9\[\]|டு௦-௯]{1,4}\s*){0,2}கலைஞரின்\s*கடிதங்கள்?\s*"),
]

# Running headers / pure page-number lines to strip.
HEADERS = [
    re.compile(r"^\s*\d{0,3}\s*கலைஞரின்?\s*கடிதங்கள்?\s*\d{0,3}\s*$"),
    re.compile(r"^\s*தலைவ[ரா]்?\s*கலைஞர்?\s*[\d\]lI|]{0,4}\s*$"),
    re.compile(r"^\s*[\d௦-௯\]lI|]{1,4}\s*$"),
]

# CATCH-ALL for header lines whose கலைஞர் dissolved into arbitrary junk
# ("தலைவர் HONEY HIM 309", "தலைவர் HONE ERM 63", "தலைவர் கலை(சா் 255",
# "தலைவர் கலைஞாரா் 1 49"). A SHORT standalone line starting தலைவர் is dropped
# only when its remainder carries a junk signal — a Latin letter, digit,
# Tamil digit or bracket, or a garbled கலை fragment. Genuine prose lines that
# happen to start with தலைவர் (…பேரவைத்\nதலைவர் அனுமதி…) continue in pure
# Tamil and never match.
HEADER_RESIDUE = re.compile(r"^\s*தலைவ[ரா]்?\s+(?P<rest>.{1,26})$")
JUNK_SIGNAL = re.compile(r"[A-Za-z0-9௦-௯()\[\]|]")

def norm(s: str) -> str:
    return unicodedata.normalize("NFC", ZW.sub("", s))

def is_header_line(line: str) -> bool:
    line = line.strip()
    if any(h.match(line) for h in HEADERS):
        return True
    m = HEADER_RESIDUE.match(line)
    if m:
        rest = m.group("rest").strip()
        if JUNK_SIGNAL.search(rest) or rest.startswith("கலை"):
            return True
    return False

def clean_lines(paragraphs):
    """Flatten a page's paragraphs to lines, dropping running headers —
    both standalone header lines and headers glued into body lines."""
    lines = []
    for p in paragraphs:
        for ln in norm(p).split("\n"):
            if not ln.strip() or is_header_line(ln):
                continue
            for rx in INLINE_HEADERS:
                ln = rx.sub(" ", ln)
            ln = re.sub(r"\s{2,}", " ", ln).rstrip()
            if ln.strip():
                lines.append(ln)
        lines.append("")  # paragraph break marker
    return lines

def parse_date(text):
    m = DATE.search(text)
    if not m:
        return None
    d, mo, y = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    if not (1 <= d <= 31 and 1 <= mo <= 12 and 1940 <= y <= 2018):
        return None
    return f"{y:04d}-{mo:02d}-{d:02d}"

def lines_to_paragraphs(lines):
    paras, cur = [], []
    for ln in lines:
        if ln == "":
            if cur:
                paras.append(" ".join(cur)); cur = []
        else:
            cur.append(ln.strip())
    if cur:
        paras.append(" ".join(cur))
    return paras

CURATED_DIR = Path(__file__).resolve().parent / "curated"


def curated_path(volume):
    return CURATED_DIR / f"murasoli-v{volume}-overrides.json"


def apply_curated_overrides(letters, path, report):
    """Human-verified per-letter facts beat OCR. The overrides file maps
    letter id -> {title: {en, ta}, date: "YYYY-MM-DD"}; empty values are
    ignored. Maintained by hand against the printed volume/TOC — this is
    the right home for garbled TITLES and missing DATES, which are
    per-letter facts, not global token corrections."""
    path = Path(path)
    if not path.exists():
        report["curatedOverridesApplied"] = 0
        return
    overrides = json.loads(path.read_text(encoding="utf-8")).get("letters", {})
    n = 0
    for l in letters:
        o = overrides.get(l["id"])
        if not o:
            continue
        changed = False
        t = o.get("title") or {}
        if isinstance(t, dict):
            for k in ("en", "ta"):
                if t.get(k):
                    l["title"][k] = t[k]; changed = True
        if o.get("date"):
            l["date"] = o["date"]; changed = True
        if changed:
            l["curated"] = True
            n += 1
    report["curatedOverridesApplied"] = n
    report["curatedOverridesFile"] = str(path.resolve())


def write_overrides_template(letters, volume, path):
    """Write an editable template with current values (never overwrites)."""
    path = Path(path)
    if path.exists():
        print(f"[template] {path} already exists — not touching it")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = {
        "note": "Human-verified letter facts for volume %d. Correct titles and "
                "fill dates against the printed volume/TOC; empty strings are "
                "ignored. Re-run the splitter after editing." % volume,
        "letters": {
            l["id"]: {"number": l["number"],
                      "title": {"en": l["title"]["en"], "ta": l["title"]["ta"]},
                      "date": l["date"] or "",
                      "pages": f"{l['pages'][0]}..{l['pages'][-1]}"}
            for l in letters
        },
    }
    write_json_atomic(path, doc)
    print(f"[template] wrote {path} ({len(letters)} letters) — edit and re-run")

def split_volume(volume, pages_dir=PAGES_DIR, allow_unnumbered=True):
    files = sorted(
        fn for fn in glob.glob(f"{pages_dir}/m{volume}-p*.json")
        if not fn.endswith(".orig.json")
    )
    if not files:
        raise SystemExit(
            f"No corrected page JSON found for volume {volume} in {pages_dir}.\n"
            f"Run: python3 run_volume_pipeline.py correct --volume {volume}\n"
            "Then run the chapters command again."
        )
    letters, report = [], {
        "volume": volume, "pagesScanned": len(files), "letterStarts": 0,
        "startsWithoutNumber": 0, "signoffsSeen": 0, "lettersWithDate": 0,
        "numberGaps": [], "orphanPagesBeforeFirstLetter": [], "warnings": [],
    }
    cur = None  # current letter accumulator

    def close_current():
        nonlocal cur
        if cur:
            cur["paragraphs"] = lines_to_paragraphs(cur.pop("lines"))
            letters.append(cur)
            cur = None

    for fn in files:
        d = json.load(open(fn, encoding="utf-8"))
        if d.get("pageType") in ("cover", "frontmatter", "toc"):
            continue
        lines = clean_lines(d["paragraphs"])
        page_text = "\n".join(lines)

        # Table-of-contents heuristic: many dates + many short lines, no salutation.
        if (len(DATE.findall(page_text)) >= 4 and not SALUT.search(page_text)
                and not SIGNOFF.search(page_text) and sum(len(l) for l in lines) / max(len(lines), 1) < 45):
            continue

        i = 0
        while i < len(lines):
            ln = lines[i]
            hm = HEAD.match(ln)
            # A numbered heading only starts a letter if the salutation follows soon.
            lookahead = "\n".join(lines[i:i + 24])
            if hm and SALUT.search(lookahead):
                close_current()
                number = int(hm.group(1))
                # title = heading remainder + lines up to the salutation
                title_parts = [hm.group(2).strip()] if hm.group(2).strip() else []
                j = i + 1
                while j < len(lines) and not SALUT.search(lines[j]):
                    if lines[j].strip():
                        title_parts.append(lines[j].strip())
                    j += 1
                title_ta = " ".join(title_parts).strip(" -–—!")
                cur = {
                    "id": f"m{volume}-l{number:04d}",
                    "collection": "murasoli-letter", "volume": volume,
                    "number": number, "date": None,
                    "title": {"en": f"Letter {number}", "ta": title_ta or f"கடிதம் {number}"},
                    "salutation": "உடன்பிறப்பே,",
                    "pages": [d["id"]], "lines": [],
                    "ocrStatus": d.get("ocrStatus", "uncorrected"),
                }
                report["letterStarts"] += 1
                i = j + 1  # skip past the salutation line
                continue
            # Salutation with no readable serial number → still a letter start.
            # DISABLE with --no-unnumbered when the volume's numbered coverage is
            # contiguous: letters QUOTE the salutation mid-text, and every
            # salutation-only "letter" is then a false split that chops the tail
            # off the preceding letter (V54: all 36 serials present; the 3
            # unnumbered starts were quotes inside l4025/l4046 + front matter).
            if allow_unnumbered and SALUT.search(ln) and cur is None:
                report["letterStarts"] += 1
                report["startsWithoutNumber"] += 1
                cur = {
                    "id": f"m{volume}-l-unnumbered-{d['page']:04d}",
                    "collection": "murasoli-letter", "volume": volume,
                    "number": None, "date": None,
                    "title": {"en": f"Letter (number unclear, p. {d['page']})",
                              "ta": f"கடிதம் (எண் தெளிவில்லை, பக். {d['page']})"},
                    "salutation": "உடன்பிறப்பே,",
                    "pages": [d["id"]], "lines": [],
                    "ocrStatus": d.get("ocrStatus", "uncorrected"),
                }
                i += 1
                continue
            if cur:
                if d["id"] not in cur["pages"]:
                    cur["pages"].append(d["id"])
                cur["lines"].append(ln)
                # sign-off closes the letter; grab the trailing date.
                # Anchor on the "அன்புள்ள" line itself (blank paragraph-break
                # markers sit between it, "மு.க." and the date), then read an
                # 8-line window forward for மு.க. + the date.
                tail = "\n".join(lines[i:i + 8])
                normal_signoff = re.search(r"அன்?புள்?ள", ln) and SIGNOFF.search(tail)
                compact_signoff = COMPACT_SIGNOFF.match(ln) and parse_date(tail)
                if normal_signoff or compact_signoff:
                    report["signoffsSeen"] += 1
                    # consume the sign-off block (up to 6 lines, stop after a date)
                    k = i + 1
                    if not parse_date(ln):
                        consumed = 0
                        while k < len(lines) and consumed < 6:
                            cur["lines"].append(lines[k])
                            if lines[k].strip() and parse_date(lines[k]):
                                k += 1
                                break
                            k += 1
                            consumed += 1
                    dt = parse_date(tail)
                    if dt:
                        cur["date"] = dt
                        report["lettersWithDate"] += 1
                    close_current()
                    i = k
                    continue
            else:
                if not report["orphanPagesBeforeFirstLetter"] or \
                        report["orphanPagesBeforeFirstLetter"][-1] != d["id"]:
                    if ln.strip():
                        report["orphanPagesBeforeFirstLetter"].append(d["id"])
            i += 1
    close_current()

    nums = sorted(l["number"] for l in letters if l["number"])
    for a, b in zip(nums, nums[1:]):
        if b - a > 1:
            report["numberGaps"].append(f"{a} → {b} (missing {b - a - 1})")
    if nums:
        report["serialRange"] = f"{nums[0]}–{nums[-1]}"
    report["lettersAssembled"] = len(letters)
    # keep the orphan list readable
    report["orphanPagesBeforeFirstLetter"] = report["orphanPagesBeforeFirstLetter"][:20]
    return letters, report

def safe_folder_name(chapter):
    title = chapter.get("title", {}).get("ta") or "chapter"
    title = re.sub(r'[\\/:*?"<>|\x00-\x1f]+', " ", title)
    title = re.sub(r"\s+", "_", title).strip("._ ")
    if len(title) > 72:
        title = title[:72].rstrip("._ ")
    return f"{chapter['id']}_{title or 'chapter'}"


def write_json_atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    temp.replace(path)


def chapter_markdown(chapter):
    number = chapter.get("number")
    title = chapter.get("title", {}).get("ta") or "கடிதம்"
    heading = f"{number}. {title}" if number else title
    paragraphs = [p.strip() for p in chapter.get("paragraphs", []) if p.strip()]
    body = "\n\n".join(paragraphs)
    parts = [f"# {heading}", chapter.get("salutation") or "உடன்பிறப்பே,"]
    if body:
        parts.append(body)
    return "\n\n".join(parts).rstrip() + "\n"


def discover_source_images(images_dir):
    if not images_dir:
        return {}
    images_dir = Path(images_dir)
    if not images_dir.is_dir():
        raise SystemExit(f"Source image folder not found: {images_dir}")
    by_page = {}
    for path in images_dir.iterdir():
        if not path.is_file() or path.suffix.lower() not in {
            ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp"
        }:
            continue
        match = re.search(r"(\d+)$", path.stem)
        if match:
            by_page[int(match.group(1))] = path
    return by_page


def place_image(source, destination, mode):
    if destination.exists() and destination.stat().st_size > 0:
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    if mode == "copy":
        shutil.copy2(source, destination)
        return
    if mode == "symlink":
        destination.symlink_to(source)
        return
    try:
        os.link(source, destination)
    except OSError:
        shutil.copy2(source, destination)


def archive_stale_chapter_folders(output, chapter, current_dir):
    archived = []
    archive_root = output.parent / f"{output.name}_stale"
    for candidate in sorted(output.glob(f"{chapter['id']}_*")):
        if candidate == current_dir or not candidate.is_dir():
            continue
        metadata = candidate / "chapter.json"
        try:
            candidate_id = json.loads(metadata.read_text(encoding="utf-8")).get("id")
        except (OSError, json.JSONDecodeError):
            continue
        if candidate_id != chapter["id"]:
            continue

        archive_root.mkdir(parents=True, exist_ok=True)
        destination = archive_root / candidate.name
        suffix = 2
        while destination.exists():
            destination = archive_root / f"{candidate.name}_{suffix}"
            suffix += 1
        candidate.rename(destination)
        archived.append(str(destination.resolve()))
    return archived


def write_chapters(letters, report, output, images_dir=None, image_mode="hardlink"):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    source_images = discover_source_images(images_dir)
    missing_images = []
    archived_folders = []
    previous_folders = {}
    previous_index = output / "chapters-index.json"
    if previous_index.exists():
        try:
            previous_data = json.loads(previous_index.read_text(encoding="utf-8"))
            previous_folders = {
                row.get("id"): row.get("folder")
                for row in previous_data.get("chapters", [])
                if row.get("id") and row.get("folder")
            }
        except (OSError, json.JSONDecodeError):
            previous_folders = {}
    current_ids = {chapter["id"] for chapter in letters}
    archive_root = output.parent / f"{output.name}_stale"
    for previous_id, previous_name in previous_folders.items():
        if previous_id in current_ids:
            continue
        previous_dir = output / previous_name
        if not previous_dir.is_dir():
            continue
        archive_root.mkdir(parents=True, exist_ok=True)
        destination = archive_root / previous_dir.name
        suffix = 2
        while destination.exists():
            destination = archive_root / f"{previous_dir.name}_{suffix}"
            suffix += 1
        previous_dir.rename(destination)
        archived_folders.append(str(destination.resolve()))
    index_rows = []
    for chapter in letters:
        folder_name = safe_folder_name(chapter)
        chapter_dir = output / folder_name
        previous_name = previous_folders.get(chapter["id"])
        previous_dir = output / previous_name if previous_name else None
        if (
            previous_dir is not None
            and previous_dir != chapter_dir
            and previous_dir.is_dir()
            and not chapter_dir.exists()
        ):
            previous_dir.rename(chapter_dir)
        chapter_dir.mkdir(parents=True, exist_ok=True)
        archived_folders.extend(
            archive_stale_chapter_folders(output, chapter, chapter_dir)
        )
        write_json_atomic(chapter_dir / "chapter.json", chapter)
        markdown = chapter_markdown(chapter)
        temp_md = chapter_dir / "chapter.md.tmp"
        temp_md.write_text(markdown, encoding="utf-8")
        temp_md.replace(chapter_dir / "chapter.md")
        if source_images and image_mode != "none":
            for page_id in chapter.get("pages", []):
                match = re.search(r"-p(\d+)$", page_id)
                if not match:
                    continue
                page = int(match.group(1))
                source = source_images.get(page)
                if source is None:
                    missing_images.append({"chapter": chapter["id"], "page": page})
                    continue
                place_image(source, chapter_dir / "images" / source.name, image_mode)
        index_rows.append({
            "id": chapter["id"],
            "number": chapter.get("number"),
            "date": chapter.get("date"),
            "title": chapter.get("title"),
            "sourcePages": chapter.get("pages", []),
            "folder": folder_name,
        })

    index = {
        "collection": "murasoli-chapters",
        "volume": report["volume"],
        "chapterCount": len(index_rows),
        "chapters": index_rows,
    }
    report["sourceImagesMissing"] = missing_images
    report["staleChapterFoldersArchived"] = archived_folders
    write_json_atomic(output / "chapters-index.json", index)
    write_json_atomic(output / "chapter_report.json", report)


def main():
    ap = argparse.ArgumentParser(
        description="Group corrected Murasoli page JSON into cleaned chapter text."
    )
    ap.add_argument("--volume", type=int, required=True)
    ap.add_argument("--pages-dir", required=True, help="folder containing mNN-pXXXX.json")
    ap.add_argument("--output", required=True, help="chapter output folder")
    ap.add_argument(
        "--overrides",
        type=Path,
        default=None,
        help="curated per-letter title/date overrides JSON",
    )
    ap.add_argument(
        "--write-overrides-template",
        action="store_true",
        help="write a starter overrides file when one does not exist",
    )
    ap.add_argument("--images-dir", default=None, help="optional rendered page-image folder")
    ap.add_argument(
        "--image-mode",
        choices=["hardlink", "symlink", "copy", "none"],
        default="hardlink",
        help="how source page images are placed in each chapter folder",
    )
    ap.add_argument("--no-unnumbered", action="store_true",
                    help="ignore salutation-only starts when numbered coverage is complete")
    args = ap.parse_args()

    letters, report = split_volume(
        args.volume,
        args.pages_dir,
        allow_unnumbered=not args.no_unnumbered,
    )
    overrides = args.overrides or curated_path(args.volume)
    if args.write_overrides_template:
        write_overrides_template(letters, args.volume, overrides)
    apply_curated_overrides(letters, overrides, report)
    write_chapters(letters, report, args.output, args.images_dir, args.image_mode)
    print(f"volume {args.volume}: {report['lettersAssembled']} chapters "
          f"({report['startsWithoutNumber']} unnumbered), "
          f"{report['lettersWithDate']} dated, gaps: {len(report['numberGaps'])}")
    print(f"clean chapter folders: {Path(args.output).resolve()}")
    archived = report.get("staleChapterFoldersArchived", [])
    if archived:
        print(f"archived {len(archived)} obsolete chapter folder(s)")

if __name__ == "__main__":
    main()
