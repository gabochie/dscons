# 07 — Working Modus Operandi: DS's New Website & Web Developer

**Situation (verified 6 Nov 2026):** DS rebuilt its website — **hand-coded static HTML (not WordPress)** — and added/refreshed social pages (Facebook existing, new Instagram `@d.s_construction_l.t.d`, LinkedIn legacy page). An IT/web vendor built it. This document defines how the consultant engagement works **alongside** that vendor, protects the client's assets, and avoids scope collisions.

---

## 1. Division of labour (RACI)

| Workstream | Consultant (Gideon) | Web vendor | DS staff |
|---|---|---|---|
| Strategy, positioning, offer architecture | **A/R** | C | Approve |
| Technical site fixes (titles/meta/OG/speed/links/form backend) | Brief + verify (A) | **R** | — |
| SEO landing pages & content | Write briefs + copy (**R**) | Publish/technical (R) | Approve |
| Google Business Profile, reviews, testimonials | **A/R** | — | Coordinate clients |
| Social media editorial calendar & scripts | **A/R** | — (optional posting) | Nov generation can support |
| Sales system / CRM / pipeline | **A/R** | — | Daily operation (Sales Coordinator) |
| Site hosting, domain, deployments | Commissioner (A) | **R** | Pay & own |
| Analytics G4/pixel setup | Brief (A) | Install (R) | Own the properties |

**Rule:** the consultant never rebuilds the site behind the vendor's back; all site changes go through briefs (or are done by the consultant only if the client explicitly prefers). This respects the existing investment and relationship, and avoids the classic "my guy vs your guy" friction in family firms.

## 2. Ownership & access checklist (kickoff, Day 1 — non-negotiable)

Confirm **who owns and controls** (the #1 trap: vendors register assets under their own names):
1. Domain dscons-gh.com — registrar account login
2. Hosting account — provider + login
3. WhatsApp number +233 50 182 5430 — whose SIM/phone? Register as **WhatsApp Business** under the company
4. Facebook page — role check: manager rights belong on **company** profiles, not held personally by the vendor
5. Instagram professional account — email/phone on file = company
6. LinkedIn page — admin access
7. Site source files (FTP/GitHub or otherwise) + any paid licences
8. New brand accounts: GA4, Google Business Profile, Search Console — created under **info@dscons-gh.com** with DS owner + consultant as users

Handover principle: **the company owns every account; specialists are granted access roles.** Get this in one line of the engagement letter.

## 3. Immediate technical correction brief (for the web vendor, Week 1)

Priority order:
1. **Test the quote/contact form end-to-end today** — static sites frequently have dead forms; if so, wire a working backend (Formspree/Netlify-style service or WhatsApp fallback CTA) *before* any promo traffic arrives
2. Install GA4 + Meta Pixel (consultant provides IDs)
3. Per-page titles & meta descriptions (consultant supplies copy); Open Graph tags for WhatsApp/IG link previews
4. Remove the public `/webmail` footer link; fix Privacy/Terms dead links; fix the wrong tel: hyperlink (+233 24 436 0846 → tel:+233244360846); restore product dropdown
5. Restore client logos (Ashesi, UG, Toyota Ghana, GNAT, GEA) to homepage; add testimonials as they're collected
6. Add favicon, robots.txt, sitemap.xml
7. Later (Phase 2): convert the 8 product cards into real product pages (consultant writes the content)

## 4. How this reshapes the proposal (already updated in `client/01`)

- Reframe: **the client has already made the right first move** — credit it explicitly (respectful to family + vendor, positions consultant as accelerator, not critic)
- Phase 1 shifts from "website emergency refresh" to "site activation & technical correction" (brief-based via the vendor)
- The **sales system** angle becomes even more central: a live WhatsApp line + quote CTAs with *no* intake, log, SLA or follow-up = the highest-value gap in the whole engagement
- New §8 item: collaborative engagement with the existing web developer

## 5. Vendor-management hygiene for DS (advise them)

- New WhatsApp number should replace borrowing lines for lead capture; publish it uniformly
- Agree a small **retainer for the web vendor** for 90 days of fixes (they know the codebase) — cheaper than parallel maintenance
- All future changes to the site go through a simple change-request log (even a WhatsApp group note) so nothing breaks silently
