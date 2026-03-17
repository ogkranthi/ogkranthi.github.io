# Homepage Redesign — Conversion-First Personal Brand

**Date:** 2026-03-17
**Status:** Approved
**Goal:** Transform index.html from a blog-first site into a conversion-first personal brand hub that attracts speaking invitations and project/collaboration opportunities.

---

## Context

The current site is blog-first: writing is the hero, the About section is secondary, and there are no dedicated sections for speaking history, projects, or contact pathways. The redesign transforms the homepage so that Kranthi's identity, credibility, and availability lead — with writing demoted to supporting evidence.

**Primary goals:**
1. Get invited to speak at conferences, workshops, and panels
2. Get brought in for AI architecture projects and collaborations

**Reference inspiration:** karuparti.com (personal brand hub pattern)
**Chosen approach:** Conversion-First Profile (Approach B) — every section feeds the two goals

---

## Page Structure

### Navigation (updated)
```
Speaking · Projects · Writing · Newsletter · Contact
```
- Remove current "About" nav item (About content merged into hero)
- Add "Speaking", "Projects", "Contact" as anchor links
- Keep "Newsletter" linking to Substack
- LinkedIn moves out of nav (into Connect section)

---

### Section 1: Hero (full replacement)

**Label (mono uppercase):** `AI Architect · Speaker · Builder`

**Headline (serif, large):**
> "I design AI agent systems that make it from *research to production* — and I'm available to speak, collaborate, and build."

**Subtitle:**
> Enterprise AI architecture across high tech, finance, healthcare, and regulated industries. Production systems at scale, not proof-of-concepts.

**CTAs (side by side):**
- Primary (dark filled button): `Invite Me to Speak →`
- Secondary (outline button): `Start a Project →`
- Both link to `#connect` anchor

**Credibility stats strip (4 columns, below CTAs):**
| Stat | Label |
|------|-------|
| 100+ | Architectures Piloted |
| 6+ | Industries |
| 10+ | Conferences & Workshops |
| Weekly | Publishing |

> Note: The 10+ stat is accurate — the 6 talk cards in the Speaking section are a curated subset, not the full history. The stat and card count mismatch is intentional. Cards show the most notable/documented appearances; the stat reflects the full count.

**What's removed:** topic pills, featured post slot from hero area

---

### Section 2: Speaking & Workshops

**Anchor:** `#speaking`
**Section label (mono uppercase):** `Speaking & Workshops`

**Intro line:**
> "Available for conference talks, workshops, and panels on AI architecture, agentic systems, and enterprise AI deployment."

**Talk cards** — grid layout, each card shows:
- Event name + year
- Talk/workshop title
- Type tag: `TALK` / `WORKSHOP` / `PANEL`
- External link icon (where URL exists)

**Talk card data:**

| Event | Year | Title | Type | URL |
|-------|------|-------|------|-----|
| AWS re:Invent | 2022 | Amazon Managed Blockchain — Workshop | WORKSHOP | https://catalog.us-east-1.prod.workshops.aws/workshops/fa60245b-9832-4910-8183-0616997a9ebf/en-US |
| AWS Summits | 2022–2023 | Amazon Managed Blockchain — Workshop | WORKSHOP | https://catalog.us-east-1.prod.workshops.aws/workshops/fa60245b-9832-4910-8183-0616997a9ebf/en-US |
| DevOps Summit Canada | 2023 | Unleashing the Power of Amazon CodeWhisperer | TALK | — |
| AWS Symposium | 2024 | Chain of Verification Agent | TALK | — |
| Microsoft Agentic AI Workshop · Boston | 2025 | Agentic AI Workshop | WORKSHOP | — |
| Midwest Architecture Talk | (year unknown — omit year field on card) | Perimeterless Security | TALK | — |

**Topics I speak on** (pill tags below cards):
`Agentic AI Architecture` · `Enterprise AI Strategy` · `Cloud + AI Integration` · `Responsible AI` · `Blockchain & Web3`

**CTA:**
> "Organizing a conference or workshop? I'm available for 2026."
> `Get in Touch →` → links to `#connect`

---

### Section 3: Projects & Contributions

**Anchor:** `#projects`
**Section label (mono uppercase):** `Projects & Contributions`

**Intro line:**
> "Production systems shipped across cloud, AI, and blockchain. Open-source contributions, industry standards work, and original research."

**Project cards** — each shows: title, one-line description, tag, external link where available:

| Title | Description | Tag | URL |
|-------|-------------|-----|-----|
| GPT-RAG | Original contribution to retrieval-augmented generation architecture | `OPEN SOURCE` | — (no external link for now — add when repo URL confirmed) |
| LLMOps Workshop | End-to-end LLM operations framework | `OPEN SOURCE` | — (no external link for now — add when repo URL confirmed) |
| AWS Managed Blockchain Workshop | Co-authored and presented at re:Invent & AWS Summits | `WORKSHOP` | https://catalog.us-east-1.prod.workshops.aws/workshops/fa60245b-9832-4910-8183-0616997a9ebf/en-US |
| Ballerina OCI | Public cloud module for open source — spearheaded ideation to implementation | `OPEN SOURCE` | https://github.com/oracle/ballerina-oci |
| Oracle Blockchain — Wine Distribution | Built and led the blockchain integrity system for wine distribution | `CASE STUDY` | https://blogs.oracle.com/cloud-infrastructure/post/oracle-blockchain-commits-to-wine-distribution-integrity |
| SageMaker Clarify | AI fairness and explainability tooling | `OPEN SOURCE` | — (no external link for now — add GitHub URL when confirmed) |
| Linux Foundation Courses | Co-authored LFD272 (Hyperledger Fabric for Developers) + HFCP certification exam | `CERTIFICATION` | https://training.linuxfoundation.org/training/hyperledger-fabric-for-developers-lfd272/ |
| NIST AI Agents Response | Peer review: Practices for Automated Benchmark Evaluations of LLMs | `STANDARDS` | — |
| Cloud Security Alliance | Co-authored: Quantum Computing & Artificial Intelligence | `STANDARDS` | — |
| GenAI Component in Web3 Workshop | Embedded GenAI module into AWS Blockchain workshop | `WORKSHOP` | https://catalog.workshops.aws/buildweb3/en-US/module2 |
| RAGAs Framework | Customer-deployed evaluation framework for RAG applications | `OPEN SOURCE` | — (no external link for now) |

**CTA:**
> "Interested in building together?"
> `Start a Project →` → links to `#connect`

---

### Section 4: Writing

**Anchor:** `#writing`
**Section label:** `Writing`

Existing posts grid — kept largely intact but:
- Remove the "featured post" hero card (or keep as a compact featured strip, not full-width hero)
- Keep the post count and category filter pills
- "See all posts" link if the grid is truncated

Show the **6 most recent posts** in the grid. No truncation logic needed — if more than 6 exist, show the 6 newest. Add a "View all writing →" link below the grid pointing to the full posts list (already rendered below in the same page).

---

### Section 5: Newsletter

Existing Substack embed — kept as-is.

---

### Section 6: Connect

**Anchor:** `#connect`
**Section label (mono uppercase):** `Connect`

**Headline:**
> "Let's build something."

**Availability statement:**
> "Currently available for: conference talks and workshops, AI architecture consulting, open-source collaborations, and advisory roles."

**Three contact paths (cards or prominent links):**
- `Email` → direct email link
- `LinkedIn` → linkedin.com/in/kranthimanchikanti/
- `X / Twitter` → x.com/ogkranthi

**Optional:** Short note: *"Response time: within 48 hours for speaking and project inquiries."*

---

## Design System (no changes)

- Fonts: Inter (sans) · Newsreader (serif) · JetBrains Mono (mono)
- Colors: existing blue accent (`#1e40af`), off-white bg, dark text
- Component patterns: same `.callout`, `.compare-table`, `.arch-block`, `.cta-section` patterns
- Existing components reused: `.cta-section`, `.cta-btn`, `.cta-btn-ghost`, `.article-label`, `.compare-table` (confirmed present in current stylesheet)
- New components needed: `.talk-card`, `.project-card`, `.stats-strip`, `.topics-pills`
- GitHub star counts on project cards must be **static hardcoded values** — the site has no build step or JS data fetching. Update manually when counts change significantly.

---

## Content Assets Needed

All of these exist — they need to be surfaced, not created:

- Talk titles and years (confirmed above, user to verify dates/add missing)
- Project URLs (most confirmed above)
- Email address for Connect section
- GitHub profile for SageMaker Clarify, GPT-RAG repos (for star counts)
- Any additional talks the user recalls ("I might have more")

---

## What Does NOT Change

- All existing blog post HTML files — untouched
- feed.xml, sitemap.xml, robots.txt — auto-updated by existing GitHub Action
- The overall monochrome + blue accent design system
- The newsletter Substack embed

---

## Success Criteria

- A conference organizer who lands on the homepage can find the Speaking section within 2 scrolls
- The speaking section shows ≥6 talk cards with titles and venues
- Both CTAs ("Invite Me to Speak" and "Start a Project") resolve to the Connect section
- The projects section shows ≥8 cards with real external links where available
- Mobile: all sections readable and navigable without horizontal scroll
