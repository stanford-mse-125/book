# Clinical Trial Data for MSE 125

## Recommended Dataset: ACTG 175

**AIDS Clinical Trials Group Study 175** is the recommended primary dataset for teaching hypothesis testing. See evaluation of alternatives below.

### Source

- Original paper: Hammer et al. (1996), "A Trial Comparing Nucleoside Monotherapy with Combination Therapy in HIV-Infected Adults with CD4 Cell Counts from 200 to 500 per Cubic Millimeter", NEJM 335(15):1081-1090
- R package: `speff2trial` (extracted from CRAN archive)
- Downloaded: `ACTG175.csv` (2139 patients, 27 variables)

### Study Design

Randomized clinical trial comparing HIV treatments in adults with CD4 counts 200-500 cells/mm^3:

| Arm | Code | Treatment | n |
|-----|------|-----------|---|
| 0 | ZDV mono | Zidovudine monotherapy (control) | 532 |
| 1 | ZDV+ddI | Zidovudine + didanosine | 522 |
| 2 | ZDV+ddC | Zidovudine + zalcitabine | 524 |
| 3 | ddI mono | Didanosine monotherapy | 561 |

### Schema

| Column | Description | Type |
|--------|-------------|------|
| `pidnum` | Patient ID | int |
| `age` | Age in years at baseline | int |
| `wtkg` | Weight in kg at baseline | float |
| `hemo` | Hemophilia (0=no, 1=yes) | binary |
| `homo` | Homosexual activity (0=no, 1=yes) | binary |
| `drugs` | History of IV drug use (0=no, 1=yes) | binary |
| `karnof` | Karnofsky performance score (0-100) | int |
| `oprior` | Non-ZDV antiretroviral therapy pre-175 (0=no, 1=yes) | binary |
| `z30` | ZDV in 30 days pre-175 (0=no, 1=yes) | binary |
| `zprior` | ZDV prior to 175 (0=no, 1=yes) | binary |
| `preanti` | Months of pre-175 antiretroviral therapy | float |
| `race` | Race (0=white, 1=non-white) | binary |
| `gender` | Gender (0=female, 1=male) | binary |
| `str2` | Antiretroviral history (0=naive, 1=experienced) | binary |
| `strat` | Antiretroviral stratum (1=naive, 2=exp >1yr, 3=exp <=1yr) | int |
| `symptom` | Symptomatic indicator (0=no, 1=yes) | binary |
| `treat` | Treatment indicator (0=ZDV mono, 1=other) | binary |
| `offtrt` | Off treatment before 96 weeks (0=no, 1=yes) | binary |
| `cd40` | CD4 count at baseline | int |
| `cd420` | CD4 count at 20 +/- 5 weeks | int |
| `cd496` | CD4 count at 96 +/- 5 weeks | int |
| `r` | CD4 at 96 weeks observed (0=missing, 1=observed) | binary |
| `cd80` | CD8 count at baseline | int |
| `cd820` | CD8 count at 20 weeks | int |
| `cens` | Event indicator (1=failure: AIDS/death) | binary |
| `days` | Days to failure or censoring | int |
| `arms` | Treatment arm (0, 1, 2, 3) | int |

### Key Statistics

- **Primary outcome (CD4 change at 20 weeks)**: ZDV mono mean = -17.1, combination therapy mean = +33.3
- **Welch's t-test**: t = 9.15, p = 2.8e-19
- **95% CI for difference**: [39.6, 61.2] cells/mm^3
- **Permutation test**: p < 0.0001 (10,000 permutations)
- **Event rate**: 24.4% experienced AIDS or death
- **Randomization balance**: Excellent across all covariates (age, gender, race, baseline CD4)

### AI Traps

These are mistakes that LLMs and naive analysts commonly make with this data:

1. **Multiple comparisons (primary trap)**: Testing treatment effect in 20 subgroups (by age, race, gender, baseline CD4, etc.) and reporting the most significant one. With 20 tests at alpha=0.05, we expect ~1 false positive. In our analysis, testing for *differential* treatment effects across 20 subgroups found 1/20 "significant" (Baseline CD4 Q2, p=0.017) -- exactly the false positive rate we'd predict by chance. After Bonferroni correction: 0/20 significant.

2. **Ignoring the `treat` vs `arms` distinction**: The `treat` column (0/1) collapses three different combination arms. An AI might use this and miss that ZDV+ddI (arm 1, mean change +54.4) is substantially better than ZDV+ddC (arm 2, mean change +19.3).

