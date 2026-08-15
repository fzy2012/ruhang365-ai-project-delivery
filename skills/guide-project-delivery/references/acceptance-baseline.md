# Two-layer acceptance baseline

Create only the sections applicable to the selected delivery path.

## User acceptance

Describe observable outcomes without requiring technical knowledge.

```markdown
| ID | 前置条件 | 用户操作或触发条件 | 可观察的预期结果 | 验证方式 | 优先级 |
|---|---|---|---|---|---|
| UA-01 |  |  |  |  | Must |
```

Cover applicable areas:

- the core journey and final useful outcome;
- empty, loading, success, failure, retry, timeout, and permission feedback;
- data preservation after failure;
- desktop, mobile, device, browser, or channel behavior;
- cost, account, third-party, or privacy-visible consequences.

## Engineering acceptance

Choose technical checks according to risk. Do not ask the user to design them.

```markdown
| ID | Contract or risk | Expected result | Verification method | Evidence required | Priority |
|---|---|---|---|---|---|
| EA-01 |  |  |  |  | Must |
```

Consider when applicable:

- build, type, lint, unit, integration, and end-to-end checks;
- authentication, authorization, tenant and user isolation;
- input validation, error handling, retry, idempotency, and concurrency;
- data schema, migration, backup, restore, and rollback;
- performance thresholds and accessibility;
- logging, monitoring, alerting, secret and privacy boundaries;
- Preview, Production, provider receipt, public route, and user acceptance as separate evidence layers.

## Decision record

```markdown
- Confirmed decisions:
- Assumptions:
- Known risks:
- External dependencies:
- Out of scope:
- Implementation authorization required:
```

## Result states

- `PASS`: direct evidence exists.
- `FAIL`: the observed result violates the baseline.
- `BLOCKED`: an external condition prevents verification.
- `N/A`: confirmed not applicable, with a reason.
