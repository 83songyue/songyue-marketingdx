# Songyue Marketing Diagnosis Skills

<p align="center">
  <img src="assets/songyue-avatar.png" alt="Songyue avatar" width="140">
</p>

Give an AI agent a marketing proposal and ask it to stop giving vague, generic feedback. This skill helps the agent read the proposal like an experienced brand strategist: identify where the plan gets stuck, why it is not sharp enough, and what should be changed in the next draft.

`songyue-marketingdx` is a public Agent Skill released by Song Yue. It is based on 20 years of hands-on brand marketing and creative strategy experience, including work at Ogilvy, Tencent, and Tianyukong, plus judgment patterns distilled from 100+ 4A-level marketing cases and real marketing diagnosis product experience.

[中文说明](README.md)

## Can It Work With English Proposals?

Yes. The underlying judgment methods are useful for English-language proposals too: problem definition, audience and scenario, strategic proposition, creative expression, channel/action design, and evidence discipline are not limited to Chinese.

That said, this skill is Chinese-first. It is strongest when diagnosing Chinese marketing proposals or China-market work. For English proposals, explicitly tell the agent what language you want in the output:

```text
Use $songyue-marketingdx to diagnose this English marketing proposal. Please answer in English.
```

## What It Helps With

You can use it to review:

- Integrated marketing plans
- Communications and PR launch plans
- Brand strategy or positioning proposals
- Creative scripts, content ideas, and short-video plans
- A client Brief plus a proposal draft

It helps answer:

- Is the real business problem clearly defined?
- Is the audience and usage/decision scenario specific enough?
- Does the proposition have a real point of view, or is it just polished wording?
- Does the creative idea serve the strategy?
- Do channels and actions support the goal?
- Which claims are backed by evidence, and which are only asserted by the proposal?
- What should be changed first in the next draft?

## Wake Phrases

After installation, the natural way to invoke it is:

```text
帮我诊断一下这个营销方案。
```

or:

```text
诊断方案。
```

If your agent environment does not automatically trigger the skill, call it explicitly:

```text
Use $songyue-marketingdx to diagnose this marketing plan.
```

Then paste the proposal text. If you have a Brief, include it too. If no Brief is provided, the skill should diagnose only from the proposal text and avoid inventing budgets, channel resources, brand history, or business data.

## First-Round Output

The first diagnosis uses four sections:

```markdown
## 核心判断

## 为什么这样判断

## 更锋利的一版

## 下一步怎么改
```

It is not a scoring machine. It is closer to a pre-meeting strategy reviewer: it identifies the proposal type, evaluates the dimensions that matter for that type, and marks irrelevant dimensions as `本方案不评`.

## Installation

The core package is the `songyue-marketingdx/` folder. In any Agent Skills-compatible environment, import or copy the entire folder. Do not copy only `SKILL.md`, because the skill also uses `agents/openai.yaml` and `references/`.

Common local Codex setup:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R songyue-marketingdx "${CODEX_HOME:-$HOME/.codex}/skills/"
```

For Claude Code, Workbody, Hermes, or other compatible environments, the concept is the same: import the complete `songyue-marketingdx/` folder. The exact entry point or directory depends on the tool.

## Case Privacy

The public examples in this repository are desensitized composite cases and smoke tests. They are not real client cases.

They remove or abstract:

- Brand names, product models, project names, departments, years, and file paths
- Original slogans, client wording, and searchable unique sentences
- Exact budgets, sales numbers, internal metrics, and unpublished results
- Specific celebrities, IPs, media, cities, timing, and unique execution combinations

The public cases preserve reusable judgment patterns, not the original client projects.

The `references/` folder includes the public knowledge layer used by the skill: judgment principles, type playbooks, anti-patterns, desensitized composite case cards, and output examples.

## Validation

Before publishing, maintainers can run:

```bash
python3 path/to/skill-creator/scripts/quick_validate.py songyue-marketingdx
python3 scripts/smoke_check.py
python3 scripts/privacy_scan.py
```

For a more realistic manual test, use `tests/fresh_agent_prompts.md`.

## License

This project is licensed under `GPL-3.0-or-later`.

You may use, study, modify, and redistribute it, including for commercial purposes. If you distribute a modified version, you must keep it under the GPL, provide the corresponding source/text, preserve copyright and license notices, and clearly state your changes.

The names `宋老师`, `songyue-marketingDx`, `Songyue MarketingDx`, and related personal branding or marks are not licensed as trademarks or endorsement rights. Modified versions must not imply endorsement by the original author or present themselves as an official product by the original author.
