# Distillation & RL Guardrails Blog Post — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Write and publish a ~2,500–3,000 word technical blog post titled *"Your API Is a Training Dataset: How Distillation Attacks Work and How to Stop Them"* as a new HTML page matching the existing blog style.

**Architecture:** Copy the HTML scaffold from `pediatric-disaster-edge-ai.html`, update all meta/content, write 7 sections of prose, embed 3 hand-drawn SVG diagrams, and add a post card to `index.html`.

**Tech Stack:** Vanilla HTML/CSS (no build tools), inline SVG diagrams, JetBrains Mono + Newsreader + Inter fonts (already loaded via Google Fonts), Mailchimp script (copy from existing post).

---

## Reference Files

- Template to copy: `pediatric-disaster-edge-ai.html`
- Index to update: `index.html` (post card at line ~802, count at line ~797)
- Design doc: `docs/plans/2026-02-25-distillation-rl-blog-design.md`
- Source article: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks

## HTML CSS Classes to Know

From `pediatric-disaster-edge-ai.html`:
- `.article-wrap` — max-width 760px centered container
- `.article-label` — mono uppercase tag above title
- `.article-title` — serif large heading, supports `<em>` for italic accent
- `.article-subtitle` — lead paragraph in secondary color
- `.article-meta` — date/read-time/author metadata bar
- `.article-body h2` — serif section headings
- `.article-body h3` — sans-serif sub-headings
- `.article-body p` — body paragraphs (font-weight 300)
- `.callout` — left-bordered highlight box with `.callout-label` and `<p>`
- `.arch-block` — dark code/diagram block with `<pre>` inside
- SVG diagrams go inline inside a `<div class="diagram-wrap">` with inline `<style>` for sizing

---

## Task 1: Create HTML scaffold

**Files:**
- Create: `distillation-rl-guardrails.html` (copy from `pediatric-disaster-edge-ai.html`)

**Step 1: Copy the template**

```bash
cp pediatric-disaster-edge-ai.html distillation-rl-guardrails.html
```

**Step 2: Update `<head>` meta tags**

Replace in `distillation-rl-guardrails.html`:

```html
<title>Your API Is a Training Dataset: How Distillation Attacks Work and How to Stop Them | Kranthi Manchikanti</title>
<meta name="description" content="How industrial-scale distillation attacks work, why RL makes them so powerful, and a layered guardrail checklist for every API and model builder.">
<meta property="og:title" content="Your API Is a Training Dataset: How Distillation Attacks Work and How to Stop Them">
<meta property="og:description" content="DeepSeek, Moonshot, and MiniMax ran 16M+ exchanges to steal Claude's capabilities. Here's how distillation attacks work mechanically — and how to stop them.">
```

**Step 3: Update article header HTML**

Find the `.article-label`, `.article-title`, `.article-subtitle`, `.article-meta` block and replace with:

```html
<div class="article-label">AI Security · Model Defense</div>
<h1 class="article-title">Your API Is a Training Dataset: <em>How Distillation Attacks Work and How to Stop Them</em></h1>
<p class="article-subtitle">DeepSeek, Moonshot, and MiniMax ran 16 million exchanges through 24,000 fraudulent accounts to extract Claude's capabilities. This is how distillation attacks work mechanically — and a layered guardrail checklist for every API and model builder.</p>
<div class="article-meta">
  <div class="article-meta-item">
    <span class="article-meta-label">Author</span>
    <span class="article-meta-value">Kranthi Manchikanti</span>
  </div>
  <div class="article-meta-item">
    <span class="article-meta-label">Published</span>
    <span class="article-meta-value">Feb 2026</span>
  </div>
  <div class="article-meta-item">
    <span class="article-meta-label">Read time</span>
    <span class="article-meta-value">16 min</span>
  </div>
  <div class="article-meta-item">
    <span class="article-meta-label">Category</span>
    <span class="article-meta-value">AI Security</span>
  </div>
</div>
```

**Step 4: Delete all existing article-body content** (everything between `<div class="article-body">` and its closing `</div>`) so you have a clean body to fill in.

**Step 5: Verify in browser**

Open `distillation-rl-guardrails.html` in a browser. Confirm: correct title, correct header text, empty body area below the meta bar.

**Step 6: Commit**

```bash
git add distillation-rl-guardrails.html
git commit -m "feat: add HTML scaffold for distillation attacks blog post"
```

---

## Task 2: Write Section 1 — The Heist

**Files:**
- Modify: `distillation-rl-guardrails.html` — inside `<div class="article-body">`

