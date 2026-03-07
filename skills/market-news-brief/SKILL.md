---
name: market-news-brief-pro
description: Summarize broad market news and market tone using yfinance. No API key required.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"📰","requires":{"bins":["uv"]}}}
---

# Skill: Market News Brief


## Prerequisites

- `uv` is installed (the script will automatically handle dependency installation and execution)


## When to use
- The user wants broad market headlines affecting the overall tape rather than a single company.
- The user wants a quick macro and index-level news brief before reviewing individual stocks.
- The user wants a compact market snapshot, top headlines, and dominant themes in one place.
- The user wants either a global view by default or a country/region-specific market view.

## Step-by-step approach
- If the user does not specify a market scope, assume `GLOBAL`.
- If the user specifies a supported country or region, use that scope.
- If the user passes a ticker with an obvious exchange suffix (for example, `NOV.DE`), infer the market scope from that suffix.
- Use the `main.py` script to collect index snapshots and recent broad-market headlines from Yahoo Finance proxy tickers.
- Treat this as a quick market brief. If the user needs deeper news coverage, cite that a dedicated news API may be more complete.
- If Yahoo Finance has sparse news for the chosen scope, return the market snapshot and clearly note that headline coverage is limited.

## Usage Examples

**Get the default global market brief:**
```bash
uv run main.py
```

**Explicitly request the global market brief:**
```bash
uv run main.py GLOBAL
```

**Request a regional or country market brief:**
```bash
uv run main.py EUROPE
uv run main.py GERMANY
uv run main.py US
```

**Infer the market from a suffixed ticker:**
```bash
uv run main.py NOV.DE
uv run main.py SONY.T
```

## Output Format

The script prints a human-readable market brief to stdout.

### Example Output
```text
Market News Brief: US
Market Tone: Mixed

Market Snapshot:
S&P 500 (SPY): $563.10 ▲$2.44 (0.44%)
Nasdaq 100 (QQQ): $487.22 ▲$4.01 (0.83%)
Dow Jones (DIA): $418.51 ▼$0.63 (-0.15%)
Russell 2000 (IWM): $204.72 ▲$0.88 (0.43%)
Volatility Index (^VIX): $14.30 ▼$0.41 (-2.79%)

Dominant Themes:
- Fed and rates (3 headlines)
- Technology leadership (2 headlines)
- Inflation and economy (2 headlines)

Top Headlines:
1. Stocks edge higher as investors parse fresh inflation data
   Source: Reuters | Published: 2026-03-07 13:45:00 GMT
   Link: https://example.com/story
2. Treasury yields ease while megacap tech leads the Nasdaq
   Source: Bloomberg | Published: 2026-03-07 14:10:00 GMT
   Link: https://example.com/story-2
```

## Technical Notes
- Uses the `yfinance` library to fetch market proxy quotes and related news from Yahoo Finance.
- No API key required.
- The Python implementation is split into `main.py`, `service.py`, `utils.py`, and `constants.py` to separate orchestration, scope logic, formatting helpers, and configuration.
- The default behavior is a `GLOBAL` market brief built from configured country scopes.
- Supported explicit scopes currently include `GLOBAL`, `EUROPE`, `ASIA`, `US`, `UK`, `GERMANY`, `NETHERLANDS`, `JAPAN`, and `SOUTH_KOREA`.
- Obvious exchange suffixes can be used to infer a market scope (for example, `.DE`, `.L`, `.AS`, `.T`, `.KS`, `.KQ`).
- Broad-market news is filtered with simple keyword rules to favor macro and market-wide headlines.
- News availability can vary by ticker and by time of day.
- Non-US headline coverage can be thinner than quote coverage, so the script may return coverage notes when Yahoo Finance news is sparse.

## Troubleshooting
- If headlines are sparse, Yahoo Finance may not have recent broad-market news available for the selected proxies. The script will still return the market snapshot and label coverage as limited.
- If a requested market scope is unsupported, the script will return an error listing the supported scopes.
- Bare tickers such as `AAPL` are not auto-mapped to markets. Use an explicit scope like `US`, or pass an exchange-suffixed ticker like `NOV.DE`.
- If a quote metric shows as `N/A`, the data source did not provide that field at request time.
