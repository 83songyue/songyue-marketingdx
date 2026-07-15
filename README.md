# 宋老师的营销诊断 skills

`songyue-marketingdx` 是一个面向中文营销方案的公开 Agent Skill，用于帮助 Codex、Claude Code 等兼容 Agent Skills 的智能体，对营销方案做类型路由、证据边界检查和第一轮修改建议。

English summary: `songyue-marketingdx` is a public Agent Skill for evidence-bound diagnosis of Chinese marketing, brand, PR, creative, and integrated campaign proposals.

它不是线上诊断后台，也不包含私有客户案例、内部提示词、深度根因规则或校准材料。这个仓库只发布公开 L1.5 能力：让个人用户和创作者可以安装、学习、使用，并在修改和再分发时继续遵守 GPL 开源义务。

## 适合谁

- 自媒体作者、品牌顾问、市场部和广告从业者，用来快速检查方案是否站得住。
- 正在写整合营销、传播/公关、品牌策略、创意内容方案的人。
- 想把营销判断流程做成 Agent Skill 的学习者和开发者。

## 能做什么

这个 skill 支持四类方案路由：

- `整合营销`
- `传播/公关`
- `策略/品牌`
- `创意/内容`

首轮诊断会固定输出：

```markdown
## 核心判断

## 为什么这样判断

## 更锋利的一版

## 下一步怎么改
```

诊断会遵守三个原则：

- 只基于用户提交的方案和 Brief，不虚构预算、渠道资源、品牌历史或业务数据。
- 只评价当前方案类型的核心维度；不适用的维度标记为 `本方案不评`。
- 不计算总分，优先给出商业上可执行的修改方向。

## 不能做什么

这个公开版不包含：

- 真实客户项目、客户原文、原始广告语或内部文件路径。
- 私有校准材料、专家修正意见、深度根因问题链、PR 风险规则。
- 线上服务后端、缓存、真实使用数据、支付或账号系统。
- 对任何品牌、项目或用户业务结果的事实背书。

## 安装

把 `songyue-marketingdx/` 文件夹复制到兼容 Agent Skills 的环境即可。

本地 Codex 常见安装方式：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R songyue-marketingdx "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## 使用

在 Agent 中调用：

```text
Use $songyue-marketingdx to diagnose this Chinese marketing plan.
```

然后提供方案正文；如果有 Brief，也一起提供。

也可以这样问：

```text
Use $songyue-marketingdx to review this PR launch plan. I have no Brief, only the proposal text.
```

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

## 案例和脱敏

仓库中的案例是公开安全的复合案例和冒烟测试，不是真实客户案例。

它们已经移除或抽象化：

- 品牌名、产品型号、项目名、客户部门、年份和文件路径。
- 原始广告语、客户原话、可搜索的独特句式。
- 精确预算、销售数字、内部指标和未公开结果。
- 特定艺人、IP、媒体、城市、节点和独有执行组合。

这些案例只用于验证 skill 是否能正确路由四类方案、标记不适用维度、遵守 Brief 证据边界和保持输出结构。

## 验证

发布前建议运行：

```bash
python3 path/to/skill-creator/scripts/quick_validate.py songyue-marketingdx
python3 scripts/smoke_check.py
python3 scripts/privacy_scan.py
```

说明：

- `quick_validate.py` 验证 skill 元数据和基础结构。
- `scripts/smoke_check.py` 检查公开 skill 结构、四类冒烟案例和固定输出标题。
- `scripts/privacy_scan.py` 检查常见私有路径、密钥和禁止发布的内部标记。

## License

This project is licensed under `GPL-3.0-or-later`.

你可以使用、学习、修改和再分发本项目，包括商业使用；但如果你分发修改版，需要继续使用 GPL，提供对应源码/文本，保留版权和许可证声明，并明确说明你做过修改。

`宋老师`、`songyue-marketingDx`、`Songyue MarketingDx` 及相关个人品牌或标识不随 GPL 授权为商标或背书权。修改版不得暗示由原作者背书，也不得包装成原作者官方产品。
