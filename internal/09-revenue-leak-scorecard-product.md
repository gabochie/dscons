# Revenue Leak Scorecard — Product Draft (Gabochie Marketing)

**Status:** Draft v0.1 · 6 Nov 2026 · internal use (do not send)
**Build status:** Landing page + interactive 16-question scorecard **LIVE** at https://mkt.gabochie.com/business-systems-audit/ (staging `ba72689` / master `54974ad`). Capture currently posts to the **free Apps Script endpoint** (same one as `free-audit.html`), so each result becomes a row in the **Leads** Google Sheet (`source = revenue-leak-scorecard`, score/band/top leaks/answers in Notes). Supabase capture is coded and the migration kept at `supabase/migrations/20261107000001_scorecard_capture.sql` (form_submissions insert policy + admin read + scorecard→lead trigger) — **switch back once the Supabase project is paid/active**, then backfill the sheet rows. Fallback on failure: prefilled WhatsApp/email handoff.
**Owner:** Gideon B. Abochie (Gabochie Marketing)
**One-liner:** A free 3-minute diagnostic that scores a Ghanaian SME's business systems across 8 domains and estimates, in GHS, how much revenue leaks every month — then sells the fix.

---

## 1. Positioning

- **Category:** business-systems diagnostic + implementation (not "consulting", not "audit").
- **Promise:** "Find the leaks before they cost you another quarter."
- **Narrative:** Most SMEs don't have broken marketing — they have broken *systems* between the lead and the money: slow response, no follow-up, manual bookings, untracked payments, no reviews, WhatsApp chaos, no numbers, no AI.
- **Differentiator:** Ties every finding to a monthly GHS leak figure, then a 90-day fix roadmap. Architect + built-environment systems thinking, not generic digital-agency talk.
- **Brand:** run under Gabochie Marketing as a second line (`/systems-audit`), not a separate brand yet. Cross-sell with the Google Maps visibility offer.

**Anti-positioning:** do not sell "AI transformation" as the headline, and do not lead with "audit" in the name — SMEs buy outcomes and speed.

---

## 2. Ideal client / anti-client

**Good fit**
- Ghanaian SME, 5–50 staff, GHS 50k–500k monthly revenue
- 20+ inbound inquiries/month (calls, WhatsApp, DMs, walk-ins)
- Owner-operated; owner is the bottleneck
- Has ambition to scale or is losing deals they "don't know why"

**Poor fit**
- Pre-revenue / no consistent inquiries (sell visibility first)
- Enterprise with an internal ops team (procurement cycle too long for a pilot)
- Wants only a website (sell the WordPress/visibility offer)

---

## 3. Offer ladder

| Stage | Offer | Price (indicative) | Goal |
|---|---|---|---|
| 1 | **Revenue Leak Scorecard** (free, 3 min) | Free | Lead capture, instant value |
| 2 | **20-min debrief call** | Free | Qualify, build trust |
| 3 | **Deep Systems Audit** (2 weeks) | GHS 1,500–3,000, credited 100% toward Stage 4 | Paid commitment, roadmap |
| 4 | **90-Day Fix Sprint** (implementation) | GHS 4,000–8,000/mo retainer (3 tiers) | Core revenue |
| 5 | **Ongoing ops retainer** | GHS 2,500+/mo | Recurring |

Pricing calibrated in pilot; do not publish Stage 3+ prices until 2 pilots validate.

---

## 4. The scorecard — 8 domains, 16 questions

Each domain = 2 questions. Each answer scored **0 / 1 / 2 / 3**. Domain max = 6.

### A. Lead capture & response speed (weight 20%)
1. When a lead comes in (call, WhatsApp, form, walk-in), where does it land?
   - 0 nothing formal · 1 owner's head/chats only · 2 one shared inbox/sheet · 3 tracked in CRM/board with owner assigned
2. How fast does a new lead get a first human response on a working day?
   - 0 >24h or never · 1 same day (a few hours) · 2 under 1h · 3 under 15 min, every time

### B. Follow-up & pipeline (weight 20%)
3. What happens to a lead that doesn't buy today?
   - 0 dropped · 1 "I'll remember" · 2 informal list/chat reminder · 3 scheduled multi-touch follow-up (3+ touches)
