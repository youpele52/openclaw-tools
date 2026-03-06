#!/usr/bin/env python3

# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "yfinance",
# ]
# ///
#
"""
Stock Price Checker - Get current stock prices from Yahoo Finance using yfinance.
"""

import sys
from datetime import datetime, timedelta

import yfinance as yf


def format_number(num, decimals=2):
    """Format a number with commas and specified decimals."""
    if num is None:
        return "N/A"
    return f"{num:,.{decimals}f}"


def get_price_range(history, days: int) -> dict:
    """Calculate the high and low price over the last N days from historical data."""
    cutoff = datetime.now() - timedelta(days=days)
    filtered = history[history.index >= cutoff.strftime("%Y-%m-%d")]
    if filtered.empty:
        return {"high": None, "low": None}
    return {
        "high": float(filtered["High"].max()),
        "low": float(filtered["Low"].min()),
    }


def extract_upcoming_events(calendar, symbol: str) -> list:
    """Extract up to 5 upcoming events from calendar data with GMT timezone info."""
    events = []

    if not calendar:
        return events

    earnings_date = calendar.get("Earnings Date")
    if earnings_date:
        if isinstance(earnings_date, (list, tuple)) and len(earnings_date) > 0:
            earnings_date = earnings_date[0]
        if earnings_date:
            events.append({"type": "Earnings Call", "date": earnings_date})

    ex_dividend_date = calendar.get("Ex-Dividend Date")
    if ex_dividend_date:
        events.append({"type": "Ex-Dividend Date", "date": ex_dividend_date})

    dividend_date = calendar.get("Dividend Date")
    if dividend_date:
        events.append({"type": "Dividend Payment", "date": dividend_date})

    earnings_avg = calendar.get("Earnings Average")
    if earnings_avg is not None:
        events.append(
            {"type": "Earnings EPS Estimate", "date": f"Est. EPS: {earnings_avg}"}
        )

    earnings_high = calendar.get("Earnings High")
    if earnings_high is not None:
        events.append(
            {"type": "Earnings EPS High", "date": f"Est. High EPS: {earnings_high}"}
        )

    return events[:5]


def filter_relevant_news(news_list: list, symbol: str, company_name: str) -> list:
    """Filter news articles to show only those relevant to the company."""
    if not news_list:
        return []

    keywords = [symbol.upper(), company_name.upper(), company_name.split()[0].upper()]
    filtered = []

    for article in news_list:
        if not isinstance(article, dict):
            continue
        content = article.get("content", {})
        if not isinstance(content, dict):
            continue

        title = content.get("title", "").upper()
        summary = content.get("summary", "").upper()

        if any(kw in title or kw in summary for kw in keywords if kw):
            filtered.append(article)

        if len(filtered) >= 5:
            break

    return filtered


def get_stock_price(symbol: str) -> dict:
    """Get current stock price, company info, historical ranges, news, and events."""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        current_price = info.get("currentPrice") or info.get("regularMarketPrice")
        previous_close = info.get("previousClose")
        change = (
            current_price - previous_close if current_price and previous_close else None
        )
        change_percent = (
            ((change / previous_close) * 100) if change and previous_close else None
        )
        market_cap = info.get("marketCap")
        volume = info.get("volume")
        avg_volume = info.get("averageVolume")
        company_name = info.get("longName") or info.get("shortName") or symbol
        day_high = info.get("dayHigh")
        day_low = info.get("dayLow")

        # Fetch 1 year of daily history to cover all range windows
        history = ticker.history(period="1y")

        range_2w = get_price_range(history, 14)
        range_1m = get_price_range(history, 30)
        range_6m = get_price_range(history, 182)
        range_52w = get_price_range(history, 365)

        # Fetch up to 20 news articles so we have enough to filter 5 relevant ones
        raw_news = ticker.news[:20] if ticker.news else []
        news = filter_relevant_news(raw_news, symbol, company_name)

        # Extract upcoming events
        events = extract_upcoming_events(ticker.calendar, symbol)

        return {
            "symbol": symbol,
            "company_name": company_name,
            "price": current_price,
            "change": change,
            "change_percent": change_percent,
            "previous_close": previous_close,
            "market_cap": market_cap,
            "volume": volume,
            "avg_volume": avg_volume,
            "day_high": day_high,
            "day_low": day_low,
            "range_2w": range_2w,
            "range_1m": range_1m,
            "range_6m": range_6m,
            "range_52w": range_52w,
            "news": news,
            "events": events,
        }
    except Exception as e:
        return {"error": f"Could not get stock price for {symbol}: {str(e)}"}


def format_range(label: str, range_data: dict) -> str:
    """Format a price range block with separate high and low lines."""
    high = range_data.get("high")
    low = range_data.get("low")
    high_str = f"${format_number(high)}" if high is not None else "N/A"
    low_str = f"${format_number(low)}" if low is not None else "N/A"
    return f"{label} High: {high_str}\n{label} Low:  {low_str}"


