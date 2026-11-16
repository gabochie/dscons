# DS Construction Limited — Marketing Audit Project
**Consultant:** Gideon B. Abochie (BArch, KNUST · Gabochie Marketing · Gabochie Design / Gabochie Corp)

## Folder structure — client-facing vs internal

```
/public/dscons
├── README.md                      ← this index (never share raw)
├── client/                        ← SEND / SHOW to DS
│   ├── 00-simple-decision-guide.md   (plain-language "read me first" companion: three doors — free Heritage Book sample / quiet partnership (DFY or trained-staff) / full visibility system; three-question decision tree; tick-box choice table; zero jargon by design — build this for the "we are not computer people" founder)
│   ├── 00-simple-decision-guide.html (self-contained, print-ready)
│   ├── 00-simple-decision-guide-elite.html (elite presentation edition — dark engraved cover, gold/ivory palette, Marcellus/Playfair type; rendered to PDF via WeasyPrint: python3 -c "import subprocess; subprocess.run(['weasyprint','client/00-simple-decision-guide-elite.html','client/00-simple-decision-guide-elite.pdf'])"; fonts live in internal/fonts/)
│   ├── 00-simple-decision-guide-elite.pdf (send-ready 11-page A4 addressed to Daniel Sogbodjor — the meeting/print copy)
│   ├── 01-winning-offer-proposal.md   (four options: A/B/C digital + **Option D — Private Growth Partnership**, the recommended dual-path legacy-led B2B offer; KPI-tied payment structure §5; trust architecture §6; mkt.gabochie.com references only; Mermaid visuals: funnel, money-view charts, 90-day roadmap, KPI→money map, payment gates)
│   ├── 01-winning-offer-proposal.html (self-contained, print-ready; diagrams embedded as SVG)
│   ├── 02-audit-summary-giveaway.md   (upfront-give trust asset: sanitized audit summary, DS keeps it regardless of decision; Mermaid visuals: 2026 market-signal chart, competitor positioning map)
│   ├── 02-audit-summary-giveaway.html (self-contained, print-ready; diagrams embedded as SVG)
│   ├── 03-30-day-non-negotiable-foundations.md   (client annex: 30-day non-negotiable actions, owners, deadlines and direct costs; no paid ads; Klagon showroom signage sprint)
│   ├── 03-30-day-non-negotiable-foundations.html (self-contained, print-ready; diagrams embedded as SVG)
│   ├── 04-option-d-private-pipeline-agreement.md   (Option D service agreement: pathway selection, qualified-invitation definition, monthly guarantee, fee/success-fee mechanics, tax-privacy commitments, Annex A guarantee tracker, Annex B introduced-project register)
│   ├── 04-option-d-private-pipeline-agreement.html (self-contained, print-ready; sign-ready term sheet)
│   ├── 05-heritage-portfolio-sample.md   (Option D proof asset: 12-page private Heritage Portfolio sample layout and production template — cover, legacy statement, at-a-glance credibility, 3 worked case studies, capability matrix, technical/warranty page, production checklist, distribution protocol)
│   ├── 05-heritage-portfolio-sample.html (self-contained, print-ready; show to DS as the free proof-first sample)
│   ├── 05-heritage-portfolio-sample-elite.html (A1-grade brand-led edition — DS gold/charcoal palette from dscons-gh.com, DS wordmark recreated from the live site, labelled image placeholders, full-bleed case-study openers)
│   └── 05-heritage-portfolio-sample-elite.pdf (send-ready A4 PDF, 15 pages — use this edition for Door 1 and private introductions)
└── internal/                      ← YOUR STRATEGY — do not send
    ├── 02-marketing-audit-full.md            (candid findings; present as slides after signing)
    ├── 03-solutions-action-plan-internal.md  (delivery workplan, tips, week-by-week ops)
    ├── 04-budget-and-consultant-fees-confidential.md   (your pricing playbook — NEVER share)
    ├── 05-sales-system-design-internal.md    (method specs; share extracts as SOW after signing)
    ├── 06-marketing-site-redeploy-runbook.md (mkt.gabochie.com is live; 30–60 min fix path inside; all active marketing references use mkt.gabochie.com; SME tools fold into the Gabochie Corp product pipeline per owner decision 6 Nov 2026)
    ├── 07-web-vendor-collaboration.md        (DS rebuilt its site — static HTML, NOT WordPress — plus new socials; RACI with their web developer, asset-ownership checklist, technical correction brief)
    ├── 09-revenue-leak-scorecard-product.md   (GABOCHIE'S OWN PRODUCT, not DS: draft product spec for a free Revenue Leak Scorecard + paid systems audit — 8 domains, 16 questions, GHS leak model, landing copy, pilot plan)
    └── build-client-html.py                   (regenerates client/*.html from the .md sources; embeds diagrams as SVG data URIs)

Also in `internal/`: `08-value-at-stake-model.md` — the revenue-leak quantification (three leaks: visibility, follow-up, speed/proof; indicative GHS 2.6–14M/yr, mid ≈ GHS 5M+/yr, all calibratable Week 1) and the KPI→money mapping used to justify the KPI-tied payment structure in the proposal (§5).
```

