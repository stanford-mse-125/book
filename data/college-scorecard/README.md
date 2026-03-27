# College Scorecard Data

**Source:** [U.S. Department of Education College Scorecard](https://collegescorecard.ed.gov/data/)

**File:** `scorecard.csv` — 7,703 institutions, 122 columns

## Key columns (~20 most important)

### Institution identifiers
| Column | Description |
|--------|-------------|
| `UNITID` | Unique institution ID (IPEDS) |
| `INSTNM` | Institution name |
| `STABBR` | State abbreviation |
| `CONTROL` | 1 = Public, 2 = Private nonprofit, 3 = Private for-profit |
| `PREDDEG` | Predominant degree: 0 = Not classified, 1 = Certificate, 2 = Associate, 3 = Bachelor's, 4 = Graduate |
| `HBCU` | Historically Black College or University (0/1) |
| `LOCALE` | Locale code (urban/suburban/rural) |

### Selectivity & test scores
| Column | Description | Non-null |
|--------|-------------|----------|
| `SAT_AVG` | Average SAT equivalent score (combined, out of 1600) | 1,304 (17%) |
| `SATVRMID` | SAT verbal 25th–75th midpoint | 1,195 |
| `SATMTMID` | SAT math 25th–75th midpoint | 1,208 |
| `ACTCMMID` | ACT composite midpoint | 1,257 |

### Student body
| Column | Description | Non-null |
|--------|-------------|----------|
| `UGDS` | Undergraduate enrollment | 6,990 (91%) |
| `UGDS_WHITE/BLACK/HISP/ASIAN` | Racial composition shares | 6,990 |
| `PCTPELL` | % receiving Pell grants (proxy for low-income) | 6,966 (90%) |
| `PCTFLOAN` | % receiving federal loans | 6,966 |
| `UG25ABV` | % of undergraduates over age 25 | 6,966 |

### Outcomes
| Column | Description | Non-null |
|--------|-------------|----------|
| `MD_EARN_WNE_P10` | Median earnings 10 years after entry | 5,693 (74%) |
| `GT_25K_P6` | Share earning >$25K 6 years after entry | 5,900 |
| `C150_4_POOLED_SUPP` | 4-year completion rate (150% normal time) | 2,381 (31%) |
| `C150_L4_POOLED_SUPP` | Less-than-4-year completion rate | 3,806 |
| `RET_FT4` | First-year retention rate (full-time, 4-yr schools) | 2,293 (30%) |
| `GRAD_DEBT_MDN_SUPP` | Median graduation debt | 6,126 |
| `RPY_3YR_RT_SUPP` | 3-year loan repayment rate | 6,120 |

## Key statistics

- **Median earnings** (10yr post-entry): median $30,600; range $9,500–$233,100
- **SAT average**: median 1,040; range 720–1,545 (only 17% of schools report)
- **4-year completion rate**: median 0.47; range 0.02–1.00 (only 31% of schools)
- **Pell grant %**: median 52%; mean 53% (proxy for fraction of low-income students)
- **Stanford**: SAT_AVG 1,465; MD_EARN_WNE_P10 $86,000; completion rate 0.95

## Naive Analysis Traps

This dataset is a minefield for naive AI/LLM analysis. Three major traps:

### 1. Massive missingness — `dropna()` destroys the data

- `dropna()` on all 122 columns: **0 rows survive** (every school is missing something)
- Adding SAT_AVG to a query drops you from 6,990 to 1,304 schools (83% gone)
- Adding completion rate + earnings + retention: only **1,236 schools** (16%) survive
- **Survivorship of `dropna()` is severely biased**: 98.4% of survivors are Bachelor's-granting institutions. Certificate programs (43% of all schools) and community colleges (20%) are almost completely eliminated.
- AI tools that silently run `dropna()` will produce analysis that only describes selective 4-year colleges, not American higher education.

### 2. Survivorship bias in earnings data

Earnings columns (`MD_EARN_WNE_P10`, `GT_25K_P6`) track **only students who received federal financial aid** (Title IV recipients). Students who never took federal aid — often the wealthiest — are excluded.

- At elite private schools (low `PCTPELL`), many students pay full tuition without federal aid
- Reported earnings for these schools are biased **downward** because they only capture the less-wealthy subset
- Stanford's reported median earnings of $86K likely understates the true median for all graduates
- 841 schools have earnings data **suppressed** for privacy (too few Title IV students with reported earnings)

### 3. Confounding: selectivity vs. causal effect

A naive regression of earnings on SAT scores yields R² = 0.56, with a coefficient of ~$24 per SAT point. But this does **not** mean raising SAT scores by 100 points causes $2,400 higher earnings.

- SAT_AVG correlates with MD_EARN_WNE_P10 at r = 0.66
- SAT_AVG correlates with PCTPELL at r = -0.72 (high-SAT schools have fewer low-income students)
- PCTPELL correlates with MD_EARN_WNE_P10 at r = -0.58

The confounding story: students at high-SAT schools come from wealthier families, attend better-resourced high schools, and have stronger professional networks. The "school effect" on earnings is confounded by student selection. Disentangling causation requires techniques from causal inference (e.g., matching, regression discontinuity, instrumental variables).

## `PrivacySuppressed` values

Seven columns contain the string `PrivacySuppressed` instead of numeric values (schools with too few students for reliable/anonymous reporting). The EDA script converts these to NaN. Affected columns and suppression counts:

| Column | Suppressed |
|--------|-----------|
| `GRAD_DEBT_MDN_SUPP` | 1,545 |
| `GRAD_DEBT_MDN10YR_SUPP` | 1,545 |
| `MD_EARN_WNE_P10` | 841 |
| `GT_25K_P6` | 634 |
| `RPY_3YR_RT_SUPP` | 573 |
| `C150_L4_POOLED_SUPP` | 166 |
| `C150_4_POOLED_SUPP` | 116 |

## Suggested course uses

### HW2: Regression + confounding
- Regress `MD_EARN_WNE_P10` on `SAT_AVG`, `PCTPELL`, `UGDS`, `CONTROL`, etc.
- Ask: does adding `PCTPELL` change the SAT coefficient? (Yes — it shrinks, demonstrating omitted variable bias.)
- Discuss what "controlling for" means and what it cannot do.
- Discuss the missingness: which schools are in your regression sample? How does that affect interpretation?

### Lec 18: Causal inference — does college cause earnings?
- Motivating question: Stanford grads earn a lot. Is that because Stanford is a great school, or because Stanford admits students who would earn a lot anyway?
- Discuss the "Dale & Krueger" natural experiment: students admitted to selective schools who chose less selective ones earned similar amounts.
- Use the data to show the confounding structure: SAT → Earnings is confounded by family wealth (PCTPELL).
- Discuss what experiment you would need to estimate the causal effect of attending a more selective school.
- Survivorship bias: who is missing from the earnings data, and how does that affect our conclusions?

## Plots (generated by `eda.py`)

| File | Contents |
|------|----------|
| `missing_profile.png` | Histogram of % missing per column |
| `outcome_distributions.png` | Distributions of earnings, completion rate, SAT, ACT |
| `sat_vs_earnings.png` | Scatter plot: SAT average vs. median earnings with regression line |
| `confounding.png` | Side-by-side: SAT vs. earnings and Pell% vs. earnings |
| `dropna_survival.png` | Bar chart showing rows surviving progressive dropna |