4. Can you name your current pipeline right now (who, stage, next action, value)?
   - 0 no idea · 1 roughly, in my head · 2 a sheet/notebook · 3 live pipeline with stages + next actions

### C. Booking & scheduling (weight 12%)
5. How are appointments/quotes/site visits booked?
   - 0 ad-hoc over chats · 1 manual calendar entry by owner · 2 shared calendar with manual entry · 3 self-booking link or automated scheduling
6. How many booked appointments no-show or get rescheduled per month?
   - 0 don't track · 1 most · 2 a few · 3 under 10% with reminders

### D. Payments & invoicing (weight 12%)
7. How do you invoice and track what's owed?
   - 0 no records · 1 notebook/chat memory · 2 spreadsheet with manual follow-up · 3 invoicing tool with automatic reminders
8. What share of invoices is paid late?
   - 0 don't know · 1 >50% · 2 20–50% · 3 <10% or prepaid

### E. Reviews & reputation (weight 10%)
9. How are happy customers asked for a Google review?
   - 0 never · 1 occasionally, ad-hoc · 2 informal script · 3 systematic ask at a set moment
10. Do you respond to every review, and track rating trends?
    - 0 no · 1 sometimes · 2 most · 3 all + tracked monthly

### F. WhatsApp & comms automation (weight 10%)
11. Is there a written set of answers/scripts for the 10 most common inquiries?
    - 0 no · 1 in owner's head · 2 a doc nobody uses · 3 shared, used, updated
12. Are any responses/confirmations automated (auto-replies, templates, reminders)?
    - 0 none · 1 basic away message · 2 templates used manually · 3 automated flows

### G. Data & reporting (weight 10%)
13. Do you know inquiries, conversion rate, and average sale value for last month?
    - 0 no · 1 one of them, roughly · 2 two of them, roughly · 3 all three, accurate
14. How often do you review business numbers in a structured way?
    - 0 never · 1 when something feels wrong · 2 monthly, informal · 3 monthly review with decisions logged

### H. Agentic / AI readiness (weight 6%)
15. Is your business information (services, prices, availability, FAQs) written down somewhere a tool could read?
    - 0 no · 1 scattered in chats · 2 some docs · 3 structured, central, current
16. Are you using any automation/AI in the sales or service workflow today?
    - 0 none · 1 experimentation · 2 one tool in daily use · 3 multiple tools with measured time saved

---

## 5. Scoring bands

| Score | Band | Meaning | Leak range (see §6) |
|---|---|---|---|
| 0–25% | **Critical** | Systems are the growth ceiling; owner is the bottleneck | 30–45%/mo |
| 26–50% | **Leaking** | Real money lost weekly; fixes pay back fast | 18–30%/mo |
| 51–75% | **Developing** | Works, but fragile and not scalable | 8–18%/mo |
| 76–100% | **Solid** | Optimise and layer AI/automation | 3–8%/mo |

Also flag the **bottom 3 domains** immediately — these become the "priority leaks" in the report regardless of total score.

---

## 6. Leak quantification (indicative, calibrate on the call)

Formula, per domain:

```
gap_i     = 1 − (domain_score_i / 6)          // 0..1
leak_pct  = 45% × Σ (weight_i × gap_i)        // capped 3%..45%
leak_ghs  = monthly_inquiries × close_rate × avg_sale_value × leak_pct
```

Inputs captured on the debrief call (not in the free scorecard):
- monthly inquiries
- baseline close rate
- average sale value (GHS)
- monthly revenue (sanity check)

**Worked example:** 120 inquiries/mo × 25% close × GHS 1,500 = GHS 45,000 potential. Score 38% → leak_pct ≈ 27% → **≈ GHS 12,150/mo leaking**. State clearly: indicative, based on the owner's own numbers, refined in the paid audit.

Never present the leak figure as a guarantee; frame as "at your stated volumes, this is what the system gaps typically cost."

---

## 7. Deliverable (paid Deep Systems Audit)