3. **Survivorship bias in cd496**: Only 62.7% of patients have a 96-week CD4 count (`r` column). Analyzing cd496 without accounting for informative missingness (sicker patients drop out) biases results.

4. **Ignoring censoring for time-to-event**: Using a t-test on `days` ignores right-censoring. Proper analysis requires survival methods (Kaplan-Meier, log-rank test).

5. **Confusing correlation with causation in observational subgroups**: The trial is randomized overall, but subgroup analyses are observational (subgroups are not randomized).

### Suggested Lecture Uses

1. **Week on hypothesis testing**: "Did combination therapy improve CD4 counts?" -- t-test, permutation test, p-values, confidence intervals. The answer is unambiguously yes (p ~ 10^-19).

2. **Week on multiple comparisons**: "Does the treatment work better for men than women? For young vs old? For high vs low baseline CD4?" Test 20 subgroups, observe false positives, introduce Bonferroni correction. The pure-noise demo (random splits within control arm) makes the issue visceral.

3. **Week on study design**: Why randomization matters (excellent covariate balance). What happens with observational data. Intent-to-treat vs per-protocol (36% went off treatment).

4. **Week on missing data / survival analysis**: 37% missing at 96 weeks. Is the missingness informative? Introduction to censoring.

5. **Week on effect sizes**: The effect is statistically significant AND clinically meaningful (~50 CD4 cells/mm^3). Discuss when statistical significance != practical significance.

---

## Alternative: Streptomycin TB Trial (1948)

**File**: `strep_tb.csv` (107 patients, 14 variables)

The first modern randomized controlled trial. MRC trial of streptomycin for pulmonary tuberculosis.

### Pros
- Historic significance: the birth of the RCT
- Simple two-arm design (Streptomycin vs Control)
- Clear binary outcome (improved: 69% vs 33%, chi2=12.76, p=0.0004)
- Small enough to examine individual records
- Rich ordinal outcome (6-level radiologic assessment)

### Cons
- Only 107 patients -- too small for meaningful subgroup analysis
- Multiple comparisons demo doesn't work well (subgroups too small)
- Limited covariates for demonstrating confounding
- Historical context may feel remote to students

### Verdict
Excellent for a 15-minute "history of the RCT" segment or a homework problem, but too small to be the primary teaching dataset.

---

## Other Candidates Considered

### SPRINT Trial (Systolic Blood Pressure Intervention)
- **Pros**: 9,361 patients, recent (2015), clear clinical question, rich covariates, subgroup analyses were controversial
- **Cons**: Not freely available as a CSV (requires NHLBI BioLINCC application, ~2 week approval). Complex composite endpoint. Blood pressure is less dramatic than AIDS.
- **Verdict**: Would be excellent but access barrier makes it impractical for a course dataset.

### COVID-19 Vaccine Trials (Pfizer, Moderna)
- **Pros**: Extremely topical, students have personal experience, dramatic effect sizes
- **Cons**: Individual-level data not publicly available. Published results only. Would need to simulate data or use aggregate tables.
- **Verdict**: Good for discussion/worked examples using published summary statistics, but no downloadable patient-level CSV.

### WHI (Women's Health Initiative)
- **Pros**: Large (16,608 in HRT trial), multiple endpoints, real controversy over subgroup findings
- **Cons**: Requires dbGaP application. Complex study design. Results are nuanced (harm in some outcomes, benefit in others).
- **Verdict**: Too complex for an intro course; access restricted.

---

## Final Recommendation

**Use ACTG 175 as the primary dataset** because it has:
1. Large sample (n=2139) with 4 well-balanced arms
2. Clear, continuous primary outcome (CD4 count change)
3. Unambiguous main result (p ~ 10^-19) that students can discover
4. Rich covariates enabling 20+ subgroup tests for the multiple comparisons lesson
5. Built-in complexity for advanced topics (missing data, censoring, multiple arms)
6. Real clinical stakes (HIV treatment, lives on the line)
7. Freely available, no access restrictions

Use the **streptomycin trial** as a supplementary dataset for historical context and as a simpler homework exercise (n=107, two arms, binary outcome).

---

## Files

| File | Description | Rows | Cols |
|------|-------------|------|------|
| `ACTG175.csv` | ACTG 175 HIV trial data | 2139 | 27 |
| `strep_tb.csv` | 1948 Streptomycin TB trial | 107 | 14 |
| `eda.py` | EDA script with hypothesis tests and visualizations | - | - |
| `eda_plots.png` | 6-panel visualization (boxplots, distributions, permutation test, multiple comparisons) | - | - |
