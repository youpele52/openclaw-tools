---
name: stock-price-checker
description: Check stock prices using yfinance library. No API key required.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"📈","requires":{"bins":["python3","yfinance"]}}}
---

# Skill: Stock Price Checker

## When to use
- The user wants to check the current stock price of a company.
- The user wants to check the stock price of an ETF or index.

## Step-by-step approach

- When given a company name, you must first locate the corresponding stock ticker symbol using Yahoo Finance or another reliable service. 
- If the user doesn't specify currency, assume USD for stock prices NVO. If the user specifically ask for euros, don't convert but use the german stock exchange eg NOV.DE.
- Once the ticker is identified, you will use that sticker or symbol to as input to the stock price checker script. The script will then fetch the current stock price and related information using the yfinance library.  eg, uv run stock-price.py AAPL for Apple Inc.

# Check another stock
uv run stock-price.py AAPL
```

## Usage Examples

**Check NVIDIA stock:**
```bash
uv run stock-price.py NVDA
```

**Check VOO (S&P 500 ETF):**
```bash
uv run stock-price.py VOO
```

**Check QQQ (Nasdaq-100 ETF):**
```bash
uv run stock-price.py QQQ
```

**Check any stock symbol:**
```bash
uv run stock-price.py TSLA
uv run stock-price.py MSFT
uv run stock-price.py AAPL
```

## Output Format

```json
{
  "symbol": "NVDA",
  "price": 189.52,
  "change": 3.05,
  "change_percent": 1.64,
  "previous_close": 186.47,
  "market_cap": 4614243483648,
  "volume": 112439494,
  "fifty_two_week_high": 212.19,
  "fifty_two_week_low": 86.62
}
```

## Technical Notes

- Uses yfinance library to fetch data from Yahoo Finance
- No API key required
- Handles errors gracefully
- Works with most major stocks and ETFs
- Returns comprehensive data including market cap, volume, and 52-week range

## Troubleshooting

- If the stock symbol is invalid, the script will return an error
- Some data (like market cap) may not be available for all symbols
