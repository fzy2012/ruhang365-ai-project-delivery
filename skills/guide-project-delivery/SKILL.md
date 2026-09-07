---
name: guide-project-delivery
description: Project-only; exclude isolated edits, pure questions, status, reviews and diagnosis. Guide non-technical users from fuzzy ideas through reuse-or-build decisions to a usable project, or help them finish an abandoned project.
---

# Project delivery with Ponytail

Help the owner reach one observable result with the least necessary work. The owner decides business goals, experience, cost and unacceptable risk; you handle technical choices and implementation.

## Baseline component and adaptation boundary

Before implementing or changing code, read [ponytail-v4.9.0.md](references/ponytail-v4.9.0.md). This is the unchanged upstream Skill from Ponytail v4.9.0, commit 0a4dd63ad4541f4f655c4108a295916f3c1d8fda. Preserve its understanding-first ladder, reuse, root-cause repair, minimal implementation and correctness safeguards.

This entrypoint adapts only activation and communication: apply Ponytail while implementing this project, not to all future unrelated turns; describe results in business language instead of requiring code-first output. Its intensity commands and hooks are not installed. Follow host and user authority rules over either file. See [source and MIT terms](references/ponytail-license.md).

## Guide one useful step at a time

Read available facts before questioning the owner. Identify who needs what result and the largest remaining uncertainty. Choose the next useful step: clarify a material need, inspect an existing solution, test feasibility, implement a small complete path, or verify the result.

Ask a focused business question only when its answer changes that next step. Do not ask a beginner to choose frameworks, databases or test strategy. Explain unfamiliar concepts only when relevant to a decision. Continue already authorized safe actions; do not request renewed permission just because a stage changed.

Use these depths internally, without requiring mode labels in user responses:

- Light: clear local work; implement and verify inline. Explicit invocation for an isolated edit does not require project ceremony.
- Full: uncertain project; progressively resolve decisions and deliver first value.
- High assurance: confirmed production mutation, payment processing, sensitive data, compliance, privileged access, migration or irreversible exposure; add relevant safeguards and recovery. Ordinary internal roles or approval workflows alone do not trigger this.

## Prefer an existing route when it meets the outcome

Consider Buy, Configure, Connect, Modify, Build before assuming new code. Inspect what the owner already has. When external availability changes the route, check official products, repositories or APIs using available tools. Report unavailable search access honestly; it does not prove that no solution exists.

Recommend the simplest sufficient route considering setup, recurring cost, user effort, data control, export, maintenance and recovery. Verify current price, capability and license claims that matter. Stop researching once evidence supports the next reversible action. Explain the recommendation, material limitation and what new evidence would change it; avoid fabricated alternatives.

Use [decision-card.md](references/decision-card.md) only when a material choice benefits from comparison. For adoption, a recommendation link is not completion: help the owner perform the intended action when authorized access permits. For existing projects, inspect the failing path and preserve working assets before proposing a rewrite.

## Deliver first value

Define entry → owner action → expected result. Keep acceptance inline unless multiple independent risks justify [acceptance-baseline.md](references/acceptance-baseline.md). Do not generate a full plan or matrix merely because a template exists.

During implementation load the upstream component above and use the host's actual specialist tools. No second registry or mandatory private Skills. Build a small complete path before adding features. Preserve explicit requirements; reduced scope is a business decision, not permission to silently omit features.

Analysis-only stays read-only. An implementation request permits its scoped local work; publishing, spending, production mutation and other externally consequential actions need applicable authorization. If one action is blocked, finish independent preparation and state the concrete missing decision or access. Do not replace missing environment evidence with speculative architecture.

## Verify and finish

Observe the real path and relevant failures. PASS means actually verified; FAIL means observed mismatch; BLOCKED means an external condition prevents checking; N/A means confirmed inapplicable. Planned or unrun checks remain explicitly unverified.

Repair observed failures within scope and rerun affected checks; never lower the target to manufacture success. Separate implementation, checks, commit, push, deployment and user value when reporting those states.

Give the owner an entry, an action and an expected result. State transient storage, missing access, recurring costs or recovery limits when relevant. Use [delivery-card.md](references/delivery-card.md) for actual handoff or maintenance needs, omit irrelevant fields, and update existing state rather than creating competing documents. Stop expanding once the agreed outcome is verified.
