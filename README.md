# 宋老师的营销诊断 skills

<p align="center">
  <img src="assets/songyue-avatar.png" alt="宋玥头像" width="140">
</p>

[English](README_EN.md)

把一份营销方案丢给 AI，让它别只会“泛泛而谈、没有重点”，而是像一个有经验的品牌策略顾问一样，指出这个方案到底卡在哪里、为什么不够锋利、下一版该怎么改。

`songyue-marketingdx` 是宋玥开放出来的营销方案诊断 Agent Skill。它基于作者 20 年品牌营销和创意策略的实战经验（曾在 Ogilvy、腾讯、天与空等公司工作），长期服务和观察品牌、广告、内容和商业增长项目；同时基于 100+ 4A 级营销案例拆出的判断语料和真实营销诊断产品中积累的诊断框架，整理成一个可以安装到 Codex、Claude Code 等 Agent 环境里的公开 skill。

English summary: `songyue-marketingdx` is a Chinese marketing proposal diagnosis skill based on Songyue's 20 years of brand, creative, and marketing strategy experience. It helps an AI agent critique and improve campaign, PR, brand strategy, and creative/content proposals with practical, evidence-based feedback.

这套判断方法也可以用于英文营销方案。它最擅长的仍然是中文方案和中国市场语境；如果要诊断英文方案，可以明确告诉 Agent 用英文输出。

## 它能帮你做什么

你可以把下面这些内容发给 AI：

- 一份整合营销方案
- 一份传播/公关方案
- 一份品牌策略或定位方案
- 一组创意脚本、内容选题或短视频方案
- 一份客户 Brief，加上你写的提案初稿

它会帮你回答几个最关键的问题：

- 这个方案真正的问题是不是找对了？
- 人群、场景和品牌角色是不是具体？
- 主张是不是有判断力，还是只有漂亮话？
- 创意是不是服务策略，还是只是热闹？
- 渠道和动作是不是能支持目标？
- 哪些判断有证据，哪些只是方案自己说自己？
- 下一版应该先改哪里，怎么改会更锋利？

## 唤醒词 / 使用方式

安装后，最自然的用法就是直接说：

```text
帮我诊断一下这个营销方案。
```

或者更短一点：

```text
诊断方案。
```

也可以说得更具体：

```text
帮我看这份品牌定位方案，重点判断它的问题定义和品牌主张是否成立。
```

```text
帮我诊断这份传播方案，没有 Brief，只有方案正文。
```

如果你的 Agent 环境没有自动触发 skill，或者你想确保一定调用这个 skill，就显式写：

```text
使用 $songyue-marketingdx 诊断下面这份营销方案。
```

英文环境也可以写：

```text
Use $songyue-marketingdx to diagnose this marketing plan.
```

然后把方案正文贴进去。如果有 Brief，也一起贴；如果没有 Brief，它会只基于方案文本判断，不会脑补预算、渠道资源、品牌历史或业务数据。

## 它会怎么输出

首轮诊断固定用四段：

```markdown
## 核心判断

## 为什么这样判断

## 更锋利的一版

## 下一步怎么改
```

这不是打分器，也不是自动生成“万能优化建议”。它更像一个精通营销创意的审稿人：先判断方案类型，再只看这个类型真正该关注的问题。不适合评价的部分，会明确标成 `本方案不评`，避免什么都评、什么都浅。

## 背后的经验和案例

这个公开 skill 来自三层沉淀：

- **20 年一线经验**：奥美创意总监 / 腾讯BG事业群市场创意负责人 / 北京天与空创始合伙人
- **真实营销诊断经验**：服务数十个不同类型的客户，涵盖互联网、快消、新消费、食品饮料等多个领域
- **脱敏复合案例**：100+ 4A 级营销案例拆出的判断语料，27 个营销判断知识点和 7 类常见问题

为了保护客户和项目隐私，公开版不会放真实客户方案、客户原话、原始广告语、内部路径、精确预算、销售数字、未公开结果或可搜索的独特表达。

## 安装

这个项目的核心是 `songyue-marketingdx/` 这个 skill 文件夹。只要某个 Agent 环境支持 Agent Skills，原则上就是把整个文件夹导入或复制到它的 skills 目录里。不要只复制 `SKILL.md`，因为还需要 `agents/openai.yaml` 和 `references/`。

本地 Codex 常见安装方式：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R songyue-marketingdx "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Claude Code、Workbody、Hermes 或其他兼容 Agent Skills 的环境，安装逻辑是一样的：导入整个 `songyue-marketingdx/` 文件夹；具体入口、目录名或上传方式以各自工具为准。

安装后，可以用自然语言唤醒；不确定是否触发时，用 `$songyue-marketingdx` 显式唤醒。

## 仓库结构

```text
.
├── README.md
├── README_EN.md
├── LICENSE
├── NOTICE
├── assets/
│   └── songyue-avatar.png
├── songyue-marketingdx/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── anti-patterns.md
│       ├── diagnostic-model.md
│       ├── judgment-principles.md
│       ├── output-examples.md
│       ├── public-case-cards.md
│       ├── type-playbooks.md
│       └── composite-examples.md
├── scripts/
│   ├── privacy_scan.py
│   └── smoke_check.py
└── tests/
    ├── fresh_agent_prompts.md
    └── smoke_cases/
        ├── integrated-marketing.md
        ├── pr-communications.md
        ├── strategy-brand.md
        └── creative-content.md
```

## 案例脱敏说明

仓库中的案例只用于说明和测试，不是真实客户案例。

已经处理掉：

- 品牌名、产品型号、项目名、客户部门、年份和文件路径。
- 原始广告语、客户原话、可搜索的独特句式。
- 精确预算、销售数字、内部指标和未公开结果。
- 特定艺人、IP、媒体、城市、节点和独有执行组合。

公开案例保留的是可迁移的判断规律，而不是某个客户项目本身。

`references/` 里已经包含公开安全的判断原则、类型打法、常见反模式、脱敏复合案例卡和输出样例。它们是给 Agent 使用的知识资产，不是私有案例原文。

## 发布前验证

维护者发布前建议运行：

```bash
python3 path/to/skill-creator/scripts/quick_validate.py songyue-marketingdx
python3 scripts/smoke_check.py
python3 scripts/privacy_scan.py
```

三个检查分别用于验证 skill 结构、四类冒烟案例和隐私泄露风险。

如果要做一次更接近真实使用的测试，可以按 `tests/fresh_agent_prompts.md` 里的四组提示词，在新 Agent 会话里分别测试自然语言唤醒和首轮输出结构。

## License

This project is licensed under `GPL-3.0-or-later`.

你可以使用、学习、修改和再分发本项目，包括商业使用；但如果你分发修改版，需要继续使用 GPL，提供对应源码/文本，保留版权和许可证声明，并明确说明你做过修改。

`宋老师`、`songyue-marketingDx`、`Songyue MarketingDx` 及相关个人品牌或标识不随 GPL 授权为商标或背书权。修改版不得暗示由原作者背书，也不得包装成原作者官方产品。
