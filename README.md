# 宋老师的营销诊断 skills

`songyue-marketingdx` is a public Agent Skill for evidence-bound diagnosis of Chinese marketing proposals.

It supports public L1.5 review of four proposal types:

- 整合营销
- 传播/公关
- 策略/品牌
- 创意/内容

The skill diagnoses only the material provided by the user and optional Brief. It does not include private customer cases, production prompts, backend code, gold standards, or deep private routing rules.

## Install

Copy the `songyue-marketingdx/` folder into an Agent Skills-compatible environment.

For local Codex skills, one common setup is:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R songyue-marketingdx "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Use

Ask the agent:

```text
Use $songyue-marketingdx to diagnose this Chinese marketing plan.
```

Then provide the proposal and, if available, the Brief.

## Validate

Run:

```bash
python3 path/to/skill-creator/scripts/quick_validate.py songyue-marketingdx
python3 scripts/smoke_check.py
python3 scripts/privacy_scan.py
```

The first command validates the skill metadata. The smoke check confirms the public skill structure, four route cases, and required first-response headings. The privacy scan checks for common private-leak markers before publishing.

## Public Boundary

This repository intentionally excludes real client materials, original customer copy, private gold standards, deep root-cause routing, PR risk rules, production prompts, backend services, caches, and usage data.

## License

This project is licensed under `GPL-3.0-or-later`. You may use, study, modify, and redistribute it, including for commercial purposes, under the GPL terms.

If you distribute a modified version, you must keep the same GPL license, provide the corresponding source, preserve copyright and license notices, and clearly state that you changed it.

The names `宋老师`, `songyue-marketingDx`, `Songyue MarketingDx`, and related personal branding or marks are not licensed as trademarks or endorsement rights. Modified versions must not imply endorsement by the original author.
