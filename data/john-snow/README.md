# John Snow Cholera Data

## Overview

In 1854, a devastating cholera outbreak struck the Soho district of London, killing over 600 people in a few weeks. Dr. John Snow used careful data collection and reasoning to demonstrate that cholera was transmitted through contaminated water -- not through "miasma" (bad air), which was the prevailing theory. His work is considered a founding moment of epidemiology and one of the earliest examples of causal inference from observational data.

**Use in MSE 125**: Causal inference demo, natural experiments, the difference between correlation and causation.

## Data Source

- **Original**: John Snow, "On the Mode of Communication of Cholera" (1855)
- **Deaths and pumps data**: [vincentarelbundock/Rdatasets](https://github.com/vincentarelbundock/Rdatasets) (HistData package)
- **Water company data**: Manually compiled from Snow's Table IX

## Files and Schema

### `snow_deaths.csv` (578 rows)
Death locations from the Broad Street outbreak.

| Column | Type | Description |
|--------|------|-------------|
| `rownames` | int | Row index |
| `case` | int | Case number |
| `x` | float | X coordinate (map units) |
| `y` | float | Y coordinate (map units) |

### `snow_pumps.csv` (13 rows)
Water pump locations in the Soho area.

| Column | Type | Description |
|--------|------|-------------|
| `rownames` | int | Row index |
| `pump` | int | Pump number |
| `label` | str | Pump name (e.g., "Broad St") |
| `x` | float | X coordinate |
| `y` | float | Y coordinate |

### `snow_dates.csv` (44 rows)
Daily epidemic timeline (Aug 19 - Sep 30, 1854).

| Column | Type | Description |
|--------|------|-------------|
| `rownames` | int | Row index |
| `date` | date | Date |
| `attacks` | int | New cholera cases |
| `deaths` | int | Deaths |

### `snow_water_companies.csv` (3 rows)
The key natural experiment data from Snow's Table IX.

| Column | Type | Description |
|--------|------|-------------|
| `company` | str | Water company name |
| `houses` | int | Number of houses served |
| `deaths` | int | Cholera deaths |
| `death_rate_per_10000` | int | Deaths per 10,000 houses |

## Key Statistics

### The Epidemic
- **Total death locations**: 578
- **Date range**: August 19 - September 30, 1854
- **Peak attacks**: 143 on September 1
- **Peak deaths**: 127 on September 2
- **Pump handle removed**: September 8 (epidemic was already declining)

### The Map Evidence
- 62.1% of deaths were nearest to the Broad Street pump (359 of 578)
- The spatial clustering around the Broad St pump was striking visual evidence

### The Natural Experiment (The Key Evidence)
Snow's most powerful evidence was not the map -- it was the comparison of water companies.

| Water Company | Houses | Deaths | Rate per 10,000 |
|--------------|--------|--------|-----------------|
| Southwark & Vauxhall (polluted) | 40,046 | 1,263 | 315 |
| Lambeth (clean) | 26,107 | 98 | 38 |
| Rest of London | 256,423 | 1,422 | 55 |

**Relative risk**: 8.4x higher death rate for houses served by the company drawing water downstream of sewage outflows.

**Why this is a natural experiment**: Both companies served houses on the same streets, intermingled throughout South London. The assignment of a household to one company or the other was essentially arbitrary (based on which company happened to have laid pipes to that address). This eliminates confounding by neighborhood poverty, crowding, sanitation, or any other local factor.

## The Causal Reasoning

1. **Correlation**: Deaths cluster near the Broad Street pump.
2. **Natural experiment**: Same neighborhoods, different water sources, 8.4x difference in death rates.
3. **Mechanism**: Southwark & Vauxhall drew water from the Thames downstream of sewage outflows. Lambeth moved its intake upstream in 1852.
4. **Intervention**: Removing the Broad Street pump handle (Sep 8) was associated with the end of the outbreak, though the epidemic was already declining.

This is a textbook example of how to reason about causation without a randomized controlled trial.

## AI Traps

1. **Confusing the map with the experiment**: The map (deaths near Broad St pump) is suggestive but could be explained by confounders (poverty, crowding in that area). The water company comparison is the real causal evidence because it controls for neighborhood factors.

2. **Post hoc ergo propter hoc**: The epidemic was already declining before the pump handle was removed on Sep 8. An AI might naively attribute the decline to the intervention, but the timing is ambiguous.

3. **Ecological fallacy**: The water company data is at the household level, not individual level. We know which company served each house, not which water each person actually drank.

## Suggested Lecture/HW Uses

- **Natural experiments**: What makes Snow's water company comparison a natural experiment? What assumptions are needed?
- **Confounding**: Why is the map alone not sufficient to establish causation? What confounders could explain the spatial clustering?
- **Hypothesis testing**: Use the water company data for a two-proportion z-test or chi-squared test
- **Causal diagrams**: Draw a DAG for the water source -> cholera relationship. Where does "miasma" fit?
- **Historical context**: Connect to modern natural experiments (regression discontinuity, instrumental variables)
- **Visualization**: Recreate Snow's cholera map as an exercise in data visualization

## Files

- `snow_deaths.csv` -- death locations (578 cases)
- `snow_pumps.csv` -- pump locations (13 pumps)
- `snow_dates.csv` -- daily epidemic timeline
- `snow_water_companies.csv` -- water company comparison (Snow's Table IX)
- `eda.py` -- exploratory data analysis script
- `plots/` -- generated visualizations (epidemic curve, map, water company comparison, etc.)
