# EPA Air Quality Index (AQI) - California

## Overview

Daily Air Quality Index (AQI) data for all U.S. counties, filtered to California. AQI measures how polluted the air is on a given day, with values influenced by ozone, particulate matter, and other pollutants. In California, wildfire smoke events cause dramatic AQI spikes that are fundamentally different from normal air quality variation.

**Use in MSE 125**: Backtesting, time series validation, regime changes, non-stationarity.

## Data Source

- **Source**: U.S. Environmental Protection Agency (EPA) Air Quality System
- **URL**: https://aqs.epa.gov/aqsweb/airdata/download_files.html
- **Files**: `daily_aqi_by_county_YYYY.zip` for years 2021-2024
- **License**: Public domain (U.S. government data)

## Schema

| Column | Type | Description |
|--------|------|-------------|
| `State Name` | str | State name (filtered to "California") |
| `county Name` | str | County name |
| `State Code` | int | FIPS state code (06 for CA) |
| `County Code` | int | FIPS county code |
| `Date` | date | Measurement date |
| `AQI` | int | Air Quality Index value (0 = best) |
| `Category` | str | AQI category (Good, Moderate, Unhealthy, etc.) |
| `Defining Parameter` | str | Which pollutant determined the AQI |
| `Defining Site` | str | Monitoring site ID |
| `Number of Sites Reporting` | int | Number of monitoring sites |

### AQI Categories
| AQI Range | Category | Health Implication |
|-----------|----------|-------------------|
| 0-50 | Good | Satisfactory |
| 51-100 | Moderate | Acceptable |
| 101-150 | Unhealthy for Sensitive Groups | Risk for sensitive individuals |
| 151-200 | Unhealthy | Everyone may experience effects |
| 201-300 | Very Unhealthy | Health alert |
| 301+ | Hazardous | Emergency conditions |

## Key Statistics

- **California rows**: 75,449 (2021-2024)
- **Counties**: 53
- **Date range**: 2021-01-01 to 2024-12-31
- **Mean AQI**: 54.9 (Moderate)
- **Median AQI**: 48 (Good)
- **Max AQI**: 8,368 (Mono County, extreme dust/wildfire event)

### Wildfire/Extreme Events
- Days with AQI > 150 (Unhealthy): 1,353 county-days
- Days with AQI > 200 (Very Unhealthy): 287
- Days with AQI > 300 (Hazardous): 104
- Worst counties: Mono (extreme dust events), Trinity, Tulare, Riverside

### Seasonal Pattern
- Summer/fall months (Jul-Sep) have highest average AQI due to wildfire season
- Winter months also elevated in some areas (inversions, wood burning)

### Backtesting Demonstration
- **Naive random split MAE**: 16.2 (optimistically biased)
- **Proper temporal split MAE**: 19.5
- The naive split leaks future information through lag features, making the model appear 3.2 MAE points better than it actually is

## Naive Analysis Traps

1. **Regime changes**: Wildfire smoke events are fundamentally different from normal air quality. A linear model trained on "normal" data underpredicts AQI by ~27 points during smoke events. AI models extrapolate linearly and fail during regime changes.

2. **Naive train/test split**: Random splitting of time series data leaks future information through lag features, producing optimistically biased error estimates. Students must use temporal backtesting (train on past, test on future).

3. **Non-stationarity**: The mean and variance of AQI change over time. Wildfire years have heavier tails. A model calibrated on 2021-2022 may not generalize to 2023-2024.

4. **Extreme values**: Mono County has AQI readings above 8,000 (likely from dust storms near Mono Lake). These are real measurements but extreme outliers that can dominate model fitting.

5. **Spatial correlation**: Neighboring counties share air quality events. Treating each county independently ignores this structure.

## Suggested Lecture/HW Uses

- **Backtesting**: Compare naive random split vs temporal split -- quantify the optimism bias
- **Time series basics**: Autocorrelation, lag features, rolling statistics
- **Non-stationarity**: Show that AQI distribution shifts year to year
- **Regime detection**: Can you detect when a wildfire smoke event is happening vs normal variation?
- **Prediction intervals**: Point predictions are insufficient -- how wide should confidence intervals be to cover smoke events?
- **Feature engineering**: Lag features, rolling means, day-of-year seasonality, county fixed effects

## Files

- `daily_aqi_by_county_2021.csv` through `daily_aqi_by_county_2024.csv` -- raw EPA data (all U.S. counties)
- `daily_aqi_by_county_2021.zip` through `daily_aqi_by_county_2024.zip` -- compressed originals
- `eda.py` -- exploratory data analysis script (filters to CA, generates all plots)
- `plots/` -- generated visualizations (time series, seasonal patterns, backtesting comparison, etc.)
