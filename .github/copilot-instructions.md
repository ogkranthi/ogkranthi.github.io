# Copilot instructions for this blog repository

This repository is a technical blog focused on enterprise AI, AI agents, AI architectures,
reinforcement learning, human-in-the-loop systems, and AI safety.

Core rules:
- Never publish directly to the default branch.
- Prefer small, reviewable pull requests.
- Preserve the author's voice: architecture-first, practical, technical, non-hype.
- Do not invent facts, sources, dates, quotes, or statistics.
- If a post references current events, tools, research, or companies, leave TODO markers for verification if the issue does not provide sources.
- Do not modify site-wide layout, theme, config, analytics, or deployment files unless explicitly asked.
- Keep drafts structured, skimmable, and useful to senior engineers and architects.
- When drafting a post, include:
  - strong title
  - thesis in opening paragraph
  - clear section structure
  - practical implications
  - risks / limitations
  - conclusion
- When opening a PR, include:
  - what draft or page was created/updated
  - what assumptions were made
  - where human fact-checking is still needed
  - any suggested follow-up posts
 
- # Diagram requirements for workflow and architecture posts

For any post that describes a system, workflow, control plane, agent loop, or multi-step process:

- Include at least one diagram for each major workflow described in the article.
- Prefer inline SVG diagrams embedded directly in the HTML file.
- Diagrams must clarify architecture, state transitions, boundaries, approvals, or control flow.
- Do not add decorative diagrams.
- Every diagram must have:
  - figure label
  - short caption
  - consistent visual style
  - accessible text or title where practical
- If the article includes sections on orchestration, escalation, evaluation, or approvals, those sections should usually have a corresponding diagram.
- When opening a PR, explicitly list which diagrams were added and which sections they support.
