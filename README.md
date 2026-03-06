# OpenClaw Tools

A collection of reusable skills and tools for [OpenClaw](https://github.com/anomalyco/opencode), an AI-powered CLI assistant for software engineering.

## Overview

This repository contains modular skills that extend OpenClaw's capabilities. Each skill is a self-contained tool with metadata that describes when and how to use it.

## Directory Structure

```
openclaw-tools/
├── skills/                    # Reusable skills for OpenClaw
│   └── stock-price-checker/   # Example skill: stock price lookup
│       ├── SKILL.md           # Skill definition and usage guide
│       ├── stock-price.py     # Python implementation
│       └── stock-price.sh     # Shell wrapper
```

## Available Skills

### Stock Price Checker

Check current stock prices using Yahoo Finance. No API key required.

**Usage:**
```bash
uv run stock-price.py AAPL
uv run stock-price.py NVDA
uv run stock-price.py VOO
```

See [`skills/stock-price-checker/SKILL.md`](skills/stock-price-checker/SKILL.md) for detailed documentation.

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
