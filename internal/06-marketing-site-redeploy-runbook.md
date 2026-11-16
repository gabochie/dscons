# Runbook — Redeploying gabochie-mkt → mkt.gabochie.com

**Status (6 Nov 2026, late session): LIVE at `https://mkt.gabochie.com`.** Repo renamed `gabochie-mkt` → `mkt-gabochie`; Pages builds from `staging` (root); CNAME fixed on `master` + `staging`; Cloudflare CNAME `mkt → gabochie.github.io` (DNS-only) added and propagating; HTTPS serving 200; all PWA assets verified. `marketing.gabochie.com` is fully dead (NXDOMAIN). **Remaining:** "Enforce HTTPS" toggle in Pages settings (API returns 404 for that call), optional global domain sweep in secondary pages.

## Status matrix

| URL | Status | Note |
|---|---|---|
| gabochie.com | ✅ LIVE | Gabochie Corp HQ site — working |
| github.com/gabochie | ✅ live | 20 repos; bio says "Available for projects and freelance" (typo: "freelancec" — fix) |
| gabochie/mkt-gabochie | ✅ repo active | Renamed from `gabochie-mkt`. Static HTML site: index.html, blog/, services/, tools/, admin/, client/, assets/, manifest.json, sw.js, CNAME |
| mkt.gabochie.com | ✅ LIVE | **Owner choice 6 Nov 2026 — canonical subdomain** (prefers `mkt` over `marketing`). Serves from GitHub Pages (CNAME → gabochie.github.io, DNS-only). Repo: `gabochie/mkt-gabochie`, Pages source branch **`staging`** (root). Custom domain + CNAME file fixed to `mkt.gabochie.com`; `marketing.gabochie.com` fully removed (NXDOMAIN) |
| studio.gabochie.com | ✅ LIVE | Verified 6 Nov 2026: resolves to same Cloudflare IPs as gabochie.com (172.67.155.59 / 104.21.82.82). Approved redirect target for legacy content, if any |
| gabochie-marketing.business.site | ? | Old Yellow Pages listing pointed here (Google business.site URLs were sunset by Google in 2024 — assume dead) |

## Redeploy steps (completed 6 Nov 2026)

1. **Enable Pages:** github.com/gabochie/mkt-gabochie → Settings → Pages → source branch **`staging`**, root. Build verified.
2. **Custom domain:** `mkt.gabochie.com` set in Pages settings; CNAME file committed as `mkt.gabochie.com` on both `staging` and `master`.
3. **DNS record:** Cloudflare CNAME `mkt → gabochie.github.io`, **DNS-only (grey cloud)** — added and live (verified resolving + HTTPS 200).
4. **Verify:** mkt.gabochie.com renders over HTTPS; sitemap/robots reachable; `marketing.gabochie.com` confirmed gone (NXDOMAIN).
5. **Watch-outs:**
   - `backend/` and `supabase/` folders suggest features (admin, pay.html, referral, free-audit forms) that need Supabase keys env — for a fast redeploy, ensure those pages degrade gracefully or temporarily hide in nav if they error.
   - `ga*scripts`/keys: if old integrations (Supabase, payment) have lapsed, stub them before pitching DS traffic to the site.

## PWA / mobile-install support (added this session)

