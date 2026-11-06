# Course 3 of 6: Build

**Plan First, Then Code: Build in the AI-Native SDLC**

This course covers Stage 3 of Anthropic's AI-native SDLC playbook. It runs hands-on in Claude Code, using the Catalyst Holdings support-ticket triage scenario. It runs alone or as part of the series, because it starts from its own checkpoint repo.

| | |
|---|---|
| Workshop app alias | `ai-native-sdlc-03-build-v1` |
| Length | 90 minutes: 70 minutes of core steps, 200 points |
| Audience | Engineers |
| Starts from | `starter/catalyst-checkpoint-2.zip` (contains intent.md, spec.md and policy skills) |
| Hands off | plan.md, CLAUDE.md, .claude/settings.json hooks, app/ triage service with unit tests |
| Playbook lessons | Stage 3: Claude Code plan mode as the default starting point; The CLAUDE.md; Skills as institutional knowledge; Parallel sessions and subagents |

## Learning objectives

1. Use plan mode so no implementation starts without an accepted plan.md.
2. Write a short CLAUDE.md with commands, conventions and recurring mistakes.
3. Add hooks that enforce guardrails deterministically, and explain skills (advisory) vs hooks (enforced).
4. Build with a report-only verifier subagent and a parallel session in its own worktree.

## Get started

```
unzip starter/catalyst-checkpoint-2.zip && cd catalyst-triage
make setup && make test
git log --oneline
claude
```

`git log` shows one commit per artifact from the earlier stages. Accept the workspace trust prompt when Claude Code opens, so the project settings and hooks load.

## Labs

Every lab has four tabs in the workshop app: Catalyst Holdings (the guided path), Bring your own use case, If you're stuck, and What good looks like.

- **Lab A, Plan mode as the default.** In plan mode, have Claude read spec.md and produce plan.md (files, order of work, tests); review and accept it before any edit.
  You finish with: plan.md accepted by the engineer.
- **Lab B, Write CLAUDE.md.** Capture Catalyst's run, test and lint commands, conventions and known mistakes; apply the rule of adding a correction once a mistake repeats.
  You finish with: CLAUDE.md under version control.
- **Lab C, Hooks as build-time guardrails.** Add protect-paths.sh (blocks gold-label edits and credentials) and lint-on-edit.sh (runs pyflakes after every edit) in .claude/settings.json, then watch a blocked edit.
  You finish with: .claude/settings.json, .claude/hooks/protect-paths.sh and lint-on-edit.sh.
- **Lab D, Build with a verifier.** Implement the first step of plan.md (redact.py and its unit tests), then run a verifier subagent that reports and never fixes; start a second session in its own git worktree for the route tests.
  You finish with: app/triage/redact.py with passing tests, .claude/agents/verifier.md (full service: checkpoint-3).

## Human gate

The engineer accepts the plan; code owners review the PR; a tech lead or architect reviews higher-risk changes. Name one system of record per artifact.

## Measures

- Leading: Time from plan approval to merged PR.
- Lagging: First-pass merge rate and count of repeated mistakes.

## Run of show

| Clock | Segment | Min | Pts |
|---|---|---|---|
| 0:00 to 0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | 5 |  |
| 0:05 to 0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | 8 | 15 |
| 0:13 to 0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | 7 | 10 |
| 0:20 to 0:31 | Lab A: Plan mode as the default | 11 | 25 |
| 0:31 to 0:42 | Lab B: Write CLAUDE.md | 11 | 25 |
| 0:42 to 0:52 | Lab C: Hooks as build-time guardrails | 10 | 25 |
| 0:52 to 1:02 | Lab D: Build with a verifier | 10 | 25 |
| 1:02 to 1:09 | The human gate and governance | 7 | 20 |
| 1:09 to 1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | 6 | 15 |
| 1:15 to 1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | 10 |  |
| 1:25 to 1:30 | Wrap: what is committed, next course preview, feedback | 5 |  |

## Files in this folder

- `agenda.md`: the full agenda, with step detail and facilitator notes.
- `starter/catalyst-checkpoint-2.zip`: the repo participants start from.
- `diagrams/loop-build.svg`
- `diagrams/c3-plan-mode.svg`
- `diagrams/c3-claude-md.svg`
- `diagrams/c3-hooks-guardrails.svg`
- `diagrams/c3-build-and-verify.svg`
- `diagrams/c3-gate.svg`
- `diagrams/c3-handoff.svg`

All people, tickets and figures in the Catalyst Holdings scenario are fictional, and the data is synthetic.
