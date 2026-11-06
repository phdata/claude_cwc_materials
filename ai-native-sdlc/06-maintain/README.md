# Course 6 of 6: Maintain

**Close the Loop: Maintain in the AI-Native SDLC**

This course covers Stage 6 of Anthropic's AI-native SDLC playbook. It runs hands-on in Claude Code, using the Catalyst Holdings support-ticket triage scenario. It runs alone or as part of the series, because it starts from its own checkpoint repo.

| | |
|---|---|
| Workshop app alias | `ai-native-sdlc-06-maintain-v1` |
| Length | 90 minutes: 70 minutes of core steps, 200 points |
| Audience | Engineers |
| Starts from | `starter/catalyst-checkpoint-5.zip` (contains deployed service with REVIEW.md, gates and CI) |
| Hands off | ops/bands.yaml, ops/lessons.md, intent/0002-ember-recall-product-safety-misroute.md (input to Course 1) |
| Playbook lessons | Stage 6: Closing the loop on metrics; Closing thoughts and resources |

## Learning objectives

1. Set deterministic detection with rolling-baseline bands so no model runs until a band is breached.
2. Have Claude diagnose a breach read-only and propose a fix only at the highest band.
3. Feed findings back into the pipeline as a new intent.md.
4. Schedule recurring scans and keep a version-controlled lessons file.

## Get started

```
unzip starter/catalyst-checkpoint-5.zip && cd catalyst-triage
make setup && make test
git log --oneline
claude
```

`git log` shows one commit per artifact from the earlier stages. Accept the workspace trust prompt when Claude Code opens, so the project settings and hooks load.

## Labs

Every lab has four tabs in the workshop app: Catalyst Holdings (the guided path), Bring your own use case, If you're stuck, and What good looks like.

- **Lab A, Deterministic bands.** Write ops/bands.yaml for agent_override_rate (rolling 30-day baseline, Western Electric rules, three tiers), have Claude confirm ops/detect.py implements exactly that contract, then run python -m ops.detect with no model involved.
  You finish with: ops/bands.yaml and a detection log.
- **Lab B, Diagnose a breach.** Run python -m ops.detect --invoke against the Ember heater recall spike (override rate 19.0% vs 8.1% baseline); Claude reads the override records only and drafts an intent with evidence.
  You finish with: Diagnosis note with evidence.
- **Lab C, Close the loop.** Review the drafted intent as the service owner (fix, schedule or dismiss), correct it and commit it as intent/0002, ready for Course 1's product-owner gate.
  You finish with: intent/0002-ember-recall-product-safety-misroute.md.
- **Lab D, Scans and lessons.** Write the post-mortem to ops/lessons.md and schedule a recurring codebase scan (a scheduled Claude Code task or a CI cron job) whose findings go through the PR gate.
  You finish with: lessons file entry and a scheduled scan definition.

## Human gate

The service owner or on-call engineer triages each finding (fix, schedule or dismiss); fixes go through the PR gate; only pre-approved runbooks run automatically.

## Measures

- Leading: Time from band breach to triage item.
- Lagging: Share of findings that become merged fixes; repeat incidents of the same class.

## Run of show

| Clock | Segment | Min | Pts |
|---|---|---|---|
| 0:00 to 0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | 5 |  |
| 0:05 to 0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | 8 | 15 |
| 0:13 to 0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | 7 | 10 |
| 0:20 to 0:31 | Lab A: Deterministic bands | 11 | 25 |
| 0:31 to 0:42 | Lab B: Diagnose a breach | 11 | 25 |
| 0:42 to 0:52 | Lab C: Close the loop | 10 | 25 |
| 0:52 to 1:02 | Lab D: Scans and lessons | 10 | 25 |
| 1:02 to 1:09 | The human gate and governance | 7 | 20 |
| 1:09 to 1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | 6 | 15 |
| 1:15 to 1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | 10 |  |
| 1:25 to 1:30 | Wrap: what is committed, next course preview, feedback | 5 |  |

## Files in this folder

- `agenda.md`: the full agenda, with step detail and facilitator notes.
- `starter/catalyst-checkpoint-5.zip`: the repo participants start from.
- `diagrams/loop-maintain.svg`
- `diagrams/override-bands.svg`
- `diagrams/c6-override-pairs.svg`
- `diagrams/c6-close-the-loop.svg`
- `diagrams/c6-scans-and-lessons.svg`
- `diagrams/c6-gate.svg`
- `diagrams/c6-handoff.svg`

All people, tickets and figures in the Catalyst Holdings scenario are fictional, and the data is synthetic.
