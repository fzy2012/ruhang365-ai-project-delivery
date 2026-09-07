# Forward evaluation protocol

## Purpose

Test whether the Skill changes project-delivery behavior rather than merely producing polished text.

## Frozen inputs

- Use `cases/cases.v1.json` without revealing `expected_behavior`, `forbidden_behavior`, or `required_evidence` to the evaluated agent.
- Provide only the case prompt and setup artifacts.
- Run the same model, reasoning level, tool access, and repository snapshot for comparable variants.

## Variant prompt materialization

The `prompt` stored in `cases/cases.v1.json` is the canonical explicit-Skill prompt.

- Baseline: remove only the exact leading text `使用 $guide-project-delivery：`; do not otherwise rewrite the business request.
- Explicit Skill: use the canonical prompt unchanged.
- Implicit trigger: use the same normalized business request as Baseline, without naming the Skill.

For controlled component comparison, disable long-term memory for every variant so a prior project record cannot reveal the Skill source, expected behavior, rubric, or earlier output. Keep the same global governance, model, reasoning level, ordinary Skill catalog, tool access, and fixture snapshot across variants. Run fixture workspaces outside this source repository so an evaluated agent cannot discover the Skill or rubric by traversing parent directories. This controlled comparison is separate from later user-facing validation with the normal memory configuration.

## Variants

1. Baseline: run without the Skill.
2. Skill: run with `$guide-project-delivery` explicitly invoked.
3. Implicit trigger: run without naming the Skill after global installation is separately authorized.

Phase 1 freezes the cases and validates their structure. It does not claim independent model results until a fresh task is authorized and executed.

## Isolation

- Use a fresh task for each run.
- Do not provide the desired answer, rubric, prior diagnosis, or another run’s output.
- Reset repository fixtures between runs.
- Save raw outputs under `runs/<date>/<case>/<variant>/`; do not commit private or secret material.
- Do not allow real deployment, paid actions, production mutation, or external outreach.

## Scoring

- Score with `rubric.md` after the run completes.
- Preserve failures and unexpected behavior.
- Do not change thresholds after seeing results without versioning the cases and explaining the change.
- Report structural validation, single-run model behavior, repeated behavior, user acceptance, and production evidence separately.

## V1 forward gate

Before calling the Skill behaviorally validated:

- all three cases must run in explicit Skill mode;
- no critical violation may occur;
- each case must reach the rubric threshold;
- at least one new-project run must be reviewed by the target non-technical user;
- implicit triggering remains a separate gate after installation.

## Outcome and cost gate — 2026-09-08

This additional gate records the owner's revised product requirement. It does not rewrite frozen V1 cases, fixtures, rubric or historical results. Freeze any new journey prompts, scripted owner replies, acceptance targets and comparison settings before their runs.

- Evaluate natural multi-turn journeys: a fuzzy idea through a usable result, and resuming an unfinished project; include nearby ordinary-task negatives. Owners should see useful progress and business decisions, not internal mode labels. Explicit invocation remains an internal test variant; user-facing acceptance requires automatic matching.
- The main cost comparator is the same Codex environment without this Skill versus with it. Keep host rules, other capabilities, model, reasoning, tools, fixture and cache policy equal. Run the existing configured environment and ordinary Codex separately; do not pool them. An upstream-only comparison answers baseline preservation, not the cost of adding this Skill to Codex.
- Compare the complete agreed journey, including relevant failure checks, retries, rework and all initiated runs. Keep failed, blocked and unknown attempts in the record and cost total. An unfinished baseline provides no successful-delivery denominator; record that outcome without inventing a savings percentage.
- Quality and acceptance must not regress. Extra questions, user effort, missing requirements or omitted verification cannot fund a claimed saving. Record time, owner interventions and tool calls alongside results; do not disguise shifted work as reduced cost.
- Freeze the cost basis before viewing results. Prefer provider money or account-credit usage; otherwise a reproducible estimate needs verified model identity, pricing and billing semantics. Report cached input, uncached input, output and reasoning usage without double-counting. Raw tokens alone are diagnostic, not proof of monetary savings. Record paid tool charges too; keep human time separate unless a valuation was agreed in advance. No paid operation is authorized by this protocol.
- For matched completed journeys, cost must be **at most 110%** of the Codex-only baseline; the target is **100% or lower**, preferably a reduction. Apply the ceiling to each evaluated scenario and the aggregate, so savings on an easy case cannot hide an expensive regression. Better claimed quality does not automatically waive the ceiling. A zero-cost baseline requires an absolute comparison, not division by zero.
- Missing model or cost evidence leaves cost compliance **unverified**; missing charges are not zero. Preserve available usage evidence and state the limitation. Static checks, fewer instruction words and an isolated smoke cannot establish this gate.

Start with one paired pilot on a real fuzzy-project journey. If it fails the quality or cost ceiling, investigate that failure before expanding the run set. A passing pilot needs repeat and unseen-journey confirmation under pre-frozen settings before claiming a reproducible gain. Record the result in the existing run receipt; do not build a separate cost platform.
