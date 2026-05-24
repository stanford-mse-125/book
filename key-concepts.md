# Key Concepts by Lecture — MSE 125 (Spring 2026)

This document maps each lecture to the course learning objectives it advances, the key concepts students must understand, the vocabulary introduced, prerequisites assumed, and connections to other lectures. It serves as the reference for the `critique-objectives` reviewer.

**Learning objectives** are numbered 1–23 per `docs/course-plan-2026.md`.

Every lecture should end with a **Study guide** section containing: key definitions, key ideas (one sentence each), computational tools (`function_name()` — what it does), and "for the quiz" guidance.

---

## Statistical Aphorisms

These memorable phrases anchor key ideas across the course. Each should appear in the lecture where it's most relevant, attributed properly.

| Aphorism | Attribution | Lecture(s) | Anchors |
|----------|-------------|------------|---------|
| "In God we trust; all others must bring data" | W. Edwards Deming | Lec 1 | Empirical mindset |
| "The best thing about being a statistician is that you get to play in everyone's backyard" | John Tukey | Lec 1 | Why applied stats is fun |
| "All models are wrong, but some are useful" | George Box | Lec 5, 6, 7 | Models as approximations |
| "The combination of some data and an aching desire for an answer does not ensure that a reasonable one can be extracted" | John Tukey | Lec 3 | AI gotchas — AI always produces *something* |
| "Far better an approximate answer to the right question, which is often vague, than an exact answer to the wrong question, which can always be made precise" | John Tukey | Lec 1, 17 | Framing matters more than precision |
| "If you torture the data long enough, it will confess to anything" | Ronald Coase | Lec 11 | Multiple testing / p-hacking |
| "No amount of experimentation can ever prove me right; a single experiment can prove me wrong" | (attr. Einstein) | Lec 10 | Reject or fail to reject — never "prove" |
| "With four parameters I can fit an elephant, and with five I can make him wiggle his trunk" | John von Neumann | Lec 6 | Overfitting / bias-variance |
| "Prediction is very difficult, especially about the future" | Niels Bohr (attr.) | Lec 16 | Backtesting / non-stationarity |
| "Correlation is not causation" | (common) | Lec 11, 18 | Confounding |
| "Wisdom of the crowd, even of overfit trees" | (course) | Lec 13 | Bagging / variance reduction |

---

## Lecture 1: Introduction

**Objectives addressed:** 1 (explore/visualize), 3 (evaluate AI analyses), 20 (AI failure modes)

**Key concepts:**
- Applied statistics = decisions under uncertainty
- Three course themes: explore & model, test & decide, complex models
- Consequential decisions: hospital fines, Airbnb pricing, drug approval, sports betting
- First look at real, messy data — what AI gets right and wrong
- Missing data as a signal, not just a nuisance ("Too Few to Report")

**Key vocabulary:**
- Applied statistics
- Excess Readmission Ratio (ERR)
- "Too Few to Report" (missing data mechanism)

**Prerequisites:** None (first lecture)

