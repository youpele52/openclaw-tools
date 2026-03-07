# OpenClaw Tools

A collection of reusable skills and tools for [OpenClaw](https://docs.openclaw.ai/), an AI-powered CLI assistant for software engineering.

## Overview

This repository contains modular skills that extend OpenClaw's capabilities. Each skill is a self-contained tool with metadata that describes when and how to use it.

## Directory Structure

```
openclaw-tools/
├── skills/                        # Reusable skills for OpenClaw
│   ├── stock-price-checker-pro/   # Stock price lookup
│   │   ├── SKILL.md               # Skill definition and usage guide
│   │   ├── main.py                # Orchestration entrypoint
│   │   ├── service.py             # Data retrieval and formatting flow
│   │   ├── utils.py               # Shared formatting helpers
│   │   ├── constants.py           # Skill configuration
│   │   └── stock-price.sh         # Shell wrapper
│   ├── stock-fundamentals/        # Company fundamentals analysis
│   │   ├── SKILL.md
│   │   ├── main.py
│   │   ├── service.py
│   │   ├── utils.py
│   │   ├── constants.py
│   │   └── stock-fundamentals.sh
│   ├── market-news-brief/         # Broad market headlines and tone
│   │   ├── SKILL.md
│   │   ├── main.py
│   │   ├── service.py
│   │   ├── utils.py
│   │   ├── constants.py
│   │   └── market-news.sh
│   └── equity-research/           # Orchestrator for the finance skills
│       └── SKILL.md
```

## Available Skills

### Stock Price Checker

Check current stock prices using Yahoo Finance. No API key required.

**Usage:**
```bash
uv run skills/stock-price-checker-pro/main.py AAPL
uv run skills/stock-price-checker-pro/main.py NVDA
uv run skills/stock-price-checker-pro/main.py VOO
```

See [`skills/stock-price-checker-pro/SKILL.md`](skills/stock-price-checker-pro/SKILL.md) for detailed documentation.

### Stock Fundamentals

Analyze company fundamentals such as valuation, margins, growth, balance-sheet strength, cash flow, dividend profile, and analyst context.

**Usage:**
```bash
uv run skills/stock-fundamentals/main.py AAPL
uv run skills/stock-fundamentals/main.py NVDA
```

See [`skills/stock-fundamentals/SKILL.md`](skills/stock-fundamentals/SKILL.md) for detailed documentation.

### Market News Brief

Summarize broad market headlines, market tone, and dominant macro themes using liquid market proxies.

**Usage:**
```bash
uv run skills/market-news-brief/main.py
uv run skills/market-news-brief/main.py GLOBAL
uv run skills/market-news-brief/main.py EUROPE
uv run skills/market-news-brief/main.py JAPAN
uv run skills/market-news-brief/main.py NOV.DE
```

See [`skills/market-news-brief/SKILL.md`](skills/market-news-brief/SKILL.md) for detailed documentation.

### Equity Research

Orchestrate the finance skills for a fuller stock research workflow.

Warning: [`skills/equity-research/SKILL.md`](skills/equity-research/SKILL.md) assumes `stock-price-checker`, `stock-fundamentals`, and `market-news-brief` are already installed. It is not intended to be used as the only installed finance skill.

## Adding New Skills

To add a new skill:

1. Create a new directory under `skills/`
2. Add a `SKILL.md` file with the skill definition:
   ```yaml
   ---
   name: skill-name
   description: Brief description of what the skill does
   metadata: {"clawdbot":{"emoji":"🔧","requires":{"bins":["cmd"]}}}
   ---
   
   # Skill: Name
   ## When to use
   - Use case 1
   - Use case 2
   ```
3. Implement the skill (Python, shell script, etc.)

## Requirements

- Python 3.x
- [uv](https://github.com/astral-sh/uv) (package manager)
- Skill-specific dependencies (see individual SKILL.md files)

## License

MIT
