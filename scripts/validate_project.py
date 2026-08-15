#!/usr/bin/env python3
"""Validate the repository's static V1 delivery contract without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "guide-project-delivery"

REQUIRED_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "docs" / "PRODUCT_SPEC.md",
    ROOT / "docs" / "ACCEPTANCE.md",
    ROOT / "docs" / "LAB_INTEGRATION.md",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    SKILL / "references" / "decision-card.md",
    SKILL / "references" / "acceptance-baseline.md",
    SKILL / "references" / "delivery-card.md",
    ROOT / "evals" / "cases" / "cases.v1.json",
    ROOT / "evals" / "protocol.md",
    ROOT / "evals" / "rubric.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def require_text(text: str, path: Path, snippets: list[str]) -> None:
    for snippet in snippets:
        if snippet not in text:
            fail(f"{path.relative_to(ROOT)} missing required contract: {snippet}")


def validate_skill() -> None:
    skill_path = SKILL / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("Skill frontmatter is missing or malformed")

    keys = []
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            keys.append(line.split(":", 1)[0])
    if keys != ["name", "description"]:
        fail(f"Skill frontmatter keys must be name, description; got {keys}")

    require_text(
        text,
        skill_path,
        [
            "Light",
            "Full",
            "High assurance",
            "Buy",
            "Configure",
            "Connect",
            "Modify",
            "Build",
            "PASS",
            "FAIL",
            "BLOCKED",
            "N/A",
            "references/decision-card.md",
            "references/acceptance-baseline.md",
            "references/delivery-card.md",
        ],
    )

    for ref in ["decision-card.md", "acceptance-baseline.md", "delivery-card.md"]:
        if not (SKILL / "references" / ref).is_file():
            fail(f"Referenced file does not exist: {ref}")


def validate_evals() -> None:
    path = ROOT / "evals" / "cases" / "cases.v1.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) != 3:
        fail("V1 must contain exactly three frozen evaluation cases")

    expected_categories = {"simple-task", "new-project", "existing-project"}
    categories = {case.get("category") for case in cases}
    if categories != expected_categories:
        fail(f"Evaluation categories mismatch: {categories}")

    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)):
        fail("Evaluation case IDs must be unique")

    required = {
        "id",
        "category",
        "prompt",
        "setup",
        "expected_behavior",
        "forbidden_behavior",
        "required_evidence",
    }
    for case in cases:
        missing = required - set(case)
        if missing:
            fail(f"Evaluation case {case.get('id')} missing fields: {sorted(missing)}")
        for field in ["expected_behavior", "forbidden_behavior", "required_evidence"]:
            if not isinstance(case[field], list) or not case[field]:
                fail(f"Evaluation case {case['id']} has empty {field}")


def main() -> int:
    missing = [path.relative_to(ROOT) for path in REQUIRED_FILES if not path.is_file()]
    if missing:
        fail(f"Missing required files: {', '.join(map(str, missing))}")

    validate_skill()
    validate_evals()
    print("PASS: repository static contract is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
