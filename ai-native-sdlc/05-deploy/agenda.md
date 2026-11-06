# Course 5 of 6: Gates That Hold: Deploy in the AI-Native SDLC

**Alias:** `ai-native-sdlc-05-deploy-v1`  
**Playbook stage:** 5. Deploy  
**Academy lessons covered:** Stage 5: AI in the PR review loop; Hooks as approval gates; CI/CD integration and deployment  
**Length:** 90 minutes (70 minutes of core steps, 200 points)  
**Audience:** engineers, hands-on in Claude Code  
**Runs:** alone or in sequence. It starts from a checkpoint repo, so no earlier course is required.

## Learning objectives

1. Define review passes and severity in REVIEW.md and have Claude review PRs in both directions
2. Use hooks as approval gates that allow, ask or block, including a production gate
3. Run Claude non-interactively in CI with scoped credentials and tiered autonomy by environment
4. Rehearse rollback and explain managed settings for regulated environments

## Starts from / hands off

- **Starts from:** checkpoint-4: tested service, evals and CI eval workflow
- **Hands off:** REVIEW.md, production-gate hook, ci.yml, deployment and rollback record

## Run of show

| Clock | Segment | Step id | Min | Pts |
|---|---|---|---|---|
| 0:00-0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | facilitator | 5 | |
| 0:05-0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | `orient` | 8 | 15 |
| 0:13-0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | `get-the-checkpoint` | 7 | 10 |
| 0:20-0:31 | Lab A: Write REVIEW.md | `review-md` | 11 | 25 |
| 0:31-0:42 | Lab B: Close the PR fix loop | `pr-fix-loop` | 11 | 25 |
| 0:42-0:52 | Lab C: Hooks as approval gates | `approval-hooks` | 10 | 25 |
| 0:52-1:02 | Lab D: CI/CD and rollback | `cicd-and-rollback` | 10 | 25 |
| 1:02-1:09 | The human gate and governance | `gate` | 7 | 20 |
| 1:09-1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | `hand-off` | 6 | 15 |
| 1:15-1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | facilitator | 10 | |
| 1:25-1:30 | Wrap: what is committed, next course preview, feedback | facilitator | 5 | |
| bonus | Expose a deployment tool to Claude through MCP with read-only scope | `bonus-deploy-mcp` | | 20 |
| bonus | Review a managed-settings file for a regulated team | `bonus-managed-settings` | | 20 |

## Step detail

### Orient (`orient`, 8 min)

Traditional: line-by-line human review and committee-driven change approval. AI-native: Claude reviews and addresses review comments, hooks enforce gates as the agent acts, and the agent does everything up to the production gate and nothing past it.

**Quick check:** Can Claude's review findings approve a PR?  
**Answer:** No; branch protection still requires a code owner

### Get the checkpoint (`get-the-checkpoint`, 7 min)

Clone checkpoint-4, run `make setup && make test`, and read CLAUDE.md plus the incoming artifact before changing anything.

### Lab A: Write REVIEW.md (`review-md`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Define review passes (bugs, security, compliance) and severity levels, then have Claude review an open Catalyst PR against them. |
| Bring your own use case | Turn your team's review checklist into REVIEW.md passes. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** REVIEW.md and a review with severity-tagged findings

### Lab B: Close the PR fix loop (`pr-fix-loop`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Leave @claude comments on Claude's own PR and let it address them; fallback is a local claude -p review of the diff. |
| Bring your own use case | Write the three review comments your team leaves most often and test them. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** PR thread with resolved comments

### Lab C: Hooks as approval gates (`approval-hooks`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Add production-gate.sh, ask Claude to run ./deploy/deploy.sh production --shadow, and read the block; set RELEASE_APPROVAL only as the release manager would. Compare team hooks with admin-managed settings. |
| Bring your own use case | Name your production gate and who holds the authorization. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** .claude/hooks/production-gate.sh and its decision log

### Lab D: CI/CD and rollback (`cicd-and-rollback`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Add a sandboxed, non-interactive judgment step to ci.yml with scoped credentials, tier autonomy by environment, and rehearse a rollback. |
| Bring your own use case | Map which environments your agent may act in without a person. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** .github/workflows/ci.yml and a rollback record

### The human gate and governance (`gate`, 7 min)

Code-owner approval through branch protection, release-manager authorization for production, and change-management sign-off. Walk through the playbook's managed-settings example (deny lists, OS sandbox, managed-only hooks and MCP, minimum version).

### Measure and hand off (`hand-off`, 6 min)

- **Leading indicator:** Time to first review
- **Lagging indicator:** Share of review comments resolved without a human touching the branch; DORA metrics
- Commit and push: REVIEW.md, production-gate hook, ci.yml, deployment and rollback record
- Knowledge check: three questions covering the stage's artifact, its gate and its measures

## Facilitator notes

GitHub-dependent steps have a local fallback; confirm repo permissions in the pre-session checklist.

## Before you begin (participant card)

- Claude Code installed and signed in with a Claude Team or Enterprise seat (claude --version works)
- git, Python 3.9+, and make on the workstation
- A GitHub account with permission to create a private repo (CI and PR labs have a local fallback)
- Optional: one real system of your own in mind for the Bring your own use case tab
