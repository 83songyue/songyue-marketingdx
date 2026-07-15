#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SKILL_HEADINGS = [
    "## Workflow",
    "## First Response Structure",
    "## Diagnostic Rules",
    "## Style",
]

REQUIRED_OUTPUT_HEADINGS = [
    "## 核心判断",
    "## 为什么这样判断",
    "## 更锋利的一版",
    "## 下一步怎么改",
]

PLAN_TYPES = {
    "integrated-marketing.md": "整合营销",
    "pr-communications.md": "传播/公关",
    "strategy-brand.md": "策略/品牌",
    "creative-content.md": "创意/内容",
}

DIMENSIONS = [
    "商业问题定义",
    "人群与场景",
    "战略主张",
    "创意表达",
    "渠道与行动设计",
    "证据与可行性",
]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"Missing file: {rel}")
    return path.read_text(encoding="utf-8")


def require_contains(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label} missing `{needle}`")


def check_skill() -> None:
    skill = read("songyue-marketingdx/SKILL.md")
    for heading in REQUIRED_SKILL_HEADINGS:
        require_contains(skill, heading, "SKILL.md")
    for heading in REQUIRED_OUTPUT_HEADINGS:
        require_contains(skill, heading, "SKILL.md first-response structure")
    require_contains(skill, "本方案不评", "SKILL.md")
    require_contains(skill, "do not calculate an overall score", "SKILL.md")


def check_references() -> None:
    model = read("songyue-marketingdx/references/diagnostic-model.md")
    for plan_type in PLAN_TYPES.values():
        require_contains(model, plan_type, "diagnostic-model.md")
    for dimension in DIMENSIONS:
        require_contains(model, dimension, "diagnostic-model.md")
    require_contains(model, "未提供 Brief，以下判断只基于方案文本", "diagnostic-model.md")

    examples = read("songyue-marketingdx/references/composite-examples.md")
    require_contains(examples, "not real customer cases", "composite-examples.md")


def check_smoke_cases() -> None:
    smoke_dir = ROOT / "tests" / "smoke_cases"
    if not smoke_dir.is_dir():
        raise AssertionError("Missing smoke case directory")

    actual_files = {path.name for path in smoke_dir.glob("*.md")}
    expected_files = set(PLAN_TYPES)
    if actual_files != expected_files:
        raise AssertionError(
            f"Smoke case files mismatch. Expected {sorted(expected_files)}, got {sorted(actual_files)}"
        )

    for filename, route in PLAN_TYPES.items():
        text = read(f"tests/smoke_cases/{filename}")
        require_contains(text, f"Expected route: `{route}`", filename)
        require_contains(text, "Expected check:", filename)
        if filename != "integrated-marketing.md":
            require_contains(text, "本方案不评", filename)


def check_readme() -> None:
    readme = read("README.md")
    require_contains(readme, "$songyue-marketingdx", "README.md")
    require_contains(readme, "scripts/privacy_scan.py", "README.md")
    require_contains(readme, "scripts/smoke_check.py", "README.md")


def main() -> int:
    checks = [
        check_skill,
        check_references,
        check_smoke_cases,
        check_readme,
    ]
    try:
        for check in checks:
            check()
    except AssertionError as exc:
        print(f"Smoke check failed: {exc}")
        return 1

    print("Smoke check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
