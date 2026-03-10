# Blog Design: AutoResearch, Harness Engineering, and Agentic AI

**Date:** 2026-03-10
**Status:** Draft

---

## Title

*"AutoResearch, Harness Engineering, and the Next Layer of Agentic AI"*

---

## Context

Andrej Karpathy's AutoResearch project and OpenAI's "harness engineering" framing demonstrate a deeper pattern for reliable agentic AI: bounded loops, narrow write surfaces, fixed evaluation budgets, rollback discipline, and repository-native feedback systems. This post translates that pattern into lessons for enterprise AI and production agentic systems.

---

## Audience

Enterprise architects, senior engineers, AI platform teams, and technical leaders designing production AI systems.

---

## Angle

Architecture-first analysis — not a news summary of AutoResearch, but a structural decomposition of _why_ it works and what enterprises should extract from the pattern.

---

## Scope

- AutoResearch as a case study in harness engineering
- The deeper pattern: bounded agent loops with deterministic scaffolding
- Enterprise translation: what to copy, what to avoid, where HITL remains essential

---

## Post Outline

### 1. Opening — The Pattern, Not the Product
- AutoResearch runs ML experiments overnight with no human in the loop
- The interesting part is not the autonomy — it's the constraints that make the autonomy safe
- Thesis: the real innovation is harness engineering

### 2. What AutoResearch Actually Does
- High-level overview of the system
- Agent proposes experiments, runs them, evaluates results, iterates
- Key constraints: fixed compute budgets, narrow code mutations, automated evaluation

### 3. The Harness Engineering Pattern
- OpenAI's framing: harness engineering as a discipline
- Five principles: bounded loops, narrow write surfaces, fixed evaluation budgets, rollback discipline, repository-native feedback
- Why this is different from "just let the agent run"

### 4. Why Scaffolding Beats Autonomy
- The trap of raw autonomy: agents that can do anything tend to do nothing reliably
- Deterministic orchestration as the foundation for reliable agent behavior
- Evaluation harnesses as the missing piece in most enterprise agent deployments

### 5. The Enterprise Checklist — What to Copy
- Deterministic orchestration
- Explicit evaluation harnesses
- Narrow mutation surfaces
- Auditability and trace logging
- Escalation boundaries

### 6. What Not to Copy Blindly
- AutoResearch operates in a narrow domain with clean metrics (ML experiments)
- Enterprise domains have ambiguous success criteria, regulatory constraints, multi-stakeholder workflows
- The risk of over-constraining vs. under-constraining

### 7. Why HITL Still Matters
- Outside narrow optimization loops, human judgment remains essential
- Escalation design as the boundary between agent autonomy and human oversight
- The continuum from fully automated to fully supervised

### 8. Closing — Harness Engineering as a Discipline
- This is the real infrastructure layer for agentic AI
- The teams that invest in harness engineering will ship reliable agents; the rest will ship demos

---

## Diagrams (SVG, matching existing blog style)

1. **Harness Engineering Loop** — bounded agent cycle: propose → execute → evaluate → decide (continue/rollback/escalate)
2. **Enterprise Adoption Checklist** — visual comparison table of what to copy vs. what to adapt

---

## Style Notes

- Monochrome design, matches existing blog
- Newsreader serif for headings, Inter sans for body, JetBrains Mono for labels
- ~2,500–3,000 words
- New file: `autoresearch-harness-engineering.html`

---

## Internal Links (Suggested)

1. `distillation-rl-guardrails.html` — "Your API Is a Training Dataset" (AI Security, guardrail patterns)
2. `engram.html` — "DeepSeek Engram" (AI Architectures, agent memory systems)
3. HITL Frameworks post (referenced in index, covers human oversight in agentic systems)

---

## Sources

- https://openai.com/index/harness-engineering/
- https://github.com/karpathy/autoresearch
- Existing site posts on agents, HITL, safety, and architecture

---

## Fact-Check Items (TODO)

- [ ] Verify exact AutoResearch capabilities and constraints from Karpathy's repo
- [ ] Confirm OpenAI's harness engineering article details and framing
- [ ] Verify any specific metrics or benchmarks cited about AutoResearch results
- [ ] Confirm the relationship between Karpathy and OpenAI (he left OpenAI; AutoResearch is independent work)