**Connections:**
- Forward: Lec 2 (deep EDA on same datasets), Lec 3 (AI gotchas), Lec 18 (Simpson's paradox in hospital data revisited causally)

**Aphorisms:** "In God we trust; all others must bring data" (Deming); "The best thing about being a statistician is that you get to play in everyone's backyard" (Tukey); "Far better an approximate answer to the right question..." (Tukey)

**Surprise moment:** ~15% of hospital data is "Too Few to Report" — AI silently drops it

---

## Lecture 2: EDA & Visualization

**Objectives addressed:** 1 (explore/visualize, outliers, missing data), 22 (reports with visualizations)

**Key concepts:**
- EDA workflow: shape → types → distributions → missing data
- Histograms, box plots, scatter plots — choosing the right plot for the question
- Identifying outliers (Airbnb $10k/night listings)
- Missing data patterns: MNAR vs. random missingness
- Summary statistics can mislead (Anscombe's quartet idea)

**Key vocabulary:**
- Exploratory Data Analysis (EDA)
- Data types: continuous, discrete, nominal/categorical, ordinal, text, identifier
- Semantic type vs. storage type (dtype)
- Missing Not At Random (MNAR)
- Distribution, histogram, box plot, scatter plot
- Outlier

**Prerequisites:** Basic Python (CS 106A)

**Connections:**
- Backward: Lec 1 (hospital and Airbnb datasets introduced)
- Forward: Lec 3 (cleaning what we found), Lec 5 (Airbnb regression)
- ORIE 4741: EDA lecture opens with "always visualize before modeling" (Anscombe's quartet)

**Surprise moment:** Naive hospital rankings penalize hospitals treating sicker patients — the "worst" hospitals by raw readmission rates are often performing at or below expectations after adjusting for patient mix (confounding by severity)

---

## Lecture 3: Data Munging + AI Gotchas

**Objectives addressed:** 2 (clean/transform/join), 3 (evaluate AI analyses), 20 (AI failure modes)

**Key concepts:**
- Joins: inner vs. left join and when each is appropriate
- Missing data strategies: drop, impute with mean, leave as NaN — each changes the answer
- Type conversions (strings to numbers, dates, categoricals mistaken for numerics)
- Missing data patterns: MCAR, MAR, MNAR — MNAR is the hardest to handle
- Informative missingness: the absence of data itself carries a signal
- Data leakage: features that encode the target by construction
- AI failure modes in data cleaning: silently dropping rows, wrong metric, data leakage, treating categoricals as numbers
- Missingness is unevenly distributed across groups → biased comparisons

**Key vocabulary:**
- Inner join, left join, join key
- Data munging / wrangling
- Mean imputation
- Selection bias (from dropping rows)
- Informative missingness
- MCAR, MAR, MNAR
- Data leakage

**Prerequisites:** CS 106A (basic Python, pandas intro)

**Connections:**
- Backward: Lec 2 (found the mess), Lec 1 (hospital data)
- Forward: Lec 5 (missingness indicators as features), Lec 13 (trees handle missing values natively)
- ORIE 4741: Feature engineering lecture covers informative vs. uninformative missingness

**Surprise moment:** Missing data is unevenly distributed across hospital ownership types — group comparisons are biased

---

## Lecture 4: From the Mean to Simple Regression

**Objectives addressed:** 4 (vectors, linear combinations, span), 5 (regression as projection — simple case)

**Key concepts:**
- Two views of a dataset: rows as points in R^d, columns as vectors in R^n
- Visualizing high-dimensional column vectors via index plots (value vs sorted index)
- Norms measure vector length and prediction error
- Predicting with a constant: the mean minimizes squared error; the median minimizes absolute error
- Residuals sum to zero: 1^T ε = 0 (the first "normal equation")
- Linear combinations of feature vectors produce predictions
- Span of {1, x} = set of all reachable lines through the data
- Inner products measure how aligned two vectors are
- Orthogonality is the optimality condition: residual ⊥ every feature vector
- Simple regression as projection onto span{1, x}
- R² as fraction of variance explained
- R² = cos²θ (Pythagorean decomposition)
- R² = r² in simple regression
- Regression to the mean (Galton's heights)

**Key vocabulary:**
- Vector, scalar
- Norm, distance
- Linear combination, span
- Inner product, dot product
- Orthogonal
- Residual, projection
- Linear function
- R-squared (R²)
- Cosine similarity
- Coefficient interpretation
- Regression to the mean

**Key formulas:**
- ŷ = β₀ (mean model) → ŷ = β₀ + β₁x (simple regression)
- ε = y − ŷ (residual)
- 1^T ε = 0, x^T ε = 0 (orthogonality conditions)
- R² = 1 − ||ε||²/||y − ȳ||²
- R² = cos²θ (angle between centered y and centered ŷ)

**Prerequisites:** MS&E 120 (vectors as random variables); some students have EE103/CME103 (VMLS)

**Connections:**
- Forward: Lec 5 (multiple regression, normal equations, feature engineering), Lec 14 (PCA as finding optimal column space)
- VMLS: Ch 1 (vectors), Ch 13 (least squares)
- ORIE 4741: linear.tex uses column space framing for least squares

**Surprise moment:** The mean-and-feature principle generalizes — adding one feature is just the mean model with one more orthogonality condition. "Normal equations" already appeared when we minimized squared error with no features.

---

## Lecture 5: Multiple Regression and Feature Engineering

**Objectives addressed:** 5 (regression as projection — matrix form), 12 (feature engineering)

**Key concepts:**
- Multiple regression generalizes simple regression: stack orthogonality conditions into X^T ε = 0
- Column space of X = set of all reachable predictions (generalizes span from Lec 4)
- Normal equations: β = (X^T X)^{-1} X^T y
- "Holding constant" interpretation of coefficients in multiple regression
- One-hot encoding: categorical variables → binary indicator columns
- Reference level: drop one category; others interpreted relative to it
- "Linear in parameters, not features": the design matrix can be built from any transformation of the raw data
- Interaction terms: when one feature's effect depends on another
- Missing values as features (missingness indicator)
- Log transforms on y change coefficient interpretation (percentage vs dollar); motivated by proportional structure in the data and by the fat right tail of the response
- Four log-transform combinations (level-level, log-level, level-log, log-log)
- Adjusted R²: penalizing complexity
- Multicollinearity: nearly parallel features create unstable coefficients
- Residual diagnostics: reading fan / curve / cluster patterns as evidence of missing model structure

**Key vocabulary:**
- Column space, multiple regression
- Normal equations, matrix form
- One-hot encoding, reference level, indicator variable
- Feature engineering
- Interaction term
- Log transform, elasticity
- Adjusted R-squared
- Multicollinearity
- Residual diagnostics

**Key formulas:**
- ŷ = Xβ (matrix form)
- X^T ε = 0 (stacked orthogonality conditions)
- β = (X^T X)^{-1} X^T y (normal equations)

**Prerequisites:** Lec 4 (simple regression, span, orthogonality, inner product, R²)

**Connections:**
- Backward: Lec 4 (single-feature version of everything here)
- Forward: Lec 6 (validation — train/test R²), Lec 13 (trees as automatic feature engineering), Lec 12 (which features are statistically significant?), Lec 18 (when is a coefficient causal?)
- VMLS: Ch 5 (linear independence), Ch 13 (least squares)

**Surprise moment:** The fat-tail clue — top 5% of listings contribute ~48% of the level model's squared error budget, almost ten times their fair share. A naive least-squares fit spends most of its attention on a tail it can't predict anyway, and the log transform is the fix.

---

## Lecture 6: Validation and the Bias-Variance Tradeoff

**Objectives addressed:** 11 (train/test/validate model selection)

**Key concepts:**
- Distribution shift: training data ≠ deployment data (covariate, temporal, label shift)
- Train/test split: evaluate on held-out data that simulates new observations from the same distribution
- Train R² vs test R²: fit vs generalization; the gap reveals overfitting
- Three-way split: train (fit) / validation (choose complexity) / test (report final performance)
- Cross-validation (k-fold): rotate the held-out fold for stable estimates
- Overfitting: training performance improves but test performance degrades
- Bias-variance tradeoff:
  - **Mathematical:** Bias(x) = E[f̂(x)] - f(x); Variance(x) = E[(f̂(x) - E[f̂(x)])²]; MSE = Bias² + Variance + σ²
  - **Classical (primary):** More complexity → eventually overfitting. The U-shaped test error curve.
  - **Modern (trees/bagging):** Averaging many overfit trees reduces variance. More trees never hurts.
  - **Punchline:** "Regularize and cross-validate" is more right than ever.
- Synthetic demo: line (high bias, low variance) vs degree-4 polynomial (low bias, high variance) on quadratic data
- Lasso (L1 regularization): automatic feature selection by shrinking coefficients to zero
- Ridge (L2 regularization): shrinks all coefficients but keeps them nonzero

**Key vocabulary:**
- Distribution shift (covariate, temporal, label)
- Train/test split, train R², test R²
- Three-way split (train/validation/test)
- Cross-validation (k-fold)
- Overfitting, underfitting
- f(x) (true function), f̂(x) (model prediction)
- Bias, variance, irreducible noise (σ²)
- Bias-variance tradeoff
- Lasso, Ridge, regularization

**Prerequisites:** Lec 5 (feature engineering: interactions, log transforms, residual diagnostics)

**Connections:**
- Backward: Lec 5 (polynomial overfitting motivates validation)
- Forward: Lec 13 (trees apply CV for depth selection), Lec 8 (can we trust our estimates?), Lec 12 (regression inference), Lec 16 (temporal validation breaks random splitting)

**Aphorisms:** "With four parameters I can fit an elephant, and with five I can make him wiggle his trunk" (von Neumann); "All models are wrong, but some are useful" (Box)

**Surprise moment:** The most complex model (degree-5 polynomial interactions, 1286 features for 300 training points) achieves test R² of -3.4, dramatically worse than predicting the mean.

**Study guide scope:** Students are responsible for classical bias-variance (the U-shape and the decomposition formula), overfitting concept, train/test split (what it simulates, when it breaks), three-way split (why validation is separate from test), cross-validation, Lasso and Ridge concepts. They should understand *that* averaging overfit trees works but are NOT responsible for the mathematical details of why.

---

## Lecture 7: Classification (Logistic Regression + Metrics)

**Objectives addressed:** 13 (logistic regression, classification metrics — precision, recall, ROC)

**Key concepts:**
- Binary classification: predicting categories, not quantities
- Logistic regression: sigmoid function maps linear combination to probability
- Odds and odds ratios: exp(βⱼ) = multiplicative change in odds per unit increase in xⱼ
- Gradient descent: how logistic regression coefficients are estimated (no closed-form solution)
  - The hiking metaphor: always walk downhill; reach the bottom of the valley
  - When it works: convex loss landscapes (logistic regression — one basin)
  - When it can fail: non-convex landscapes (neural networks — multiple basins, local minima)
  - Computational perspective: show the algorithm, run it, watch it converge
  - Good candidate for a homework problem
- Class imbalance: why accuracy is misleading when one class dominates
- Confusion matrix: TP, FP, TN, FN
- Precision (of those you predicted positive, how many are?) and recall (of actual positives, how many did you catch?)
- ROC curve and AUC: performance across all thresholds
- Threshold selection depends on the cost of errors ($$ decision)
- Calibration: do predicted probabilities match observed frequencies? (calibration plot, diagonal = perfect)

**Key vocabulary:**
- Logistic regression, sigmoid function
- Odds, odds ratio, log-odds (logit)
- Gradient descent, loss landscape, learning rate, convergence
- Local minimum, global minimum (for non-convex problems)
- Class imbalance, accuracy trap / accuracy paradox
- Positive class (coded 1) vs. negative class (coded 0) — terminology from medical testing, not desirability
- Confusion matrix
- True positive, false positive, true negative, false negative
- Precision, recall, F1 score
- ROC curve, AUC (Area Under Curve)
- Threshold
- Calibration, calibration plot

**Key formulas:**
- Sigmoid: p = 1 / (1 + e^(−z)) where z = β₀ + β₁x₁ + ⋯
- Logit (inverse sigmoid): log(p/(1−p)) = β₀ + β₁x₁ + ⋯
- Odds ratio: exp(βⱼ) = how odds multiply per unit increase in xⱼ
- Gradient descent update: β ← β − η · ∇L(β)
- ORIE 4741: logistic loss = log(1 + exp(−y·w^T x)) — connects to ERM framework

**Prerequisites:** Lec 4-6 (regression, feature engineering, validation)

**Connections:**
- Backward: Lec 4-5 (regression — OLS has closed form; logistic does not), Lec 6 (train/test, validation — apply to classification)
- Forward: Lec 12 (inference on logistic coefficients — z-tests, CIs on odds ratios), Lec 13 (classification trees — trees handle both regression and classification), Lec 17 (gradient boosting uses gradient descent ideas)
- ORIE 4741: losses.tex — logistic loss section

**Surprise moment:** Overall AUC ~0.75 hides dramatic failures in subgroups — the under-40 AUC is ~0.36 (below 0.5, worse than random; the tiny positive class makes the estimate noisy, but the direction stands)

---

## Lecture 8: Bootstrap and the Normal Approximation

**Objectives addressed:** 6 (sampling distributions, CLT, connection to MS&E 120), 7 (bootstrap CIs)

**Key concepts:**
- Estimand, estimator, estimate: the quantity you want, the procedure, the number you get
- Bootstrap procedure: resample with replacement, compute statistic, repeat
- Bootstrap CI (percentile method): middle 95% of bootstrap distribution
- Key observation: bootstrap distributions often look normal → CLT explains why
- Central Limit Theorem (from MS&E 120): sample means are approximately Normal(μ, σ/√n)
- Normal approximation: mean ± 1.96·SE instead of 10,000 resamples
- Advantages of normal approximation: speed, less code, analytical (power formulas), composable
- When normal approximation fails: heavy tails, small n, non-mean statistics (median), skewed data
- LLN vs CLT: "LLN says the mean converges; CLT says how fast and in what shape"
- Bootstrap for regression coefficients (brief demo — full treatment in Lec 12)

**Key vocabulary:**
- Estimand, estimator, estimate (point estimate)
- Bootstrap (resample with replacement)
- Confidence interval (percentile method)
- Central Limit Theorem (CLT)
- Standard error (SE = σ/√n for the mean)
- Normal approximation
- Sampling distribution

**Key formulas:**
- 95% Bootstrap CI = [q₀.₀₂₅, q₀.₉₇₅] of bootstrap distribution
- CLT: X̄ₙ ≈ Normal(μ, σ/√n)
- Normal CI: X̄ ± 1.96 · SE

**Prerequisites:** Lec 5 (regression — for bootstrap regression demo); MS&E 120 (probability, LLN, CLT statement)

**Connections:**
- Backward: MS&E 120 (CLT, LLN), Lec 5 (regression)
- Forward: Lec 9 (permutation tests), Lec 10 (formal hypothesis testing), Lec 12 (bootstrap vs formula CIs for regression)

**Surprise moment:** Bootstrap and normal CIs agree perfectly for the mean — but for the median, no formula exists, and the bootstrap is the only option

---

## Lecture 9: Permutation Tests

**Objectives addressed:** 8 (hypotheses, p-values, simulation)

**Key concepts:**
- Permutation test: shuffle group labels to simulate the null hypothesis
- Null distribution: what the test statistic looks like when H₀ is true
- p-value: probability of a result this extreme under H₀
- Two-sided test: |observed| vs |permuted|
- One-sided test: one tail only, with the direction chosen *before* seeing the data; default to two-sided when in doubt
- Exchangeability under the null: random assignment makes labels exchangeable under H₀
- Association vs. causation: random assignment (ACTG 175) licenses causal claims; observational comparisons (NBA home/away) detect differences but cannot decompose the confounded mechanisms
- Connection: bootstrap (Lec 8) = precision of estimate; permutation = significance of effect
- Conservative p-value estimator: (count + 1) / (n_perms + 1) (Phipson & Smyth 2010)

**Key vocabulary:**
- Permutation test (shuffle labels)
- Null distribution
- Null hypothesis (informal — formalized in Lec 10)
- p-value
- Exchangeability
- One-sided / two-sided tests
- Simulation-based inference

**Running examples:**
- ACTG 175 clinical trial (randomized → causal interpretation)
- Deflategate (narrative motivation for the one-sided test; no worked computation)
- NBA home-court scoring advantage, 2021–24 (observational → association, not causation; forward link to Ch 18)

**Prerequisites:** Lec 8 (bootstrap — students know resampling)

**Connections:**
- Backward: Lec 8 (bootstrap)
- Forward: Lec 10 (formal hypothesis testing framework), Lec 11 (multiple testing), Ch 18 (causal inference)

**Surprise moment:** None of 10,000 permutations produce an effect as large as observed — the drug works

---

## Lecture 10: Hypothesis Testing Framework

**Objectives addressed:** 8 (hypotheses, p-values, simulation, interpretation)

**Key concepts:**
- Formal framework: null hypothesis H₀, alternative hypothesis H₁
- Test statistic (e.g., difference in means, t-statistic)
- Significance level α: the false positive rate you're willing to accept
- Type I error (false positive) and Type II error (false negative)
- Power = 1 − P(Type II error) — ability to detect a real effect
- p-value distribution under H₀ is Uniform(0,1)
- CI/hypothesis test duality: a 95% CI excluding $\theta_0$ ↔ two-sided test of $\theta = \theta_0$ rejecting at α = 0.05
- Statistical significance ≠ practical importance
- $$ decision: what significance level is appropriate given the stakes?
- Chi-squared test for categorical data: goodness of fit and independence
- Power analysis (conceptual + computational, not formula derivation):
  - Power = probability of detecting a real effect
  - Bigger sample → more power; bigger effect → easier to detect
  - Simulate power curves (don't derive formulas)
  - Use `statsmodels.stats.power` for practical planning
  - $$ hook: "Before running a $2M clinical trial, you should know if you have enough patients"
  - Good HW problem: "How many users do you need for an A/B test?"

**Key vocabulary:**
- Null hypothesis (H₀), alternative hypothesis (H₁)
- Test statistic, t-statistic, Welch's t-test
- Significance level (α)
- Type I error, Type II error
- Power, power analysis, sample size planning
- p-value
- Chi-squared test, chi-squared distribution
- CI/hypothesis test duality

**Key formulas:**
- Welch's t-test statistic
- Power = 1 − β
- Chi-squared statistic: Σ (observed − expected)² / expected

**Prerequisites:** Lec 9 (permutation test, p-value intuition); MS&E 120 (probability)

**Connections:**
- Backward: Lec 9 (simulation-based p-values)
- Forward: Lec 11 (what happens when you run many tests), Lec 12 (hypothesis tests on regression coefficients)
- $$ hook: Should we approve this drug? What α is appropriate when lives are at stake?

**Aphorism:** "No amount of experimentation can ever prove me right; a single experiment can prove me wrong" (attr. Einstein) — you reject or fail to reject, never "prove"

**Surprise moment:** With n=2139 in ACTG 175, even tiny clinically meaningless effects are "significant" — statistical significance ≠ importance

---

## Lecture 11: Multiple Testing

**Objectives addressed:** 9 (multiple testing — Bonferroni, FDR)

**Key concepts:**
- The multiple testing problem: run m tests at α=0.05, expect ~m×0.05 false positives
- p-value histogram as diagnostic: uniform under H₀, spike near 0 if signal exists
- Bonferroni correction: test at α/m (controls family-wise error rate)
- False Discovery Rate (FDR): proportion of discoveries that are false
- Benjamini-Hochberg procedure: controls FDR
- Correlation ≠ causation — confounders (coaching decisions) create spurious patterns
- Simpson's paradox: aggregate trend reverses within subgroups

**Key vocabulary:**
- Multiple testing / multiple comparisons
- Family-wise error rate (FWER)
- False Discovery Rate (FDR)
- Bonferroni correction
- Benjamini-Hochberg procedure
- p-value histogram
- Simpson's paradox
- Correlation, confounding
- Pearson correlation (r)
- Ecological correlation fallacy
- Reproducibility crisis
- p-hacking, researcher degrees of freedom
- Pre-registration
- File drawer problem

**Key formulas:**
- Expected false positives = m × α
- Bonferroni threshold = α/m
- BH procedure: order p-values, find largest k where p_(k) ≤ (k/m) × q

**Prerequisites:** Lec 10 (hypothesis testing, p-values, Type I error)

**Connections:**
- Backward: Lec 10 (hypothesis testing)
- Forward: Lec 12 (regression inference — are coefficients "significant"?), Lec 18 (confounding formalized via DAGs)
- $$ hook: NBA analytics intern runs 317 shooter-vs-league tests; 141 reject at α = 0.05 — but ~16 are expected by chance under H₀ for everyone

**Aphorisms:** "If you torture the data long enough, it will confess to anything" (Coase); "Correlation is not causation"

**Surprise moment:** Simpson's paradox in NBA shot-zone data — Aaron Gordon outshoots Klay Thompson aggregate (55.7% vs 43.3%) but is *worse* zone-by-zone, because Gordon takes 65% of his shots from the restricted area (league avg 67%) while Thompson takes 53% from above-the-break threes (league avg 36%). Where you shoot dominates how well you shoot.

---

## Lecture 12: Regression Inference + Diagnostics

**Objectives addressed:** 10 (regression coefficient inference), 11 (evaluate models), 17 (regression causal vs. predictive)

**Key concepts:**
- Residual plots: the primary diagnostic for model validity (moved from old Lec 6)
- Heteroscedasticity: fan-shaped residuals mean unequal variance
- Q-Q plot: checking normality of residuals
- Inference and diagnostics together: same regression, two questions — is each coefficient distinguishable from noise (inference), and are the assumptions that justified the inference satisfied (diagnostics)
- Bootstrap CIs for regression coefficients (callback to Lec 8): resample rows, refit, collect β̂
- Formula-based CIs: t-distribution with n − p − 1 df
- When bootstrap and formula CIs agree (normal residuals) and disagree (heavy tails, heteroscedasticity)
- Prediction interval vs confidence interval for the mean
- t-test for coefficients: H₀: βⱼ = 0
- Step-by-step model building: watch coefficients change
- "Controlling for" / "holding constant" interpretation
- Practical significance vs statistical significance (Cohen's d)

**Key vocabulary:**
- Residual plot
- Heteroscedasticity
- Q-Q plot
- t-test (coefficient)
- Standard error (of a coefficient)
- "Controlling for" / "holding constant"
- Practical significance, effect size, Cohen's d
- Prediction interval

**Key formulas:**
- t = β̂ⱼ / SE(β̂ⱼ), with n − p − 1 degrees of freedom

**Prerequisites:** Lec 5 (regression, residuals), Lec 8 (bootstrap), Lec 10-11 (hypothesis testing, multiple testing)

**Connections:**
- Backward: Lec 5 (regression fitting), Lec 8 (bootstrap), Lec 10 (hypothesis testing), Lec 11 (multiple testing)
- Forward: Ch 12.5 (classification meets inference — bootstrap CI for AUC, logistic coefficient tests), Lec 13 (trees apply regression and classification), Lec 18 (when does regression estimate a causal effect?)
- Bridges Acts 1 and 2: combines modeling (regression from Act 1) with inference (testing from Act 2)

**Surprise moment:** Same machinery, two regressions, two very different conclusions. The Airbnb bathroom premium is statistically significant *and* practically meaningful (~$60/night, decision-grade). The NBA REST_DAYS coefficient is statistically significant at p < 0.001 *yet* the standardized effect is essentially zero — a textbook demonstration that with n in the tens of thousands, "significant" stops meaning "important."

---

## Chapter 12.5: Classification Meets Inference (optional)

**Objectives addressed:** 7 (bootstrap CIs), 8 (hypothesis tests), 9 (multiple testing), 13 (classification metrics)

**Key concepts:**
- Bootstrap CI for AUC
- Permutation test for classifier vs. random guessing
- Logistic coefficient hypothesis tests and odds ratio CIs (reinforces Lec 12)
- Multiple testing in feature selection (BH correction)
- Confounding in classification (Simpson's paradox for logistic regression)

**Prerequisites:** Lec 7 (classification), Lec 8-12 (all inference tools)

**Connections:**
- Backward: Lec 7 (classification model, calibration), Lec 8 (bootstrap), Lec 9 (permutation), Lec 10-11 (hypothesis testing, multiple testing), Lec 12 (regression inference)
- Forward: Lec 13 (students can apply these tools to tree-based classifiers)

---

## Lecture 13: Decision Trees and Random Forests

**Objectives addressed:** 12 (feature engineering — automatic)

**Key concepts:**
- Decision trees: recursive splitting finds patterns without manual feature engineering
- Trees handle categories and missing data natively
- A single deep tree overfits: perfect training score, poor test score
- Random forests: average many overfit trees for stable predictions
- Bagging + feature subsampling
- More trees never hurts (unlike more polynomial features)
- Feature importance: which variables does the forest rely on?
- Cross-validation for tree depth selection (applying Ch 6 framework)

**Key vocabulary:**
- Decision tree, recursive splitting
- Overfitting (single tree)
- Random forest, bagging
- Feature subsampling
- Feature importance (MDI)

**Prerequisites:** Lec 5 (feature engineering), Lec 6 (train/test, CV, bias-variance), Lec 7 (classification — students know logistic regression, confusion matrix, precision/recall, ROC)

**Connections:**
- Backward: Lec 5 (manual feature engineering — trees automate this), Lec 6 (validation, bias-variance tradeoff — trees apply these concepts), Lec 7 (classification — trees handle both regression and classification; the 2×2 matrix payoff)
- Forward: Lec 17 (AutoML; gradient boosting deepens tree ideas)
- ORIE 4741: trees material

**Surprise moment:** A single deep tree gets perfect training R² but terrible test R². Average 100 of them and test R² beats everything.

**Aphorism:** "Wisdom of the crowd, even of overfit trees" (course) — anchors bagging / variance reduction.

---

## Lecture 14: PCA / Dimensionality Reduction

**Objectives addressed:** 14 (PCA, interpret principal components)

**Key concepts:**
- Dimensionality reduction: many features → fewer meaningful dimensions
- PCA finds directions of maximum variance
- SVD decomposition: X ≈ USV^T
- Explained variance ratio and scree plot for choosing number of components
- Loadings: which original features contribute to each PC
- Standardization is essential before PCA (otherwise largest-magnitude column dominates)
- PCA as regression onto optimal covariates (the ORIE 4741 framing)

**Key vocabulary:**
- PCA (Principal Component Analysis)
- Principal component, loading
- SVD (Singular Value Decomposition)
- Singular value
- Explained variance ratio
- Scree plot, elbow method
- Standardization (z-score)
- Basis, orthonormal basis

**Key formulas:**
- SVD: X = USV^T
- Columns of V = PC directions
- Diagonal of S = singular values (proportional to variance explained)
- US = PC scores (coordinates in reduced space)
- Eckart-Young-Mirsky: SVD gives the best rank-r approximation

**Prerequisites:** Lec 4 (column space, projection); Lec 5 (projection idea)

**Connections:**
- Backward: Lec 4 (column space), Lec 5 (projection)
- Forward: Lec 15 (clustering after dimensionality reduction)
- VMLS Ch 16 (PCA)
- ORIE 4741: unsupervised.tex — PCA as low-rank approximation, GLRM framework (PCA as special case)

**Surprise moment:** PCA on raw (unstandardized) Airbnb data just picks up maximum_nights — standardization completely changes the results

**Alternative chapter versions** (not in main book, kept for 2027 reconsideration):
- `lec14alt-pca-finance.qmd` — equity factor model on S&P 100 returns; pairs with current slide deck `slides/lec14-pca.qmd`
- `lec14alt-pca-embedding.qmd` — text embedding visualization (BERT-style)

---

## Lecture 15: Clustering (K-Means)

**Objectives addressed:** 15 (k-means, evaluate cluster quality)

**Dataset:** NBA shot zones 2023-24 (`data/nba/shot_zones_2023-24.csv`) — 317 players with ≥200 FGA, shot-mix percentages by court zone. Four published case studies in "Clustering in the wild" carry their own datasets (Tabula Muris cell atlas; Haldar asthma cohorts; Drysdale/Dinga fMRI depression; Garcia-Dias APOGEE stellar spectra).

**Key concepts:**
- Unsupervised learning: finding structure without labels
- K-means algorithm: assign points to nearest centroid, recompute centroids, repeat; objective is SSE (sum of squared errors)
- Standardization is the default for distance-based methods like k-means — same reason as PCA
- Elbow and silhouette plots rule out bad k choices; they don't uniquely pick the right one
- Given cluster profiles (shot-mix archetypes), name interpretable types and identify players who cross traditional position lines
- Feature selection changes which clusters emerge — feature choice is a values judgment, not a neutral preprocessing step
- Assessing cluster stability across random seeds using ARI; k-means++ initialization reduces sensitivity
- Hierarchical clustering as a complement to k-means when the right k is unclear; Ward linkage is the SSE-consistent choice
- ARI as a comparison metric: across seeds, across feature sets, across algorithms
- **PCA → k-means as a common pipeline:** standardize → PCA to a small orthogonal basis (Ch 14) → k-means on the PC scores. Stabilizes distance computation in high-dimensional / collinear settings. Tabula Muris is the marquee published example.
- **Four published case studies (good / bad / mixed):**
  - *Tabula Muris* (Nature 2018) — PCA + graph-based clustering on n=100,605 cells × 20 mouse organs, validated against curated marker genes (the success case).
  - *Haldar et al.* (AJRCCM 2008) — Ward's hierarchical → k-means on three asthma cohorts; discordance changed which drug patients should get.
  - *Drysdale 2017 / Dinga 2019* (Nat Med / NeuroImage Clin) — four "biotypes" of depression failed independent replication; chapter's new cautionary case.
  - *Garcia-Dias et al.* (A&A 2018) — k-means on n=153,847 APOGEE stellar spectra; mixed result — the similarity metric matters as much as the algorithm.

**Key vocabulary:**
- Unsupervised learning
- K-means
- Centroid
- Sum of squared errors (SSE)
- Silhouette score
- Elbow method
- Local optimum
- Adjusted Rand Index (ARI)
- K-means++ initialization
- Hierarchical clustering
- Dendrogram
- Ward linkage
- PCA → k-means pipeline

**Key formulas:**
- K-means objective: minimize Σ_k Σ_{i∈C_k} ||x_i − μ_k||² (SSE)

**Computational tools:**
- `sklearn.cluster.KMeans`, `sklearn.metrics.silhouette_score`, `sklearn.metrics.silhouette_samples`, `sklearn.metrics.adjusted_rand_score`
- `scipy.cluster.hierarchy.linkage`, `scipy.cluster.hierarchy.dendrogram`, `scipy.cluster.hierarchy.fcluster`

**Prerequisites:** Lec 2 (EDA), Lec 4 (regression — for SSE intuition), Lec 14 (PCA — for unsupervised framing, standardization, and the PCA→k-means pipeline)

**Connections:**
- Backward: Lec 2 (EDA), Lec 4 (SSE), Lec 14 (PCA, standardization, unsupervised framing; PCA→k-means recipe)
- Forward: Lec 17 (working with AI — feature-choice stakes revisited), Lec 18-19 (causal inference — when correlational groupings mislead), Lec 20 (algorithmic fairness builds on the "feature choice is values choice" thread)

**Surprise moment(s):** (1) Clustered shot profiles reveal players who defy traditional position labels — analytics archetypes cut across PG/SG/SF/PF/C. (2) Changing which features enter k-means shifts cluster membership substantially — pairwise ARI between shot-mix / volume / efficiency clusterings drops near zero (≈0.05), an order of magnitude below the cross-seed mean (≈0.62), so feature choice scrambles membership *more* than random initialization does. (3) The Drysdale 2017 fMRI "biotypes" of depression — four visually compelling clusters with claimed 82–93% sensitivity/specificity — failed independent replication in Dinga 2019: canonical-correlation permutation p-values of 0.64 and 0.99, held-out cross-validated correlations near zero.

---

## Lecture 16: When Validation Isn't Enough (Feedback Loops, Leakage, Goodhart)

**Objectives addressed:** 11 (train/test/validate — temporal version), 12 (lag features), 20 (AI failure modes — feedback loops + Goodhart), plus new: recognize when a validated model will fail in deployment

**Key concepts:**
- Four deployment-failure modes: temporal leakage, distribution shift, feedback loops, Goodhart's law
- Temporal structure means random train/test split leaks future information
- Temporal split (backtesting): train on past, test on future
- Lag features: use past values as features for the present
- Walk-forward validation: expanding or sliding window
- Distribution shift: future data may not resemble past data
- Prediction intervals via bootstrap residual resampling
- Feedback loops: when a model's predictions change the outcome distribution (predictive policing, credit scoring, sepsis alerts, betting markets)
- Weapons of Math Destruction: unmeasurable outcome + negative consequences + self-fulfilling loop
- Goodhart's law: when a measure becomes a target, it ceases to be a good measure
- Overfitting as the ML reading of Goodhart: training loss is a proxy for test loss; hard optimization breaks the proxy
- Proxy-vs-outcome auditing: for every metric, write down the goal it's a proxy for
- Pre-deployment defenses: split by the right axis, simulate the deployed action, audit proxy-vs-outcome, stress-test tails
- Post-deployment defenses: monitor drift, hold out a control, A/B test changes

**Key vocabulary:**
- Temporal split, backtesting, walk-forward validation
- Data leakage (temporal)
- Lag features
- Distribution shift
- Prediction interval
- Feedback loop, performative prediction
- Weapon of Math Destruction (WMD)
- Goodhart's law
- Proxy, proxy-vs-outcome
- Drift monitoring, control holdout

**Prerequisites:** Lec 5 (feature engineering), Lec 6 (train/test split, cross-validation, distribution shift preview), Lec 10 (p-hacking — a special case of Goodhart)

**Connections:**
- Backward: Lec 5 (feature engineering), Lec 6 (train/test, cross-validation, overfitting as Goodhart, distribution shift preview), Lec 10 (p-hacking as Goodhart)
- Forward: Lec 17 (the "incentives and dynamics" cluster of the critical-evaluation checklist — Goodhart and feedback loops — points back here), Lec 18 (feedback loops as causal structure — the DAG view)
- FPP3 Ch 5 (the forecasting toolbox — train/test for time series)
- Cathy O'Neil, *Weapons of Math Destruction* — feedback loops + WMD framework
- ORIE 4741: feature_engineering.tex (AR, ARMA); train-test-validate.tex ("can't randomly split time series"); fairness.tex (COMPAS, feedback loops in social contexts)

**Aphorism:** "When a measure becomes a target, it ceases to be a good measure" (Goodhart); "Prediction is very difficult, especially about the future" (attr. Bohr)

**Surprise moment:** The training-loss / test-loss divergence students saw in Chapter 6 is the same phenomenon as hospitals gaming readmission penalties and VW cheating emissions tests — all are Goodhart's law

---

## Lecture 17: Working with AI

**Objectives addressed:** 3 (evaluate AI analyses), 19 (AI coding assistants), 20 (AI failure modes), 21 (prompt decomposition)

**Datasets:** Airbnb (TabPFN demo); College Scorecard (selection bias worked example); NBA rest days (Simpson's paradox worked example).

**Key concepts:**
- **Gradient boosting** as the workhorse model AutoML reaches for first. Sequential error-correction = gradient descent in function space (bridge to Ch 7); the algorithm behind XGBoost / LightGBM / CatBoost. (Ch 13 owns trees/forests/bagging and explicitly defers gradient boosting here; lec13:495.)
- **CASH** (combined algorithm selection and hyperparameter optimization) — fold "which algorithm" into a top-level categorical hyperparameter; minimize cross-validated loss. Frame: "AutoML automates the model+hyperparameter loop you already do by hand." (Auto-WEKA, Thornton et al. KDD 2013.)
- **AutoGluon wins tabular benchmarks by ensembling + multi-layer stacking, not by cleverer search** (AMLB, Gijsbers et al. JMLR 2024; vindicates Caruana ICML 2004).
- **Tabular foundation models.** TabPFN v2 (Hollmann et al. *Nature* 2025): pretrained on synthetic data; predicts via **in-context learning** with no per-dataset tuning; beats tuned XGBoost / CatBoost on small data (≤ ~10K rows, ~500 features). TabICL (Qu et al. ICML 2025) pushes the row cap higher.
- **LLM agents that write analysis pipelines.** CAAFE (LLM feature engineering, NeurIPS 2023); AIDE; AutoKaggle; Data Interpreter. Evaluated by **MLE-bench** (Chan et al. ICLR 2025; ~16.9% bronze-medal level for the best setup) and **DABStep** (Egg et al. 2025; ~76% Easy vs. ~15% Hard splits the failure profile).
- **OBOE → TabPFN through-line.** OBOE (Yang, Akimoto, Kim, Udell, KDD 2019): the model-performance matrix is low-rank → recommend models via matrix completion. TabPFN takes the same shared-structure bet and pushes it into a pretrained transformer.
- **One-shot vs tool-using agent distinction.** Execution + iteration kills the *crash class* of errors (a fabricated p-value can't survive being computed); it does not kill the *judgment class* — wrong test, leakage, causal misattribution run cleanly and return wrong-but-plausible answers.
- **Honest capability boundaries**, framed as *mistakes anyone can make that you must check for*, NOT as motives or strawman LLM behavior. Calibration framing: recoverable-but-degraded (Tian 2023 on verbalized confidence; Kadavath 2022 on base-model calibration), not "they don't calibrate." Best-documented failure is *omission of assumption checks* unless prompted (Ordak 2023; Ruta et al. 2025) — measured, not motivational.
- **Selection bias from naively dropping missing data** (College Scorecard worked example).
- **Simpson's paradox in within-player NBA rest data** (worked example).
- **Prompt decomposition** — break an analysis into small, verifiable steps so you can catch errors before they propagate (the Ruta 2025 32.5% → 92.5% prompt-specificity gradient is the empirical case).
- **The critical-evaluation checklist, regrouped into 5 clusters** — delivering the [Chapter 1](lec01-intro.qmd) promise:
  1. **The data** — source/dictionary, who's missing/MNAR/survivorship, types
  2. **The model** — right metric for the decision, truly held-out / temporal split, no leakage, same population / distribution shift
  3. **The signal** — base rate vs. "99% accuracy", multiple testing, uncertainty / CI width, effect large enough to matter
  4. **The claim** — correlation or causation? what's the DAG?
  5. **The incentives and dynamics** — Goodhart / gaming, feedback loops, who paid for it

**Key vocabulary:**
- Gradient boosting (function-space gradient descent)
- CASH (combined algorithm selection and hyperparameter optimization)
- AutoML
- Ensembling, stacking
- Tabular foundation model
- In-context learning
- LLM agent (data analysis)
- MLE-bench, DABStep
- One-shot vs tool-using agent
- Shared-structure principle (OBOE → TabPFN)
- Selection bias
- 5-cluster critical-evaluation checklist (data; model; signal; claim; incentives and dynamics)
- Prompt decomposition

**Prerequisites:** Ch 6 (validation / cross-validation — the loss AutoML searches over), Ch 13 (decision trees and random forests — gradient boosting builds on these); selected back-references to Ch 7 (gradient descent), Ch 11 (multiple testing), Ch 16 (Goodhart, feedback loops), Ch 18 (DAGs / confounding — for the "claim" cluster forward-reference).

**Connections:**
- Backward: Ch 6 (validation), Ch 7 (gradient descent → gradient boosting), Ch 11 (multiple testing — referenced in checklist item 3), Ch 13 (trees / forests — defers gradient boosting here), Ch 16 (Goodhart + feedback loops — referenced in checklist item 5)
- Forward: Ch 20 (fairness as the marquee case where judgment automation cannot make the call)
- Ties together the AI theme threaded throughout the course; delivers the Ch 1 promise

**Aphorism:** "Far better an approximate answer to the right question..." (Tukey) — revisited at course end

**Surprise moment:** A frontier AI agent scores ~76% on DABStep Easy and ~15% on DABStep Hard. Same agent, same dataset — the Easy/Hard gap *is* the failure profile (reliable on the mechanical step, unreliable on the judgment-laden workflow).

---

## Lecture 18: Causal Inference I — DAGs + Confounding

**Objectives addressed:** 16 (DAGs, confounders, colliders), 17 (regression causal vs. predictive)

**Key concepts:**
- Correlation ≠ causation (formalized)
- Confounders: common causes of treatment and outcome that create spurious associations
- Causal DAGs: directed acyclic graphs representing causal structure
- Causal path vs. confounding path (backdoor path)
- Colliders: conditioning on a common effect opens a spurious path
- When regression estimates a causal effect (all backdoor paths blocked) vs. when it doesn't
- Simpson's paradox explained via DAGs

**Key vocabulary:**
- Causal inference
- Confounder
- DAG (Directed Acyclic Graph)
- Causal path, backdoor path
- Collider
- Spurious correlation / association
- Observational data vs. experimental data

**Prerequisites:** Lec 5 (regression), Lec 12 (regression coefficients, "controlling for"), Lec 16 (feedback loops — the DAG view formalizes them)

**Connections:**
- Backward: Lec 2 (hospital data — "worst hospitals"), Lec 11 (correlation ≠ causation), Lec 12 (regression as partial control), Lec 16 (feedback loops — now given the DAG-view treatment; prediction is an intervention)
- Forward: Lec 19 (natural experiments, DiD)
- The Effect Ch 1-6 (DAGs, confounding)
- $$ hook: "Does your college cause higher earnings?" — College Scorecard as confounding showcase

**Aphorism:** "Correlation is not causation" — now formalized via DAGs

**Surprise moment:** John Snow's famous cholera map was NOT the evidence that convinced people — it was the natural experiment comparing water companies

---

## Lecture 19: Causal Inference II — Natural Experiments + A/B Tests

**Objectives addressed:** 18 (natural experiments, DiD)

**Key concepts:**
- Counterfactual: what would have happened without the treatment?
- RCTs (A/B tests) as the gold standard for causal inference
- Natural experiments: when nature or policy creates near-random assignment
- Difference-in-differences (DiD): comparing before/after changes across treatment and control
- Parallel trends assumption: treatment and control would have followed the same trend without treatment
- DiD as regression with an interaction term: Y ~ Treated + Post + Treated × Post
- Instrumental variables and regression discontinuity as other quasi-experimental tools (brief mention)
- **Propensity score matching (PSM):** estimate $e(x) = P(T=1 \mid X=x)$, match treated/control units with similar scores, compare outcomes within matched pairs — balances all *observed* covariates simultaneously but cannot address unmeasured confounders

**Key vocabulary:**
- Counterfactual
- Randomized Controlled Trial (RCT), A/B test
- Natural experiment
- Difference-in-differences (DiD)
- Parallel trends assumption
- Treatment effect
- Instrumental variable (IV), regression discontinuity (RD)
- **Propensity score**, **propensity score matching**, **hidden (unmeasured) confounder**
- SUTVA (stable unit treatment value assumption), peeking in A/B tests

**Key formulas:**
- DiD = (Ȳ_treated,after − Ȳ_treated,before) − (Ȳ_control,after − Ȳ_control,before)
- DiD regression: Y = β₀ + β₁·Treated + β₂·Post + β₃·Treated×Post + ε
- β₃ = the causal effect estimate
- Propensity score: $e(x) = P(T=1 \mid X=x)$, typically fit via logistic regression

**Prerequisites:** Lec 18 (DAGs, confounding); Lec 8-10 (hypothesis testing for evaluating treatment effects); Lec 7 (logistic regression — prerequisite for estimating propensity scores)

**Connections:**
- Backward: Lec 8-10 (ACTG 175 clinical trial revisited with causal lens), Lec 18 (DAGs), Lec 7 (logistic regression used to estimate propensity scores)
- The Effect Ch 16-18 (DiD, natural experiments); Rosenbaum & Rubin 1983 (propensity score theory)

**Aphorism:** "Compared to what?" — every causal claim hides a counterfactual comparison

**Surprise moment:** a single rule change (MLB's 1973 designated-hitter rule) creates a textbook natural experiment — Bradbury & Drinen showed AL pitchers hit batters ~15% more often than NL pitchers after 1973, explained causally by moral hazard (they no longer had to bat themselves)

---

## Lecture 20: Fairness in Algorithmic Decision-Making (enrichment)

**Status:** Enrichment material — reading-only. Not on the final exam. No quiz problems.

**Objectives addressed:** beyond the original 23 — gives students the vocabulary to read a fairness debate (newsroom story, court filing, tech-company report) and tell what each side is and isn't claiming.

**Dataset:** ProPublica COMPAS recidivism (`data/compas/compas-scores-two-years.csv`) — 6,172 Broward County defendants after the standard ProPublica filter (days_b_screening_arrest within ±30 days; non-ordinary charge; non-N/A score; race in {African-American, Caucasian}); decile_score ≥ 5 thresholded for the binary classifier. Synthetic SCM (5,000 samples, `np.random.default_rng(0)`) for the unawareness-fails and counterfactual-flip demos.

**Key concepts:**
- **Lead with the COMPAS dispute, not definitions.** ProPublica (2016) vs. Northpointe — two analyses, same data, opposite conclusions about whether the algorithm was fair. Each chose a different mathematical definition; the definitions are mutually incompatible.
- **Protected attributes are legally specified** (Title VII, ECOA, Fair Housing Act, ADA in the US; EU AI Act 2024/1689; NYC Local Law 144; Colorado SB 24-205). Barocas & Selbst (*Cal. L. Rev.* 2016) is the standard reference for how US antidiscrimination doctrine maps onto algorithmic decisions.
- **Fairness through unawareness fails.** Dropping the protected attribute is not enough — correlated proxies leak the signal back in. Demonstrated on a synthetic SCM where the proxy = z + 0.8·a + noise.
- **Four group-fairness criteria, four different intuitions:**
  - *Demographic parity*: $P(\hat y = 1 \mid a)$ equal across groups; $\hat y \perp a$
  - *Equalized odds* (Hardt-Price-Srebro NeurIPS 2016): TPR and FPR equal across groups; $\hat y \perp a \mid y$
  - *Equality of opportunity*: TPR alone equal (the qualified-group-focused relaxation of equalized odds)
  - *Predictive parity / calibration within groups*: PPV equal across groups; per-decile re-arrest rates match across race in the calibration plot
- **The impossibility theorem** (Kleinberg-Mullainathan-Raghavan, ITCS 2017, LIPIcs vol 67 paper 43, arXiv:1609.05807; Chouldechova *Big Data* 2017 5(2)). When group base rates differ, no non-trivial classifier can simultaneously satisfy predictive parity and equalized odds. COMPAS demonstrates this numerically — base rates differ by ~13 percentage points, PPV is approximately equal, and the FPR/FNR gap follows.
- **Counterfactual fairness** (Kusner, Loftus, Russell, Silva, NeurIPS 2017) — the causal-inference bridge. A classifier is counterfactually fair if its prediction is unchanged when the protected attribute is flipped and the flip is propagated through the assumed structural causal model. The criterion is the most demanding of the four and the most dependent on a structural model the modeler has to commit to.
- **For COMPAS there is no credible SCM** — we can compute the group-fairness metrics but not counterfactual fairness in good faith.
- **The counterfactual frame itself is contested** (Kohler-Hausmann 2019; Hu & Kohler-Hausmann FAccT 2020) — flipping a socially-constructed attribute while fixing the features it is constitutive of describes a person who does not exist. Acknowledged in one paragraph, not a deep dive.
- **Practice has moved beyond "pick a metric"** to four ideas working together: sociotechnical reframing (Selbst et al. FAT* 2019); auditing as a discipline (NYC LL 144, OMB M-24-10, EU AI Act); participatory design with affected communities; compliance-language framing.
- **Three cases since COMPAS** (with primary-source documentation): Optum healthcare risk score (Obermeyer et al. *Science* 2019 — wrong label, not wrong metric); Dutch SyRI (Hague Court Feb 2020 — first European court ruling on algorithmic discrimination); UK Ofqual A-level grades (Aug 2020 — public-pressure reversal).
- **Tooling pointer:** Fairlearn (Microsoft, scikit-learn-style API); AIF360 (IBM); Aequitas (DSAPP, audit-report deliverable); HolisticAI (covers EU AI Act high-risk obligations more broadly).

**Key vocabulary:**
- Protected attribute
- Fairness through unawareness
- Demographic parity (statistical parity)
- Equalized odds
- Equality of opportunity
- Predictive parity
- Calibration within groups
- Impossibility theorem (KMR / Chouldechova)
- Counterfactual fairness
- Structural causal model (SCM)

**Key formulas / notation:**
- $\hat y \perp a$ (demographic parity)
- $\hat y \perp a \mid y$ (equalized odds)
- $P(y=1 \mid \hat y = 1, a)$ equal across $a$ (predictive parity)
- $\hat Y_{a \leftarrow a'}(U) = \hat Y_{a \leftarrow a}(U)$ for all $a, a'$ (counterfactual fairness)

**Computational tools:**
- `sklearn.linear_model.LogisticRegression` — to demonstrate proxy leakage under unawareness
- `df.groupby(a)['y_hat'].mean()` — positive-rate by group
- Per-group confusion-table rates (TPR, FPR, PPV) — usually shown as a grouped bar chart and a small table
- Per-decile calibration plot across groups
- The standard ProPublica COMPAS filter (codified in the chapter for reproducibility)
- `fairlearn.metrics.MetricFrame`; `fairlearn.postprocessing.ThresholdOptimizer` — production tooling pointer

**Prerequisites:** Ch 7 (logistic regression, confusion matrix, FPR/TPR/PPV — predictive parity is just precision-per-group); Ch 11 (multiple testing — for the base-rate / Bayes-rule arithmetic); Ch 18–19 (DAGs, counterfactuals — needed to define counterfactual fairness honestly).

**Connections:**
- Backward: Ch 1 (fulfills the "formalize this in Act 3" promise about COMPAS — lec01:67); Ch 7 (confusion-matrix rates per group); Ch 11 (correlation ≠ causation, base rates); Ch 15 (the feature-choice-is-a-values-choice thread, applied to a new domain); Ch 17 (the fifth checklist cluster: incentives and dynamics — fairness is the marquee case where judgment automation cannot make the call); Ch 18-19 (DAGs, counterfactuals)
- Forward: none (final chapter)
- ORIE 4741: fairness.tex — COMPAS, fairness metrics, impossibility theorem, feedback loops in social contexts

**Aphorism:** none directly — the course thesis ("taste is the bottleneck") lands as the chapter's closing line: fairness is the case where the criteria are mathematically incompatible, the data does not pick between them, and the choice belongs to whoever is responsible for the decision.

**Surprise moment:** Both ProPublica's claim (unequal FPR/FNR across groups) and Northpointe's claim (approximately equal PPV and per-decile calibration) are correct on the same COMPAS data — the disagreement is not about the arithmetic but about which definition of fairness should govern. The impossibility theorem says no clever algorithm escapes the constraint.

---

## Objective Coverage Summary

| # | Objective | Primary lectures | Secondary |
|---|-----------|-----------------|-----------|
| 1 | Explore/visualize, outliers, missing data | **Lec 2** | Lec 1 |
| 2 | Clean/transform/join | **Lec 3** | |
| 3 | Evaluate AI analyses | **Lec 3, 17** | Lec 1 |
| 4 | Vectors, linear combinations, span, regression | **Lec 4** | |
| 5 | Feature engineering, regression diagnostics | **Lec 5** | |
| 6 | Sampling distributions, CLT | **Lec 8** | |
| 7 | Bootstrap CIs | **Lec 8** | Lec 12 |
| 8 | Hypotheses, p-values, simulation | **Lec 9, 10** | |
| 9 | Multiple testing (Bonferroni, FDR) | **Lec 11** | |
| 10 | Regression coefficient inference (t-tests) | **Lec 12** | |
| 11 | Train/test/validate model selection | **Lec 6** | Lec 12, 16 |
| 12 | Feature engineering, trees | **Lec 5, 13** | Lec 6, 16 |
| 13 | Logistic regression, classification metrics | **Lec 7** | |
| 14 | PCA, interpret PCs | **Lec 14** | |
| 15 | K-means, cluster quality | **Lec 15** | |
| 16 | DAGs, confounders, colliders | **Lec 18** | |
| 17 | Regression causal vs. predictive | **Lec 18** | Lec 12 |
| 18 | Natural experiments, DiD | **Lec 19** | |
| 19 | AI coding assistants | **Lec 17** | |
| 20 | AI failure modes | **Lec 17** | Lec 1, 3 |
| 21 | Prompt decomposition | **Lec 17** | |
| 22 | Reports with visualizations | **Lec 2** | |
| 23 | Present/defend findings | *Not in lectures — addressed via HW review sessions and project* | |

### Gaps and notes

- **Objective 23** (present/defend findings) has no lecture coverage. This is by design — it's assessed through homework review sessions (15% of grade) and the project.
- **F-tests** — CUT from course. Too mechanical for the audience; t-tests on individual coefficients are sufficient.
- **Colliders** (Objective 16) should be explicitly introduced in Lec 18 — verify in draft.
- **Objective 22** (reports with visualizations) is lightly addressed. Consider whether Lec 2 or the project guidelines should do more.
- **Chi-squared tests** — added to Lec 10 for categorical data (goodness of fit, independence).
- **Gradient descent** — added to Lec 7 with hiking/landscape metaphor. Good HW problem candidate.

### Editorial decisions (2026-03-17)

**Imported from prior offerings:**
- ✅ **Estimand / estimator / estimate** vocabulary → Lec 8
- ✅ **Odds ratios** (exp(β) interpretation) → Lec 7
- ✅ **Gradient descent** (metaphorical + computational, hiking/landscape, convex vs non-convex) → Lec 7; HW problem candidate
- ✅ **Chi-squared tests** (goodness of fit, independence) → Lec 10
- ✅ **Lasso** → Lec 6, alongside bias-variance tradeoff and model complexity control
- ✅ **VIF** → Lec 6 "further reading" only (too technical for lecture)
- ✅ **Random forests as black-box benchmark** → Lec 13 (practical tree intro); how trees work → Lec 17
- ✅ **Trees handle missing values** → forward-referenced from Lec 3 to Lec 13
- ✅ **Power analysis** → Lec 10 (conceptual + computational via simulation/statsmodels, not formula derivation); HW problem candidate
- ✅ **Statistical aphorisms** → distributed across lectures (see aphorisms table)
- ✅ **Study guide sections** → structural requirement for every lecture .qmd

**Cut:**
- ❌ **F-tests** — too mechanical for this audience
- ❌ **Additive models / splines / NAMs** — cut from 2026; may mention briefly in Lec 17

**Still to import (from ORIE 4741):**
- **"The loss function determines what the model finds"** (L2→mean, L1→median) — natural fit for Lec 5 or 7
- **PCA as "regression onto optimal covariates"** — for Lec 14
- **K-means as GLRM special case** — may be too advanced, but PCA↔k-means connection is valuable for Lec 15
- **Informative vs. uninformative missingness** (ambulance heart rate example) — for Lec 3
- **Bias-variance tradeoff + double descent** — for Lec 6 (RESOLVED: teach classical as primary framework; 10-15 min frontier window on double descent; three-level understanding; key refs: Belkin 2019, Hastie 2022)
- **Hospital buying an ML system** opening — $$ framing for Lec 6
