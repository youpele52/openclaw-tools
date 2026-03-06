---
name: stock-price-checker-pro
description: Check stock prices using yfinance library. No API key required.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"📈","requires":{"bins":["uv"]}}}
---

# Skill: Stock Price Checker


## Prerequisites

- `uv` is installed (the script will automatically handle dependency installation and execution)


## When to use
- The user wants to check the current stock price of a company, ETF, or index.
- The user wants related market data (previous close, market cap, volume) and recent news or corporate events.

## Step-by-step approach
- When given a company name, first locate the corresponding stock ticker symbol using Yahoo Finance or another reliable service.
- If the user doesn't specify a currency, assume USD for stock prices. For stocks listed on other exchanges (e.g., German exchanges), use the appropriate ticker (e.g., `NOV.DE`) rather than converting currencies.
- Once the ticker is identified, use the ticker as input to the `stock-price.py` script. The script will fetch the current price and related information using the `yfinance` library (e.g., `uv run stock-price.py AAPL`).

## Usage Examples

**Check NVIDIA stock:**
```bash
uv run stock-price.py NVDA
```

**Check VOO (S&P 500 ETF):**
```bash
uv run stock-price.py VOO
```

**Check any stock symbol:**
```bash
uv run stock-price.py TSLA
uv run stock-price.py MSFT
uv run stock-price.py AAPL
```

## Output Schema

The skill returns a single JSON object. Refer to the example JSON below for the exact fields and structure returned by the script — the example demonstrates the canonical output shape used by the skill. Numeric fields may be `null` when data is unavailable; arrays like `news` and `events` may be empty.

### Example Output
```json
{
  "symbol": "NVDA",
  "company_name": "NVIDIA Corporation",
  "price": 189.52,
  "change": 3.05,
  "change_percent": 1.64,
  "previous_close": 186.47,
  "market_cap": 4614243483648,
  "volume": 112439494,
  "avg_volume": 98000000,
  "day_high": 190.10,
  "day_low": 185.00,
  "range_2w": "172.50 - 195.00",
  "range_1m": "160.00 - 195.00",
  "range_6m": "120.00 - 210.00",
  "range_52w": "86.62 - 212.19",
  "news": [
    {
      "title": "NVIDIA reports record data center revenue",
      "source": "Reuters",
      "link": "https://www.reuters.com/...",
      "published_at": "2026-03-05T13:45:00Z"
    }
  ],
  "events": [
    {
      "type": "earnings",
      "date": "2026-05-01",
      "description": "Q1 2026 earnings release"
    }
  ]
}
```

## Technical Notes
- Uses the `yfinance` library to fetch data from Yahoo Finance.
- No API key required.
- The returned schema is intended to be stable; however, some numeric fields may be `null` when the data source lacks them.
- `market_cap`, `volume`, and `avg_volume` are returned as raw numbers (integers). Consumer code should format these for display (e.g., using SI suffixes).
- Range fields (`range_2w`, `range_1m`, `range_6m`, `range_52w`) are returned as human-friendly `"low - high"` strings. If you need numeric pairs, parse the strings accordingly.

## Troubleshooting
- If the stock symbol is invalid or not found, the script will return an error object or exit with a non-zero status depending on how it's invoked.
- Some data (like market cap) may be delayed or unavailable for certain tickers (e.g., OTC or very small-cap symbols).
- For international tickers, specify the exchange suffix (e.g., `BMW.DE`) to ensure data is pulled from the correct market.
- If `news` or `events` are empty arrays, it means the script could not find recent items for that symbol.

## Change Log
- Removed the redundant detailed field list and replaced it with a reference to the example JSON for exact structure and fields.