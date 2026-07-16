#!/usr/bin/env python3
"""Scan public repository text for generic private-source and credential traces."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__"}

FORBIDDEN_MARKERS = {
    "private_handoff": re.compile(r"OPEN_SOURCE_" + r"PROJECT_HANDOFF\.md"),
    "private_gold_standard": re.compile("真实金" + "标准"),
    "private_production_prompt": re.compile(
        "生产" + r"\s*" + "Prompt|内部" + r"\s*" + "Prompt|内部提" + "示词",
        re.I,
    ),
    "private_knowledge_pack": re.compile("VIP/企业知" + "识包"),
    "private_source_tree": re.compile("knowledge" + "-engine|aliyun" + "-fc", re.I),
    "absolute_private_path": re.compile(
        r"/(?:Users|home)/[^/\s]+/(?:Documents|Desktop|Library|scripts|\.claude|\.codex)"
    ),
    "api_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "credential_assignment": re.compile(
        r"(?i)(?:api[_-]?key|secret|token|password)\s*[:=]\s*[\"'][^\"']{8,}[\"']"
    ),
}


def is_text_file(path: Path) -> bool:
    try:
        path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False
    return True


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.is_file() and is_text_file(path):
            files.append(path)
    return files


def main() -> int:
    findings: list[str] = []
    for path in iter_text_files():
        text = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN_MARKERS.items():
            if pattern.search(text):
                findings.append(f"{path.relative_to(ROOT)}: {label}")

    if findings:
        print("Privacy scan failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Privacy scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
