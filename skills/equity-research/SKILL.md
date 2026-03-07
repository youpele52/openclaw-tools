---
name: equity-research-pro
description: Orchestrate stock price, fundamentals, and market-news skills for a fuller equity research workflow.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"🧭","requires":{"bins":["uv"]}}}
---

# Skill: Equity Research


## Warning

- This is an orchestration skill, not a standalone data-fetching skill.
- It assumes the companion finance skills are already installed.
- Required companion skills: `stock-price-checker-pro`, `stock-fundamentals`, and `market-news-brief`.
- If those companion skills are missing, this skill will be incomplete and should not be used as the only installed finance skill.


## Prerequisites

- `uv` is installed.
- `stock-price-checker-pro`, `stock-fundamentals`, and `market-news-brief` are already installed and available to OpenClaw.


## When to use
- The user wants a fuller equity research pass rather than a single data point.
- The user wants price action, company fundamentals, and broad market context combined into one workflow.
- The user wants a concise research-style answer assembled from the companion finance skills.

## Step-by-step approach
- First locate the correct ticker symbol if the user provided only a company name.
- Run the `stock-price-checker-pro` skill for price action, recent company news, and upcoming events.
- Run the `stock-fundamentals` skill for valuation, profitability, growth, financial health, and analyst context.
- Run the `market-news-brief` skill for broad market drivers affecting the tape.
- Combine the outputs into one concise answer that distinguishes company-specific factors from market-wide factors.

## Companion Skills

- `stock-price-checker-pro`: quick quote, ranges, company-specific news, and events
- `stock-fundamentals`: fundamental analysis and balance-sheet context
- `market-news-brief`: broader market headlines and market tone

## Notes

- This skill should orchestrate the companion skills rather than duplicate their logic.
- If a user only wants one narrow task, prefer the standalone companion skill directly instead of this orchestrator.
