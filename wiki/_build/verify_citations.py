"""Verify the HeyReach Brain wiki: citations resolve, wikilinks resolve, articles cited.

Usage: python verify_citations.py
- Every (source: "Title") must match a citation_title in sources.tsv (byte-exact).
- Every [[slug]] must match a wiki/**/<slug>.md file.
- Every article must carry >=1 citation.
Exit 0 only when there are 0 unresolved citations and 0 broken wikilinks.
"""
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path

BRAIN = Path(r"D:\HeyReach Brain")
WIKI = BRAIN / "wiki"
BUILD = WIKI / "_build"

# Valid citation titles from the manifest
valid_titles = set()
for line in (BUILD / "sources.tsv").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title = line.split("\t")[0]
    valid_titles.add(title)

# All article files (exclude _build and navigation indexes)
NAV_FILES = {"INDEX.md"}
articles = [p for p in WIKI.rglob("*.md") if "_build" not in p.parts]
content_articles = [p for p in articles if p.name not in NAV_FILES]
slugs = {p.stem for p in articles}

CIT_RE = re.compile(r'source:\s*"([^"]+)"')          # catches standalone + multi-source groups
WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')

unresolved_cites = {}   # title -> [files]
broken_links = {}       # slug -> [files]
no_citation = []
total_cites = 0
total_links = 0

for art in articles:
    text = art.read_text(encoding="utf-8", errors="replace")
    cites = CIT_RE.findall(text)
    total_cites += len(cites)
    if not cites and art.name not in NAV_FILES:
        no_citation.append(str(art.relative_to(BRAIN)))
    for c in cites:
        if c not in valid_titles:
            unresolved_cites.setdefault(c, []).append(art.name)
    for link in WIKILINK_RE.findall(text):
        slug = link.split("|")[0].split("#")[0].strip()
        total_links += 1
        if slug and slug not in slugs:
            broken_links.setdefault(slug, []).append(art.name)

print(f"Articles: {len(articles)} | citations: {total_cites} | wikilinks: {total_links}")
print(f"Valid source titles in manifest: {len(valid_titles)}")
print()

ok = True
if no_citation:
    ok = False
    print(f"ARTICLES WITH NO CITATIONS ({len(no_citation)}):")
    for f in no_citation:
        print(f"   {f}")
    print()

if unresolved_cites:
    ok = False
    print(f"UNRESOLVED CITATIONS ({len(unresolved_cites)} distinct titles):")
    for title, files in sorted(unresolved_cites.items()):
        print(f'   "{title}"  <- {len(files)}x e.g. {files[0]}')
    print()

if broken_links:
    ok = False
    print(f"BROKEN WIKILINKS ({len(broken_links)} distinct slugs):")
    for slug, files in sorted(broken_links.items()):
        print(f"   [[{slug}]]  <- {len(files)}x e.g. {files[0]}")
    print()

if ok:
    print("PASS: 0 unresolved citations, 0 broken wikilinks, every article cited.")
    sys.exit(0)
else:
    print("FAIL: see above.")
    sys.exit(1)
