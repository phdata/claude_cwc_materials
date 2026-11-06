# AI-Native SDLC Course Series

Six 90-minute, hands-on Claude Code courses for engineers, one per stage of Anthropic's [AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook): Plan, Design, Build, Test, Deploy and Maintain. The playbook is the benchmark for the content and the rubric for reviewing it (`playbook-rubric.md`).

The courses run in order as a series, or individually. Each one starts from a checkpoint repo that already holds every earlier stage's artifacts. That lets a participant who missed the earlier courses join at any point.

## Courses

| # | Course | Title | Starts from | Hands off |
|---|---|---|---|---|
| 1 | [Plan](01-plan/) | Capture Intent: Plan in the AI-Native SDLC | checkpoint-0 | intent/0001-ticket-triage.md (accepted) |
| 2 | [Design](02-design/) | Spec with Policy Built In: Design in the AI-Native SDLC | checkpoint-1 | spec.md plus .claude/skills/* (policy), committed beside intent.md |
| 3 | [Build](03-build/) | Plan First, Then Code: Build in the AI-Native SDLC | checkpoint-2 | plan.md, CLAUDE.md, .claude/settings.json hooks, app/ triage service with unit tests |
| 4 | [Test](04-test/) | Check Your Own Work: Test in the AI-Native SDLC | checkpoint-3 | app/tests/, evals/ (dataset, graders, thresholds.json), CI eval workflow |
| 5 | [Deploy](05-deploy/) | Gates That Hold: Deploy in the AI-Native SDLC | checkpoint-4 | REVIEW.md, production-gate hook, ci.yml, deployment and rollback record |
| 6 | [Maintain](06-maintain/) | Close the Loop: Maintain in the AI-Native SDLC | checkpoint-5 | ops/bands.yaml, ops/lessons.md, intent/0002-ember-recall-product-safety-misroute.md (input to Course 1) |

Course 6 produces `intent/0002`, which goes back into Course 1's product owner gate.

## How a course runs

Every course follows the same 90-minute shape:
- 5 minutes to open.
- 70 minutes of core steps: orient, get the checkpoint, four labs, the human gate, and measure-and-hand-off.
- 10 minutes of share-out.
- 5 minutes to wrap.

Each lab has a Catalyst Holdings tab and a Bring your own use case tab.

## Customizing for a client

The company name stays Catalyst Holdings. Before the session, the scenario in the Catalyst Holdings tab is rebuilt from the client's answers to `use-case-intake.md`.

## Before you begin

- Claude Code installed and signed in with a Claude Team or Enterprise seat (claude --version works)
- git, Python 3.9+, and make on the workstation
- A GitHub account with permission to create a private repo (CI and PR labs have a local fallback)
- Optional: one real system of your own in mind for the Bring your own use case tab
- macOS, Linux or WSL with `unzip`

## Instructors

`instructor/` holds the facilitator guide and checkpoint-6, the reference end state of the whole series.

The course templates themselves are imported into the workshop app as CSV/JSON. They are not stored in this repo.
