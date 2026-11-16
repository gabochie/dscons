#!/usr/bin/env python3
"""Build self-contained, print-ready HTML from the client markdown files.

Diagrams are rendered to SVG via mermaid.ink and embedded as data URIs so the
HTML works offline. Run from anywhere:  python3 internal/build-client-html.py
"""

import base64
import pathlib
import re
import sys
import time
import urllib.request

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
CLIENT = ROOT / "client"

DOCS = [
    {
        "src": "00-simple-decision-guide.md",
        "out": "00-simple-decision-guide.html",
        "eyebrow": "READ ME FIRST · PLAIN-LANGUAGE GUIDE",
        "title": "Your Options, Explained Simply",
        "subtitle": "Three doors, every one safe — pay the big money only after you have seen the results",
        "note": "This guide sits in front of the full proposal and is enough to decide on its own. If any part of the full proposal feels heavy, rely on this one — it is written in everyday language by design.",
        "meta": [
            ("To", "Mr. Daniel Sogbodjor — Director, DS Construction Limited (and the DS Management Team)"),
            ("Prepared by", "<strong>Gideon B. Abochie</strong> — Founder, Gabochie Design · Gabochie Marketing (B2B brand of Gabochie Design)"),
            ("Contact", "admin@gabochie.com · +233 26 824 8970 · mkt.gabochie.com · P.O. Box SK 2125, Sakumono, Tema"),
            ("Date", "November 2026"),
            ("Valid until", "6 December 2026"),
        ],
        "enclosures": [
            ("01-winning-offer-proposal.html", "The DS Growth & Sales System — Full Proposal"),
            ("05-heritage-portfolio-sample.html", "The Heritage Book — Sample Layout (the free Door-1 sample)"),
        ],
        "captions": [],
    },
    {
        "src": "01-winning-offer-proposal.md",
        "out": "01-winning-offer-proposal.html",
        "eyebrow": "PROPOSAL",
        "title": "The DS Growth & Sales System",
        "subtitle": 'From "well-known but invisible" to Ghana\'s default glazing choice',
        "note": None,
        "meta": [
            ("To", "Management, DS Construction Limited"),
            ("Prepared by", "<strong>Gideon B. Abochie</strong> — BArch (KNUST) Architect · Founder, Gabochie Marketing · Principal, Gabochie Design / Gabochie Corp (Built-Environment Intelligence)"),
            ("Contact", "admin@gabochie.com · +233 26 824 8970 · mkt.gabochie.com · P.O. Box SK 2125, Sakumono, Tema"),
            ("Date", "6 November 2026"),
            ("Validity", "30 days — valid until 6 December 2026"),
        ],
        "enclosures": [
            ("02-audit-summary-giveaway.html", "Market & Digital Presence Audit — Summary"),
            ("03-30-day-non-negotiable-foundations.html", "30-Day Non-Negotiable Foundations"),
        ],
        "captions": [
            "The conversion funnel and the three revenue leaks.",
            "Annual leak vs the Option B maximum fee (GHS millions).",
            "Share of the annual leak by source (indicative).",
            "90-day delivery roadmap (Option B).",
            "The private growth partnership workflow — from heritage proof to signed contract.",
            "How the six Day-90 KPIs map to the money.",
            "How payment follows verified results.",
        ],
    },
    {
        "src": "02-audit-summary-giveaway.md",
        "out": "02-audit-summary-giveaway.html",
        "eyebrow": "AUDIT SUMMARY",
        "title": "Market & Digital Presence Audit",
        "subtitle": "DS Construction Limited · Prepared by Gideon B. Abochie (Gabochie Marketing / Gabochie Corp) · 6 November 2026",
        "note": "This summary is yours to keep whether or not you proceed with the accompanying proposal. The full detailed audit is shared after engagement begins.",
        "meta": [],
        "enclosures": [
            ("03-30-day-non-negotiable-foundations.html", "30-Day Non-Negotiable Foundations"),
            ("01-winning-offer-proposal.html", "The DS Growth & Sales System — Proposal"),
        ],
        "captions": [
            "2026 market signals (% change).",
            "Competitive positioning on public evidence (November 2026).",
        ],
    },
    {
        "src": "03-30-day-non-negotiable-foundations.md",
        "out": "03-30-day-non-negotiable-foundations.html",
        "eyebrow": "CLIENT ANNEX · DAY 1–30",
        "title": "30-Day Non-Negotiable Foundations",
        "subtitle": "Immediate actions to make the DS Growth & Sales System executable",
        "note": None,
        "meta": [
            ("Client", "DS Construction Limited"),
            ("Prepared by", "Gideon B. Abochie — Gabochie Marketing / Gabochie Corp"),
            ("Date", "6 November 2026"),
            ("Window", "Day 1–30 from kickoff"),
            ("Guiding rule", "No paid ads. No ad tracking. Organic, owned and referral channels only."),
            ("Reference", "mkt.gabochie.com"),
        ],
        "enclosures": [
            ("01-winning-offer-proposal.html", "The DS Growth & Sales System — Proposal"),
            ("02-audit-summary-giveaway.html", "Market & Digital Presence Audit — Summary"),
        ],
        "captions": [
            "30-day non-negotiable sprint.",
            "Indicative 30-day foundation budget (mid-case, GHS).",
        ],
    },
    {
        "src": "04-option-d-private-pipeline-agreement.md",
        "out": "04-option-d-private-pipeline-agreement.html",
        "eyebrow": "AGREEMENT · OPTION D",
        "title": "Private Growth Partnership — Service Agreement",
        "subtitle": "Option D · Legacy-led B2B pipeline · 100% private — no public advertising",
        "note": "Commercial term sheet. Either party may request legal review before signature.",
        "meta": [
            ("Client", "DS Construction Limited"),
            ("Consultant", "Gideon B. Abochie — Gabochie Marketing / Gabochie Corp"),
            ("Date", "7 November 2026"),
            ("Validity", "30 days (for signature)"),
            ("Reference", "mkt.gabochie.com"),
        ],
        "enclosures": [
            ("01-winning-offer-proposal.html", "The DS Growth & Sales System — Proposal"),
            ("05-heritage-portfolio-sample.html", "26 Years of Engineering Glass & Steel — Portfolio Sample"),
        ],
        "captions": [],
    },
    {
        "src": "05-heritage-portfolio-sample.md",
        "out": "05-heritage-portfolio-sample.html",
        "eyebrow": "PRIVATE PORTFOLIO · SAMPLE LAYOUT",
        "title": "26 Years of Engineering Glass & Steel",
        "subtitle": "Selected Structural Glazing Case Studies in Ghana — private portfolio sample and production template",
        "note": "Sample layout only. Replace bracketed placeholders with verified DS project facts and photographs before any use. Private distribution only — never post publicly.",
        "meta": [
            ("Prepared for", "DS Construction Limited"),
            ("Prepared by", "Gideon B. Abochie — Gabochie Marketing / Gabochie Corp"),
            ("Date", "7 November 2026"),
            ("Status", "Sample layout and production template"),
            ("Confidentiality", "Private distribution only — not for public posting"),
        ],
        "enclosures": [
            ("01-winning-offer-proposal.html", "The DS Growth & Sales System — Proposal"),
            ("04-option-d-private-pipeline-agreement.html", "Private Growth Partnership — Service Agreement"),
        ],
        "captions": [],
    },
]


