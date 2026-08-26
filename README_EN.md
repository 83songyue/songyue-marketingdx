# Songyue Marketing Diagnosis Skills

<p align="center">
  <img src="assets/songyue-avatar.png" alt="Songyue avatar" width="140">
</p>

Give an AI agent a marketing proposal and ask it to stop giving vague, generic feedback. This skill helps the agent read the proposal like an experienced brand strategist: identify where the plan gets stuck, why it is not sharp enough, and what should be changed in the next draft.

`songyue-marketingdx` is a public Agent Skill released by Song Yue. It is based on 20 years of hands-on brand marketing and creative strategy experience, including work at Ogilvy, Tencent, and Tianyukong, plus judgment patterns distilled from 100+ 4A-level marketing cases and real marketing diagnosis product experience.

[中文说明](README.md)

## Online Diagnosis

To try the marketing diagnosis online or contact Songyue about collaboration, visit [songyue.me](https://songyue.me).

This GitHub repository provides the installable, learnable public skill. The online version provides the full web experience and a direct contact channel.

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

## About the author

Songyue (宋玥) is a brand marketing and creative strategy practitioner with 20 years of hands-on experience, including roles as:

- Creative Director at Ogilvy
- Marketing Creative Lead for a Business Group at Tencent
- Founding Partner of Beijing Tianyukong (天与空)

His work spans brand, advertising, content, and business growth projects across internet services, fast-moving consumer goods, emerging consumer brands, and food and beverages.

To learn more or contact Songyue, visit [songyue.me](https://songyue.me).

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
python3 scripts/smoke_check.py
python3 scripts/privacy_scan.py
```

For a more realistic manual test, use `tests/fresh_agent_prompts.md`. Four reviewable isolated-run outputs and a forward-test report are included under `tests/`; they validate these sample contracts, not equivalence across every host model or with the online product.

## License

This project is licensed under `CC BY-NC-SA 4.0`.

You may use, study, copy, adapt, and share this project for noncommercial purposes, including installing the complete skill in your own Agent environment. When sharing the original or an adaptation, credit Songyue, retain the copyright and license link, and indicate your changes. Adaptations must use `CC BY-NC-SA 4.0` or a compatible license.

You may not use this project or an adaptation for a product, service, delivery, or online diagnosis tool primarily intended for commercial advantage or monetary compensation. Commercial use requires separate written permission from the author.

The names `宋老师`, `songyue-marketingDx`, `Songyue MarketingDx`, and related personal branding or marks are not licensed as trademarks or endorsement rights. Modified versions must not imply endorsement by the original author or present themselves as an official product by the original author.
