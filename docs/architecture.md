# Repository Architecture

**ogkranthi.github.io** — static blog published via GitHub Pages.

---

## Tech Stack

- **No build tools.** Every page is a hand-authored HTML file with inline CSS. No Jekyll, no static site generator, no bundler.
- **Fonts:** Inter (sans), Newsreader (serif), JetBrains Mono (mono) — loaded from Google Fonts.
- **Diagrams:** Inline SVG inside each post HTML file.
- **Automation:** GitHub Actions + Python 3 (standard library only).

---

## Directory Layout

```
ogkranthi.github.io/
├── index.html                          # Homepage (hero, post grid, featured essay)
│
├── # — Post pages (one file per article)
├── engram.html
├── pediatric-disaster-edge-ai.html
├── distillation-rl-guardrails.html
├── autoresearch-harness-engineering.html
├── governed-agent-distribution.html
├── openclaw-control-plane-agents.html
│
├── # — Claude Certified Architect guide (multi-part series)
├── claude-certified-architect-guide.html
├── claude-certified-architect-strategy.html
├── claude-certified-architect-domains.html
│
├── # — Auto-generated on every push to main
├── feed.xml                            # RSS 2.0 feed
├── sitemap.xml                         # XML sitemap
├── robots.txt                          # Points crawlers to sitemap
│
├── .github/
│   ├── workflows/
│   │   ├── update-featured.yml         # Triggered on *.html push to main
│   │   ├── weekly-blog-ideas.yml       # Cron: creates GitHub issues from topic queue
│   │   └── assign-blog-issues-to-copilot.yml  # Label trigger: routes issues to Copilot
│   ├── scripts/
│   │   └── update-featured.py          # Updates featured post, feed, sitemap
│   ├── ISSUE_TEMPLATE/
│   │   └── blog-post.yml               # Structured template for new article issues
│   └── blog-topic-queue.json           # Queue of upcoming article ideas
│
└── docs/
    ├── architecture.md                 # This file
    ├── plans/                          # Per-article implementation plans
    └── superpowers/specs/              # Design specs from brainstorming sessions
```

---

## Publishing: GitHub Pages

The site is served directly from the `main` branch root — no `gh-pages` branch, no `_config.yml`, no `.nojekyll` needed. GitHub Pages serves the root as static files.

**Live URL:** `https://ogkranthi.github.io`

Every merge to `main` is live within ~30 seconds. There is no build step.

---

## Design System

All pages share the same inline CSS. Variables are declared in `:root` and used throughout.

```css
:root {
  --bg: #fafaf9;           /* page background */
  --bg-elevated: #ffffff;  /* cards */
  --text-primary: #1a1a1a;
  --text-secondary: #555555;
  --text-muted: #999999;
  --accent: #1e40af;       /* blue — nav CTA, labels, italic title accents */
  --accent-dim: #1e3a8a;   /* hover state */
  --accent-light: #dbeafe; /* light blue tint */
  --border: #e8e8e5;
  --serif:  'Newsreader', Georgia, serif;
  --sans:   'Inter', -apple-system, sans-serif;
  --mono:   'JetBrains Mono', monospace;
}
```

**Post category tag colors** (index.html only):

| Variable        | Category   | Use |
|-----------------|------------|-----|
| `--tag-cloud`   | `#1e40af`  | Cloud / AI Agents |
| `--tag-llm`     | `#0f766e`  | LLM / Architecture |
| `--tag-robotics`| `#854d0e`  | Edge AI / Robotics |
| `--tag-safety`  | `#991b1b`  | AI Safety |
| `--tag-hitl`    | `#3730a3`  | HITL / Certification |

---

## SEO & Discoverability

Every page includes:

| Signal | Implementation |
|--------|---------------|
| Canonical URL | `<link rel="canonical" href="https://ogkranthi.github.io/[page].html">` |
| Open Graph | `og:title`, `og:description`, `og:type` |
| Twitter Card | `twitter:card: summary`, `twitter:site: @ogkranthi` |
| JSON-LD | `WebSite` schema on homepage; `Article` schema on post pages |
| RSS feed | `<link rel="alternate" type="application/rss+xml" href=".../feed.xml">` |
| Sitemap | `/sitemap.xml` referenced in `robots.txt` |

---

## Post Card Pattern (index.html)

Each article in the grid is an `<article>` tag with two data attributes the JS and Python automation depend on:

```html
<article class="post-card reveal"
         data-category="cloud"
         data-date="2026-03-16"
         onclick="window.location.href='openclaw-control-plane-agents.html'">
  <h3>Post Title</h3>
  <p class="post-excerpt">One-sentence excerpt.</p>
  <span class="post-date">Mar 2026 · 15 min</span>
</article>
```

