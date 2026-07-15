# Fresh-Agent Test Prompts

Use these prompts in a fresh Agent session after installing `songyue-marketingdx/`. The goal is to test whether natural Chinese requests can trigger the skill and whether the first response follows the expected structure.

## How to Run

For each case:

1. Start a fresh conversation or clear prior case context.
2. Paste the prompt and the matching file from `tests/smoke_cases/`.
3. Check the acceptance points below.

## Required First-Response Headings

Every first response should include:

```markdown
## 核心判断
## 为什么这样判断
## 更锋利的一版
## 下一步怎么改
```

## Case 1: Integrated Marketing

Prompt:

```text
帮我诊断一下这个营销方案。我没有 Brief，只有方案正文。
```

Use: `tests/smoke_cases/integrated-marketing.md`

Accept if:

- Routes as `整合营销`.
- Evaluates all six public dimensions or clearly explains any exception.
- Does not calculate an overall score.
- States that no Brief was provided and does not invent missing budget, channel resource, brand history, or sales data.

## Case 2: Communications/PR

Prompt:

```text
诊断方案：这是一份传播/公关发布方案，帮我判断它站不站得住。
```

Use: `tests/smoke_cases/pr-communications.md`

Accept if:

- Routes as `传播/公关`.
- Focuses on topic, news value, credibility, evidence, and communication sequence.
- Marks pure creative execution as `本方案不评` unless it explicitly evaluates the supplied expression.
- Does not invent media resources or external endorsements.

## Case 3: Strategy/Brand

Prompt:

```text
帮我看这份品牌定位方案，重点判断它的问题定义和品牌主张是否成立。
```

Use: `tests/smoke_cases/strategy-brand.md`

Accept if:

- Routes as `策略/品牌`.
- Focuses on business problem, audience scene, strategic proposition, and evidence.
- Marks `创意表达` and `渠道与行动设计` as `本方案不评` unless explaining why they are included.

## Case 4: Creative/Content

Prompt:

```text
帮我改这组创意内容，先诊断它最大的问题。
```

Use: `tests/smoke_cases/creative-content.md`

Accept if:

- Routes as `创意/内容`.
- Focuses on audience scene, brand role, proposition-to-idea connection, memorability, and evidence.
- Marks `商业问题定义` and `渠道与行动设计` as `本方案不评` unless the answer explicitly limits the judgment.

## Failure Signals

Treat these as failures:

- The answer only gives generic praise or generic optimization tips.
- The answer ignores the four required headings.
- The answer evaluates every dimension without marking non-core dimensions.
- The answer invents facts not present in the proposal or Brief.
- The answer carries facts from a previous case into a new uploaded proposal.
