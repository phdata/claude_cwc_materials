# Course 4 of 6: Test

**Check Your Own Work: Test in the AI-Native SDLC**

This course covers Stage 4 of Anthropic's AI-native SDLC playbook. It runs hands-on in Claude Code, using the Catalyst Holdings support-ticket triage scenario. It runs alone or as part of the series, because it starts from its own checkpoint repo.

| | |
|---|---|
| Workshop app alias | `ai-native-sdlc-04-test-v1` |
| Length | 90 minutes: 70 minutes of core steps, 200 points |
| Audience | Engineers |
| Starts from | `starter/catalyst-checkpoint-3.zip` (contains triage service, plan.md, CLAUDE.md, hooks and the eval suite from spec section 4 (no CI yet, redaction bug still present)) |
| Hands off | app/tests/, evals/ (dataset, graders, thresholds.json), CI eval workflow |
| Playbook lessons | Stage 4: Give Claude a feedback loop; Continuous evals in CI |

## Learning objectives

1. Give Claude quantifiable checks (tests, build, lint) so every session verifies itself.
2. Fix a bug test-first, with a hook locking the failing test during the fix.
3. Build a small eval set from real tasks with graders and thresholds.
4. Run evals in CI on a schedule and whenever CLAUDE.md, skills or hooks change.

## Get started

```
unzip starter/catalyst-checkpoint-3.zip && cd catalyst-triage
make setup && make test
git log --oneline
claude
```

`git log` shows one commit per artifact from the earlier stages. Accept the workspace trust prompt when Claude Code opens, so the project settings and hooks load.

## Labs

Every lab has four tabs in the workshop app: Catalyst Holdings (the guided path), Bring your own use case, If you're stuck, and What good looks like.

- **Lab A, Give Claude a feedback loop.** Wire make test and lint into the session and have Claude iterate until they pass, quoting the literal output.
  You finish with: Literal test and lint output in the session log.
- **Lab B, Failing test first.** Reproduce the redaction bug (a ZIP mid-sentence after a state code, a French street address) as failing tests, then fix redact.py with TRIAGE_FIX_MODE=1 so protect-paths.sh blocks any edit to app/tests.
  You finish with: Two new failing tests in test_redact.py, then a passing fix in redact.py.
- **Lab C, Read the gold set, run a slice.** Read the 66-case gold set (7 slices), the graders and thresholds.json (copied from spec section 4), then run make eval-slice SLICE=injection (about 1 minute, under $0.30).
  You finish with: Slice result scored against thresholds.json.
- **Lab D, Continuous evals in CI.** Add the workflow that runs evals on a schedule and on config changes, enforce the pass rate as a merge check, and turn a past incident into a permanent eval.
  You finish with: .github/workflows/agent-evals.yml and an incident eval case.

## Human gate

A pass-rate threshold is enforced as a merge check; the team that owns the configuration approves changes to it.

## Measures

- Leading: First-pass CI success rate.
- Lagging: Regressions caught in CI vs in production.

## Run of show

| Clock | Segment | Min | Pts |
|---|---|---|---|
| 0:00 to 0:05 | Facilitator open: the loop, today's stage, pick a path (Catalyst or BYO) | 5 |  |
| 0:05 to 0:13 | Orient: traditional vs AI-native for this stage, plus a 1-question quick check | 8 | 15 |
| 0:13 to 0:20 | Get the checkpoint: clone, run, read CLAUDE.md and the incoming artifact | 7 | 10 |
| 0:20 to 0:31 | Lab A: Give Claude a feedback loop | 11 | 25 |
| 0:31 to 0:42 | Lab B: Failing test first | 11 | 25 |
| 0:42 to 0:52 | Lab C: Read the gold set, run a slice | 10 | 25 |
| 0:52 to 1:02 | Lab D: Continuous evals in CI | 10 | 25 |
| 1:02 to 1:09 | The human gate and governance | 7 | 20 |
| 1:09 to 1:15 | Measure and hand off: indicators, commit the artifact, knowledge check | 6 | 15 |
| 1:15 to 1:25 | Share-out: 2 to 3 participants show their artifact (BYO first), facilitator debrief | 10 |  |
| 1:25 to 1:30 | Wrap: what is committed, next course preview, feedback | 5 |  |

## Files in this folder

- `agenda.md`: the full agenda, with step detail and facilitator notes.
- `starter/catalyst-checkpoint-3.zip`: the repo participants start from.
- `diagrams/loop-test.svg`
- `diagrams/c4-feedback-loop.svg`
- `diagrams/c4-failing-test-first.svg`
- `diagrams/c4-eval-slices.svg`
- `diagrams/c4-evals-in-ci.svg`
- `diagrams/c4-gate.svg`
- `diagrams/c4-handoff.svg`

All people, tickets and figures in the Catalyst Holdings scenario are fictional, and the data is synthetic.