## What to show, and when

| Stage | Share / Show | Keep back |
|---|---|---|
| Pitch / first meeting | Lead with `client/00-simple-decision-guide` (send the .html; it is the plain-language cover for the whole offer — read §3 choice table with him aloud, tick Door 1 together before leaving). Then talk through `client/01` §1–4 verbally **plus** show `client/05-heritage-portfolio-sample.html` as the free proof-first close. **Do not send `client/04` yet** — it is the signature-stage document. | Everything in `internal/` — especially fee models & negotiation anchors (04) and candid audit criticism (02) |
| Verbal Q&A during pitch | Talk about the 90-day outcomes table (proposal §4); skim the audit *content* verbally if asked "what did you find?" — but don't hand over the document: it contains blunt language ("weak digital presence", scores, competitor sharpshoot) that can irritate before commitment | Same |
| Option D agreed in principle | Send `client/04-option-d-private-pipeline-agreement.html` for pathway selection and signature. At kickoff, confirm the qualified-invitation definition, the monthly guarantee tracker (Annex A) and the introduced-project register (Annex B). | Internal fee logic (`internal/04`) and any margin/commission ceilings |
| After go-ahead (kickoff week) | Share `client/02` (if not already given) and `client/03` — the 30-day non-negotiable checklist — and lock the owners/costs in the kickoff meeting. Present internal audit findings as a **slide summary** (reword neutrally: "opportunities" not "weaknesses"); share `internal/05-sales-system-design-internal.md` extracts re-labelled e.g. "Sales System Specification" | 04 fee playbook & negotiation anchors — for your eyes only |
| Month 4+ (retainer live) | Share progress vs. the 90-day roadmap (from `03`), KPI dashboard, tool budget (Section C of `04`, sanitized) | Your fee logic and comparables analysis remain internal |

## Usage notes for the pitch call

