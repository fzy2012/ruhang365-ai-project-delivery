# Forward evaluation protocol

## Purpose

Test whether the Skill changes project-delivery behavior rather than merely producing polished text.

## Frozen inputs

- Use `cases/cases.v1.json` without revealing `expected_behavior`, `forbidden_behavior`, or `required_evidence` to the evaluated agent.
- Provide only the case prompt and setup artifacts.
- Run the same model, reasoning level, tool access, and repository snapshot for comparable variants.

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
