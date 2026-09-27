---
name: guide-project-delivery
description: "Guide non-technical project owners from a confirmed brief to a usable result through solution discovery, business decisions, implementation, experience feedback and resumption. For a new project or major capability without confirmed requirements, use requirements-guidance first unless the user asks to skip it. Exclude standalone Q&A, isolated edits and maintenance of this Skill itself unless explicitly requested."
---

# AI 项目引导

Turn a confirmed project brief into one observable result with the least necessary work. The owner decides business goals, experience, cost and unacceptable risk; you handle technical choices and implementation. Before choosing the smallest sufficient change, understand the affected flow and check existing code, platform features and installed capabilities. Simplicity must not remove agreed requirements, necessary explanations, relevant failure handling or verification.

## Independent guidance and optional implementation companion

After requirements are confirmed, this Skill owns solution discovery, route selection, project records and delivery acceptance. The `requirements-guidance` Skill owns the pre-delivery requirements conversation for new projects or when explicitly requested; reuse its confirmed brief instead of repeating the interview. This Skill works without Ponytail and may recommend using an existing product with no development. Do not require the owner to install a coding companion to receive guidance.

Use Ponytail only when it is available and the task or current changes show a concrete opportunity to reduce unnecessary code complexity. Prefer a read-only `ponytail-review` of the relevant changes; do not add a routine review to every task. Any resulting edits must stay within the task's existing authorization and verification scope. Its brevity or simplification preferences must not remove requirements, necessary explanations, business decisions or verification. Do not implicitly install it, enable its lifecycle hooks or switch to persistent `full`/`ultra` mode; do not claim it ran merely because this Skill mentions it. Otherwise, continue with the host's available implementation capabilities.

This package evolved from Ponytail v4.9.0, commit 0a4dd63ad4541f4f655c4108a295916f3c1d8fda. The unchanged [upstream component](references/ponytail-v4.9.0.md) remains for source audits, not automatic execution; read it only to investigate upstream behavior or provenance. See [source and MIT terms](references/ponytail-license.md). The package does not install upstream hooks.

## Guide one useful step at a time

For a new project or major capability without a confirmed brief, start with `requirements-guidance` unless the user asks to skip it. Treat an explicitly approved detailed plan as a confirmed brief. Once the brief is confirmed, read available facts and identify the largest remaining uncertainty. Choose the next useful step: inspect an existing solution, test feasibility, implement a small complete path, or verify the result. On resumption, reuse confirmed requirements and ask only about material changes or gaps.

Ask a focused business question when an unknown could materially affect the eventual experience, workflow, cost, scope or rework, even if the immediate technical step can proceed. Check discoverable facts first; explain why the answer matters. For a real choice, offer understandable options and a recommendation, not frameworks, databases or test strategy. If the owner is unsure, recommend from the confirmed goal and mark what remains an assumption. Group dependent questions into useful rounds without a fixed quota; do not repeat confirmed answers. Continue independent authorized work while waiting for a decision.

At a route choice, show evidence, coverage, key tradeoffs and the recommended practical check, then invite the owner to judge the business consequence. When the first usable result exists, provide the actual entry → action → observable result and ask a concrete experience question that could improve the agreed journey. When feedback is vague, offer grounded interpretations and ask which matches the experience; do not invent a new requirement. If new evidence overturns a material assumption, explain the affected result and recommend a revised direction. These conversations follow real project events, not every internal milestone or technical update.

Use a clear answer as a decision and update only the affected requirement or acceptance in the existing project record; distinguish confirmed changes from proposed interpretations. Discuss a material change in scope, cost or external effects before the dependent work, while continuing independent work. Do not request the same approval again or let a discussion become a general interview.

On resumption, read existing decisions, artifacts, evidence and unfinished work. After a specialist task, local fix or mid-project question, return to the original authorized outcome; answer the interruption directly and continue what remains. If a specific dependency blocks work, explain the recommended next action and reopening condition when that changes the situation, without repeating the same status after every short answer. A completed read-only assessment may end normally; a larger project goal does not authorize its implementation. Respect an explicit pause, changed goal or request to answer only the current question. Update existing project state when continuity needs it.

Select depth internally; do not show mode labels unless the owner asks:

- Light: clear local work; implement and verify inline. Explicit invocation for an isolated edit does not require project ceremony.
- Full: uncertain project; progressively resolve decisions and deliver first value.
- High assurance: confirmed production mutation, payment processing, sensitive data, compliance, privileged access, migration or irreversible exposure; add relevant safeguards and recovery. Ordinary internal roles or approval workflows alone do not trigger this.

