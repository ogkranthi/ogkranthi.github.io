# Blog Design: Distillation Attacks & RL — Builder's Guide

**Date:** 2026-02-25
**Status:** Approved

---

## Title

*"Your API Is a Training Dataset: How Distillation Attacks Work and How to Stop Them"*

---

## Context

Inspired by Anthropic's article on detecting and preventing distillation attacks, which revealed that DeepSeek, Moonshot, and MiniMax ran industrial-scale campaigns (16M+ exchanges, ~24K fraudulent accounts) to extract Claude's capabilities — including RL-generated chain-of-thought traces.

---

## Audience

AI product and API builders — teams building on top of foundation models or serving their own fine-tuned/specialized models via API.

---

## Angle

Mix of narrative-first (Option A) and actionable builder checklist (Option C):
- Use the Anthropic case as a dramatic opening hook
- Explain mechanics conceptually with SVG diagrams (no code)
- Generalize to distillation attacks as a class of threat
- Close with a concrete, layered guardrail checklist for builders

---

## Scope

Use Anthropic as the opening hook, then generalize — cover distillation attacks as a category of threat that any API or model provider faces.

---

## Post Outline

### 1. The Heist *(narrative hook)*
- The Anthropic case: 3 companies, 16M exchanges, 24K fraudulent accounts
- Attackers pivoting within 24 hours of new model releases
- Make it vivid — this is industrial espionage at AI scale

### 2. What Is Model Distillation? *(conceptual mechanics)*
- Legitimate teacher-student training vs. illicit extraction at scale
- How knowledge transfers from a larger model to a smaller one
- **SVG diagram:** teacher model → synthetic outputs → student model training loop

### 3. How RL Supercharges Distillation *(key insight)*
- Why chain-of-thought traces and agentic reasoning are far more valuable than raw outputs
- What DeepSeek was actually collecting and why it matters
- RL-generated synthetic data as the "secret ingredient"
- **SVG diagram:** RL data generation pipeline (query → CoT trace → reward signal → student training)

### 4. The Attack Architecture *(how attackers operate)*
- Hydra cluster pattern: distributed accounts, rotating identity, behavioral mimicry
- How attackers evade rate limits and detection systems
- **SVG diagram:** hydra evasion architecture

### 5. You're a Target Too *(pivot to builders)*
- Not just frontier labs — anyone with a specialized/fine-tuned model served via API
- The framing: "your API is a training dataset if you're not careful"
- What makes a model worth stealing (specialization, fine-tuning, RLHF)

### 6. The Builder's Guardrail Checklist *(actionable core)*
- **Layer 1:** Smart rate limiting — behavioral limits, not just token counts
- **Layer 2:** Behavioral fingerprinting — detecting systematic, programmatic query patterns
- **Layer 3:** Output watermarking & canary data — detecting if your outputs appear in other models
- **Layer 4:** Account/identity verification — friction against bulk fraudulent accounts
- **Layer 5:** Model-level countermeasures — what Anthropic did (detection classifiers, model-level defenses)

### 7. The Honest Closing *(arms race reality)*
- Detection and evasion will keep co-evolving
- What a mature, layered defense posture looks like
- The broader implication: AI model IP protection as a serious engineering discipline

---

## Diagrams (SVG, hand-drawn style matching existing blog)

1. **Teacher-Student Distillation Loop** — linear flow diagram
2. **RL Data Generation Pipeline** — shows query → CoT trace → reward → student training cycle
3. **Hydra Cluster Architecture** — distributed attack topology

---

## Style Notes

- Monochrome design, matches existing blog (engram.html, pediatric-disaster-edge-ai.html)
- Newsreader serif for headings, Inter sans for body, JetBrains Mono for any technical terms
- Hand-drawn SVG style for diagrams
- ~2,500–3,000 words
- New file: `distillation-rl-guardrails.html`

---

## Source

Anthropic article: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
