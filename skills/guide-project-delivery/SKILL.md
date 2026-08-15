---
name: guide-project-delivery
description: Guide non-technical or zero-code users from a project idea to a verified delivery by routing task complexity, checking feasibility, comparing buy/configure/connect/modify/build paths, establishing decision gates and two-layer acceptance criteria, coordinating implementation, and producing an evidence-backed handoff. Use when a user wants to start a new project, turn a business goal into an executable delivery plan, compare delivery paths before coding, or manage an end-to-end project through acceptance. Do not use for isolated low-risk edits, code review, or diagnosis unless the user explicitly requests the full delivery workflow.
---

# Guide Project Delivery

## Core promise

Help the user control goals, experience, cost, and unacceptable risks while taking responsibility for technical judgment, implementation planning, and verification evidence. Do not assume that delivery requires custom code.

Obey system, user, workspace, repository, and safety rules before this workflow. Treat the selected delivery mode as an execution depth, not permission to write, publish, deploy, spend money, or handle real data.

## Route the task before expanding the process

Assess four dimensions:

- scope uncertainty;
- technical and business risk;
- reversibility;
- number of decisions that materially affect cost, data, security, maintenance, or user experience.

Choose one mode:

| Mode | Use when | Required flow |
|---|---|---|
| Light | The target is clear, low-risk, reversible, and local | Restate target → define brief acceptance → implement if authorized → verify |
| Full | A new project or meaningful feature has multiple reasonable delivery paths | Preflight → compare paths → decision → two-layer acceptance → milestones → delivery |
| High assurance | Payment, permissions, migration, production, real data, compliance, or irreversible operations are involved | Full mode + risk register + rollback + separate approval + stronger evidence |

Do not force three options, long documents, or architecture decisions onto a light task. If this skill was invoked for an isolated low-risk change, state that light mode is sufficient and continue proportionally.

## Stage 1: Establish authority and delivery feasibility

Convert the request into one verifiable outcome sentence. Separate:

- confirmed facts;
- low-risk assumptions;
- unknowns that change the path;
- actions already authorized;
- actions that still require authorization.

For an existing project, inspect only what is necessary before proposing a path: project rules, Git state, recent commits, current architecture, dependencies, target modules, public contracts, and unrelated dirty changes.

Check delivery feasibility early:

- file and repository access;
- build, test, browser, device, or API verification capability;
- required accounts, permissions, credentials, reviews, and paid services;
- target environment: local, test, Preview, or Production;
- ownership of domains, data, infrastructure, and long-term costs.

Report only facts that change the decision or block delivery. Never ask the user to paste secrets into chat.

If the user requested analysis, planning, or “do not change anything,” remain read-only. Do not treat approval of a plan as approval to deploy or publish.

## Stage 2: Choose among buy, configure, connect, modify, and build

Evaluate these paths before custom development:

| Path | Meaning |
|---|---|
| Buy | Use a mature product directly |
| Configure | Configure an existing product, plugin, or no-code system |
| Connect | Integrate existing systems or automate their data flow |
| Modify | Extend an existing project while preserving users and contracts |
| Build | Create a new system when differentiation or control justifies ownership cost |

Offer one to three genuinely different paths. Do not create fake alternatives by changing only a technology stack. Compare only decision-relevant consequences:

- final result and omitted scope;
- time to first usable outcome;
- setup and recurring cost;
- third-party dependency and lock-in;
- data control and security exposure;
- maintenance and recovery burden;
- expansion limits and migration path.

Give a recommendation first. Explain it in business language. Use [decision-card.md](references/decision-card.md) when the user must choose.

Stop for confirmation only when the choice materially changes scope, experience, cost, data, security, ownership, lock-in, maintenance, or irreversibility. Otherwise record the assumption and continue.

## Stage 3: Establish the acceptance baseline

After a delivery path is selected, load [acceptance-baseline.md](references/acceptance-baseline.md).

Create two layers:

1. User acceptance: observable behavior and outcomes the user can judge.
2. Engineering acceptance: build, type, test, security, failure, performance, compatibility, migration, rollback, or runtime checks selected by the AI.

Every required item must have a verification method and an unambiguous expected result. Avoid terms such as “good experience,” “fast enough,” or “high accuracy” without a measurable threshold.

Use only these result states:

- `PASS`: actually verified and passed;
- `FAIL`: actually verified and failed;
- `BLOCKED`: external access, service, device, credential, approval, or information prevents verification;
- `N/A`: confirmed not applicable.

Do not mark planned, coded, mocked, reviewed, committed, merged, deployed, or HTTP-successful work as user acceptance unless the corresponding acceptance evidence exists.

In Full and High assurance modes, obtain explicit implementation authorization after the acceptance baseline. A generic “continue” advances only the current bounded stage and never authorizes publishing, deployment, spending, real-data mutation, or destructive operations.

## Stage 4: Implement in visible milestones

Before editing, reread current target files and recheck relevant state. State the files or modules to be touched.

Build the smallest working end-to-end path first. Use project-native conventions and existing mature dependencies. Do not add unrelated abstractions, refactors, dependencies, or future-facing infrastructure.

For medium and complex projects, create milestones that are:

- runnable;
- observable by the user;
- honest about real versus placeholder behavior;
- independently verifiable;
- reversible where practical.

Call specialized skills or tools for implementation domains instead of duplicating their instructions here. Preserve existing APIs, data formats, links, and automation unless the user explicitly approves a breaking migration with rollback.

Explain any user action as:

- why it is needed;
- exact place to operate;
- exact action;
- expected visible result;
- safety note;
- failure recovery;
- what reply will let work continue.

Complete all safe in-scope work before transferring an action to the user.

## Stage 5: Verify and repair

Run the real system with verification proportional to risk. Select applicable evidence such as:

- build, type, lint, and unit tests;
- integration, end-to-end, API, browser, device, and viewport checks;
- empty, loading, error, timeout, retry, duplicate, partial-success, and permission states;
- migration, backup, rollback, logging, monitoring, privacy, and security checks;
- exact Preview or Production artifact and public route checks.

For each `FAIL`, identify the cause, repair it within scope, rerun the relevant checks, and update the result. Do not reduce the acceptance target to manufacture completion.

For each `BLOCKED`, report the evidence, impact, remaining risk, and exact condition needed to finish. Distinguish implementation, validation, release, public proof, user acceptance, and business outcome.

## Stage 6: Deliver for continued ownership

Load [delivery-card.md](references/delivery-card.md) for a Full or High assurance delivery, or whenever another person or AI must continue the project.

Ensure the user can:

- access the result;
- use the core flow;
- understand dependencies and recurring cost;
- maintain and troubleshoot it;
- recover from failed updates or data loss where applicable;
- hand it to another person or AI without hidden configuration.

End each stage with only:

- what is complete;
- how it was verified;
- what decision or user action is required;
- what happens next;
- remaining risk that changes the user’s judgment.

## Maintain a compact state snapshot

For Full and High assurance modes, keep this snapshot current in the conversation or an authorized project artifact:

```markdown
- Mode:
- Current stage:
- Confirmed decisions:
- Assumptions:
- Blockers:
- Authorized actions:
- Next gate:
```

Do not write a project artifact merely to preserve state when the user requested read-only analysis.

## Load references only when needed

- Read [decision-card.md](references/decision-card.md) when a material user choice is required.
- Read [acceptance-baseline.md](references/acceptance-baseline.md) after a path is selected or before implementation acceptance.
- Read [delivery-card.md](references/delivery-card.md) when closing a Full or High assurance delivery or preparing handoff.