def inline(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    return s


def fetch_svg(mmd, retries=5):
    code = base64.urlsafe_b64encode(mmd.encode("utf-8")).decode("ascii")
    url = f"https://mermaid.ink/svg/{code}"
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=90) as resp:
                svg = resp.read()
            if b"Syntax error" in svg or b'aria-roledescription="error"' in svg:
                raise RuntimeError("mermaid parse error")
            return svg
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(2 + i)
    raise RuntimeError(f"render failed: {last}")


def body_after_header(text):
    lines = text.splitlines()
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[i + 1 :])
    return text


def build(doc):
    src = CLIENT / doc["src"]
    text = src.read_text(encoding="utf-8")
    body = body_after_header(text)

    blocks = re.findall(r"```mermaid\n(.*?)```", body, re.S)
    state = {"i": 0}

    def placeholder(_m):
        idx = state["i"]
        state["i"] += 1
        return f'<figure class="diagram" data-idx="{idx}"></figure>'

    body = re.sub(r"```mermaid\n(.*?)```", placeholder, body, flags=re.S)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc"],
        extension_configs={"toc": {"toc_depth": "2"}},
    )
    content = md.convert(body)
    toc = md.toc

    content = content.replace("<table>", '<div class="table-wrap"><table>').replace(
        "</table>", "</table></div>"
    )
    content = re.sub(
        r"<li>\[ \]\s*(.*?)</li>",
        r'<li class="task"><span class="cb" aria-hidden="true"></span>\1</li>',
        content,
        flags=re.S,
    )

    def figure(match):
        idx = int(match.group(1))
        svg = fetch_svg(blocks[idx])
        b64 = base64.b64encode(svg).decode("ascii")
        cap = doc["captions"][idx] if idx < len(doc["captions"]) else ""
        alt = cap.replace('"', "&quot;")
        caption = f'<figcaption>Figure {idx + 1} — {cap}</figcaption>' if cap else ""
        return (
            f'<figure class="diagram">'
            f'<img src="data:image/svg+xml;base64,{b64}" alt="{alt}" loading="lazy">'
            f"{caption}</figure>"
        )

    content = re.sub(
        r'<figure class="diagram" data-idx="(\d+)"></figure>', figure, content
    )
    print(f"  {doc['src']}: {len(blocks)} diagram(s) embedded", file=sys.stderr)

    meta_html = ""
    if doc["meta"]:
        meta_html = '<dl class="meta">' + "".join(
            f"<div><dt>{k}</dt><dd>{inline(v)}</dd></div>" for k, v in doc["meta"]
        ) + "</dl>"

    enclosure_html = ""
    if doc["enclosures"]:
        items = "".join(
            f'<li><span>Companion:</span> <a href="{href}">{label}</a></li>'
            for href, label in doc["enclosures"]
        )
        enclosure_html = f'<ul class="enclosure-list">{items}</ul>'

    note_html = f'<p class="cover-note">{inline(doc["note"])}</p>' if doc["note"] else ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{doc['title']} — DS Construction Limited</title>