**Step 1: Add the section prose**

Paste inside `<div class="article-body">`:

```html
<h2>The Heist</h2>

<p>In late 2024 and early 2025, three Chinese AI labs — DeepSeek, Moonshot AI, and MiniMax — ran what Anthropic would later describe as an "industrial-scale" campaign to steal its most capable model's knowledge. Not by hacking servers. Not by acquiring training data. By <strong>talking to Claude</strong>.</p>

<p>Across roughly 24,000 fraudulent accounts, coordinated in distributed clusters designed to evade detection, the three companies generated over 16 million exchanges. They weren't looking for information. They were building a dataset — systematically eliciting Claude's reasoning traces, its agentic behaviors, its chain-of-thought patterns — everything needed to train a cheaper model to behave like a much more expensive one.</p>

<p>The scale is striking. <strong>MiniMax alone generated 13 million exchanges</strong>, focused almost entirely on agentic coding. When Anthropic released a new model, MiniMax pivoted within 24 hours to target the upgraded version. Moonshot collected 3.4 million exchanges targeting reasoning and computer-use capabilities. DeepSeek — smaller in volume but arguably most strategic — focused on generating chain-of-thought training data and finding ways to elicit responses that bypassed censorship filters.</p>

<p>This wasn't opportunistic scraping. It was a coordinated intelligence operation against a commercial AI system. And Anthropic only detected it because they built classifiers specifically designed to catch it.</p>

<div class="callout">
  <div class="callout-label">Why this matters to you</div>
  <p>You don't need to be Anthropic for this to be your problem. Any fine-tuned model with specialized capabilities — medical reasoning, legal analysis, domain-specific code generation — is a target. Your API is a training dataset if you're not treating it like one.</p>
</div>
```

**Step 2: Verify**

Open in browser. Confirm section renders with correct heading, paragraph styles, and callout box.

**Step 3: Commit**

```bash
git add distillation-rl-guardrails.html
git commit -m "feat: add Section 1 - The Heist"
```

---

## Task 3: Write Section 2 — What Is Model Distillation? + SVG Diagram 1

**Files:**
- Modify: `distillation-rl-guardrails.html`

**Step 1: Add section prose and first SVG diagram**

Append inside `.article-body`:

```html
<h2>What Is Model Distillation?</h2>

<p>Model distillation was invented as a compression technique. The idea is elegant: you have a large, expensive "teacher" model with strong capabilities, and you want a small, cheap "student" model that behaves similarly. Instead of training the student on raw data, you train it on the <strong>outputs of the teacher</strong> — its probability distributions, its reasoning traces, its answers. The student learns to mimic the teacher's behavior without needing the teacher's scale.</p>

<p>Legitimate distillation is how companies build efficient models for deployment. GPT-4 distilled into smaller variants. LLaMA fine-tuned on GPT-4 outputs (before OpenAI's terms changed). This is well-established ML engineering.</p>

<p>The attack version is the same technique applied without consent, at scale, against a commercial API. Instead of authorized access to the teacher's internals, attackers use the <strong>public API as a synthetic data generator</strong>. Every response is a labeled training example. Every reasoning trace is a dataset row. The student model trains on millions of these examples until it approximates the teacher's behavior — without any of the teacher's safety training, RLHF fine-tuning, or constitutional alignment.</p>
```

**Step 2: Add SVG Diagram 1 — Teacher-Student Distillation Loop**

Append after the prose:

```html
<!-- DIAGRAM 1: Teacher-Student Distillation Loop -->
<div style="margin: 2.5rem 0; padding: 2rem; background: #f8f8f7; border: 1px solid #e8e8e5; border-radius: 10px;">
  <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.62rem; letter-spacing: 0.12em; text-transform: uppercase; color: #999; margin-bottom: 1.25rem;">Fig. 1 — Illicit Distillation Loop</div>
  <svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:700px;display:block;margin:0 auto;" font-family="'JetBrains Mono', monospace">
    <!-- Teacher Model box -->
    <rect x="20" y="70" width="150" height="60" rx="6" fill="#1a1a1a" stroke="none"/>
    <text x="95" y="97" text-anchor="middle" fill="#fff" font-size="10" font-weight="500">TEACHER MODEL</text>
    <text x="95" y="113" text-anchor="middle" fill="#999" font-size="9">(Claude / GPT-4 / etc.)</text>

    <!-- Arrow: Teacher → API Queries -->
    <line x1="170" y1="100" x2="240" y2="100" stroke="#c4c4c0" stroke-width="1.5" marker-end="url(#arrow)"/>
    <text x="205" y="92" text-anchor="middle" fill="#999" font-size="8">Fraudulent</text>
    <text x="205" y="103" text-anchor="middle" fill="#999" font-size="8">API queries</text>

    <!-- Synthetic Output box -->
    <rect x="240" y="70" width="150" height="60" rx="6" fill="#fff" stroke="#e8e8e5" stroke-width="1.5"/>
    <text x="315" y="97" text-anchor="middle" fill="#1a1a1a" font-size="10" font-weight="500">SYNTHETIC OUTPUTS</text>
    <text x="315" y="113" text-anchor="middle" fill="#777" font-size="9">Answers + CoT traces</text>

    <!-- Arrow: Synthetic → Training Set -->
    <line x1="390" y1="100" x2="460" y2="100" stroke="#c4c4c0" stroke-width="1.5" marker-end="url(#arrow)"/>
    <text x="425" y="92" text-anchor="middle" fill="#999" font-size="8">Training</text>
    <text x="425" y="103" text-anchor="middle" fill="#999" font-size="8">dataset</text>

    <!-- Student Model box -->
    <rect x="460" y="70" width="150" height="60" rx="6" fill="#52525b" stroke="none"/>
    <text x="535" y="97" text-anchor="middle" fill="#fff" font-size="10" font-weight="500">STUDENT MODEL</text>
    <text x="535" y="113" text-anchor="middle" fill="#d4d4d8" font-size="9">No safeguards. Cheap.</text>

    <!-- Feedback loop arrow (bottom) -->
    <path d="M535 130 Q535 160 315 160 Q100 160 95 130" fill="none" stroke="#c4c4c0" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow-gray)"/>
    <text x="315" y="178" text-anchor="middle" fill="#aaa" font-size="8">Iterate: target new capabilities, pivot on new model releases</text>

    <!-- Arrow markers -->
    <defs>
      <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L6,3 z" fill="#c4c4c0"/>
      </marker>
      <marker id="arrow-gray" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L6,3 z" fill="#c4c4c0"/>
      </marker>
    </defs>
  </svg>
</div>
```

**Step 3: Verify**

Open in browser. SVG should show a clean 3-box flow (Teacher → Synthetic Outputs → Student) with a dashed feedback loop below.

**Step 4: Commit**

```bash
git add distillation-rl-guardrails.html
git commit -m "feat: add Section 2 with distillation loop SVG diagram"
```

---

## Task 4: Write Section 3 — How RL Supercharges Distillation + SVG Diagram 2

**Files:**
- Modify: `distillation-rl-guardrails.html`

**Step 1: Add section prose**

Append inside `.article-body`:

```html
<h2>How Reinforcement Learning Supercharges Distillation</h2>

<p>Raw output copying is table stakes. What makes modern distillation attacks dramatically more powerful is the use of <strong>reinforcement learning to generate synthetic training data</strong> at scale.</p>

<p>Here's the key insight: a model that can solve a problem step-by-step, showing its reasoning trace, is worth far more as a training target than a model that just gives you the answer. When DeepSeek queried Claude for chain-of-thought traces — the "think out loud" reasoning that Claude shows before answering — they weren't collecting answers. They were collecting a <strong>reasoning curriculum</strong>.</p>

<p>In RL-augmented distillation, attackers go further. They generate thousands of specialized tasks, query the teacher model for solutions with full reasoning traces, then use those traces as reward signal to train the student model's own reasoning process. The student doesn't just memorize answers — it <strong>learns the underlying reasoning strategy</strong>. This is why the resulting models are so capable despite their smaller size: they've been trained on the distilled reasoning of a much larger model, not just its surface outputs.</p>

<p>Moonshot's focus on "agentic reasoning and computer-use capabilities" makes sense in this light. These are high-value, hard-to-train behaviors. Generating synthetic demonstrations of agent-style reasoning — plan → tool call → observe → adapt — via an existing capable model is orders of magnitude cheaper than training those capabilities from scratch.</p>

<div class="callout">
  <div class="callout-label">The RL insight</div>
  <p>Chain-of-thought traces are not just verbose answers. They are a transferable reasoning dataset. When you elicit CoT from a capable model at scale, you are building a fine-tuning curriculum — not just collecting outputs.</p>
</div>
```

**Step 2: Add SVG Diagram 2 — RL Data Generation Pipeline**

Append after the prose:

```html
<!-- DIAGRAM 2: RL Data Generation Pipeline -->
<div style="margin: 2.5rem 0; padding: 2rem; background: #f8f8f7; border: 1px solid #e8e8e5; border-radius: 10px;">
  <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.62rem; letter-spacing: 0.12em; text-transform: uppercase; color: #999; margin-bottom: 1.25rem;">Fig. 2 — RL-Augmented Distillation Pipeline</div>
  <svg viewBox="0 0 700 240" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:700px;display:block;margin:0 auto;" font-family="'JetBrains Mono', monospace">
    <defs>
      <marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L6,3 z" fill="#c4c4c0"/>
      </marker>
    </defs>

    <!-- Step 1: Task Generator -->
    <rect x="20" y="20" width="130" height="55" rx="6" fill="#fff" stroke="#e8e8e5" stroke-width="1.5"/>
    <text x="85" y="44" text-anchor="middle" fill="#1a1a1a" font-size="9" font-weight="600">TASK GENERATOR</text>
    <text x="85" y="58" text-anchor="middle" fill="#777" font-size="8">Specialized prompts</text>
    <text x="85" y="69" text-anchor="middle" fill="#777" font-size="8">at scale</text>

    <!-- Arrow down -->
    <line x1="85" y1="75" x2="85" y2="105" stroke="#c4c4c0" stroke-width="1.5" marker-end="url(#arr2)"/>

    <!-- Step 2: Teacher API -->
    <rect x="20" y="105" width="130" height="55" rx="6" fill="#1a1a1a" stroke="none"/>
    <text x="85" y="129" text-anchor="middle" fill="#fff" font-size="9" font-weight="600">TEACHER API</text>
    <text x="85" y="143" text-anchor="middle" fill="#aaa" font-size="8">Returns answer +</text>
    <text x="85" y="154" text-anchor="middle" fill="#aaa" font-size="8">CoT reasoning trace</text>

    <!-- Arrow right -->
    <line x1="150" y1="132" x2="220" y2="132" stroke="#c4c4c0" stroke-width="1.5" marker-end="url(#arr2)"/>
    <text x="185" y="125" text-anchor="middle" fill="#999" font-size="8">(Query +</text>
    <text x="185" y="136" text-anchor="middle" fill="#999" font-size="8">CoT trace)</text>

    <!-- Step 3: Reward Scoring -->
    <rect x="220" y="105" width="140" height="55" rx="6" fill="#fff" stroke="#e8e8e5" stroke-width="1.5"/>
    <text x="290" y="129" text-anchor="middle" fill="#1a1a1a" font-size="9" font-weight="600">REWARD SCORING</text>
    <text x="290" y="143" text-anchor="middle" fill="#777" font-size="8">Correctness + reasoning</text>
    <text x="290" y="154" text-anchor="middle" fill="#777" font-size="8">quality signals</text>

    <!-- Arrow right -->
    <line x1="360" y1="132" x2="430" y2="132" stroke="#c4c4c0" stroke-width="1.5" marker-end="url(#arr2)"/>

    <!-- Step 4: Student Training -->
    <rect x="430" y="105" width="140" height="55" rx="6" fill="#52525b" stroke="none"/>
    <text x="500" y="129" text-anchor="middle" fill="#fff" font-size="9" font-weight="600">STUDENT TRAINING</text>
    <text x="500" y="143" text-anchor="middle" fill="#d4d4d8" font-size="8">RL updates on</text>
    <text x="500" y="154" text-anchor="middle" fill="#d4d4d8" font-size="8">reasoning traces</text>

    <!-- Arrow up from Student -->
    <line x1="500" y1="105" x2="500" y2="75" stroke="#c4c4c0" stroke-width="1.5" marker-end="url(#arr2)"/>

    <!-- Step 5: Capable Student -->
    <rect x="430" y="20" width="140" height="55" rx="6" fill="#fff" stroke="#1a1a1a" stroke-width="1.5"/>
    <text x="500" y="44" text-anchor="middle" fill="#1a1a1a" font-size="9" font-weight="600">CAPABLE STUDENT</text>
    <text x="500" y="58" text-anchor="middle" fill="#555" font-size="8">Learns reasoning strategy,</text>
    <text x="500" y="69" text-anchor="middle" fill="#555" font-size="8">not just surface outputs</text>

    <!-- Loop label -->
    <text x="350" y="210" text-anchor="middle" fill="#bbb" font-size="8">Iterate → target new capabilities → pivot within 24h of teacher model updates</text>
  </svg>
</div>
```

**Step 3: Verify**

Open in browser. Diagram should show 5 labeled boxes in an L-shaped pipeline with arrows flowing through the RL loop.

