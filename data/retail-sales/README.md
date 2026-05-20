# US Retail Sales (FRED RSAFSNA)

## Overview

Monthly US retail and food services sales, not seasonally adjusted (NSA). The seasonally-unadjusted version preserves the strong December holiday spike and January/February dip, which is exactly the pattern Holt-Winters and classical decomposition are designed to model.

**Use in MSE 125**: trend + seasonality, classical decomposition, Holt-Winters / triple exponential smoothing, walk-forward validation on monthly data.

## Data Source

- **Series**: `RSAFSNA` — Advance Retail Sales: Retail Trade and Food Services, Not Seasonally Adjusted
- **Publisher**: U.S. Census Bureau, retrieved via FRED (Federal Reserve Bank of St. Louis)
- **URL**: https://fred.stlouisfed.org/series/RSAFSNA
- **License**: U.S. government data, public domain
- **Units**: Millions of U.S. dollars
- **Frequency**: Monthly, first of month timestamps

## Schema

| Column | Type | Description |
|--------|------|-------------|
| `date` | date | Month (first-of-month timestamp) |
| `sales` | int | Total US retail and food services sales for that month, in millions of dollars |

## Key features

- **Strong upward trend**: monthly sales roughly quadrupled from $140B in 1992 to ~$750B in 2026.
- **Multiplicative seasonality**: December runs about 15% above the local trend; January/February about 10% below. The seasonal *percentage* is roughly stable but the dollar amplitude grows with the trend, which is why a multiplicative decomposition fits better than an additive one.
- **COVID disruption**: visible as a sharp dip in March–April 2020 followed by a large overshoot. Useful for distribution-shift discussions.

## Fetching a fresh copy

```bash
curl -L 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=RSAFSNA' \
  -o fred_rsafsna_monthly.csv
```

The committed snapshot was captured in May 2026.
