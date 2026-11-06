# Course 4 of 6: Check Your Own Work: Test in the AI-Native SDLC

**Alias:** `ai-native-sdlc-04-test-v1`  
**Playbook stage:** 4. Test  
**Academy lessons covered:** Stage 4: Give Claude a feedback loop; Continuous evals in CI  
**Length:** 90 minutes (70 minutes of core steps, 200 points)  
**Audience:** engineers, hands-on in Claude Code  
**Runs:** alone or in sequence. It starts from a checkpoint repo, so no earlier course is required.

## Learning objectives

1. Give Claude quantifiable checks (tests, build, lint) so every session verifies itself
2. Fix a bug test-first, with a hook locking the failing test during the fix
3. Build a small eval set from real tasks with graders and thresholds
4. Run evals in CI on a schedule and whenever CLAUDE.md, skills or hooks change

## Starts from / hands off

- **Starts from:** checkpoint-3: triage service, plan.md, CLAUDE.md, hooks and the eval suite from spec section 4 (no CI yet, redaction bug still present)
- **Hands off:** app/tests/, evals/ (dataset, graders, thresholds.json), CI eval workflow

## Run of show

| Clock | Segment | Step id | Min | Pts |
|---|---|---|---|---|
| 0:00-0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | facilitator | 5 | |
| 0:05-0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | `orient` | 8 | 15 |
| 0:13-0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | `get-the-checkpoint` | 7 | 10 |
| 0:20-0:31 | Lab A: Give Claude a feedback loop | `feedback-loop` | 11 | 25 |
| 0:31-0:42 | Lab B: Failing test first | `failing-test-first` | 11 | 25 |
| 0:42-0:52 | Lab C: Read the gold set, run a slice | `eval-set` | 10 | 25 |
| 0:52-1:02 | Lab D: Continuous evals in CI | `evals-in-ci` | 10 | 25 |
| 1:02-1:09 | The human gate and governance | `gate` | 7 | 20 |
| 1:09-1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | `hand-off` | 6 | 15 |
| 1:15-1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | facilitator | 10 | |
| 1:25-1:30 | Wrap: what is committed, next course preview, feedback | facilitator | 5 | |
| bonus | Calibrate an LLM judge against human-labeled cases | `bonus-judge-calibration` | | 20 |
| bonus | Use a screenshot comparison as the feedback loop for a UI change | `bonus-screenshot-diff` | | 20 |

## Step detail

### Orient (`orient`, 8 min)

Traditional: QA tests after the build and agent configuration is never tested. AI-native: every session runs its own checks before a person sees it, and the configuration that steers the agent is regression-tested like code.

**Quick check:** What should trigger a re-run of the eval suite besides a schedule?  
**Answer:** Any change to CLAUDE.md, skills or hooks

### Get the checkpoint (`get-the-checkpoint`, 7 min)

Clone checkpoint-3, run `make setup && make test`, and read CLAUDE.md plus the incoming artifact before changing anything.

### Lab A: Give Claude a feedback loop (`feedback-loop`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Wire make test and lint into the session and have Claude iterate until they pass, quoting the literal output. |
| Bring your own use case | Identify the one command that proves your system works and make Claude run it. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** Literal test and lint output in the session log

### Lab B: Failing test first (`failing-test-first`, 11 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Reproduce the redaction bug (a ZIP mid-sentence after a state code, a French street address) as failing tests, then fix redact.py with TRIAGE_FIX_MODE=1 so protect-paths.sh blocks any edit to app/tests. |
| Bring your own use case | Write the failing test for a bug from your own backlog. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** Two new failing tests in test_redact.py, then a passing fix in redact.py

### Lab C: Read the gold set, run a slice (`eval-set`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Read the 66-case gold set (7 slices), the graders and thresholds.json (copied from spec section 4), then run make eval-slice SLICE=injection (about 1 minute, under $0.30). |
| Bring your own use case | List 20 real tasks from your system that would form your first eval set. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** Slice result scored against thresholds.json

### Lab D: Continuous evals in CI (`evals-in-ci`, 10 min)

| Tab | Content |
|---|---|
| Catalyst Holdings | Add the workflow that runs evals on a schedule and on config changes, enforce the pass rate as a merge check, and turn a past incident into a permanent eval. |
| Bring your own use case | Decide your own pass-rate threshold and who owns changing it. |
| If you're stuck | Symptom, hint and rescue prompt (written at build time) |
| What good looks like | Excerpt of the finished artifact |

**Done looks like:** .github/workflows/agent-evals.yml and an incident eval case

### The human gate and governance (`gate`, 7 min)

A pass-rate threshold is enforced as a merge check; the team that owns the configuration approves changes to it.

### Measure and hand off (`hand-off`, 6 min)

- **Leading indicator:** First-pass CI success rate
- **Lagging indicator:** Regressions caught in CI vs in production
- Commit and push: app/tests/, evals/ (dataset, graders, thresholds.json), CI eval workflow
- Knowledge check: three questions covering the stage's artifact, its gate and its measures

## Facilitator notes

The playbook suggests starting with 20 to 50 real tasks. The full suite (v1 vs v2, 3 runs, about 8 minutes, about $6 of usage) is a facilitator demo only; labs run one slice. Start make eval at the top of Lab C and use the talk track in the facilitator guide while it runs.

## Before you begin (participant card)

- Claude Code installed and signed in with a Claude Team or Enterprise seat (claude --version works)
- git, Python 3.9+, and make on the workstation
- A GitHub account with permission to create a private repo (CI and PR labs have a local fallback)
- Optional: one real system of your own in mind for the Bring your own use case tab
