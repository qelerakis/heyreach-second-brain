# HeyReach Brain — Synthesis Caveats (every synthesis agent reads this first)

You are turning the extraction notes in `D:\HeyReach Brain\wiki\_build\notes-batch-*.md` into a
cited wiki. The whole corpus is **HeyReach's own content** — YouTube videos, blog posts, outbound
playbooks, certified-expert profiles, and product pages. That shapes how you must write.

## The corpus is first-party marketing — handle COI with discipline
- **Everything here promotes HeyReach.** Present the tactics, workflows, and data faithfully, but
  never launder a HeyReach sales claim into neutral fact. "HeyReach is the best / the only tool
  that…" is a **vendor claim** — attribute it ("HeyReach positions itself as…", "HeyReach claims…").
- **Attribute outside practitioners by name.** Playbooks and many videos feature named people and
  agencies (e.g. campaign case studies, certified experts). Attribute their tactics, numbers, and
  opinions to **them** — with their agency noted as a COI — never as HeyReach's own generic advice.
- **Benchmarks are self-reported.** Reply rates, acceptance rates, connection rates, conversion
  rates, meetings booked, revenue — all come from HeyReach or its featured practitioners. Cite them
  as **claimed**, keep the context (who, ICP/vertical, sample size, timeframe if given), and never
  present them as independently verified. Where two sources give different numbers for the same
  thing, preserve BOTH — don't silently reconcile.
- **Title-only / hype numbers:** a figure that appears only in a title/headline and is never
  substantiated in the body → flag it or omit it; never record it as a result.
- **Era-tag.** LinkedIn limits and outreach tactics change fast. Note the date / "as of 2026" /
  "new LinkedIn algorithm" context where a tactic or number is time-bound.

## Citations — resolve to 0
- **Every claim cites its source inline:** `(source: "citation_title")` — the EXACT title from the
  notes' `##` headers. Copy it **byte-for-byte**: curly quotes `'` `"`, emoji (e.g. `SalesCaptain 🚢`),
  `.io`, `&`, `%`, `…`, `❘`, punctuation and capitalization exactly. Citations resolve by exact match,
  so any drift breaks them.
- **Multiple sources** for one claim: `(source: "A"; source: "B")`.
- If you're unsure a title is exact, grep the notes for it before citing:
  `grep -rh '^## ' notes-batch-*.md | sort -u`.

## Wikilinks
- `[[article-slug]]` liberally to related articles in ANY category — the slug is the target
  filename without `.md` (e.g. `[[safe-linkedin-sending-limits]]`). A short **## Related** footer of
  `[[links]]` at the end of each article is expected.
- Only link articles that exist or that another agent is writing this run (coordinate via the article
  list in SYNTHESIS-PROMPT.md). A missing target is fixed in the verify pass, but aim to link real ones.

## Writing rules
- **Merge by topic, not per source.** One article per coherent topic; pull from every source that
  touches it (video + blog + playbook + product page together).
- **Extractive accuracy:** their words, their numbers, never your inventions. Punchy verbatim quotes
  (≤15 words) welcome.
- **Voice:** this is a brand knowledge base, not a person. Write as a clear, authoritative, neutral
  distillation of HeyReach's playbook and product — useful to a practitioner or to the HeyReach team.
  Do NOT write in the first person as HeyReach.
- **Structure each article:** a one-paragraph summary up top → sections with specifics (steps,
  thresholds, scripts, tables) → a `## Related` `[[wikilink]]` footer.
- **Note gaps** honestly rather than padding.

## Return
A markdown list of every article you created: `- [[slug]] — one-line description` (this goes into
INDEX.md verbatim), plus counts and anything you couldn't cover.
