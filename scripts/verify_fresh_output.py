#!/usr/bin/env python3
"""Validate one real fresh-agent answer against a smoke-case acceptance contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "## 核心判断",
    "## 为什么这样判断",
    "## 更锋利的一版",
    "## 下一步怎么改",
]
SCORE_PATTERN = re.compile(r"[：:]\s*(2|4|6|8|10)(?:[。．]|\s)")


def block_after(case: str, heading: str) -> str:
    match = re.search(rf"{re.escape(heading)}\n\n((?:- .*\n)+)", case)
    if not match:
        raise AssertionError(f"Smoke case is missing `{heading}`")
    return match.group(1)


def expected_dimensions(case: str, heading: str) -> list[str]:
    return re.findall(r"- `([^`]+)`", block_after(case, heading))


def chinese_character_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def rewrite_block(output: str) -> str:
    match = re.search(
        r"## 更锋利的一版\s*(.*?)(?=\n## 下一步怎么改|\Z)",
        output,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("Missing `更锋利的一版` body")
    return match.group(1).strip()


def verify(case_path: Path, output_path: Path) -> None:
    case = case_path.read_text(encoding="utf-8")
    output = output_path.read_text(encoding="utf-8")

    route_match = re.search(r"Expected route: `([^`]+)`", case)
    primary_match = re.search(r"Expected primary opportunity: `([^`]+)`", case)
    if not route_match or not primary_match:
        raise AssertionError("Smoke case is missing route or primary opportunity")

    route = route_match.group(1)
    primary = primary_match.group(1)
    applicable = expected_dimensions(case, "Expected applicable dimensions:")
    not_applicable = re.findall(
        r"- `([^`]+)`: `本方案不评`", block_after(case, "Expected not applicable:")) \
        if "Expected not applicable:" in case else []

    for heading in REQUIRED_HEADINGS:
        if heading not in output:
            raise AssertionError(f"Missing heading: {heading}")
    if f"方案类型：{route}" not in output:
        raise AssertionError(f"Wrong or missing route: expected {route}")
    if not re.search(r"未提供 Brief，以下判断只基于方案(?:文本|正文)", output):
        raise AssertionError("Missing no-Brief evidence boundary")
    if f"当前最该加分：{primary}" not in output:
        raise AssertionError(f"Wrong or missing primary opportunity: expected {primary}")
    if "/60" in output or "总分" in output or "整体等级" in output:
        raise AssertionError("Output calculated an overall grade")

    for dimension in applicable:
        pattern = re.compile(rf"{re.escape(dimension)}{SCORE_PATTERN.pattern}")
        if not pattern.search(output):
            raise AssertionError(f"Missing 2/4/6/8/10 judgment for {dimension}")
    for dimension in not_applicable:
        if not re.search(rf"{re.escape(dimension)}[^\n]*本方案不评", output):
            raise AssertionError(f"Missing not-applicable mark for {dimension}")

    rewrite_length = chinese_character_count(rewrite_block(output))
    if not 350 <= rewrite_length <= 500:
        raise AssertionError(
            f"Rewrite has {rewrite_length} Chinese characters; expected 350-500"
        )
    for label in ["**重定义：**", "**主方向：**", "**具体成品：**", "**如何落到方案：**"]:
        if label not in rewrite_block(output):
            raise AssertionError(f"Rewrite is missing required label: {label}")

    print(f"Fresh-agent output passed: {case_path.name} ({rewrite_length} Chinese characters).")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        verify(args.case, args.output)
    except (AssertionError, OSError) as exc:
        print(f"Fresh-agent output failed: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
