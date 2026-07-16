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
    "洞察锐度",
    "创意记忆",
    "品牌关联",
    "传播势能",
    "逻辑通顺",
    "增长有效",
]

TYPE_MATRIX = {
    "整合营销": {"evaluate": DIMENSIONS, "not_applicable": []},
    "传播/公关": {
        "evaluate": ["洞察锐度", "创意记忆", "传播势能", "逻辑通顺"],
        "not_applicable": ["品牌关联", "增长有效"],
    },
    "策略/品牌": {
        "evaluate": ["洞察锐度", "品牌关联", "逻辑通顺", "增长有效"],
        "not_applicable": ["创意记忆", "传播势能"],
    },
    "创意/内容": {
        "evaluate": ["洞察锐度", "创意记忆", "品牌关联", "逻辑通顺"],
        "not_applicable": ["传播势能", "增长有效"],
    },
}

REFERENCE_FILES = [
    "songyue-marketingdx/references/diagnostic-model.md",
    "songyue-marketingdx/references/judgment-principles.md",
    "songyue-marketingdx/references/type-playbooks.md",
    "songyue-marketingdx/references/anti-patterns.md",
    "songyue-marketingdx/references/public-case-cards.md",
    "songyue-marketingdx/references/output-examples.md",
    "songyue-marketingdx/references/composite-examples.md",
]

FRESH_OUTPUT_VERIFIER = "scripts/verify_fresh_output.py"
FORWARD_TEST_REPORT = "tests/forward_test_report.md"


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
    require_contains(skill, "Do not calculate a total score", "SKILL.md")
    require_contains(skill, "当前最该加分", "SKILL.md")
    require_contains(skill, "350-500", "SKILL.md")
    for label in ["**重定义：**", "**主方向：**", "**具体成品：**", "**如何落到方案：**"]:
        require_contains(skill, label, "SKILL.md rewrite gate")
    for rel in REFERENCE_FILES:
        name = Path(rel).name
        require_contains(skill, f"references/{name}", "SKILL.md reference routing")


def check_references() -> None:
    for rel in REFERENCE_FILES:
        read(rel)

    model = read("songyue-marketingdx/references/diagnostic-model.md")
    for plan_type in PLAN_TYPES.values():
        require_contains(model, plan_type, "diagnostic-model.md")
    for dimension in DIMENSIONS:
        require_contains(model, dimension, "diagnostic-model.md")
    require_contains(model, "未提供 Brief，以下判断只基于方案文本", "diagnostic-model.md")
    for mark in ["`2`", "`4`", "`6`", "`8`", "`10`"]:
        require_contains(model, mark, "diagnostic-model.md quality marks")
    for ceiling in ["cannot exceed `6`", "cannot exceed `4`"]:
        require_contains(model, ceiling, "diagnostic-model.md quality ceilings")
    require_contains(model, "Brief 已给资源", "diagnostic-model.md")
    require_contains(model, "do not count as plan capability", "diagnostic-model.md")

    examples = read("songyue-marketingdx/references/composite-examples.md")
    require_contains(examples, "not real customer cases", "composite-examples.md")

    principles = read("songyue-marketingdx/references/judgment-principles.md")
    require_contains(principles, "27.", "judgment-principles.md")
    require_contains(principles, "Delete-brand test", "judgment-principles.md")

    playbooks = read("songyue-marketingdx/references/type-playbooks.md")
    for plan_type in PLAN_TYPES.values():
        require_contains(playbooks, plan_type, "type-playbooks.md")

    anti_patterns = read("songyue-marketingdx/references/anti-patterns.md")
    require_contains(anti_patterns, "Channel List Pretending To Be Communication Design", "anti-patterns.md")

    case_cards = read("songyue-marketingdx/references/public-case-cards.md")
    require_contains(case_cards, "## 12.", "public-case-cards.md")
    require_contains(case_cards, "not real client cases", "public-case-cards.md")

    output_examples = read("songyue-marketingdx/references/output-examples.md")
    for heading in REQUIRED_OUTPUT_HEADINGS:
        require_contains(output_examples, heading, "output-examples.md")


def check_agents_metadata() -> None:
    metadata = read("songyue-marketingdx/agents/openai.yaml")
    require_contains(metadata, 'display_name: "宋老师的营销诊断 skills"', "agents/openai.yaml")
    require_contains(metadata, 'short_description: "帮你看清营销方案卡在哪里、下一版怎么改"', "agents/openai.yaml")
    require_contains(metadata, 'default_prompt: "使用 $songyue-marketingdx 诊断下面这份营销方案。"', "agents/openai.yaml")


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
        require_contains(text, "Expected primary opportunity:", filename)
        for dimension in TYPE_MATRIX[route]["evaluate"]:
            require_contains(text, f"- `{dimension}`", filename)
        for dimension in TYPE_MATRIX[route]["not_applicable"]:
            require_contains(text, f"- `{dimension}`: `本方案不评`", filename)


def check_fresh_agent_prompts() -> None:
    prompts = read("tests/fresh_agent_prompts.md")
    for filename, route in PLAN_TYPES.items():
        require_contains(prompts, filename, "fresh_agent_prompts.md")
        require_contains(prompts, route, "fresh_agent_prompts.md")
    for heading in REQUIRED_OUTPUT_HEADINGS:
        require_contains(prompts, heading, "fresh_agent_prompts.md")
    require_contains(prompts, "帮我诊断一下这个营销方案", "fresh_agent_prompts.md")
    require_contains(prompts, "诊断方案", "fresh_agent_prompts.md")
    require_contains(prompts, "350-500", "fresh_agent_prompts.md")
    require_contains(prompts, "当前最该加分", "fresh_agent_prompts.md")
    read(FRESH_OUTPUT_VERIFIER)


def check_forward_test_artifacts() -> None:
    report = read(FORWARD_TEST_REPORT)
    for filename in PLAN_TYPES:
        require_contains(
            report,
            f"forward_test_outputs/{filename}",
            "forward_test_report.md",
        )
        read(f"tests/forward_test_outputs/{filename}")


def check_readme() -> None:
    avatar = ROOT / "assets" / "songyue-avatar.png"
    if not avatar.is_file():
        raise AssertionError("Missing avatar image: assets/songyue-avatar.png")

    readme = read("README.md")
    require_contains(readme, "$songyue-marketingdx", "README.md")
    require_contains(readme, "assets/songyue-avatar.png", "README.md")
    require_contains(readme, "README_EN.md", "README.md")
    require_contains(readme, "scripts/privacy_scan.py", "README.md")
    require_contains(readme, "scripts/smoke_check.py", "README.md")

    readme_en = read("README_EN.md")
    require_contains(readme_en, "$songyue-marketingdx", "README_EN.md")
    require_contains(readme_en, "assets/songyue-avatar.png", "README_EN.md")
    require_contains(readme_en, "Chinese-first", "README_EN.md")
    require_contains(readme_en, "judgment principles", "README_EN.md")
    require_contains(readme_en, "README.md", "README_EN.md")


def main() -> int:
    checks = [
        check_skill,
        check_references,
        check_agents_metadata,
        check_smoke_cases,
        check_fresh_agent_prompts,
        check_forward_test_artifacts,
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
