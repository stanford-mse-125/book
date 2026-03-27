# Framingham Heart Study

## Overview

The Framingham Heart Study is one of the most important longitudinal epidemiological studies in history. Begun in 1948, it has followed residents of Framingham, Massachusetts to identify risk factors for cardiovascular disease. This dataset contains a subset used for predicting 10-year risk of coronary heart disease (CHD).

**Use in MSE 125**: Classification homework (logistic regression, model evaluation, class imbalance, confounding).

## Data Source

- **Original study**: [Framingham Heart Study](https://www.framinghamheartstudy.org/)
- **This CSV**: Downloaded from [JishnuMoorthy/Framingham_Heart_Study](https://github.com/JishnuMoorthy/Framingham_Heart_Study) on GitHub (public mirror of the commonly used Kaggle version).

## Schema

| Column | Type | Description |
|--------|------|-------------|
| `male` | int | Sex (1 = male, 0 = female) |
| `age` | int | Age at exam (years, range 32-70) |
| `education` | float | Education level (1 = some HS, 2 = HS/GED, 3 = some college, 4 = college+) |
| `currentSmoker` | int | Currently smoking (1 = yes, 0 = no) |
| `cigsPerDay` | float | Cigarettes smoked per day |
| `BPMeds` | float | On blood pressure medication (1 = yes, 0 = no) |
| `prevalentStroke` | int | History of stroke (1 = yes, 0 = no) |
| `prevalentHyp` | int | Prevalent hypertension (1 = yes, 0 = no) |
| `diabetes` | int | Has diabetes (1 = yes, 0 = no) |
| `totChol` | float | Total cholesterol (mg/dL) |
| `sysBP` | float | Systolic blood pressure (mmHg) |
| `diaBP` | float | Diastolic blood pressure (mmHg) |
| `BMI` | float | Body mass index (kg/m^2) |
| `heartRate` | float | Heart rate (bpm) |
| `glucose` | float | Blood glucose level (mg/dL) |
| `TenYearCHD` | int | **TARGET**: 10-year risk of coronary heart disease (1 = event, 0 = no event) |

## Key Statistics

- **Rows**: 4,240
- **Columns**: 16 (15 features + 1 target)
- **Positive class (CHD)**: 644 (15.2%) -- imbalanced
- **Negative class (no CHD)**: 3,596 (84.8%)
- **Neg:Pos ratio**: 5.6:1

### Missing Data
| Column | Missing % |
|--------|-----------|
| glucose | 9.15% |
| education | 2.48% |
| BPMeds | 1.25% |
| totChol | 1.18% |
| cigsPerDay | 0.68% |
| BMI | 0.45% |
| heartRate | 0.02% |

### Strongest Correlations with CHD
| Feature | Correlation |
|---------|------------|
| age | +0.225 |
| sysBP | +0.216 |
| prevalentHyp | +0.177 |
| diaBP | +0.145 |
| glucose | +0.126 |

### Logistic Regression Baseline
- Accuracy: 0.862
- ROC AUC: 0.726
- The model has very low recall on the positive class (0.14), because the class imbalance biases it toward predicting "no CHD"

## Naive Analysis Traps

1. **Correlated risk factors**: sysBP and diaBP are correlated at r=0.78. BMI, blood pressure, and cholesterol cluster together. A naive model double-counts these overlapping signals. Students should think about multicollinearity.

2. **Confounding by SES**: Education (a proxy for socioeconomic status) is negatively correlated with sysBP (-0.13) and BMI (-0.14). Risk factors are not independent of social context. A naive model ignores this causal structure and may produce misleading feature importances.

3. **Class imbalance**: With only 15.2% positive rate, accuracy is misleading (a "predict all negative" model gets 85%). Students need to use AUC, precision/recall, or resampling.

4. **Missing data patterns**: Glucose is missing for 9% of observations. Missingness may not be random (sicker patients may have had glucose measured more often). Naive deletion can introduce bias.

## Suggested Lecture/HW Uses

- **Logistic regression**: Fit a model, interpret coefficients, compare standardized vs unstandardized
- **Model evaluation**: ROC curves, precision-recall tradeoff, confusion matrix, why accuracy is misleading with imbalanced classes
- **Confounding**: Use DAGs to reason about whether education is a confounder, mediator, or collider
- **Missing data**: Compare complete-case analysis vs imputation
- **Feature selection**: Do all 15 features help? What happens with correlated predictors?
- **Classification threshold**: How does changing the decision threshold affect the precision-recall tradeoff for a clinical screening tool?

## Files

- `framingham.csv` -- the dataset
- `eda.py` -- exploratory data analysis script
- `plots/` -- generated visualizations (class balance, correlations, ROC curve, feature importance, etc.)
