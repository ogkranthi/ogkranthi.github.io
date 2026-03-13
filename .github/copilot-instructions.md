# Copilot instructions for this blog repository

This repository is a technical blog focused on enterprise AI, AI agents, AI architectures,
reinforcement learning, human-in-the-loop systems, and AI safety.

Core rules:
- Never publish directly to the default branch.
- Prefer small, reviewable pull requests.
- Preserve the author's voice: human, educational, architecture-first, practical, technical, non-hype, Give gist upfront with main ideas and summary for people who might not have time to read the entire blog and call out this specifically.
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

## Publishing contract for blog posts

A blog post is not complete if only a standalone HTML page is created.

For every new post or significant refresh, also update:
- the homepage listing in index.html
- the homepage post count
- the featured essay section if the post is the newest featured article
- any related-reading links that should point to the new post

When opening a PR for a new post, include:
- new file created
- exact homepage sections updated
- whether the featured essay changed
- whether the post count changed
- any internal links added or updated

Do not leave the homepage stale after adding a live article.

## SEO requirements for every page

Every new blog post HTML must include these in `<head>`, after the `og:type` meta tag and before the Mailchimp script:

1. Canonical URL:
   `<link rel="canonical" href="https://ogkranthi.github.io/{filename}.html">`

2. Twitter card meta tags:
   ```html
   <meta name="twitter:card" content="summary">
   <meta name="twitter:site" content="@ogkranthi">
   <meta name="twitter:title" content="{same as og:title}">
   <meta name="twitter:description" content="{same as og:description}">
   ```

3. JSON-LD Article structured data:
   ```html
   <script type="application/ld+json">
   {
     "@context": "https://schema.org",
     "@type": "Article",
     "headline": "{article title}",
     "description": "{meta description}",
     "author": { "@type": "Person", "name": "Kranthi Manchikanti" },
     "publisher": { "@type": "Person", "name": "Kranthi Manchikanti" },
     "url": "https://ogkranthi.github.io/{filename}.html"
   }
   </script>
   ```

These are required. Do not publish a post without them.