- `manifest.json` upgraded: `id`, `scope`, `lang`, categories, install shortcut (Free Audit), icons = PNG 192 + PNG 512 + maskable 512 + SVG fallback.
- Icons regenerated from the `favicon-pin.svg` geometry (brand green `#1A7B3A` pin); `apple-touch-icon.png` replaced at 180×180 (opaque).
- `sw.js` service worker: precache core shell, network-first for navigations (offline fallback `/offline.html`), cache-first for static assets, stale-while-revalidate updates; excludes `/admin/`, `/client/`, `/api/` from caching.
- `assets/js/pwa.js`: registers the SW and shows an "Install app" button when `beforeinstallprompt` fires; auto-hides after install.
- `index.html`: apple/mobile web-app meta tags, `apple-touch-icon` sizes, PWA script include; canonical + JSON-LD URL moved to `https://mkt.gabochie.com`.
- Committed to `staging` (`af24b40`) and `master` (`9ee2f3d`); Pages rebuilt; all assets verified live over HTTPS.
- **Mobile bottom bar (added):** app-style fixed tab bar on <768px — Home · How It Works · **Free Audit** (raised green CTA) · Blog · WhatsApp (`wa.me/233506384917`), with active-tab highlighting, safe-area padding, and content offset so the footer isn't hidden. Injected site-wide via `assets/js/bottom-nav.js` on 20 public pages (index, free-audit, legal, referral, saas-vote, ai-agent-architecture, blog/*, services/*); the old floating bottom-right CTA is hidden on mobile to avoid duplication; the "Install app" pill is lifted above the bar. Committed `d3f8ea7` (staging) / `13a6658` (master), verified live.
- **App-feel polish (added):** mobile header slimmed to logo-only (brand text + hamburger + mobile accordion hidden — bottom bar is the nav); top bar auto-hides on scroll down / re-shows on scroll up; subtle page fade-in; tab press scale + `navigator.vibrate(8)` tap feedback (Android). Committed `9c45b6d` (staging) / `861d981` (master), verified live.
- **Optional next:** PWA screenshots for a richer install sheet.
- **Partial:** `marketing.gabochie.com` references replaced in `index.html`, `sitemap.xml`, `robots.txt` only — blog/services/tools/admin pages may still carry the old domain (global replace pending).

## Strategic note (why this matters for the DS proposal)

The proposal references the consultant's live machinery: a **dead link is a credibility leak**. Actions:
- Redeploy before pitching, OR
- Edit proposal references (already sanitized: client-facing material now anchors on `mkt.gabochie.com`, which is live, plus Archinect).
- Legacy standalone domain retired — **not used anywhere in this project**. All active references point to `mkt.gabochie.com`. The SME-tools offer lives as a product under Gabochie Corp (`studio.gabochie.com` / Gabochie Corp products) rather than a separate lifetime domain.

## Follow-ups for Gideon

- [x] Enable GitHub Pages on gabochie-mkt (branch deploy) — Pages is live, build "built"; **source branch is `staging`, not `master`** (the site was already enabled on staging before token work began)
- [x] Rename repo to `mkt-gabochie` (API, completed this session)
- [x] Fix CNAME file on both `master` and `staging` → `mkt.gabochie.com`; Pages `cname` confirms `mkt.gabochie.com`
- [x] Add CNAME record `mkt.gabochie.com → gabochie.github.io` at DNS host — done, DNS-only; verified resolving to GitHub Pages + HTTPS 200
- [ ] Enforce HTTPS; retest all 6 top pages **← user clicks after DNS propagates; or hand me a Cloudflare API token to automate**
- [ ] Global replace remaining `marketing.gabochie.com` → `mkt.gabochie.com` in blog/services/tools/admin pages + their canonicals (index, sitemap, robots already done)
- [ ] Optional: PWA screenshots for richer install UI
- [x] Mobile bottom tab bar — live on 20 public pages (see PWA section)
- [ ] Fix GitHub bio typo ("freelancec") — token lacked account scope
- [x] **DECIDED (owner, 6 Nov 2026):** the legacy standalone marketing domain is retired and **must not be used anywhere in this project**; all active references point to `mkt.gabochie.com`. The SME productivity/revenue tools become part of the **Gabochie Corp product pipeline** (alongside Gabochie Design, BuildCostGH, GHBC, AEC Agent API, AEC Project OS). Proposal §7 now anchors the machinery story on `mkt.gabochie.com` — no further edits needed. Keep the product name under the existing "Gabochie Corp → Products/Membership" structure rather than re-launching a separate domain.
- [ ] Before retirement: check github.com/gabochie repos (20 total) for a backup of the legacy marketing codebase; screenshot/archive its best tools (quote automation, WhatsApp scripts) as product-iteration baseline
- [x] **Do not renew or re-register the legacy domain.** Leave it parked/unused; all active references are `mkt.gabochie.com` (owner decision, 6 Nov 2026)
