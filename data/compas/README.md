# COMPAS Recidivism Dataset (ProPublica)

## Source

Downloaded from [github.com/propublica/compas-analysis](https://github.com/propublica/compas-analysis) at commit `bafff5da` on 2026-05-12. The data was compiled by ProPublica for their 2016 *Machine Bias* investigation of the COMPAS risk-scoring algorithm used in pretrial bail decisions in Broward County, Florida.

## Citation

Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). Machine Bias: There's software used across the country to predict future criminals. And it's biased against blacks. *ProPublica*. <https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing>

## License and reuse

The data is derived from Broward County public records obtained via FOIA. ProPublica's analysis page grants reuse for non-commercial research with attribution. Cite ProPublica when using this dataset.

## File

- `compas-scores-two-years.csv` — 7,214 rows × 53 columns, ~2.4 MB. Each row is one defendant who received a COMPAS risk score in Broward County between 2013 and 2014, with a two-year follow-up window for recidivism.

## Key columns

| Column | Meaning |
|---|---|
| `id` | Record ID (numeric; the dataset is **not** de-identified — real names are in `name`, `first`, `last` columns) |
| `name` | Defendant name (public record) |
| `race` | Self-reported race (African-American, Caucasian, Hispanic, Asian, Other, Native American) |
| `sex` | Male / Female |
| `age` | Age at screening |
| `priors_count` | Number of prior arrests at time of screening |
| `juv_fel_count` | Juvenile felony count |
| `juv_misd_count` | Juvenile misdemeanor count |
| `juv_other_count` | Other juvenile offense count |
| `c_charge_degree` | Charge degree (F=felony, M=misdemeanor, O=other) |
| `decile_score` | COMPAS general recidivism risk score (1-10, low to high) |
| `v_decile_score` | COMPAS violent recidivism risk score (1-10) |
| `score_text` | Risk category (Low / Medium / High) |
| `is_recid` | Re-arrested within 2 years (1=yes, 0=no); separate column `two_year_recid` gives the canonical two-year recidivism label used in ProPublica's analysis |
| `two_year_recid` | Recidivism within two years — the canonical target variable in ProPublica's *Machine Bias* analysis |
| `days_b_screening_arrest` | Days between screening and arrest event |

## Standard filter (ProPublica's recipe)

ProPublica's *Machine Bias* analysis applies four filter steps before analysis. On *this* file (`compas-scores-two-years.csv`), only the `days_b_screening_arrest` step removes rows — the other three steps are no-ops because the file ProPublica published here is already partially filtered. We keep all four steps in our standard recipe for parity with ProPublica's published code, even though three of them are no-ops on this file:

```python
df = pd.read_csv('data/compas/compas-scores-two-years.csv')
df = df[(df['days_b_screening_arrest'] <= 30) & (df['days_b_screening_arrest'] >= -30)]
df = df[df['is_recid'] != -1]
df = df[df['c_charge_degree'] != 'O']
df = df[df['score_text'] != 'N/A']
# Result: 6,172 rows
```

## Notes

- **Duplicate column names.** The CSV header lists `decile_score` and `priors_count` twice each (positions 11/39 and 14/48). `pd.read_csv` silently renames the second occurrence to `decile_score.1` and `priors_count.1`. For the general recidivism score and prior count, use the unsuffixed column name; the suffixed columns appear to be ProPublica's join keys from the raw scores file.
- ProPublica's analysis has been discussed and re-analyzed across many follow-up papers (Flores, Bechtel, Lowenkamp 2016; Chouldechova 2017; Corbett-Davies et al. 2017). The dataset is used in Chapter 20 (Fairness) to demonstrate the group-fairness metrics and the Kleinberg-Mullainathan-Raghavan / Chouldechova impossibility theorem numerically; the chapter does not adjudicate whether COMPAS itself is biased, only what each side's claim is and isn't saying.
- Defendant names are kept in the file (they were already public records) but should not be quoted in chapter prose.
