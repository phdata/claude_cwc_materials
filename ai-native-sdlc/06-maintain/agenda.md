# Course 6 of 6: Close the Loop: Maintain in the AI-Native SDLC

**Alias:** `ai-native-sdlc-06-maintain-v1`  
**Playbook stage:** 6. Maintain  
**Academy lessons covered:** Stage 6: Closing the loop on metrics; Closing thoughts and resources  
**Length:** 90 minutes (70 minutes of core steps, 200 points)  
**Audience:** engineers, hands-on in Claude Code  
**Runs:** alone or in sequence. It starts from a checkpoint repo, so no earlier course is required.

## Learning objectives

1. Set deterministic detection with rolling-baseline bands so no model runs until a band is breached
2. Have Claude diagnose a breach read-only and propose a fix only at the highest band
3. Feed findings back into the pipeline as a new intent.md
4. Schedule recurring scans and keep a version-controlled lessons file

## Starts from / hands off

- **Starts from:** checkpoint-5: deployed service with REVIEW.md, gates and CI
- **Hands off:** ops/bands.yaml, ops/lessons.md, intent/0002-ember-recall-product-safety-misroute.md (input to Course 1)

## Run of show

| Clock | Segment | Step id | Min | Pts |
|---|---|---|---|---|
| 0:00-0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | facilitator | 5 | |
| 0:05-0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | `orient` | 8 | 15 |
| 0:13-0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | `get-the-checkpoint` | 7 | 10 |
| 0:20-0:31 | Lab A: Deterministic bands | `bands` | 11 | 25 |
| 0:31-0:42 | Lab B: Diagnose a breach | `breach-diagnosis` | 11 | 25 |
| 0:42-0:52 | Lab C: Close the loop | `close-the-loop` | 10 | 25 |
| 0:52-1:02 | Lab D: Scans and lessons | `scans-and-lessons` | 10 | 25 |
| 1:02-1:09 | The human gate and governance | `gate` | 7 | 20 |
| 1:09-1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | `hand-off` | 6 | 15 |
| 1:15-1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | facilitator | 10 | |
| 1:25-1:30 | Wrap: what is committed, next course preview, feedback | facilitator | 5 | |
| bonus | Facilitator demo in the demo environment: Claude Tag joins a Slack incident channel and writes the lesson (public beta) | `bonus-claude-tag` | | 20 |
| bonus | Write the pre-approved rollback runbook Claude may trigger at 3 sigma, and the conditions that keep it human-only | `bonus-runbook` | | 20 |

## Step detail

### Orient (`orient`, 8 min)

Traditional: dashboards wait for someone to look and incidents end in a wiki page. AI-native: a deterministic trigger invokes Claude without a person starting it, and its findings re-enter the pipeline as intent.md.

**Quick check:** At which band does Claude first get invoked, and with what permissions?  
**Answer:** At 2 sigma, read-only diagnosis; detection below that stays model-free

### Get the checkpoint (`get-the-checkpoint`, 7 min)

Clone checkpoint-5, run `make setup && make test`, and read CLAUDE.md plus the incoming artifact before changing anything.

### Lab A: Deterministic bands (`bands`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Write ops/bands.yaml for agent_override_rate (rolling 30-day baseline, Western Electric rules, three tiers), have Claude confirm ops/detect.py implements exactly that contract, then run python -m ops.detect with no model involved. |
| Bring your own use case | Pick one metric from your system and set its three bands. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** ops/bands.yaml and a detection log

### Lab B: Diagnose a breach (`breach-diagnosis`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Run python -m ops.detect --invoke against the Ember heater recall spike (override rate 19.0% vs 8.1% baseline); Claude reads the override records only and drafts an intent with evidence. |
| Bring your own use case | Describe what read-only access Claude would need to diagnose your metric. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** Diagnosis note with evidence

### Lab C: Close the loop (`close-the-loop`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Review the drafted intent as the service owner (fix, schedule or dismiss), correct it and commit it as intent/0002, ready for Course 1's product-owner gate. |
| Bring your own use case | Write the intent your own breach would produce. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** intent/0002-ember-recall-product-safety-misroute.md

### Lab D: Scans and lessons (`scans-and-lessons`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Write the post-mortem to ops/lessons.md and schedule a recurring codebase scan (a scheduled Claude Code task or a CI cron job) whose findings go through the PR gate. |
| Bring your own use case | Choose the scan cadence and owner for your system. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** lessons file entry and a scheduled scan definition

### The human gate and governance (`gate`, 7 min)

The service owner or on-call engineer triages each finding (fix, schedule or dismiss); fixes go through the PR gate; only pre-approved runbooks run automatically.

### Measure and hand off (`hand-off`, 6 min)

- **Leading indicator:** Time from band breach to triage item
- **Lagging indicator:** Share of findings that become merged fixes; repeat incidents of the same class
- Commit and push: ops/bands.yaml, ops/lessons.md, intent/0002-ember-recall-product-safety-misroute.md (input to Course 1)
- Knowledge check: three questions covering the stage's artifact, its gate and its measures

## Facilitator notes

Claude Tag runs only in the instructor demo environment; participants watch. End the series by showing intent/0002 entering Course 1's gate. Close by naming the next step: the product owner reviews intent/0002.

## Before you begin (participant card)

- Claude Code installed and signed in with a Claude Team or Enterprise seat (claude --version works)
- git, Python 3.9+, and make on the workstation
- A GitHub account with permission to create a private repo (CI and PR labs have a local fallback)
- Optional: one real system of your own in mind for the Bring your own use case tab