1. Cover page: score, band, leak/mo, leak/yr
2. Leak waterfall: domain-by-domain GHS contribution
3. Top 3 priority leaks with evidence (from interviews/screenshots)
4. 90-day roadmap: Week 1 quick wins → Month 1 core fixes → Month 2–3 scale
5. Quick-win list the owner can start before signing implementation
6. Investment options (3 tiers) and expected impact per tier

Turnaround: 2 weeks. Include one 60-min findings presentation.

---

## 8. Funnel & lead mechanics

```
Ad / post / WhatsApp status / referral
        ↓
/business-systems-audit landing page
        ↓
Free scorecard (16 Q, 3 min) → email + WhatsApp number
        ↓
Instant score + top 3 leaks (tease, not full report)
        ↓
Auto-book 20-min debrief (Calendly/WhatsApp)
        ↓
Paid Deep Systems Audit → 90-Day Fix Sprint
```

Rules:
- Scorecard result shows score, band, top-3 domain flags, and a partial leak range — never the full GHS model (that's the debrief hook).
- Every result email links to the Google Maps audit too (cross-sell both directions).
- Add `?ref=` on all links for tracking.
- v1 build: static page + Google Form/Sheets + Looker Studio PDF; v2: embedded JS scorecard → Supabase (existing infra) + instant score + WhatsApp notification.

---

## 9. Landing page copy (draft)

**H1:** Where is your business leaking money?
**Sub:** Take the free 3-minute Revenue Leak Scorecard. Get a score across the 8 systems that decide whether inquiries become paying customers — and the GHS value of your biggest leaks.
**CTA:** Take the free scorecard
**Micro-trust:** No jargon. No sales call required. Built by the team behind [DS Construction audit] and the Google Maps Profit System.

**Section — "You're not losing to competitors. You're losing to gaps."**
Slow first response. No follow-up. Bookings in WhatsApp. Invoices in a notebook. No reviews. No numbers. That's where the money goes.

**Section — What you get (free)**
- A 0–100 systems score across 8 domains
- Your 3 biggest leak areas, ranked
- An indicative GHS range you're losing monthly
- A 1-page next-step plan

**Section — How it works**
1. Answer 16 questions (3 minutes)
2. Get your score and top leaks instantly
3. Book a free 20-minute debrief to see the full leak model

**Section — Who it's for**
Owner-run businesses with steady inquiries that "should" be converting better. Not for pre-revenue startups.

**FAQ**
- Is this just a sales pitch? The scorecard and score are free and yours to keep.
- Do I need to prepare anything? No — answer from memory; the debrief refines the numbers.
- What does it cost after? Only if you want the deep audit; it's credited toward implementation.
- Is my data safe? Contact details are used only to send your result and book the debrief.

**Final CTA:** Find your leaks in 3 minutes → Take the free scorecard

---

## 10. Launch plan and KPIs

**Pilot first (2–3 clients, discounted but paid):** validate questions, leak model acceptance, price sensitivity. Use the DS Construction engagement as the case study (with permission).

**Test targets to validate (assumptions, not forecasts):**
- Landing → scorecard start: 25%
- Start → complete: 60%
- Complete → debrief booked: 20%
- Debrief → paid audit: 25%
- Paid audit → implementation: 40%

**Instrument:** page views, start, complete, email capture, debrief booked, audit sold, average ticket, time-to-close.

---

## 11. Build notes (site integration)

- New page: `/business-systems-audit` (static HTML, same Tailwind CDN + components as the rest of the site).
- Include: bottom-nav script, PWA manifest already site-wide; add a nav link under "Services" and a home-page section cross-linking both audits.
- v1: form posts to Google Sheet; Zapier/Apps Script sends the result email + WhatsApp alert.
- v2: JS scorecard (scoring logic is deterministic — same rubric as §4/§5), Supabase table `scorecard_responses`, instant score rendering, PDF export.
- Keep the Google Maps audit untouched as the primary funnel; this is the secondary funnel until it proves out.

---

## 12. Open decisions

- Final name: **Revenue Leak Scorecard** vs "Business Leak Finder" (test in pilot)
- Paid audit price band and crediting terms
- Whether implementation tiers are published or quoted only
- Whether this runs under Gabochie Marketing or a "Gabochie Systems" sub-label
