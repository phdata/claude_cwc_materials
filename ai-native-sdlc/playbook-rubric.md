# Playbook alignment rubric

Each course is scored against the five parts every play in Anthropic's AI-native SDLC playbook carries,
plus three cross-cutting principles. A course passes only when every row names the step that covers it.
Score each cell 0 (missing), 1 (mentioned) or 2 (practiced hands-on or demonstrated). Release bar: no 0s, and
Implementation steps and Governance score 2.

Source: Anthropic, "The AI-native SDLC playbook" (claude.com/resources/articles/the-ai-native-sdlc-playbook).

## Coverage matrix (step ids)

| Rubric row | C1 Plan | C2 Design | C3 Build | C4 Test | C5 Deploy | C6 Maintain |
|---|---|---|---|---|---|---|
| What changes | `orient` | `orient` | `orient` | `orient` | `orient` | `orient` |
| Getting started (prerequisites, infrastructure) | `get-the-checkpoint` | `get-the-checkpoint` | `get-the-checkpoint` | `get-the-checkpoint` | `get-the-checkpoint` | `get-the-checkpoint` |
| Implementation steps | `brainstorm-intent`, `commit-intent`, `intent-command`, `po-review` | `policy-skills`, `design-pass`, `resolve-concerns`, `codify-design` | `plan-mode`, `claude-md`, `hooks-guardrails`, `build-and-verify` | `feedback-loop`, `failing-test-first`, `eval-set`, `evals-in-ci` | `review-md`, `pr-fix-loop`, `approval-hooks`, `cicd-and-rollback` | `bands`, `breach-diagnosis`, `close-the-loop`, `scans-and-lessons` |
| Governance (human gate) | `gate` | `gate` | `gate` | `gate` | `gate` | `gate` |
| Measurement (leading and lagging) | `hand-off` | `hand-off` | `hand-off` | `hand-off` | `hand-off` | `hand-off` |
| Principle: each stage commits an artifact the next reads | `hand-off` to next checkpoint | `hand-off` to next checkpoint | `hand-off` to next checkpoint | `hand-off` to next checkpoint | `hand-off` to next checkpoint | `hand-off` to Course 1 (intent/0002) |
| Principle: humans own judgment gates | `gate`, `po-review` | `gate` | `gate` | `gate` | `gate` | `gate` |
| Principle: detection stays deterministic | n/a | n/a | n/a | n/a | n/a | `bands` |

## Playbook practice coverage

| Playbook practice | Course | Step id |
|---|---|---|
| Capture as intent.md | 1 | brainstorm-intent, commit-intent |
| Product owner accept/reject | 1 | po-review |
| Requirements and design in one session | 2 | design-pass |
| Organization skills as constraints | 2 | policy-skills |
| Flagged areas of concern resolved with policy owners | 2 | resolve-concerns |
| Codify as slash command, automate as headless job | 2 | codify-design |
| Plan mode as default | 3 | plan-mode |
| CLAUDE.md | 3 | claude-md |
| Skills as institutional knowledge | 3 | hooks-guardrails (contrasted with policy-skills from C2) |
| Hooks as build-time guardrails | 3 | hooks-guardrails |
| Parallel sessions and subagents | 3 | build-and-verify |
| Auto mode (later stage) | 3 | bonus-auto-mode |
| One source of truth per artifact | 3 | gate, bonus-source-of-truth |
| Give Claude a feedback loop | 4 | feedback-loop |
| Failing test first, test locked during fix | 4 | failing-test-first |
| Start evals with 20 to 50 real tasks | 4 | eval-set |
| Continuous evals in CI, incident becomes eval | 4 | evals-in-ci |
| REVIEW.md and AI in the PR loop | 5 | review-md, pr-fix-loop |
| Hooks as approval gates | 5 | approval-hooks |
| Managed settings | 5 | gate, bonus-managed-settings |
| CI/CD integration, tiered autonomy, rollback | 5 | cicd-and-rollback |
| Deterministic bands (1, 2, 3 sigma) | 6 | bands |
| Read-only diagnosis | 6 | breach-diagnosis |
| Findings re-enter as intent.md | 6 | close-the-loop |
| Recurring scans and lessons file | 6 | scans-and-lessons |
| Claude Tag (public beta, instructor demo environment) | 6 | bonus-claude-tag |
| Pre-approved runbooks at 3 sigma | 6 | bonus-runbook |
