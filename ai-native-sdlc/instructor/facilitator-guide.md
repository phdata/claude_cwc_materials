# AI-Native SDLC Series: Facilitator Guide

Six 90-minute, hands-on Claude Code courses for engineers. They follow one Catalyst Holdings scenario: an LLM support-ticket triage service. Each course covers one stage of Anthropic's AI-native SDLC playbook. Each course also starts from its own checkpoint repo, so it runs alone or in sequence.

The per-course agendas live in `plan/agendas/`. This guide covers what the agendas leave out: preparation, the instructor-only demos, and the talk tracks.

## Before any session

| When | Check | How |
|---|---|---|
| 2 weeks out | Client intake received (custom cut only) | `plan/use-case-intake.md`. Rebuild the Catalyst tab content and the checkpoints from it. |
| 1 week out | Checkpoint zips are live | Open `/assets/workshops/ai-native-sdlc/catalyst-checkpoint-N.zip` on the production site for N = 0 to 6 |
| 1 week out | Templates imported | Import `out/exports/ai-native-sdlc-series-v1.csv` (or one CSV per course) into production |
| 1 week out | Preview looks right | Load each `out/json/*.json` in `Course_Assets/Template Test/preview-template.html` |
| 2 days out | Participants can run Claude Code | Send the Before You Begin list. `claude --version`, `python3 --version` (3.9+), `git`, `make`, `unzip` |
| Day of, 30 min out | Instructor checkpoint ready | Unzip the course's checkpoint, `make setup && make test`, then open Claude Code in it |
| Day of, Course 4 | Eval preflight | Run `make eval-slice SLICE=routine` once in checkpoint-3 to confirm the CLI backend works |
| Day of, Course 6 | Demo environment for Claude Tag | Sign in to the demo Slack workspace with Claude Tag added to an incident channel |

**Shared run of show.** Every course uses the same order:
- 0:00 to 0:05: open.
- 0:05 to 1:15: core steps.
- 1:15 to 1:25: share-out, with Bring-your-own-use-case participants first.
- 1:25 to 1:30: wrap.

Watch the clock at Lab C (0:42). Anyone behind at that point should download the next checkpoint and continue from there.

**Two paths in every lab.** The Catalyst Holdings tab is the guided path. The Bring your own use case tab applies the same move to the participant's own system. Remind BYO participants to paste only material they are cleared to share in training.

## Course notes

**Course 1, Plan.** Open the series here. Draw the six-stage loop once and point at the artifact each stage commits. In Lab A, keep the brainstorm in the originator's voice: Claude asks and the person answers. If Claude proposes a design, use the rescue prompt and name the moment: "that is Stage 2 work."

**Course 2, Design.** The design pass in Lab B takes a few minutes. While it runs, read section 3 (areas of concern) aloud as it appears. Concern C2 is a real policy conflict and usually the longest discussion of the session. The PII library cannot redact addresses that policy PRV-04 says must never reach the model.

**Course 3, Build.** Lab D builds only the first plan step. Say so up front so nobody tries to build the whole service in 10 minutes; checkpoint-3 has it. In Lab C, the blocked edit under `evals/dataset/` is the moment to stop and ask: "Which of today's rules would you trust to a skill, and which need a hook?"

**Course 4, Test.** Start the full eval suite at the top of Lab C and use the talk track below. Participants run one slice, about a minute and under $0.30 each.

**Course 5, Deploy.** Most rooms won't have the Claude GitHub app installed. Lab B's local fix loop is the default path, and the `@claude` path is a short demo if your repo has it. In Lab C, read the block message aloud. It names the release manager and the change ticket, so the agent tells the human exactly who approves.

**Course 6, Maintain.** Lab B (`ops.detect --invoke`) takes about 40 seconds and about $0.10. The bonus Claude Tag demo runs **only in the instructor demo environment**; participants watch. End the series by opening intent 0002's pull request and saying where it goes next: Course 1's product owner gate.

## Talk track: the full eval suite (Course 4, about 8 minutes)

Run in your checkpoint-3 copy at the start of Lab C:

```
make eval
```

It runs prompt v1 against v2 on the 66-case gold set, 3 runs per case, plus the calibrated LLM judge. Expect about 8 minutes and about $6 of usage. Keep talking while it runs; participants work on their slice and look up when you call out a point.

**0:00 to 1:00. What is running.**
- 66 synthetic tickets in 7 slices: routine, ambiguous, multi-issue, escalation, non-English, injection and PII.
- Two prompt versions, three runs each. "Three runs, because the same input can come back with a different answer, and we want to see the spread, not one lucky draw."

**1:00 to 3:00. The graders.**
- Most of the checks are deterministic code: schema validity, category, queue, priority, the human-review flag, PII leaks and injection resistance. No model grades another model where code can.
- Only summary quality uses an LLM judge, and only after it agreed with human labels on the calibration set.
- Ask the room: "Which of these would you trust a model to grade?"

**3:00 to 5:00. Thresholds are the spec.**
- Open `evals/thresholds.json` beside spec section 4: same numbers, same owner. Changing a threshold needs the product owner.
- Changing a gold label needs Care ops. The hook from Course 3 blocks it otherwise.
- Ask the room: "Which threshold would you never relax?" The usual answers are zero PII leaks and needs-human recall.

**5:00 to 7:00. Reading the result.**
- When the run finishes, compare v1 and v2 metric by metric against the thresholds.
- The last recorded run of the source repo, on 2026-10-08, had this pattern:
  - v2 met 10 of 11 thresholds and missed cost at $5.12 against $5.00 per 1,000 tickets.
  - v1 failed 6, because its summaries were too long for the schema.
- Your numbers will differ from run to run, which is why each case runs three times.

**7:00 to 8:00. The decision is human.**
- "The suite says v2 misses cost by 12 cents per 1,000 tickets. Does it ship?" Let the room argue for 30 seconds.
- Close with: the merge check enforces the bar, and a person decides whether the bar is right. That leads straight into Lab D, putting this run in CI.

**If the run fails or stalls,** show the results from your pre-session run and keep the same talk track. Never edit `evals/dataset/` to make a case pass on stage.

## Talk track: Claude Tag demo (Course 6 bonus, demo environment only)

Claude Tag is a public beta and runs only in the instructor demo environment. In the incident channel, show:
1. Claude joining as a channel member.
2. The thread where the on-call human makes the triage call.
3. The lesson Claude writes to the version-controlled lessons file.

Ask the room which of the three a human must still own. The answer is the triage call.
