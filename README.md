# 宋老师的营销诊断 skills

把一份中文营销方案丢给 AI，让它别只会夸“思路清晰、亮点突出”，而是像一个有经验的品牌策略顾问一样，指出这个方案到底卡在哪里、为什么不够锋利、下一版该怎么改。

`songyue-marketingdx` 是松邀客（宋老师）开放出来的营销方案诊断 Agent Skill。它基于我 20 年品牌营销和创意策略经验沉淀：曾在 Ogilvy、腾讯、天与空等公司工作，长期服务和观察品牌、广告、内容和商业增长项目；同时结合我在真实营销诊断产品中积累的大量方案判断、脱敏案例和诊断框架，整理成一个可以安装到 Codex、Claude Code 等 Agent 环境里的公开 skill。

English summary: `songyue-marketingdx` is a Chinese marketing proposal diagnosis skill based on Songyue's 20 years of brand, creative, and marketing strategy experience. It helps an AI agent critique and improve campaign, PR, brand strategy, and creative/content proposals with practical, evidence-based feedback.

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

安装后，在 Codex 或其他支持 Agent Skills 的环境里，直接这样说：

```text
Use $songyue-marketingdx to diagnose this marketing plan.
```

如果你用中文，也可以这样说：

```text
使用 $songyue-marketingdx 诊断下面这份营销方案。
```

更具体一点：

```text
Use $songyue-marketingdx to review this PR launch plan. I have no Brief, only the proposal text.
```

```text
使用 $songyue-marketingdx 帮我看这份品牌定位方案，重点判断它的问题定义和品牌主张是否成立。
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

这不是打分器，也不是自动生成“万能优化建议”。它更像一个方案会前的策略审稿人：先判断方案类型，再只看这个类型真正该看的问题。不适合评价的部分，会明确标成 `本方案不评`，避免什么都评、什么都浅。

## 背后的经验和案例

这个公开 skill 来自三层沉淀：

- **20 年一线经验**：品牌策略、广告创意、内容营销、整合传播、互联网平台和商业咨询。
- **真实诊断产品经验**：曾经做过线上营销诊断工具，积累过大量方案类型、诊断记录、专家修正和用户反馈。
- **脱敏复合案例**：公开仓库里的案例不是客户原文，而是把多个真实项目中反复出现的问题抽象、重组、改写后的训练和测试材料。

为了保护客户和项目隐私，公开版不会放真实客户方案、客户原话、原始广告语、内部路径、精确预算、销售数字、未公开结果或可搜索的独特表达。

## 公开版和线上产品的区别

这个仓库发布的是一个 **Agent Skill**：你把它安装到自己的 Codex、Claude Code 或其他兼容环境里，用你自己的模型额度运行。

它不是原线上诊断产品的后台代码，也不包含线上版本里的账号、额度、支付、缓存、用户数据、私有诊断规则和更深层的专家校准材料。

换句话说：

- 公开版适合个人学习、方案自检、二次开发和 Agent Skill 研究。
- 线上产品/私有版会包含更多产品能力、案例资产、校准规则和服务系统。

## 安装

把 `songyue-marketingdx/` 文件夹复制到兼容 Agent Skills 的环境即可。

本地 Codex 常见安装方式：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R songyue-marketingdx "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后，用 `$songyue-marketingdx` 唤醒。

## 仓库结构

```text
.
├── README.md
├── LICENSE
├── NOTICE
├── songyue-marketingdx/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── diagnostic-model.md
│       └── composite-examples.md
├── scripts/
│   ├── privacy_scan.py
│   └── smoke_check.py
└── tests/smoke_cases/
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

## 发布前验证

维护者发布前建议运行：

```bash
python3 path/to/skill-creator/scripts/quick_validate.py songyue-marketingdx
python3 scripts/smoke_check.py
python3 scripts/privacy_scan.py
```

三个检查分别用于验证 skill 结构、四类冒烟案例和隐私泄露风险。

## License

This project is licensed under `GPL-3.0-or-later`.

你可以使用、学习、修改和再分发本项目，包括商业使用；但如果你分发修改版，需要继续使用 GPL，提供对应源码/文本，保留版权和许可证声明，并明确说明你做过修改。

`宋老师`、`songyue-marketingDx`、`Songyue MarketingDx` 及相关个人品牌或标识不随 GPL 授权为商标或背书权。修改版不得暗示由原作者背书，也不得包装成原作者官方产品。
