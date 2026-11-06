# Course 3 of 6: Plan First, Then Code: Build in the AI-Native SDLC

**Alias:** `ai-native-sdlc-03-build-v1`  
**Playbook stage:** 3. Build  
**Academy lessons covered:** Stage 3: Claude Code plan mode as the default starting point; The CLAUDE.md; Skills as institutional knowledge; Parallel sessions and subagents  
**Length:** 90 minutes (70 minutes of core steps, 200 points)  
**Audience:** engineers, hands-on in Claude Code  
**Runs:** alone or in sequence. It starts from a checkpoint repo, so no earlier course is required.

## Learning objectives

1. Use plan mode so no implementation starts without an accepted plan.md
2. Write a short CLAUDE.md with commands, conventions and recurring mistakes
3. Add hooks that enforce guardrails deterministically, and explain skills (advisory) vs hooks (enforced)
4. Build with a report-only verifier subagent and a parallel session in its own worktree

## Starts from / hands off

- **Starts from:** checkpoint-2: intent.md, spec.md and policy skills
- **Hands off:** plan.md, CLAUDE.md, .claude/settings.json hooks, app/ triage service with unit tests

## Run of show

| Clock | Segment | Step id | Min | Pts |
|---|---|---|---|---|
| 0:00-0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | facilitator | 5 | |
| 0:05-0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | `orient` | 8 | 15 |
| 0:13-0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | `get-the-checkpoint` | 7 | 10 |
| 0:20-0:31 | Lab A: Plan mode as the default | `plan-mode` | 11 | 25 |
| 0:31-0:42 | Lab B: Write CLAUDE.md | `claude-md` | 11 | 25 |
| 0:42-0:52 | Lab C: Hooks as build-time guardrails | `hooks-guardrails` | 10 | 25 |
| 0:52-1:02 | Lab D: Build with a verifier | `build-and-verify` | 10 | 25 |
| 1:02-1:09 | The human gate and governance | `gate` | 7 | 20 |
| 1:09-1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | `hand-off` | 6 | 15 |
| 1:15-1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | facilitator | 10 | |
| 1:25-1:30 | Wrap: what is committed, next course preview, feedback | facilitator | 5 | |
| bonus | Discuss when guardrails are mature enough for auto mode and what review shifts to | `bonus-auto-mode` | | 20 |
| bonus | Map each artifact to its system of record (repo, Jira, or a link between them) | `bonus-source-of-truth` | | 20 |

## Step detail

### Orient (`orient`, 8 min)

Traditional: engineers hand-write code from tickets and tribal knowledge. AI-native: Claude writes plan.md first, institutional knowledge lives in CLAUDE.md and skills, and hooks enforce the rules that must never be broken.

**Quick check:** Which mechanism enforces a rule deterministically: a skill or a hook?  
**Answer:** A hook; skills are advisory guidance Claude may follow

### Get the checkpoint (`get-the-checkpoint`, 7 min)

Clone checkpoint-2, run `make setup && make test`, and read CLAUDE.md plus the incoming artifact before changing anything.

### Lab A: Plan mode as the default (`plan-mode`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | In plan mode, have Claude read spec.md and produce plan.md (files, order of work, tests); review and accept it before any edit. |
| Bring your own use case | Ask for a plan.md for one small change in your own system and critique it. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** plan.md accepted by the engineer

### Lab B: Write CLAUDE.md (`claude-md`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Capture Catalyst's run, test and lint commands, conventions and known mistakes; apply the rule of adding a correction once a mistake repeats. |
| Bring your own use case | Draft the five lines your own repo's CLAUDE.md most needs. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** CLAUDE.md under version control

### Lab C: Hooks as build-time guardrails (`hooks-guardrails`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Add protect-paths.sh (blocks gold-label edits and credentials) and lint-on-edit.sh (runs pyflakes after every edit) in .claude/settings.json, then watch a blocked edit. |
| Bring your own use case | Name one rule in your repo that must never be broken and write its hook. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** .claude/settings.json, .claude/hooks/protect-paths.sh and lint-on-edit.sh

### Lab D: Build with a verifier (`build-and-verify`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Implement the first step of plan.md (redact.py and its unit tests), then run a verifier subagent that reports and never fixes; start a second session in its own git worktree for the route tests. |
| Bring your own use case | Define a verifier subagent for your own codebase's review checklist. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** app/triage/redact.py with passing tests, .claude/agents/verifier.md (full service: checkpoint-3)

### The human gate and governance (`gate`, 7 min)

The engineer accepts the plan; code owners review the PR; a tech lead or architect reviews higher-risk changes. Name one system of record per artifact.

### Measure and hand off (`hand-off`, 6 min)

- **Leading indicator:** Time from plan approval to merged PR
- **Lagging indicator:** First-pass merge rate and count of repeated mistakes
- Commit and push: plan.md, CLAUDE.md, .claude/settings.json hooks, app/ triage service with unit tests
- Knowledge check: three questions covering the stage's artifact, its gate and its measures

## Facilitator notes

Participants commit their own .claude/settings.json and hooks; some auto-mode setups block an agent from committing these paths, so a person commits them.

## Before you begin (participant card)

- Claude Code installed and signed in with a Claude Team or Enterprise seat (claude --version works)
- git, Python 3.9+, and make on the workstation
- A GitHub account with permission to create a private repo (CI and PR labs have a local fallback)
- Optional: one real system of your own in mind for the Bring your own use case tab