<meta name="author" content="Gideon B. Abochie, Gabochie Marketing / Gabochie Corp">
<meta name="description" content="Client document for DS Construction Limited, prepared by Gideon B. Abochie.">
<style>
:root {{
  --ink: #1f2a30;
  --muted: #5c6b73;
  --accent: #14532d;
  --accent-2: #b45309;
  --accent-soft: #eef5ef;
  --panel: #f6f8f7;
  --border: #d8e2dc;
  --paper: #ffffff;
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  margin: 0;
  background: #e9eeea;
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}}
.page {{ max-width: 980px; margin: 0 auto; background: var(--paper); box-shadow: 0 18px 60px rgba(20, 50, 35, .12); }}
.cover {{
  position: relative;
  padding: 68px 64px 52px;
  background: radial-gradient(1100px 420px at 110% -10%, rgba(20,83,45,.12), transparent 60%), linear-gradient(180deg, #fbfdfb 0%, #ffffff 100%);
  border-bottom: 1px solid var(--border);
  overflow: hidden;
}}
.cover::before {{ content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 10px; background: linear-gradient(180deg, var(--accent), var(--accent-2)); }}
.eyebrow {{ margin: 0 0 14px; color: var(--accent); font-size: 12px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; }}
.cover h1 {{ margin: 0 0 12px; font-family: Georgia, "Times New Roman", serif; font-size: clamp(34px, 5vw, 52px); line-height: 1.08; letter-spacing: -0.02em; color: var(--accent); }}
.subtitle {{ margin: 0 0 28px; max-width: 760px; color: var(--muted); font-size: 19px; line-height: 1.45; }}
.cover-note {{ margin: 0 0 26px; padding: 14px 18px; background: var(--accent-soft); border-left: 4px solid var(--accent); border-radius: 4px; font-size: 14px; }}
.meta {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px 36px; margin: 0 0 26px; padding: 24px 0 0; border-top: 1px solid var(--border); }}
.meta div {{ min-width: 0; }}
.meta dt {{ color: var(--muted); font-size: 11px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; margin-bottom: 3px; }}
.meta dd {{ margin: 0; font-size: 14.5px; line-height: 1.5; }}
.meta dd strong {{ color: var(--accent); }}
.enclosure-list {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }}
.enclosure-list li {{ padding: 12px 16px; background: var(--accent-soft); border: 1px solid var(--border); border-left: 4px solid var(--accent); border-radius: 4px; font-size: 14px; }}
.enclosure-list span {{ color: var(--muted); font-weight: 600; }}
.enclosure-list a {{ color: var(--accent); font-weight: 700; text-decoration: none; }}
.enclosure-list a:hover {{ text-decoration: underline; }}
.toc-page {{ padding: 48px 64px 56px; border-bottom: 1px solid var(--border); }}
.toc-page h2 {{ margin: 0 0 18px; font-family: Georgia, "Times New Roman", serif; font-size: 26px; color: var(--accent); }}
.toc {{ font-size: 15px; }}
.toc > ul {{ list-style: none; margin: 0; padding: 0; columns: 2; column-gap: 40px; }}
.toc ul ul {{ display: none; }}
.toc li {{ margin: 0 0 10px; break-inside: avoid; }}
.toc a {{ color: var(--ink); text-decoration: none; border-bottom: 1px dotted var(--border); }}
.toc a:hover {{ color: var(--accent); border-bottom-color: var(--accent); }}
main {{ padding: 8px 64px 72px; }}
h1, h2, h3, h4 {{ line-height: 1.25; }}
main h2 {{ margin: 52px 0 18px; padding-bottom: 10px; border-bottom: 2px solid var(--accent); font-family: Georgia, "Times New Roman", serif; font-size: 28px; color: var(--accent); scroll-margin-top: 18px; }}
main h3 {{ margin: 34px 0 10px; font-size: 19px; color: var(--accent); }}
main h4 {{ margin: 28px 0 10px; font-size: 15px; letter-spacing: .04em; text-transform: uppercase; color: var(--accent-2); }}
p {{ margin: 0 0 15px; }}
ul, ol {{ margin: 0 0 18px; padding-left: 24px; }}
li {{ margin: 0 0 8px; }}
li.task {{ list-style: none; margin-left: -24px; }}
.cb {{ display: inline-block; width: 14px; height: 14px; margin-right: 10px; border: 1.5px solid var(--accent); border-radius: 3px; vertical-align: -2px; }}
strong {{ color: #14211a; }}
a {{ color: var(--accent); }}
blockquote {{ margin: 0 0 24px; padding: 22px 26px; background: var(--accent-soft); border-left: 5px solid var(--accent); border-radius: 4px; font-size: 17px; line-height: 1.62; }}
blockquote p:last-child {{ margin-bottom: 0; }}
hr {{ border: 0; border-top: 1px solid var(--border); margin: 40px 0; }}
.table-wrap {{ width: 100%; overflow-x: auto; margin: 0 0 24px; }}
table {{ width: 100%; border-collapse: collapse; font-size: 13.5px; line-height: 1.45; }}
th, td {{ padding: 10px 12px; border: 1px solid var(--border); text-align: left; vertical-align: top; }}
thead th {{ background: var(--accent); color: #fff; font-size: 12px; letter-spacing: .03em; }}
tbody tr:nth-child(even) {{ background: #f8fbf8; }}
tbody td:first-child {{ font-weight: 600; color: #24322a; }}
figure.diagram {{ margin: 26px 0 30px; padding: 18px; background: #fff; border: 1px solid var(--border); border-radius: 8px; text-align: center; break-inside: avoid; }}
figure.diagram img {{ display: block; max-width: 100%; height: auto; margin: 0 auto; }}
figure.diagram figcaption {{ margin-top: 12px; color: var(--muted); font-size: 12.5px; font-style: italic; }}
.print-btn {{ position: fixed; right: 22px; bottom: 22px; z-index: 50; padding: 12px 18px; border: 0; border-radius: 999px; background: var(--accent); color: #fff; font: inherit; font-size: 14px; font-weight: 700; cursor: pointer; box-shadow: 0 10px 26px rgba(20, 83, 45, .28); }}
.print-btn:hover {{ background: #0f3d22; }}
.footer-note {{ margin-top: 48px; padding-top: 18px; border-top: 1px solid var(--border); color: var(--muted); font-size: 12.5px; }}
@media (max-width: 760px) {{
  .cover, .toc-page, main {{ padding-left: 24px; padding-right: 24px; }}
  .cover {{ padding-top: 44px; }}
  .meta {{ grid-template-columns: 1fr; }}
  .toc > ul {{ columns: 1; }}
  table {{ font-size: 12.5px; white-space: nowrap; }}
}}
@media print {{
  @page {{ size: A4; margin: 17mm 15mm 18mm; }}
  body {{ background: #fff; font-size: 10.5pt; line-height: 1.5; }}
  .page {{ max-width: none; box-shadow: none; }}
  .print-btn {{ display: none; }}
  .cover {{ min-height: 236mm; padding: 40mm 0 0; border: 0; break-after: page; background: #fff; }}
  .cover::before {{ width: 6px; }}
  .cover h1 {{ font-size: 38pt; }}
  .subtitle {{ font-size: 14pt; }}
  .toc-page {{ padding: 0; border: 0; break-after: page; }}
  main {{ padding: 0; }}
  main h2 {{ break-before: page; font-size: 20pt; margin-top: 0; }}
  main h2:first-of-type {{ break-before: auto; }}
  h3 {{ font-size: 13pt; }}
  table {{ font-size: 9pt; }}
  th, td {{ padding: 6px 7px; }}
  figure.diagram {{ padding: 10px; margin: 16px 0 20px; }}
  figure.diagram img {{ max-height: 105mm; width: auto; max-width: 100%; }}
  blockquote {{ padding: 14px 16px; font-size: 11pt; }}
  a {{ color: var(--ink); text-decoration: none; }}
  * {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
}}
</style>
</head>
<body>
<div class="page">
  <header class="cover">
    <p class="eyebrow">{inline(doc['eyebrow'])}</p>
    <h1>{inline(doc['title'])}</h1>
    <p class="subtitle">{inline(doc['subtitle'])}</p>
    {note_html}
    {meta_html}
    {enclosure_html}
  </header>

  <nav class="toc-page" aria-label="Contents">
    <h2>Contents</h2>
    {toc}
  </nav>

  <main>
    {content}
    <p class="footer-note">Prepared by Gideon B. Abochie · Gabochie Marketing / Gabochie Corp · admin@gabochie.com · +233 26 824 8970 · mkt.gabochie.com</p>
  </main>
</div>
<button class="print-btn" onclick="window.print()" type="button">Print / Save as PDF</button>
</body>
</html>
"""
    (CLIENT / doc["out"]).write_text(html, encoding="utf-8")
    print(f"wrote {doc['out']} ({len(html):,} bytes)")


if __name__ == "__main__":
    for document in DOCS:
        build(document)