- **`data-date`** — used by client-side JS to auto-populate the featured essay section with the newest post.
- **`data-category`** — drives the filter buttons in the grid.
- Cards go **newest first** in the DOM. Placeholder/upcoming cards use `onclick="window.location.href='#'"`.

The post count badge is kept in sync by the Python script:

```html
<span class="count">16 Posts</span>
```

---

## Automation: `update-featured.yml`

**Trigger:** Any push to `main` that touches a `*.html` file.

```
push to main (*.html changed)
        │
        ▼
python3 .github/scripts/update-featured.py
        │
        ├── reads index.html
        ├── finds first real post-card (newest by DOM order)
        ├── if featured card href ≠ first card href → patches onclick URL
        ├── if post count ≠ <span class="count"> value → patches count
        ├── rewrites index.html if changed
        ├── generates feed.xml (RSS 2.0 from all real cards)
        └── generates sitemap.xml (all *.html files + last-modified dates)
        │
        ▼
peter-evans/create-pull-request@v6
        │
        └── opens PR on branch: auto/update-featured-{run_id}
            files: index.html, feed.xml, sitemap.xml
            base: main
```

This means automation changes never push directly to `main` — they always come in as a reviewable PR.

### What the script updates

| Output | Trigger | Method |
|--------|---------|--------|
| `featured-card` onclick URL | First post card href changed | Regex patch on `<div class="featured-card" ...>` |
| `<span class="count">` | Post card count changed | Regex patch |
| `feed.xml` | Always regenerated | Builds RSS 2.0 from all cards with `data-date` |
| `sitemap.xml` | Always regenerated | Globs all `*.html`, reads file mtimes |

---

## Automation: `weekly-blog-ideas.yml`

**Trigger:** Cron — every Tuesday at 3:15 PM UTC.

**What it does:**
1. Reads `.github/blog-topic-queue.json` for queued topics.
2. Queries existing GitHub issues to find the first queued topic not yet filed.
3. Creates a new GitHub issue using that topic's title, body, and labels.
4. Assigns the issue to `copilot-swe-agent[bot]` via `COPILOT_ASSIGN_PAT` secret.

The issue body (from the queue file) contains: thesis, audience, key points, diagram requirements, and source links — everything Copilot needs to draft the article.

---

## Automation: `assign-blog-issues-to-copilot.yml`

**Trigger:** Any issue labeled `blog-draft`, `blog-refresh`, or `blog-publish`.

Assigns the issue to Copilot automatically so it can start working without manual triage.

---

## Blog Topic Queue

`.github/blog-topic-queue.json` is an array of article ideas:

```json
[
  {
    "title": "Article title",
    "status": "queued",
    "labels": ["blog-draft"],
    "body": "Full issue body: thesis, audience, key points, diagram specs..."
  }
]
```

Status values: `queued` → picked up by weekly workflow. Once an issue is created the status should be updated to `issued` to prevent duplicates.

---

## Adding a New Post: Checklist

1. **Create the HTML file** — copy the structure from an existing post (e.g., `governed-agent-distribution.html`). Include: `<meta>` block, JSON-LD Article schema, canonical URL, inline CSS, nav with Newsletter + LinkedIn buttons.

2. **Add a post card in `index.html`** — insert at the TOP of `<div class="posts-grid">` with correct `data-date` and `data-category`.

3. **Update the post count** — change `<span class="count">N Posts</span>`.

4. **Merge to main** — the `update-featured.yml` workflow will automatically open a PR updating the featured section, `feed.xml`, and `sitemap.xml`.

### SVG Diagram sizing rule

Every `<rect>` containing text must satisfy:

```
min_height = (number_of_text_lines × 14) + 24
```

- First text baseline: `rect_y + 20`
- Each subsequent line: `+14px`
- Verify: `last_text_y + 12 ≤ rect_y + height`
- Update arrow `y1`/`y2` to align with new rect center after any height change.

---

## Navigation Structure

```
Header (fixed, blurred)
  Logo "Kranthi Manchikanti."
  Nav: Writing · About · Newsletter → · LinkedIn →

Homepage sections
  Hero       (#hero)
  Featured   (auto-populated by JS from newest post-card)
  Writing    (#writing — post grid with category filter)
  About      (#about)

Footer
  Logo · GitHub · X/Twitter · Email
```

Post pages share the same header. They link back to `/#writing` and `/#about`.

---

## Client-Side Featured Post Logic

On page load, a small IIFE in `index.html` reads all `.post-card` elements, finds the one with the highest `data-date` value, and populates four elements:

```js
document.getElementById('featured-card')  // onclick URL
document.getElementById('featured-title') // h2 text
document.getElementById('featured-excerpt') // p text
document.getElementById('featured-date')   // date string
```

This means the featured essay always reflects the newest published post without any manual update — the server-side Python script additionally patches the onclick href for RSS readers and crawlers that don't run JS.
