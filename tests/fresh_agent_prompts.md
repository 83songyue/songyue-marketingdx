# Fresh-Agent Acceptance Tests

Run each case in a separate, fresh Agent conversation with only the matching case file and prompt below. This is a structured acceptance test, not proof that every host model will make equally good marketing judgments.

## Common Acceptance Contract

Accept a response only when all of these are true:

- It has `## 核心判断`, `## 为什么这样判断`, `## 更锋利的一版`, and `## 下一步怎么改`.
- It identifies the expected proposal type and uses that type's exact default applicable/not-applicable matrix.
- Every applicable dimension receives an evidence-based `2 / 4 / 6 / 8 / 10` quality judgment. It does not calculate a total or overall grade.
- It explicitly selects one `当前最该加分` dimension and supports it with plan evidence.
- It states `未提供 Brief，以下判断只基于方案文本。` and does not invent budget, product capability, media resource, customer endorsement, or external data.
- `更锋利的一版` gives one direction, is roughly 350-500 Chinese characters, and includes at least one usable strategy/copy/scene/action artifact. It does not split into several competing ideas.
- `下一步怎么改` has no more than two moves and they serve the same direction.

Treat generic praise, a missing type matrix, an invented fact, a generic rewrite, or a bare channel list as a failure. Read the saved output as part of acceptance; the script below checks repeatable structural requirements but cannot grade commercial judgment by itself.

After saving a fresh Agent answer to a local text file, run the deterministic acceptance gate:

```bash
python3 scripts/verify_fresh_output.py --case tests/smoke_cases/<case>.md --output /path/to/fresh-agent-answer.txt
```

## Case 1: Integrated Marketing

Prompt:

```text
帮我诊断一下这个营销方案。我没有 Brief，只有方案正文。
```

Use: `tests/smoke_cases/integrated-marketing.md`

Accept only if:

- It routes as `整合营销` and evaluates all six dimensions.
- It selects `增长有效` as `当前最该加分` because the business behavior to change is not defined.
- The rewrite turns the vague “清爽” goal into one conditional, specific target behavior and makes the other actions serve it.

## Case 2: Communications / PR

Prompt:

```text
诊断方案：这是一份传播/公关发布方案，帮我判断它站不站得住。
```

Use: `tests/smoke_cases/pr-communications.md`

Accept only if:

- It routes as `传播/公关`; `品牌关联` and `增长有效` are `本方案不评`.
- It selects `传播势能` as `当前最该加分`, not sales conversion or a generic media expansion.
- The rewrite creates a reportable/public expression and ties news, interview, and other actions to one proof or event.

## Case 3: Strategy / Brand

Prompt:

```text
帮我看这份品牌定位方案，重点判断它的问题定义和品牌主张是否成立。
```

Use: `tests/smoke_cases/strategy-brand.md`

Accept only if:

- It routes as `策略/品牌`; `创意记忆` and `传播势能` are `本方案不评`.
- It selects `洞察锐度` as `当前最该加分`, not a slogan rewrite alone.
- The rewrite connects the old asset, a specific household tension, and a credible new role without inventing product or service proof.

## Case 4: Creative / Content

Prompt:

```text
帮我改这组创意内容，先诊断它最大的问题。
```

Use: `tests/smoke_cases/creative-content.md`

Accept only if:

- It routes as `创意/内容`; `传播势能` and `增长有效` are `本方案不评`.
- It selects `品牌关联` as `当前最该加分`, rather than criticizing the lack of a media or conversion plan.
- The rewrite gives a unified creative device and places the brand in the on-screen problem/solution rather than the end card.
