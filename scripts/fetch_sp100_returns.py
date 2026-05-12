"""Fetch daily adjusted close prices for S&P 100 constituents via yfinance.

Outputs (relative to the book root):
  data/stocks/sp100_daily_returns_2014_2024.csv  -- rows=dates, cols=tickers, values=daily log returns
  data/stocks/sp100_metadata.csv                  -- ticker, name, sector lookup

Usage:
    cd book && python scripts/fetch_sp100_returns.py

Notes:
- Uses *current* S&P 100 roster; results are subject to survivorship bias.
- Pinned date range 2014-01-01 -- 2024-12-31.
- Idempotent: if the output CSV already exists, the script exits without re-fetching.
- Pinned yfinance version: see requirements; tested with yfinance 1.3.0.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf


# --- Configuration -----------------------------------------------------------
START_DATE = "2014-01-01"
END_DATE = "2024-12-31"

# Current S&P 100 constituents (OEX), with sector tags.  Frozen here for
# reproducibility.  Note that the index roster changes over time; the public
# replacement of $FB (Meta) by $META in 2022 is handled by yfinance's ticker
# aliasing.
SP100_RAW = [
    # ticker, name, sector
    ("AAPL", "Apple", "Technology"),
    ("ABBV", "AbbVie", "Health Care"),
    ("ABT", "Abbott Laboratories", "Health Care"),
    ("ACN", "Accenture", "Technology"),
    ("ADBE", "Adobe", "Technology"),
    ("AIG", "American International Group", "Financials"),
    ("AMD", "Advanced Micro Devices", "Technology"),
    ("AMGN", "Amgen", "Health Care"),
    ("AMT", "American Tower", "Real Estate"),
    ("AMZN", "Amazon", "Consumer Discretionary"),
    ("AVGO", "Broadcom", "Technology"),
    ("AXP", "American Express", "Financials"),
    ("BA", "Boeing", "Industrials"),
    ("BAC", "Bank of America", "Financials"),
    ("BK", "BNY Mellon", "Financials"),
    ("BKNG", "Booking Holdings", "Consumer Discretionary"),
    ("BLK", "BlackRock", "Financials"),
    ("BMY", "Bristol-Myers Squibb", "Health Care"),
    ("C", "Citigroup", "Financials"),
    ("CAT", "Caterpillar", "Industrials"),
    ("CHTR", "Charter Communications", "Communication Services"),
    ("CL", "Colgate-Palmolive", "Consumer Staples"),
    ("CMCSA", "Comcast", "Communication Services"),
    ("COF", "Capital One", "Financials"),
    ("COP", "ConocoPhillips", "Energy"),
    ("COST", "Costco", "Consumer Staples"),
    ("CRM", "Salesforce", "Technology"),
    ("CSCO", "Cisco", "Technology"),
    ("CVS", "CVS Health", "Health Care"),
    ("CVX", "Chevron", "Energy"),
    ("DE", "Deere", "Industrials"),
    ("DHR", "Danaher", "Health Care"),
    ("DIS", "Walt Disney", "Communication Services"),
    ("DUK", "Duke Energy", "Utilities"),
    ("EMR", "Emerson Electric", "Industrials"),
    ("F", "Ford", "Consumer Discretionary"),
    ("FDX", "FedEx", "Industrials"),
    ("GD", "General Dynamics", "Industrials"),
    ("GE", "GE Aerospace", "Industrials"),
    ("GILD", "Gilead Sciences", "Health Care"),
    ("GM", "General Motors", "Consumer Discretionary"),
    ("GOOG", "Alphabet (Class C)", "Communication Services"),
    ("GOOGL", "Alphabet (Class A)", "Communication Services"),
    ("GS", "Goldman Sachs", "Financials"),
    ("HD", "Home Depot", "Consumer Discretionary"),
    ("HON", "Honeywell", "Industrials"),
    ("IBM", "IBM", "Technology"),
    ("INTC", "Intel", "Technology"),
    ("JNJ", "Johnson & Johnson", "Health Care"),
    ("JPM", "JPMorgan Chase", "Financials"),
    ("KO", "Coca-Cola", "Consumer Staples"),
    ("LIN", "Linde", "Materials"),
    ("LLY", "Eli Lilly", "Health Care"),
    ("LMT", "Lockheed Martin", "Industrials"),
    ("LOW", "Lowe's", "Consumer Discretionary"),
    ("MA", "Mastercard", "Financials"),
    ("MCD", "McDonald's", "Consumer Discretionary"),
    ("MDLZ", "Mondelez", "Consumer Staples"),
    ("MDT", "Medtronic", "Health Care"),
    ("MET", "MetLife", "Financials"),
    ("META", "Meta Platforms", "Communication Services"),
    ("MMM", "3M", "Industrials"),
    ("MO", "Altria", "Consumer Staples"),
    ("MRK", "Merck", "Health Care"),
    ("MS", "Morgan Stanley", "Financials"),
    ("MSFT", "Microsoft", "Technology"),
    ("NEE", "NextEra Energy", "Utilities"),
    ("NFLX", "Netflix", "Communication Services"),
    ("NKE", "Nike", "Consumer Discretionary"),
    ("NVDA", "NVIDIA", "Technology"),
    ("ORCL", "Oracle", "Technology"),
    ("PEP", "PepsiCo", "Consumer Staples"),
    ("PFE", "Pfizer", "Health Care"),
    ("PG", "Procter & Gamble", "Consumer Staples"),
    ("PM", "Philip Morris", "Consumer Staples"),
    ("PYPL", "PayPal", "Financials"),
    ("QCOM", "Qualcomm", "Technology"),
    ("RTX", "RTX (Raytheon)", "Industrials"),
    ("SBUX", "Starbucks", "Consumer Discretionary"),
    ("SCHW", "Charles Schwab", "Financials"),
    ("SO", "Southern Company", "Utilities"),
    ("SPG", "Simon Property", "Real Estate"),
    ("T", "AT&T", "Communication Services"),
    ("TGT", "Target", "Consumer Discretionary"),
    ("TMO", "Thermo Fisher", "Health Care"),
    ("TMUS", "T-Mobile US", "Communication Services"),
    ("TSLA", "Tesla", "Consumer Discretionary"),
    ("TXN", "Texas Instruments", "Technology"),
    ("UNH", "UnitedHealth Group", "Health Care"),
    ("UNP", "Union Pacific", "Industrials"),
    ("UPS", "United Parcel Service", "Industrials"),
    ("USB", "U.S. Bancorp", "Financials"),
    ("V", "Visa", "Financials"),
    ("VZ", "Verizon", "Communication Services"),
    ("WBA", "Walgreens Boots Alliance", "Consumer Staples"),
    ("WFC", "Wells Fargo", "Financials"),
    ("WMT", "Walmart", "Consumer Staples"),
    ("XOM", "ExxonMobil", "Energy"),
]


def main() -> int:
    book_root = Path(__file__).resolve().parents[1]
    out_dir = book_root / "data" / "stocks"
    out_dir.mkdir(parents=True, exist_ok=True)
    returns_path = out_dir / "sp100_daily_returns_2014_2024.csv"
    metadata_path = out_dir / "sp100_metadata.csv"

    metadata = pd.DataFrame(SP100_RAW, columns=["ticker", "name", "sector"])

    if returns_path.exists() and metadata_path.exists():
        print(f"  skip: {returns_path} already exists (delete to refetch)")
        return 0

    tickers = [row[0] for row in SP100_RAW]
    print(f"Fetching {len(tickers)} tickers from {START_DATE} to {END_DATE}...")

    # Single batch download; auto_adjust=True gives split/dividend-adjusted prices.
    raw = yf.download(
        tickers,
        start=START_DATE,
        end=END_DATE,
        auto_adjust=True,
        progress=False,
        threads=True,
        group_by="ticker",
    )

    # yfinance returns a MultiIndex (ticker, field) when passing multiple tickers.
    # Extract the Close column for each ticker.
    close = pd.DataFrame()
    dropped = []
    for tkr in tickers:
        try:
            if (tkr, "Close") in raw.columns:
                series = raw[(tkr, "Close")]
            elif tkr in raw.columns.levels[0]:
                series = raw[tkr]["Close"]
            else:
                dropped.append((tkr, "no data"))
                continue
        except (KeyError, AttributeError):
            dropped.append((tkr, "key error"))
            continue
        if series.dropna().empty:
            dropped.append((tkr, "all NaN"))
            continue
        close[tkr] = series

    # Compute trading-day coverage and drop tickers missing more than 5% of days.
    coverage = close.notna().sum() / len(close)
    low_coverage = coverage[coverage < 0.95].index.tolist()
    for tkr in low_coverage:
        dropped.append((tkr, f"coverage {coverage[tkr]:.1%}"))
    close = close.drop(columns=low_coverage)

    # Forward-fill very small gaps (single missing day = trading halt / data error).
    close = close.ffill(limit=2)
    close = close.dropna(how="all").dropna(axis=1, how="any")

    # Log returns.
    log_returns = np.log(close).diff().dropna(how="all")

    # Order tickers alphabetically for stable column order.
    log_returns = log_returns.reindex(sorted(log_returns.columns), axis=1)

    print(f"  shape: {log_returns.shape}")
    print(f"  date range: {log_returns.index.min().date()} -- {log_returns.index.max().date()}")
    print(f"  dropped {len(dropped)} tickers:")
    for tkr, reason in dropped:
        print(f"    {tkr}: {reason}")

    log_returns.to_csv(returns_path, index_label="date")

    # Subset metadata to kept tickers.
    metadata_kept = metadata[metadata["ticker"].isin(log_returns.columns)].reset_index(drop=True)
    metadata_kept.to_csv(metadata_path, index=False)

    print(f"  wrote {returns_path} ({returns_path.stat().st_size / 1e6:.1f} MB)")
    print(f"  wrote {metadata_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
