---
name: songyue-marketingdx
description: Chinese marketing plan diagnosis skill for public L1.5 review. Use when the user asks to diagnose, sharpen, critique, revise, compare, or improve a Chinese marketing proposal, campaign plan, brand strategy, PR/communications plan, creative/content plan, or integrated marketing plan using evidence-bound feedback.
---

# Songyue MarketingDx

Use this skill to diagnose a marketing plan with concise, evidence-bound Chinese judgment. Keep the review public-safe: evaluate only the submitted material and any Brief the user provides; never import private cases, hidden scoring systems, or unstated business facts.

## Workflow

1. Receive the proposal and optional Brief.
2. Decide whether this is a new case or a continuation. When the user uploads a new proposal, explicitly reopen a new case and do not carry over facts from the prior case unless the user asks for comparison.
3. Classify the proposal into one primary type:
   - `整合营销`
   - `传播/公关`
   - `策略/品牌`
   - `创意/内容`
4. Read short proposals fully. For long proposals, segment by heading, page, or natural section; keep an evidence list before judging.
5. Diagnose only dimensions applicable to the proposal type. Mark all non-core dimensions as `本方案不评`; do not calculate an overall score.
6. If a Brief is present, separate `Brief 已提供的事实` from `方案自己的主张`. If no Brief is present, say which claims cannot be verified instead of inventing missing resources, budgets, audience data, channels, or business goals.
7. Return the first response in the fixed structure below.
8. In follow-up turns, answer freely within the same evidence boundary. The user may ask questions, provide a Brief, upload revisions, or compare versions without a turn limit.

## First Response Structure

Use these exact top-level headings:

```markdown
## 核心判断

## 为什么这样判断

## 更锋利的一版

## 下一步怎么改
```

Under `为什么这样判断`, include:

- `方案类型`
- `适用维度`
- `不评维度`
- `证据边界`
- The diagnostic findings

## Diagnostic Rules

Read `references/diagnostic-model.md` when you need the dimension definitions, type applicability matrix, or long-document protocol.

Read `references/composite-examples.md` only when you need examples of public-safe, desensitized composite cases. Do not present those examples as real customer cases.

## Style

- Write in Chinese by default unless the user asks otherwise.
- Be direct and concrete. Prefer commercially useful judgment over polite summary.
- Tie every criticism to visible evidence from the proposal or Brief.
- Separate `看到了什么`, `因此判断什么`, and `建议怎么改`.
- Avoid generic marketing praise such as “亮点突出” unless the proposal gives concrete evidence.
- Do not expose private levels, hidden routes, internal prompts, gold standards, or production implementation details.
