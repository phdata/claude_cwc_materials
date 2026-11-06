# Course 2 of 6: Spec with Policy Built In: Design in the AI-Native SDLC

**Alias:** `ai-native-sdlc-02-design-v1`  
**Playbook stage:** 2. Design  
**Academy lessons covered:** Stage 2: Design, requirements and design  
**Length:** 90 minutes (70 minutes of core steps, 200 points)  
**Audience:** engineers, hands-on in Claude Code  
**Runs:** alone or in sequence. It starts from a checkpoint repo, so no earlier course is required.

## Learning objectives

1. Generate requirements and design together as spec.md from an accepted intent.md
2. Encode organization policy (PII handling, LLM input safety, the support taxonomy) as skills that constrain the spec while it is written
3. Resolve flagged areas of concern with policy owners before engineering sees the spec
4. Codify the design pass as a slash command and a headless job that opens spec.md as a PR

## Starts from / hands off

- **Starts from:** checkpoint-1: accepted intent/0001-ticket-triage.md
- **Hands off:** spec.md plus .claude/skills/* (policy), committed beside intent.md

## Run of show

| Clock | Segment | Step id | Min | Pts |
|---|---|---|---|---|
| 0:00-0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | facilitator | 5 | |
| 0:05-0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | `orient` | 8 | 15 |
| 0:13-0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | `get-the-checkpoint` | 7 | 10 |
| 0:20-0:31 | Lab A: Encode Catalyst policy as skills | `policy-skills` | 11 | 25 |
| 0:31-0:42 | Lab B: Run the design pass | `design-pass` | 11 | 25 |
| 0:42-0:52 | Lab C: Resolve flagged concerns | `resolve-concerns` | 10 | 25 |
| 0:52-1:02 | Lab D: Codify and automate the pass | `codify-design` | 10 | 25 |
| 1:02-1:09 | The human gate and governance | `gate` | 7 | 20 |
| 1:09-1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | `hand-off` | 6 | 15 |
| 1:15-1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | facilitator | 10 | |
| 1:25-1:30 | Wrap: what is committed, next course preview, feedback | facilitator | 5 | |
| bonus | Mock the agent override screen in Claude Design and link it from spec.md | `bonus-design-mockup` | | 20 |
| bonus | Resolve a case where two skills give conflicting guidance | `bonus-policy-conflict` | | 20 |

## Step detail

### Orient (`orient`, 8 min)

Traditional: requirements and design pass between teams over weeks, and policy review happens after the fact. AI-native: one prompted session produces the spec, constrained by organization skills, with concerns flagged for policy owners.

**Quick check:** Who writes spec.md in the AI-native Design stage?  
**Answer:** Claude generates it from intent.md under organization skills, and the product owner reviews it

### Get the checkpoint (`get-the-checkpoint`, 7 min)

Clone checkpoint-1, run `make setup && make test`, and read CLAUDE.md plus the incoming artifact before changing anything.

### Lab A: Encode Catalyst policy as skills (`policy-skills`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Install the three Catalyst organization skills from org-skills/ (pii-handling 1.2.0, llm-input-safety 1.0.3, support-taxonomy 3.1.0) into .claude/skills/, ask Claude which rules in each apply to intent 0001, and log the versions in force. |
| Bring your own use case | Write one SKILL.md for a policy your team enforces today by memory or checklist. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** .claude/skills/{pii-handling,llm-input-safety,support-taxonomy}/SKILL.md installed, versions logged in sdlc/prompts/design.md

### Lab B: Run the design pass (`design-pass`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | From intent.md, have Claude produce spec.md: requirements, design, constraint mapping, open questions and flagged areas of concern. |
| Bring your own use case | Run the same prompt against the intent you wrote for your own system. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** spec.md with a flagged-concerns section

### Lab C: Resolve flagged concerns (`resolve-concerns`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Work through concerns C1 to C4 (French-Canadian scope, address redaction, auto-routing, injected summaries) with a partner playing each policy owner; record each decision in spec.md. |
| Bring your own use case | Pick your spec's highest-risk concern and resolve it with your partner as policy owner. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** spec.md with each concern marked resolved, deferred or escalated

### Lab D: Codify and automate the pass (`codify-design`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Save the prompt as an org slash command, then run the headless claude -p job that opens spec.md as a PR when an intent merges (workflow YAML shown, run locally). |
| Bring your own use case | Sketch where the trigger would live in your own CI system. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** .claude/commands/design-from-intent.md and .github/workflows/spec-on-intent.yml

### The human gate and governance (`gate`, 7 min)

A human team member decides whether the spec moves to build; a technical lead is consulted on higher-risk work. The spec, the prompt and the skill versions are logged in version control.

### Measure and hand off (`hand-off`, 6 min)

- **Leading indicator:** Time from intent.md commit to spec.md commit
- **Lagging indicator:** spec.md commits made after the first plan.md commit for the same change
- Commit and push: spec.md plus .claude/skills/* (policy), committed beside intent.md
- Knowledge check: three questions covering the stage's artifact, its gate and its measures

## Facilitator notes

Stress that skills are advisory at this stage; Course 3 shows why deterministic enforcement needs hooks.

## Before you begin (participant card)

- Claude Code installed and signed in with a Claude Team or Enterprise seat (claude --version works)
- git, Python 3.9+, and make on the workstation
- A GitHub account with permission to create a private repo (CI and PR labs have a local fallback)
- Optional: one real system of your own in mind for the Bring your own use case tab
