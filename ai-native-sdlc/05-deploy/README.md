# Course 5 of 6: Deploy

**Gates That Hold: Deploy in the AI-Native SDLC**

This course covers Stage 5 of Anthropic's AI-native SDLC playbook. It runs hands-on in Claude Code, using the Catalyst Holdings support-ticket triage scenario. It runs alone or as part of the series, because it starts from its own checkpoint repo.

| | |
|---|---|
| Workshop app alias | `ai-native-sdlc-05-deploy-v1` |
| Length | 90 minutes: 70 minutes of core steps, 200 points |
| Audience | Engineers |
| Starts from | `starter/catalyst-checkpoint-4.zip` (contains tested service, evals and CI eval workflow) |
| Hands off | REVIEW.md, production-gate hook, ci.yml, deployment and rollback record |
| Playbook lessons | Stage 5: AI in the PR review loop; Hooks as approval gates; CI/CD integration and deployment |

## Learning objectives

1. Define review passes and severity in REVIEW.md and have Claude review PRs in both directions.
2. Use hooks as approval gates that allow, ask or block, including a production gate.
3. Run Claude non-interactively in CI with scoped credentials and tiered autonomy by environment.
4. Rehearse rollback and explain managed settings for regulated environments.

## Get started

```
unzip starter/catalyst-checkpoint-4.zip && cd catalyst-triage
make setup && make test
git log --oneline
claude
```

`git log` shows one commit per artifact from the earlier stages. Accept the workspace trust prompt when Claude Code opens, so the project settings and hooks load.

## Labs

Every lab has four tabs in the workshop app: Catalyst Holdings (the guided path), Bring your own use case, If you're stuck, and What good looks like.

- **Lab A, Write REVIEW.md.** Define review passes (bugs, security, compliance) and severity levels, then have Claude review an open Catalyst PR against them.
  You finish with: REVIEW.md and a review with severity-tagged findings.
- **Lab B, Close the PR fix loop.** Leave @claude comments on Claude's own PR and let it address them; fallback is a local claude -p review of the diff.
  You finish with: PR thread with resolved comments.
- **Lab C, Hooks as approval gates.** Add production-gate.sh, ask Claude to run ./deploy/deploy.sh production --shadow, and read the block; set RELEASE_APPROVAL only as the release manager would. Compare team hooks with admin-managed settings.
  You finish with: .claude/hooks/production-gate.sh and its decision log.
- **Lab D, CI/CD and rollback.** Add a sandboxed, non-interactive judgment step to ci.yml with scoped credentials, tier autonomy by environment, and rehearse a rollback.
  You finish with: .github/workflows/ci.yml and a rollback record.

## Human gate

Code-owner approval through branch protection, release-manager authorization for production, and change-management sign-off. Walk through the playbook's managed-settings example (deny lists, OS sandbox, managed-only hooks and MCP, minimum version).

## Measures

- Leading: Time to first review.
- Lagging: Share of review comments resolved without a human touching the branch; DORA metrics.

## Run of show

| Clock | Segment | Min | Pts |
|---|---|---|---|
| 0:00 to 0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | 5 |  |
| 0:05 to 0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | 8 | 15 |
| 0:13 to 0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | 7 | 10 |
| 0:20 to 0:31 | Lab A: Write REVIEW.md | 11 | 25 |
| 0:31 to 0:42 | Lab B: Close the PR fix loop | 11 | 25 |
| 0:42 to 0:52 | Lab C: Hooks as approval gates | 10 | 25 |
| 0:52 to 1:02 | Lab D: CI/CD and rollback | 10 | 25 |
| 1:02 to 1:09 | The human gate and governance | 7 | 20 |
| 1:09 to 1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | 6 | 15 |
| 1:15 to 1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | 10 |  |
| 1:25 to 1:30 | Wrap: what is committed, next course preview, feedback | 5 |  |

## Files in this folder

- `agenda.md`: the full agenda, with step detail and facilitator notes.
- `starter/catalyst-checkpoint-4.zip`: the repo participants start from.
- `diagrams/loop-deploy.svg`
- `diagrams/c5-review-md.svg`
- `diagrams/c5-pr-fix-loop.svg`
- `diagrams/c5-approval-hooks.svg`
- `diagrams/c5-cicd-and-rollback.svg`
- `diagrams/c5-gate.svg`
- `diagrams/c5-handoff.svg`

All people, tickets and figures in the Catalyst Holdings scenario are fictional, and the data is synthetic.