def format_event_date(event_date) -> str:
    """Format an event date value into a GMT timestamp string."""
    if isinstance(event_date, str) and event_date.startswith("Est."):
        return event_date
    if isinstance(event_date, (int, float)):
        return datetime.utcfromtimestamp(event_date).strftime("%Y-%m-%d %H:%M:%S GMT")
    if isinstance(event_date, datetime):
        return event_date.strftime("%Y-%m-%d %H:%M:%S GMT")
    try:
        dt = datetime.fromisoformat(str(event_date).replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S GMT")
    except Exception:
        return str(event_date)


def format_output(data: dict) -> str:
    """Format all stock data into the final human-readable output."""
    if "error" in data:
        return f"Error: {data['error']}"

    symbol = data["symbol"]
    company_name = data["company_name"]
    price = data["price"]
    change = data["change"]
    change_percent = data["change_percent"]
    previous_close = data["previous_close"]
    market_cap = data["market_cap"]
    volume = data["volume"]
    avg_volume = data["avg_volume"]
    day_high = data.get("day_high")
    day_low = data.get("day_low")
    news = data["news"]
    events = data["events"]

    # --- Price ---
    price_str = f"${format_number(price)}"

    # --- Change ---
    if change is not None and change > 0:
        change_str = f"▲${format_number(change)}"
    elif change is not None and change < 0:
        change_str = f"▼${format_number(abs(change))}"
    else:
        change_str = "—"

    # --- Change percent ---
    change_percent_str = (
        f"({format_number(change_percent)}%)" if change_percent is not None else "(—)"
    )

    # --- Previous close ---
    prev_close_str = (
        f"${format_number(previous_close)}" if previous_close is not None else "N/A"
    )

    # --- Volume ---
    if volume is not None and avg_volume is not None and avg_volume > 0:
        volume_percent = (volume / avg_volume) * 100
        volume_str = (
            f"Vol: {format_number(volume / 1_000_000, 1)}M "
            f"Avg: {format_number(avg_volume / 1_000_000, 1)}M "
            f"| {format_number(volume_percent, 0)}% of avg"
        )
    else:
        volume_str = "Vol: N/A"

    # --- Market cap ---
    if market_cap is not None:
        if market_cap >= 1_000_000_000_000:
            market_cap_str = f"${format_number(market_cap / 1_000_000_000_000, 2)}T"
        elif market_cap >= 1_000_000_000:
            market_cap_str = f"${format_number(market_cap / 1_000_000_000, 2)}B"
        else:
            market_cap_str = f"${format_number(market_cap / 1_000_000, 2)}M"
    else:
        market_cap_str = "N/A"

    # --- Today's range ---
    today_high_str = f"${format_number(day_high)}" if day_high is not None else "N/A"
    today_low_str = f"${format_number(day_low)}" if day_low is not None else "N/A"
    today_range_str = f"Today High: {today_high_str}\nToday Low:  {today_low_str}"

    # --- Historical ranges ---
    range_2w_str = format_range("2W", data["range_2w"])
    range_1m_str = format_range("1M", data["range_1m"])
    range_6m_str = format_range("6M", data["range_6m"])
    range_52w_str = format_range("52W", data["range_52w"])

    # --- News ---
    if news:
        news_lines = "Recent News:\n"
        for i, article in enumerate(news[:5], 1):
            title = "No title"
            url = ""
            content = article.get("content", {})
            if isinstance(content, dict):
                title = content.get("title", "No title")
                click_url = content.get("clickThroughUrl", {})
                if isinstance(click_url, dict):
                    url = click_url.get("url", "")
            if url:
                news_lines += f"{i}. {title}\n   Link: {url}\n"
            else:
                news_lines += f"{i}. {title}\n"
        news_str = news_lines.rstrip()
    else:
        news_str = "Recent News: No relevant news available"

    # --- Events ---
    if events:
        events_lines = "Upcoming Events:\n"
        for i, event in enumerate(events[:5], 1):
            event_type = event.get("type", "Unknown")
            date_str = format_event_date(event.get("date", "Unknown"))
            events_lines += f"{i}. {event_type}: {date_str}\n"
        events_str = events_lines.rstrip()
    else:
        events_str = "Upcoming Events: None scheduled"

    # --- Assemble final output ---
    output = (
        f"{symbol}: {company_name}\n"
        f"{price_str} {change_str} {change_percent_str}, Prev Close: {prev_close_str}\n"
        f"{volume_str} | Mkt Cap: {market_cap_str}\n"
        f"\n"
        f"{today_range_str}\n"
        f"\n"
        f"{range_2w_str}\n"
        f"\n"
        f"{range_1m_str}\n"
        f"\n"
        f"{range_6m_str}\n"
        f"\n"
        f"{range_52w_str}\n"
        f"\n"
        f"{news_str}\n"
        f"\n"
        f"{events_str}"
    )
    return output


def main():
    """Entry point — expects a stock ticker symbol as the first CLI argument."""
    if len(sys.argv) < 2:
        print("Usage: stock-price <SYMBOL>")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    result = get_stock_price(symbol)
    print(format_output(result))


if __name__ == "__main__":
    main()