**Step 4: Commit**

```bash
git add distillation-rl-guardrails.html
git commit -m "feat: add Section 3 with RL pipeline SVG diagram"
```

---

## Task 5: Write Section 4 — The Attack Architecture + SVG Diagram 3

**Files:**
- Modify: `distillation-rl-guardrails.html`

**Step 1: Add section prose**

Append inside `.article-body`:

```html
<h2>The Attack Architecture: Hydra Clusters</h2>

<p>What made these campaigns hard to detect wasn't the queries themselves — it was the evasion architecture. Anthropic's report describes what they call "Hydra cluster architectures": distributed networks of fraudulent accounts designed to look like normal API usage.</p>

<p>The pattern works like this. Attackers create thousands of accounts — each with plausible usage patterns, realistic rate consumption, and no single fingerprint that triggers anomaly detection. Queries are spread across accounts so no individual account trips rate limits or behavioral thresholds. The "head" directing the campaign is invisible to the API provider; only the individual accounts are visible, and each looks benign in isolation.</p>

<p>When detection systems adapt — recognizing patterns in query topics, timing, or response elicitation styles — the hydra pivots. A cluster gets flagged and replaced. The campaign continues under new account identities, often within hours. This is why MiniMax could pivot within 24 hours of a new Claude release: they weren't discovering the new model, they were already querying it through a pre-built evasion infrastructure.</p>

<p>The evasion techniques documented by Anthropic include:</p>

<ul>
  <li><strong>Account rotation:</strong> Spreading load across thousands of accounts to avoid per-account anomalies</li>
  <li><strong>Rate mimicry:</strong> Consuming API at human-plausible speeds, not machine-fast bulk rates</li>
  <li><strong>Query diversification:</strong> Varying prompt structure and topics to avoid pattern detection</li>
  <li><strong>Censorship bypass:</strong> DeepSeek specifically targeted queries that elicited censorship-safe alternatives to sensitive topics</li>
  <li><strong>Rapid pivot:</strong> Automated infrastructure to shift targeting within hours of model updates</li>
</ul>
```

**Step 2: Add SVG Diagram 3 — Hydra Cluster Architecture**

Append after the prose:

```html
<!-- DIAGRAM 3: Hydra Cluster Architecture -->
<div style="margin: 2.5rem 0; padding: 2rem; background: #f8f8f7; border: 1px solid #e8e8e5; border-radius: 10px;">
  <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.62rem; letter-spacing: 0.12em; text-transform: uppercase; color: #999; margin-bottom: 1.25rem;">Fig. 3 — Hydra Cluster Evasion Architecture</div>
  <svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:700px;display:block;margin:0 auto;" font-family="'JetBrains Mono', monospace">
    <defs>
      <marker id="arr3" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L6,3 z" fill="#c4c4c0"/>
      </marker>
    </defs>

    <!-- Command Center (hidden) -->
    <rect x="270" y="10" width="160" height="45" rx="6" fill="#1a1a1a"/>
    <text x="350" y="30" text-anchor="middle" fill="#fff" font-size="9" font-weight="600">COMMAND CENTER</text>
    <text x="350" y="44" text-anchor="middle" fill="#888" font-size="8">(hidden from API provider)</text>

    <!-- Arrows from command center down to accounts -->
    <line x1="310" y1="55" x2="130" y2="105" stroke="#c4c4c0" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arr3)"/>
    <line x1="340" y1="55" x2="250" y2="105" stroke="#c4c4c0" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arr3)"/>
    <line x1="350" y1="55" x2="350" y2="105" stroke="#c4c4c0" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arr3)"/>
    <line x1="365" y1="55" x2="460" y2="105" stroke="#c4c4c0" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arr3)"/>
    <line x1="390" y1="55" x2="570" y2="105" stroke="#c4c4c0" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arr3)"/>

    <!-- Account nodes (each looks "normal") -->
    <!-- Acct 1 -->
    <circle cx="130" cy="125" r="25" fill="#fff" stroke="#e8e8e5" stroke-width="1.5"/>
    <text x="130" y="121" text-anchor="middle" fill="#555" font-size="7">Acct #1</text>
    <text x="130" y="132" text-anchor="middle" fill="#aaa" font-size="7">~normal</text>

    <!-- Acct 2 -->
    <circle cx="250" cy="125" r="25" fill="#fff" stroke="#e8e8e5" stroke-width="1.5"/>
    <text x="250" y="121" text-anchor="middle" fill="#555" font-size="7">Acct #2</text>
    <text x="250" y="132" text-anchor="middle" fill="#aaa" font-size="7">~normal</text>

    <!-- Acct 3 -->
    <circle cx="350" cy="125" r="25" fill="#fff" stroke="#e8e8e5" stroke-width="1.5"/>
    <text x="350" y="121" text-anchor="middle" fill="#555" font-size="7">Acct #3</text>
    <text x="350" y="132" text-anchor="middle" fill="#aaa" font-size="7">~normal</text>

    <!-- Acct ... -->
    <circle cx="460" cy="125" r="25" fill="#fff" stroke="#e8e8e5" stroke-width="1.5"/>
    <text x="460" y="121" text-anchor="middle" fill="#555" font-size="7">Acct #...</text>
    <text x="460" y="132" text-anchor="middle" fill="#aaa" font-size="7">~normal</text>

    <!-- Acct 24k -->
    <circle cx="570" cy="125" r="25" fill="#fff" stroke="#e8e8e5" stroke-width="1.5"/>
    <text x="570" y="121" text-anchor="middle" fill="#555" font-size="7">Acct</text>
    <text x="570" y="132" text-anchor="middle" fill="#555" font-size="7">#24,000</text>

    <!-- Arrows from accounts to API -->
    <line x1="130" y1="150" x2="280" y2="195" stroke="#c4c4c0" stroke-width="1" marker-end="url(#arr3)"/>
    <line x1="250" y1="150" x2="310" y2="195" stroke="#c4c4c0" stroke-width="1" marker-end="url(#arr3)"/>
    <line x1="350" y1="150" x2="350" y2="195" stroke="#c4c4c0" stroke-width="1" marker-end="url(#arr3)"/>
    <line x1="460" y1="150" x2="395" y2="195" stroke="#c4c4c0" stroke-width="1" marker-end="url(#arr3)"/>
    <line x1="570" y1="150" x2="420" y2="195" stroke="#c4c4c0" stroke-width="1" marker-end="url(#arr3)"/>

    <!-- Target API -->
    <rect x="270" y="195" width="160" height="45" rx="6" fill="#52525b"/>
    <text x="350" y="215" text-anchor="middle" fill="#fff" font-size="9" font-weight="600">TARGET API</text>
    <text x="350" y="229" text-anchor="middle" fill="#ccc" font-size="8">Each account = benign in isolation</text>

    <!-- Label: 24k accounts -->
    <text x="350" y="255" text-anchor="middle" fill="#bbb" font-size="8">~24,000 accounts · 16M+ exchanges · Rotate on detection · Pivot within 24h of model updates</text>
  </svg>
</div>
```

**Step 3: Verify**

Open in browser. Diagram should show a command center at top, 5 account nodes in the middle, and the target API at the bottom, connected by dashed lines.

**Step 4: Commit**

```bash
git add distillation-rl-guardrails.html
git commit -m "feat: add Section 4 with hydra cluster SVG diagram"
```

---

## Task 6: Write Sections 5–7 (You're a Target, Guardrail Checklist, Honest Closing)

**Files:**
- Modify: `distillation-rl-guardrails.html`

**Step 1: Add Section 5 — You're a Target Too**

Append inside `.article-body`:

```html
<h2>You're a Target Too</h2>

<p>It would be tempting to read the Anthropic case as a frontier-lab problem — something that only matters if you're training Claude-scale models. That's wrong.</p>

<p>The distillation attack works against any model with <strong>differentiated capabilities</strong>. A fine-tuned model for legal contract review. A specialized medical reasoning system trained on proprietary clinical guidelines. A code-generation model fine-tuned on your company's internal codebase. Any system where your model's behavior is substantially different from what an attacker could replicate with a public base model — that's a target.</p>

<p>The economics are asymmetric in the attacker's favor. Training a competitive specialized model from scratch costs millions of dollars in compute, months of expert data collection, and significant ML engineering investment. Distilling it from your API costs the price of API calls — potentially thousands of dollars against millions. Even partial distillation — capturing a subset of the target model's specialized capabilities — significantly reduces the attacker's own R&D burden.</p>

<p>The question isn't whether your model is "important enough" to be a target. The question is: does your model know something valuable that would be expensive to learn from scratch? If yes, you're a target.</p>
```

**Step 2: Add Section 6 — The Builder's Guardrail Checklist**

Append inside `.article-body`:

```html
<h2>The Builder's Guardrail Checklist</h2>

<p>Defense against distillation attacks is layered. No single control stops a determined, well-resourced attacker — but layered controls raise the cost, slow the attack, and create detection opportunities at every layer. Here's a defense-in-depth framework organized from easiest to implement to most sophisticated.</p>

<h3>Layer 1: Smart Rate Limiting</h3>

<p>Naive rate limiting (N requests per minute per API key) doesn't work against hydra clusters. Sophisticated rate limiting looks at behavioral signals, not just volume:</p>

<ul>
  <li><strong>Query diversity score:</strong> Legitimate users ask varied questions with natural distributions. Systematic extractors show unnaturally high coverage of capability domains in short time windows.</li>
  <li><strong>Reasoning trace request patterns:</strong> Monitor for unusually high rates of chain-of-thought elicitation. Normal users don't consistently request step-by-step reasoning for every query.</li>
  <li><strong>Session entropy:</strong> Human users show natural pauses, topic drift, and conversational patterns. Batch extractors show high-entropy query sequences with no conversational coherence.</li>
  <li><strong>Cross-account correlation:</strong> The same task categories queried from many accounts in coordinated time windows is a hydra signal, not individual behavior.</li>
</ul>

<h3>Layer 2: Behavioral Fingerprinting</h3>

<p>Build classifiers that detect systematic extraction behavior, not just high volume. The signals that distinguish a distillation campaign from a high-volume legitimate user include:</p>

<ul>
  <li>Queries that systematically span capability boundaries (coding, reasoning, agentic, creative) rather than staying in one domain</li>
  <li>Prompt templates that are parameterized variations of each other — signs of automated generation rather than human authorship</li>
  <li>Suspiciously complete coverage of edge cases within a capability area — the kind of systematic coverage that suggests benchmark-style extraction rather than organic use</li>
  <li>Immediate pivoting to new model capabilities within hours of a model release</li>
</ul>

<h3>Layer 3: Output Watermarking and Canary Data</h3>

<p>You can't prevent extraction if you can't detect it. Output watermarking embeds statistical signals in your model's responses that are imperceptible to users but detectable in aggregate if those outputs appear in another model's training data.</p>

<p>Canary data is complementary: inject rare but memorable knowledge into your model's training data. If another model later "knows" these canaries, you have evidence of distillation. This is less about prevention and more about legal and evidentiary positioning.</p>

<h3>Layer 4: Account and Identity Verification</h3>

<p>Hydra clusters depend on cheap, frictionless account creation. Friction is a deterrent:</p>

<ul>
  <li><strong>Phone verification:</strong> Eliminates throwaway email account bulk creation</li>
  <li><strong>Payment method binding:</strong> Real credit cards are traceable; prepaid cards can still be used but raise cost and operational complexity for the attacker</li>
  <li><strong>Organization verification for high-volume tiers:</strong> Requiring business verification for access to high-throughput API tiers cuts off bulk anonymous extraction</li>
  <li><strong>Anomaly-triggered KYC escalation:</strong> When behavioral signals trigger, require additional verification rather than immediately blocking — this reveals whether the account can produce a real identity</li>
</ul>

<h3>Layer 5: Model-Level Countermeasures</h3>

<p>Anthropic's approach included model-level defenses — training the model itself to behave differently when extraction patterns are detected. This is the hardest layer to implement but the most robust:</p>

<ul>
  <li><strong>Detection classifiers in the inference stack:</strong> Run a lightweight classifier alongside inference that scores each request for extraction signals; throttle or modify behavior for high-scoring sessions</li>
  <li><strong>Capability gating:</strong> Don't expose the full capability surface of your model through the API by default; require explicit opt-in for high-value capabilities like extended chain-of-thought reasoning</li>
  <li><strong>Output perturbation for extraction patterns:</strong> When extraction is suspected, subtly modify outputs in ways that degrade their training signal without being obviously wrong to a human reviewer</li>
</ul>

<div class="callout">
  <div class="callout-label">Implementation priority</div>
  <p>Start with Layers 1 and 4. Smart rate limiting and account friction are the highest-leverage, lowest-effort controls. Behavioral fingerprinting (Layer 2) requires more investment but provides the clearest detection signal. Layers 3 and 5 are for organizations with mature security postures and specialized AI systems worth protecting.</p>
</div>
```

**Step 3: Add Section 7 — The Honest Closing**

Append inside `.article-body`:

