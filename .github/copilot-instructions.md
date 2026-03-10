# Repository rules for Copilot coding agent

Work PR-first. Never attempt to change the default branch directly.
Prefer small, reviewable changes over broad refactors.
Run lint and tests before finishing work.
If the request is ambiguous, choose the smallest safe implementation.
Do not change auth, secrets, billing, CI, infra, or database schema unless the issue explicitly asks for it.
When opening a PR, include:
- what changed
- why it changed
- risks / edge cases
- tests run
- follow-up work not included