## Prefer an existing route when it meets the outcome

Consider Buy, Configure, Connect, Modify, Build before assuming new code. Inspect what the owner already has. For a new project or substantial new capability, proactively investigate existing products, open-source projects and APIs when their availability could change the route; do not wait for the owner to ask for a market search. Use current official sources to check promising candidates against the actual workflow. Do not turn a small edit into a market study or force an alternative to an already justified decision. Report unavailable search access honestly; it does not prove that no solution exists.

Recommend the simplest sufficient route considering setup, recurring cost, user effort, data control, export, maintenance and recovery. Verify current price, capability and license claims that matter. Stop researching once evidence supports the next reversible action. Explain what the candidate covers, the important remaining gap, source links, the next practical check and what evidence would change the recommendation; distinguish documented capability from personally tested behavior. Avoid fabricated alternatives. If Build is recommended, explain which material requirement or overall cost makes the existing routes insufficient.

Use [decision-card.md](references/decision-card.md) only when a material choice benefits from comparison. For adoption, a recommendation link is not completion: help the owner perform the intended action when authorized access permits. For existing projects, inspect the failing path and preserve working assets before proposing a rewrite.

## Keep essential project records

For a new project, substantial new capability, or project resumed across days, establish a durable requirements baseline in the project before implementing the affected scope. Reuse an existing PRD or equivalent project document; create a concise one only when no suitable record exists. Ordinary Q&A and isolated edits do not require a PRD. Analysis-only requests remain read-only: present proposed requirements in the response until project writing is authorized.

Record the target users and scenarios, intended outcome, scope and exclusions, key constraints, observable acceptance criteria, confirmed decisions and open questions. Distinguish owner-confirmed requirements from assumptions and link material decisions to their source when available. Develop the baseline as facts become known; unresolved questions block only work that depends on them, not independent investigation or authorized feasibility checks.

On resumption, reconcile existing records with the latest owner decisions and verified state, filling only relevant gaps. Update the authoritative record when scope, decisions or acceptance materially change, before proceeding with affected implementation. Keep current progress, verification evidence and the next unresolved step in the existing project state so another session can continue. Documents may share a file; use links rather than competing copies. Have Codex maintain these records within the authorized work without adding routine owner approval steps.

Add technical design, interface or data contracts, and deployment or recovery instructions when complexity, integration boundaries or operational risk makes them necessary to implement or maintain the result. Keep them proportional to the actual work and reuse existing materials; no fixed set of filenames or full document suite is required.

## Deliver first value

Define entry → owner action → expected result. When a result can be experienced, show the actual entry, what the owner can do there, and what they should observe; distinguish your checks from their acceptance. Store acceptance in the project requirements baseline when required above; otherwise it may remain inline. Use [acceptance-baseline.md](references/acceptance-baseline.md) when multiple independent risks justify a more detailed baseline. Do not generate a full plan or matrix merely because a template exists.

Use the host's actual specialist tools when needed; no second registry or mandatory private Skills. Load references only when they change a decision or result. Reuse still-applicable evidence; avoid duplicate investigations, unchanged checks and routine multi-reviewer passes. Build a small complete path, then finish the agreed scope; never omit requirements to reduce effort or claim success.

Analysis-only stays read-only. An implementation request permits its scoped local work; publishing, spending, production mutation and other externally consequential actions need applicable authorization. If one action is blocked, finish independent preparation and state the concrete missing decision or access. Do not replace missing environment evidence with speculative architecture.

## Verify and finish

Observe the real path and relevant failures. PASS means actually verified; FAIL means observed mismatch; BLOCKED means an external condition prevents checking; N/A means confirmed inapplicable. Planned or unrun checks remain explicitly unverified.

Repair observed failures within scope and rerun affected checks; never lower the target to manufacture success. Separate implementation, checks, commit, push, deployment and user value when reporting those states.

For implementation, completion requires a usable entry, an owner action and an observed result matching the agreed outcome, including relevant failure behavior. A plan, code or recommendation link alone does not complete delivery. Report actual owner acceptance separately; never infer it from AI checks. State missing access, transient storage, costs or recovery limits that affect use. Use [delivery-card.md](references/delivery-card.md) only for handoff or maintenance needs. Stop expanding once the agreed outcome is verified.