```html
<h2>The Honest Closing: This Is an Arms Race</h2>

<p>None of the controls above are permanent solutions. Every detection method has an evasion. Every fingerprinting technique can be countered with sufficiently sophisticated adversarial prompting or behavioral mimicry. The Anthropic report itself acknowledges this: these campaigns were detected after they had already collected millions of exchanges. Prevention is imperfect.</p>

<p>What a mature defense posture actually looks like isn't a checklist you complete and forget. It's a continuous practice:</p>

<ul>
  <li><strong>Monitor for new extraction signals</strong> as attacker techniques evolve</li>
  <li><strong>Share intelligence with peers</strong> — Anthropic explicitly mentions intelligence sharing with other providers as part of their response. Industry-level threat sharing slows attackers who can't rely on one provider's blindspot being universal</li>
  <li><strong>Accept that some extraction will happen</strong> and design your differentiation accordingly — if your model's value comes only from a capability that can be distilled, that's a business risk as much as a security one</li>
  <li><strong>Treat API access controls as a security surface</strong>, not just a billing concern — the design decisions you make about rate limits, account tiers, and capability exposure are security decisions</li>
</ul>

<p>The deeper question these attacks raise is about the structure of AI development itself. Distillation attacks are a form of technology transfer — one that bypasses the export controls, licensing agreements, and access restrictions that would normally govern the transfer of strategic technology. As AI capabilities become more strategically significant, the gap between what's technically possible (distillation) and what's legally or ethically acceptable will widen. The builders who understand both sides of that gap will be better positioned than those who only see the technical problem.</p>

<p>Your API is a training dataset. Treat it accordingly.</p>

<div class="callout">
  <div class="callout-label">Source</div>
  <p>This post is based on Anthropic's published findings: <a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks" style="color:var(--accent);text-decoration:underline;text-underline-offset:3px">Detecting and Preventing Distillation Attacks</a>.</p>
</div>
```

**Step 4: Verify**

Open in browser. Read through all three sections. Confirm callout boxes render, bullet lists are styled, and the source link in the closing callout works.

**Step 5: Commit**

```bash
git add distillation-rl-guardrails.html
git commit -m "feat: add Sections 5-7 (target framing, guardrail checklist, closing)"
```

---

## Task 7: Add Post Card to index.html

**Files:**
- Modify: `index.html`

**Step 1: Update post count**

Find line ~797:
```html
<span class="count">09 Posts</span>
```
Change to:
```html
<span class="count">10 Posts</span>
```

**Step 2: Add post card as first item in posts grid**

Find the opening of the posts grid at line ~800:
```html
<div class="posts-grid">
```

Insert immediately after that opening tag (before the pediatric post card):

```html
  <article class="post-card reveal" data-category="safety" onclick="window.location.href='distillation-rl-guardrails.html'">
    <span class="post-tag safety">AI Security · Model Defense</span>
    <h3>Your API Is a Training Dataset: How Distillation Attacks Work and How to Stop Them</h3>
    <p class="post-excerpt">DeepSeek, Moonshot, and MiniMax ran 16M+ exchanges to steal Claude's capabilities. How distillation attacks work mechanically — and a layered guardrail checklist for API and model builders.</p>
    <div class="post-footer">
      <span class="post-date">Feb 2026 · 16 min</span>
      <span class="post-read">Read →</span>
    </div>
  </article>
```

**Step 3: Verify**

Open `index.html` in browser. Confirm the new post card appears first in the grid with correct title, tag, excerpt, and clicking it navigates to `distillation-rl-guardrails.html`.

**Step 4: Commit**

```bash
git add index.html
git commit -m "feat: add distillation attacks post card to index"
```

---

## Task 8: Final review pass

**Files:**
- Review: `distillation-rl-guardrails.html`

**Step 1: Read through the full post in browser**

Check for:
- [ ] All 7 sections present and readable
- [ ] All 3 SVG diagrams render correctly (no broken arrows, overlapping text)
- [ ] Callout boxes styled correctly (left border, accent label)
- [ ] Source link in closing callout is clickable
- [ ] Mobile layout looks acceptable (viewport meta is set)
- [ ] Back-navigation to index.html works from the header nav

**Step 2: Check the nav link**

The `pediatric-disaster-edge-ai.html` template has a nav bar with a link back to the main site. Verify it reads correctly in the new post (no leftover pediatric-specific text anywhere).

**Step 3: Final commit if any fixes applied**

```bash
git add distillation-rl-guardrails.html index.html
git commit -m "fix: final review corrections for distillation blog post"
```

---

## Completion Checklist

- [ ] `distillation-rl-guardrails.html` exists with all 7 sections
- [ ] 3 SVG diagrams embedded and rendering
- [ ] Post card added to `index.html` with correct link
- [ ] Post count updated to 10 in `index.html`
- [ ] All changes committed
