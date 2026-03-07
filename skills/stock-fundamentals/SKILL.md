---
name: stock-fundamentals-pro
description: Analyze stock fundamentals using yfinance. No API key required.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"📊","requires":{"bins":["uv"]}}}
---

# Skill: Stock Fundamentals


## Prerequisites

- `uv` is installed (the script will automatically handle dependency installation and execution)


## When to use
- The user wants a quick fundamental read on a stock beyond the current price.
- The user wants valuation, profitability, growth, balance sheet, cash flow, dividend, or analyst expectation context for a company.
- The user wants a compact strengths-and-risks summary grounded in basic financial metrics.

## Step-by-step approach
- When given a company name, first locate the corresponding stock ticker symbol using Yahoo Finance or another reliable service.
- Once the ticker is identified, use the ticker as input to the `main.py` script. The script will fetch fundamentals using the `yfinance` library (for example, `uv run main.py AAPL`).
- Use the output as a factual financial snapshot, not as investment advice.

## Usage Examples

**Analyze Apple fundamentals:**
```bash
uv run main.py AAPL
```

**Analyze Microsoft fundamentals:**
```bash
uv run main.py MSFT
```

**Analyze any supported stock symbol:**
```bash
uv run main.py NVDA
uv run main.py COST
uv run main.py JPM
```

## Output Format

The script prints a human-readable fundamentals report to stdout.

### Example Output
```text
AAPL: Apple Inc.
Sector: Technology | Industry: Consumer Electronics | Mkt Cap: $3.21T

Valuation:
Trailing P/E: 31.20
Forward P/E: 28.60
PEG Ratio: 2.45
Price/Sales: 7.90
Price/Book: 42.10
EV/EBITDA: 23.40

Profitability:
Gross Margin: 45.7%
Operating Margin: 31.4%
Net Margin: 24.3%
ROE: 129.1%
ROA: 27.6%

Growth:
Revenue Growth: 6.1%
Earnings Growth: 9.8%

Financial Health:
Cash: $67.42B
Debt: $98.14B
Debt/Equity: 151.3
Current Ratio: 1.10
Free Cash Flow: $101.25B

Shareholder Return:
Dividend Yield: 0.5%
Payout Ratio: 15.8%

Forward View:
Analyst Target: $221.50
Recommendation: Buy
Next Earnings: 2026-05-01 20:00:00 GMT

Fundamental Highlights:
- Margins remain strong relative to many large-cap peers.
- Free cash flow is positive, supporting internal funding.

Potential Watch Items:
- Debt levels are elevated relative to equity.
- Valuation sits above a typical mature-company range.
```

## Technical Notes
- Uses the `yfinance` library to fetch fundamentals from Yahoo Finance.
- No API key required.
- The Python implementation is split into `main.py`, `service.py`, `utils.py`, and `constants.py` to separate orchestration, metric extraction, formatting helpers, and configuration.
- Many fields can be missing for ETFs, indices, ADRs, or thinly covered companies.
- The script prefers Yahoo Finance quote metadata first, then falls back to statement data where possible.
- The strengths-and-risks section is rule-based and intended as quick context only.

## Troubleshooting
- If the stock symbol is invalid or not found, the script will return an error message.
- If fields show as `N/A`, the data source did not provide that metric for the symbol.
- For international tickers, specify the exchange suffix (for example, `BMW.DE`) to ensure data is pulled from the correct market.
- ETFs and indices often have limited company-level fundamental data.
