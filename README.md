# 宋老师的营销诊断 skills

`songyue-marketingdx` is a public Agent Skill for evidence-bound diagnosis of Chinese marketing proposals.

It supports public L1.5 review of four proposal types:

- 整合营销
- 传播/公关
- 策略/品牌
- 创意/内容

The skill diagnoses only the material provided by the user and optional Brief. It does not include private customer cases, production prompts, backend code, gold standards, or deep private routing rules.

## Install

Copy or install the `songyue-marketingdx/` folder into an Agent Skills-compatible environment.

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
python3 scripts/privacy_scan.py
```

The first command validates the skill metadata. The second command checks for common private-leak markers before publishing.
