# Bring Your Use Case: Pre-Session Intake

Return this form at least 10 business days before the first session. The answers will be used to rebuild the Catalyst Holdings scenario around your use case. Your company name won't appear in course material; the scenario keeps the name Catalyst Holdings.

Use synthetic or redacted data only. Do not include customer records, credentials, or anything covered by an NDA that hasn't been cleared for training use.

## 1. The ask (Courses 1 and 2)

- **Originator role:** who raises the need, for example "support lead."
- **The problem, in the originator's words:** 3 to 5 sentences.
- **Desired outcome:** what changes for users when this works.
- **Affected users and systems:** list them.
- **Known constraints:** deadlines, platforms, regulations.

## 2. Policy to encode as skills (Course 2)

List 2 or 3 policies the design must respect, each with a named owner. Examples: an API security rule, brand voice, a UX standard, data residency.

| Policy | One-line rule | Owner role |
|---|---|---|
| | | |

## 3. The system (Course 3)

- **Language and framework:** Python is the default. Other languages need extra build time.
- **Paths that must never be edited by an agent:** for example migrations or infra.
- **Run, test and lint commands:** if you already have them.

## 4. Quality (Course 4)

- **Bug used for the failing-test-first lab:** one realistic example.
- **Eval tasks:** 20 or more real input-and-expected-output examples. Synthetic examples are fine.
- **Pass-rate threshold:** the minimum you would accept for merge.

## 5. Release (Course 5)

- **Review rules:** the review comments your team leaves most often.
- **Production gate:** the approval needed for production, and who holds it.
- **Environments:** list them, and note where an agent may act without a person.

## 6. Operations (Course 6)

- **Metric to watch:** the one metric that signals this system is degrading.
- **Baseline:** the normal range, or 4+ weeks of history if available.
- **Example breach:** a past incident to replay.

## 7. Logistics

- **Delivery:** the full series, or which individual courses.
- **Participants:** expected number and their roles.
- **Repo setup:** whether participants can create private GitHub repos. If not, the local fallbacks will be used.
- **Seats:** confirmation of Claude Team or Enterprise seats with Claude Code access.
