# Course 1 of 6: Capture Intent: Plan in the AI-Native SDLC

**Alias:** `ai-native-sdlc-01-plan-v1`  
**Playbook stage:** 1. Plan  
**Academy lessons covered:** Introduction: what changes and where to start; Stage 1: Plan, capture as intent.md  
**Length:** 90 minutes (70 minutes of core steps, 200 points)  
**Audience:** engineers, hands-on in Claude Code  
**Runs:** alone or in sequence. It starts from a checkpoint repo, so no earlier course is required.

## Learning objectives

1. Explain why code is no longer the bottleneck and where the human-speed steps now sit
2. Turn an originator's idea into a versioned intent.md with problem, outcome, users and systems, constraints and open questions
3. Codify intent capture as a reusable project command so every originator gets the same structure
4. Run the product-owner accept/reject gate as a PR review

## Starts from / hands off

- **Starts from:** checkpoint-0: Catalyst support repo with an empty intent/ home, docs/intent-template.md, Care ops notes and sample tickets
- **Hands off:** intent/0001-ticket-triage.md (accepted)

## Run of show

| Clock | Segment | Step id | Min | Pts |
|---|---|---|---|---|
| 0:00-0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | facilitator | 5 | |
| 0:05-0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | `orient` | 8 | 15 |
| 0:13-0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | `get-the-checkpoint` | 7 | 10 |
| 0:20-0:31 | Lab A: Brainstorm the ask with Claude | `brainstorm-intent` | 11 | 25 |
| 0:31-0:42 | Lab B: Write and commit intent.md | `commit-intent` | 11 | 25 |
| 0:42-0:52 | Lab C: Codify capture as /capture-intent | `intent-command` | 10 | 25 |
| 0:52-1:02 | Lab D: Run the product-owner review | `po-review` | 10 | 25 |
| 1:02-1:09 | The human gate and governance | `gate` | 7 | 20 |
| 1:09-1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | `hand-off` | 6 | 15 |
| 1:15-1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | facilitator | 10 | |
| 1:25-1:30 | Wrap: what is committed, next course preview, feedback | facilitator | 5 | |
| bonus | Draft an intent from an existing ticket through an MCP connector | `bonus-intent-from-ticket` | | 20 |
| bonus | Triage a rejected intent: rework, merge with another, or close | `bonus-rejected-intent` | | 20 |

## Step detail

### Orient (`orient`, 8 min)

Traditional: ideas live in slides, emails and tickets, retold at every handoff. AI-native: the originator brainstorms with Claude once and commits intent.md, which every later stage reads. The commit history is the audit trail.

**Quick check:** What does Stage 1 commit for the next stage to read?  
**Answer:** intent.md, written from the originator's own words and accepted by the product owner

### Get the checkpoint (`get-the-checkpoint`, 7 min)

Clone checkpoint-0, run `make setup && make test`, and read CLAUDE.md plus the incoming artifact before changing anything.

### Lab A: Brainstorm the ask with Claude (`brainstorm-intent`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | As Catalyst's support lead, describe the misrouted-ticket problem in your own words and have Claude interview you until it can draft a proto-spec. |
| Bring your own use case | Describe a real problem in a system you own; have Claude ask the questions a product owner would. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** Problem, outcome, affected users and systems, constraints, open questions

### Lab B: Write and commit intent.md (`commit-intent`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Have Claude write intent/0001-ticket-triage.md from the brainstorm using docs/intent-template.md, correct it as the originator, then branch, commit and open a PR. |
| Bring your own use case | Commit intent/0001-<your-topic>.md in your own scratch repo using the same template. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** intent/0001-ticket-triage.md on a branch with an open PR

### Lab C: Codify capture as /capture-intent (`intent-command`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Turn the brainstorm prompt into a project slash command so any originator produces the same structure. |
| Bring your own use case | Adapt the command's sections to the vocabulary your team already uses. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** .claude/commands/capture-intent.md

### Lab D: Run the product-owner review (`po-review`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | In pairs, one plays Catalyst's product owner: correct the intent, then accept or reject in PR review, recording the reason on reject. |
| Bring your own use case | Swap intents with your partner and review theirs as their product owner would. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** PR review decision with corrections or a recorded rejection reason

### The human gate and governance (`gate`, 7 min)

The product owner accepts or rejects; acceptance moves the intent to Design. Name the source of truth for intents (the repo, or a repo-to-Jira link at minimum) and who may accept.

### Measure and hand off (`hand-off`, 6 min)

- **Leading indicator:** Time from first conversation to committed intent
- **Lagging indicator:** Share of intents accepted rather than closed
- Commit and push: intent/0001-ticket-triage.md (accepted)
- Knowledge check: three questions covering the stage's artifact, its gate and its measures

## Facilitator notes

Open the series here: draw the six-stage loop and the artifact chain once. Keep the brainstorm in the originator's voice; Claude asks, the person answers.

## Before you begin (participant card)

- Claude Code installed and signed in with a Claude Team or Enterprise seat (claude --version works)
- git, Python 3.9+, and make on the workstation
- A GitHub account with permission to create a private repo (CI and PR labs have a local fallback)
- Optional: one real system of your own in mind for the Bring your own use case tab