- **Plain-language rule for this client:** he has said repeatedly "we are not computer people". Any new client-facing text must pass a jargon test: no CRM, SEO, KPI, BOQ, pixel, funnel, retainer — use "customer list", "show up on Google", "checklist", "price list", "monthly support". `client/00` is the template for that voice; keep new docs consistent with it.
- **Brand & identity rule (owner correction, 9 Nov):** Gideon B. Abochie is **Founder, Gabochie Design** (design.gabochie.com — the parent practice); **Gabochie Marketing** (mkt.gabochie.com) is the child brand delivering B2B marketing outcomes. Never sign him "Principal, Gabochie Marketing" or lead with academic credentials (no BArch/KNUST in client-facing docs). Contact split: +233 26 824 8970 / admin@gabochie.com (Design, call & WhatsApp) vs +233 50 638 4917 / gabochiemarketing@gmail.com (Marketing). Older docs (01–05) still carry the old wording — sanitize before re-use.
- **Choice architecture (why we win whatever he picks):** the guide's three doors are engineered so every outcome converts. Door 1 (free sample) = zero-cost entry that proves quality and opens Door 2's pitch with the sample already in his hands. Door 2 Path A = low GHS 4,000 entry + recurring + 1% upside on 6–7-figure contracts; Path B = high one-time build fee + low-effort GHS 3k oversight, no commission leakage — and it pre-empts "we'll use our own staff". Door 3 (Option B) remains the premium path with 57% behind verification gates. Even "let me think" retains goodwill via the kept audit summary + §4's cost-of-waiting (dry-season BQ timing, K3 pressure) framing. The only truly losing branch for us — outright refusal — is addressed by Door 1 costing us nothing.
- Proposal uses a 30-day validity & signature block — send the HTML (Print / Save as PDF) rather than the editable .md.
- **HTML deliverables are self-contained.** Open `client/*.html` in any browser; diagrams are embedded as SVG data URIs, so they render offline. Use the on-screen **Print / Save as PDF** button for the client copy. Regenerate all client HTML after any `.md` edit with `python3 internal/build-client-html.py` (04 and 05 are table/text-based and contain no Mermaid diagrams).
- **Diagrams are Mermaid** in the `.md` sources. If editing the markdown, export through a Mermaid-aware renderer (GitHub, VS Code, Typora, Obsidian, mermaid.live) or convert to PNG/SVG before PDF export. Every chart is paired with a table or bullet list so the numbers survive even if a renderer does not support Mermaid (e.g. `xychart` and `quadrantChart` need Mermaid v10.6+).
- **Reference links:** use `mkt.gabochie.com` everywhere in client-facing material. Do not use the retired legacy domain anywhere in this project.
- **Paid ads:** the client has explicitly refused paid advertising (fear of revenue-authority targeting/tracking). Do not pitch ad spend in the first 30 days; the plan is organic, owned and referral-led, with no ad pixels or audience uploads. Revisit only after Day 90, and only with written consent.
- **Klagon showroom:** there is no frontage signboard. Signage + geotagged photos are non-negotiable Week-1/2 items for Google Business Profile prominence and buyer verification. See `client/03`.
- **Tone audit done (6 Nov):** softened for a founder-couple (older generation, grown Gen Z children) — candid audit language stays internal; glossary added; "You have spent"-%narration removed in favour of analysis-led; the trust package = KPI-tied payments (§5) + trust architecture (§6) + the giveaway audit summary (`client/02`). Keep the softened tone in any verbal delivery too: respect the 26-year legacy first, opportunity second.
- If DS only wants the cheaper path: fallback = portfolio Option A now, move to Option B at Day 90 review.
- **Option D is the recommended lead.** It is the private, legacy-led B2B partnership (no public ads, no branded sponsored posts, no ad tracking) in `client/01` §5. Open the pitch with it when the client raises GRA/revenue-authority visibility or says "we could just use our own staff." Path A = done-for-you (GHS 4,000 setup + GHS 5,500/mo + 1% success fee, 3–5 guaranteed site-measurement invitations/mo); Path B = in-house engine build (GHS 12,000–15,000 setup/training + GHS 3,000/mo oversight). The close: build a free sample Heritage Portfolio from 3 iconic project photos before they pay a cedi.
- If the client wants the digital visibility system too, layer Option B/C on top of Option D — never pitch paid ads before Day 90 or without written consent.
- If asked "why you and not an agency?", use proposal §7 (architect + built-environment tech + shipped SME systems).
- Keep numbering straight: **client** = 00 simple decision guide · 01 proposal · 02 audit-summary giveaway · 03 30-day foundations · 04 Option D agreement · 05 Heritage Portfolio sample. **internal** = 02 audit · 03 plan · 04 fees · 05 sales system.

*All client names/marks referenced (Ashesi, GNAT, Toyota Ghana, K3, Emmaldo…) derive from public web research Nov 2026 — validate before print.*
