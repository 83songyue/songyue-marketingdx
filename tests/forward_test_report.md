# Fresh-Agent Forward-Test Report

Date: 2026-07-16

## Scope

Four isolated, fresh Codex Agent runs used the public skill folder and one composite smoke case each. The agent received the natural user request and the matching proposal file only; it did not receive expected answers or private project material.

## Recorded Outputs

| Proposal type | Recorded output | Rewrite length |
| --- | --- | --- |
| Integrated marketing | `forward_test_outputs/integrated-marketing.md` | 482 Chinese characters |
| Communications / PR | `forward_test_outputs/pr-communications.md` | 461 Chinese characters |
| Strategy / brand | `forward_test_outputs/strategy-brand.md` | 396 Chinese characters |
| Creative / content | `forward_test_outputs/creative-content.md` | 495 Chinese characters |

Each recorded output was checked with:

```bash
python3 scripts/verify_fresh_output.py --case tests/smoke_cases/<case>.md --output tests/forward_test_outputs/<output>.md
```

The deterministic gate verifies response headings, expected type matrix, applicable quality marks, `本方案不评`, Brief boundary, selected primary opportunity, four rewrite labels, and the 350-500 Chinese-character range.

## Limitation

This is reproducible evidence that these four public-safe examples produced structurally compliant outputs in isolated runs. It does not establish that every host model, prompt, document format, or production environment will match the online product's behavior. Review the recorded outputs for the substantive marketing judgment.
