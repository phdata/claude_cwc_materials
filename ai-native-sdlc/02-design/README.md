# Course 2 of 6: Design

**Spec with Policy Built In: Design in the AI-Native SDLC**

This course covers Stage 2 of Anthropic's AI-native SDLC playbook. It runs hands-on in Claude Code, using the Catalyst Holdings support-ticket triage scenario. It runs alone or as part of the series, because it starts from its own checkpoint repo.

| | |
|---|---|
| Workshop app alias | `ai-native-sdlc-02-design-v1` |
| Length | 90 minutes: 70 minutes of core steps, 200 points |
| Audience | Engineers |
| Starts from | `starter/catalyst-checkpoint-1.zip` (contains accepted intent/0001-ticket-triage.md) |
| Hands off | spec.md plus .claude/skills/* (policy), committed beside intent.md |
| Playbook lessons | Stage 2: Design, requirements and design |

## Learning objectives

1. Generate requirements and design together as spec.md from an accepted intent.md.
2. Encode organization policy (PII handling, LLM input safety, the support taxonomy) as skills that constrain the spec while it is written.
3. Resolve flagged areas of concern with policy owners before engineering sees the spec.
4. Codify the design pass as a slash command and a headless job that opens spec.md as a PR.

## Get started

```
unzip starter/catalyst-checkpoint-1.zip && cd catalyst-triage
make setup && make test
git log --oneline
claude
```

`git log` shows one commit per artifact from the earlier stages. Accept the workspace trust prompt when Claude Code opens, so the project settings and hooks load.

## Labs

Every lab has four tabs in the workshop app: Catalyst Holdings (the guided path), Bring your own use case, If you're stuck, and What good looks like.

- **Lab A, Encode Catalyst policy as skills.** Install the three Catalyst organization skills from org-skills/ (pii-handling 1.2.0, llm-input-safety 1.0.3, support-taxonomy 3.1.0) into .claude/skills/, ask Claude which rules in each apply to intent 0001, and log the versions in force.
  You finish with: .claude/skills/{pii-handling,llm-input-safety,support-taxonomy}/SKILL.md installed, versions logged in sdlc/prompts/design.md.
- **Lab B, Run the design pass.** From intent.md, have Claude produce spec.md: requirements, design, constraint mapping, open questions and flagged areas of concern.
  You finish with: spec.md with a flagged-concerns section.
- **Lab C, Resolve flagged concerns.** Work through concerns C1 to C4 (French-Canadian scope, address redaction, auto-routing, injected summaries) with a partner playing each policy owner; record each decision in spec.md.
  You finish with: spec.md with each concern marked resolved, deferred or escalated.
- **Lab D, Codify and automate the pass.** Save the prompt as an org slash command, then run the headless claude -p job that opens spec.md as a PR when an intent merges (workflow YAML shown, run locally).
  You finish with: .claude/commands/design-from-intent.md and .github/workflows/spec-on-intent.yml.

## Human gate

A human team member decides whether the spec moves to build; a technical lead is consulted on higher-risk work. The spec, the prompt and the skill versions are logged in version control.

## Measures

- Leading: Time from intent.md commit to spec.md commit.
- Lagging: spec.md commits made after the first plan.md commit for the same change.

## Run of show

| Clock | Segment | Min | Pts |
|---|---|---|---|
| 0:00 to 0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | 5 |  |
| 0:05 to 0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | 8 | 15 |
| 0:13 to 0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | 7 | 10 |
| 0:20 to 0:31 | Lab A: Encode Catalyst policy as skills | 11 | 25 |
| 0:31 to 0:42 | Lab B: Run the design pass | 11 | 25 |
| 0:42 to 0:52 | Lab C: Resolve flagged concerns | 10 | 25 |
| 0:52 to 1:02 | Lab D: Codify and automate the pass | 10 | 25 |
| 1:02 to 1:09 | The human gate and governance | 7 | 20 |
| 1:09 to 1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | 6 | 15 |
| 1:15 to 1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | 10 |  |
| 1:25 to 1:30 | Wrap: what is committed, next course preview, feedback | 5 |  |

## Files in this folder

- `agenda.md`: the full agenda, with step detail and facilitator notes.
- `starter/catalyst-checkpoint-1.zip`: the repo participants start from.
- `diagrams/loop-design.svg`
- `diagrams/c2-policy-skills.svg`
- `diagrams/c2-design-pass.svg`
- `diagrams/c2-resolve-concerns.svg`
- `diagrams/c2-codify-design.svg`
- `diagrams/c2-gate.svg`
- `diagrams/c2-handoff.svg`

All people, tickets and figures in the Catalyst Holdings scenario are fictional, and the data is synthetic.
