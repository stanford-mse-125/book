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
| `id` | Anonymous defendant ID |
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
| `is_recid` | Re-arrested within 2 years (1=yes, 0=no, -1=missing follow-up) |
| `days_b_screening_arrest` | Days between screening and arrest event |

## Standard filter (ProPublica's recipe)

ProPublica's *Machine Bias* analysis applies these filters before analysis to remove cases with unclear follow-up or non-standard charges. We use the same recipe:

```python
df = pd.read_csv('data/compas/compas-scores-two-years.csv')
df = df[(df['days_b_screening_arrest'] <= 30) & (df['days_b_screening_arrest'] >= -30)]
df = df[df['is_recid'] != -1]
df = df[df['c_charge_degree'] != 'O']
df = df[df['score_text'] != 'N/A']
# Result: 6,172 rows
```

## Notes

- ProPublica's analysis has been discussed and re-analyzed across many follow-up papers (Flores, Bechtel, Lowenkamp 2016; Chouldechova 2017; Corbett-Davies et al. 2017). Our Lec15 use of this dataset is illustrative of a clustering feature-choice lesson, not a definitive claim about whether COMPAS itself is biased.
- Defendant names are kept in the file (they were already public records) but should not be quoted in chapter prose.
