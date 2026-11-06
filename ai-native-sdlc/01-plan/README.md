# Course 1 of 6: Plan

**Capture Intent: Plan in the AI-Native SDLC**

This course covers Stage 1 of Anthropic's AI-native SDLC playbook. It runs hands-on in Claude Code, using the Catalyst Holdings support-ticket triage scenario. It runs alone or as part of the series, because it starts from its own checkpoint repo.

| | |
|---|---|
| Workshop app alias | `ai-native-sdlc-01-plan-v1` |
| Length | 90 minutes: 70 minutes of core steps, 200 points |
| Audience | Engineers |
| Starts from | `starter/catalyst-checkpoint-0.zip` (contains Catalyst support repo with an empty intent/ home, docs/intent-template.md, Care ops notes and sample tickets) |
| Hands off | intent/0001-ticket-triage.md (accepted) |
| Playbook lessons | Introduction: what changes and where to start; Stage 1: Plan, capture as intent.md |

## Learning objectives

1. Explain why code is no longer the bottleneck and where the human-speed steps now sit.
2. Turn an originator's idea into a versioned intent.md with problem, outcome, users and systems, constraints and open questions.
3. Codify intent capture as a reusable project command so every originator gets the same structure.
4. Run the product-owner accept/reject gate as a PR review.

## Get started

```
unzip starter/catalyst-checkpoint-0.zip && cd catalyst-triage
make setup && make test
git log --oneline
claude
```

`git log` shows one commit per artifact from the earlier stages. Accept the workspace trust prompt when Claude Code opens, so the project settings and hooks load.

## Labs

Every lab has four tabs in the workshop app: Catalyst Holdings (the guided path), Bring your own use case, If you're stuck, and What good looks like.

- **Lab A, Brainstorm the ask with Claude.** As Catalyst's support lead, describe the misrouted-ticket problem in your own words and have Claude interview you until it can draft a proto-spec.
  You finish with: Problem, outcome, affected users and systems, constraints, open questions.
- **Lab B, Write and commit intent.md.** Have Claude write intent/0001-ticket-triage.md from the brainstorm using docs/intent-template.md, correct it as the originator, then branch, commit and open a PR.
  You finish with: intent/0001-ticket-triage.md on a branch with an open PR.
- **Lab C, Codify capture as /capture-intent.** Turn the brainstorm prompt into a project slash command so any originator produces the same structure.
  You finish with: .claude/commands/capture-intent.md.
- **Lab D, Run the product-owner review.** In pairs, one plays Catalyst's product owner: correct the intent, then accept or reject in PR review, recording the reason on reject.
  You finish with: PR review decision with corrections or a recorded rejection reason.

## Human gate

The product owner accepts or rejects; acceptance moves the intent to Design. Name the source of truth for intents (the repo, or a repo-to-Jira link at minimum) and who may accept.

## Measures

- Leading: Time from first conversation to committed intent.
- Lagging: Share of intents accepted rather than closed.

## Run of show

| Clock | Segment | Min | Pts |
|---|---|---|---|
| 0:00 to 0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | 5 |  |
| 0:05 to 0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | 8 | 15 |
| 0:13 to 0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | 7 | 10 |
| 0:20 to 0:31 | Lab A: Brainstorm the ask with Claude | 11 | 25 |
| 0:31 to 0:42 | Lab B: Write and commit intent.md | 11 | 25 |
| 0:42 to 0:52 | Lab C: Codify capture as /capture-intent | 10 | 25 |
| 0:52 to 1:02 | Lab D: Run the product-owner review | 10 | 25 |
| 1:02 to 1:09 | The human gate and governance | 7 | 20 |
| 1:09 to 1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | 6 | 15 |
| 1:15 to 1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | 10 |  |
| 1:25 to 1:30 | Wrap: what is committed, next course preview, feedback | 5 |  |

## Files in this folder

- `agenda.md`: the full agenda, with step detail and facilitator notes.
- `starter/catalyst-checkpoint-0.zip`: the repo participants start from.
- `diagrams/loop-plan.svg`
- `diagrams/c1-brainstorm-intent.svg`
- `diagrams/c1-commit-intent.svg`
- `diagrams/c1-intent-command.svg`
- `diagrams/c1-po-review.svg`
- `diagrams/c1-gate.svg`
- `diagrams/c1-handoff.svg`

All people, tickets and figures in the Catalyst Holdings scenario are fictional, and the data is synthetic.
