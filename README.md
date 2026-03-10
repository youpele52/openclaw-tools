# OpenClaw Tools

A collection of reusable skills and tools for [OpenClaw](https://docs.openclaw.ai/), an AI-powered CLI assistant for software engineering.

## Overview

This repository contains modular skills that extend OpenClaw's capabilities. Each skill is a self-contained tool with metadata that describes when and how to use it.

## Directory Structure

```
openclaw-tools/
├── skills/                        # Reusable skills for OpenClaw
│   ├── economic-calendar-pro/     # TradingEconomics calendar events
│   │   ├── SKILL.md               # Skill definition and usage guide
│   │   ├── economic-calendar-pro.sh # Shell wrapper
│   │   └── src/                   # Python source files
│   │       ├── main.py            # Orchestration entrypoint
│   │       ├── service.py         # Data retrieval and formatting flow
│   │       └── utils.py           # Shared parsing and env helpers
│   ├── stock-price-checker-pro/   # Stock price lookup
│   │   ├── SKILL.md               # Skill definition and usage guide
│   │   ├── stock-price.sh         # Shell wrapper
│   │   └── src/                   # Python source files
│   │       ├── main.py            # Orchestration entrypoint
│   │       ├── service.py         # Data retrieval and formatting flow
│   │       ├── utils.py           # Shared formatting helpers
│   │       └── constants.py       # Skill configuration
│   ├── stock-fundamentals/        # Company fundamentals analysis
│   │   ├── SKILL.md
│   │   ├── stock-fundamentals.sh
│   │   └── src/
│   │       ├── main.py
│   │       ├── service.py
│   │       ├── utils.py
│   │       └── constants.py
│   ├── market-news-brief/         # Broad market headlines and tone
│   │   ├── SKILL.md
│   │   ├── market-news.sh
│   │   └── src/
│   │       ├── main.py
│   │       ├── service.py
│   │       ├── utils.py
│   │       └── constants.py
│   └── equity-research/           # Orchestrator for the finance skills
│       └── SKILL.md
```

## Available Skills

### Economic Calendar

Fetch economic calendar events for 7 days inclusive from the query day, or for an explicit date range.

**Usage:**
```bash
uv run skills/economic-calendar-pro/src/main.py
uv run skills/economic-calendar-pro/src/main.py 2026-03-10
uv run skills/economic-calendar-pro/src/main.py 2026-03-10 2026-03-24
```

Set `TRADING_ECONOMICS_API_KEY=client:secret` for TradingEconomics data, or copy `.env.example` to `.env`. If no key is present, the skill falls back to Yahoo Finance.

See [`skills/economic-calendar-pro/SKILL.md`](skills/economic-calendar-pro/SKILL.md) for detailed documentation.

### Stock Price Checker

Check current stock prices using Yahoo Finance. No API key required.

**Usage:**
```bash
uv run skills/stock-price-checker-pro/src/main.py AAPL
uv run skills/stock-price-checker-pro/src/main.py NVDA
uv run skills/stock-price-checker-pro/src/main.py VOO
```

See [`skills/stock-price-checker-pro/SKILL.md`](skills/stock-price-checker-pro/SKILL.md) for detailed documentation.

### Stock Fundamentals

Analyze company fundamentals such as valuation, margins, growth, balance-sheet strength, cash flow, dividend profile, and analyst context.

**Usage:**
```bash
uv run skills/stock-fundamentals/src/main.py AAPL
uv run skills/stock-fundamentals/src/main.py NVDA
```

See [`skills/stock-fundamentals/SKILL.md`](skills/stock-fundamentals/SKILL.md) for detailed documentation.

### Market News Brief

Summarize broad market headlines, market tone, and dominant macro themes using liquid market proxies.

**Usage:**
```bash
uv run skills/market-news-brief/src/main.py
uv run skills/market-news-brief/src/main.py GLOBAL
uv run skills/market-news-brief/src/main.py EUROPE
uv run skills/market-news-brief/src/main.py JAPAN
uv run skills/market-news-brief/src/main.py NOV.DE
```

See [`skills/market-news-brief/SKILL.md`](skills/market-news-brief/SKILL.md) for detailed documentation.

### Equity Research

Orchestrate the finance skills for a fuller stock research workflow.

Warning: [`skills/equity-research/SKILL.md`](skills/equity-research/SKILL.md) assumes `stock-price-checker`, `stock-fundamentals`, and `market-news-brief` are already installed. It is not intended to be used as the only installed finance skill.

### Website Scraper Pro

Scrape a single page into clean markdown by default, optionally use JS-aware rendering, and optionally narrow the returned content with deterministic query-focused filtering. No AI model configuration is used in this v1.

**Usage:**
```bash
uv run skills/website-scraper-pro/src/main.py https://example.com
uv run skills/website-scraper-pro/src/main.py https://example.com --js
uv run skills/website-scraper-pro/src/main.py https://example.com --query "documentation examples"
uv run skills/website-scraper-pro/src/main.py https://example.com --format json
```

See [`skills/website-scraper-pro/SKILL.md`](skills/website-scraper-pro/SKILL.md) for detailed documentation.

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
