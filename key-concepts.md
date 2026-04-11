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

---

## Lecture 1: Introduction

**Objectives addressed:** 1 (explore/visualize), 3 (evaluate AI analyses), 20 (AI failure modes)

**Key concepts:**
- Applied statistics = decisions under uncertainty
- Three course themes: explore & model, test & decide, complex models
- Dollar-sign decisions: hospital fines, Airbnb pricing, drug approval, sports betting
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
- "Linear in parameters, not features": polynomials and interactions make linear models powerful
- Polynomial features and the overfitting parade: high-degree polynomials fit training data well but extrapolate wildly
- Interaction terms: when one feature's effect depends on another
- Missing values as features (missingness indicator)
- Log transforms on y change coefficient interpretation (percentage vs dollar); motivated by extrapolation/multiplicative growth
- Four log-transform combinations (level-level, log-level, level-log, log-log)
- Adjusted R²: penalizing complexity
- Multicollinearity: nearly parallel features create unstable coefficients
- Residual diagnostics: heteroscedasticity, curves, clusters, Q-Q plots

**Key vocabulary:**
- Column space, multiple regression
- Normal equations, matrix form
- One-hot encoding, reference level, indicator variable
- Feature engineering
- Polynomial features, interaction term
- Log transform, elasticity
- Adjusted R-squared
- Multicollinearity
- Heteroscedasticity, Q-Q plot, residual diagnostics

**Key formulas:**
- ŷ = Xβ (matrix form)
- X^T ε = 0 (stacked orthogonality conditions)
- β = (X^T X)^{-1} X^T y (normal equations)

**Prerequisites:** Lec 4 (simple regression, span, orthogonality, inner product, R²)

**Connections:**
- Backward: Lec 4 (single-feature version of everything here)
- Forward: Lec 6 (validation — train/test R²), Lec 13 (trees as automatic feature engineering), Lec 12 (which features are statistically significant?), Lec 18 (when is a coefficient causal?)
- VMLS: Ch 5 (linear independence), Ch 13 (least squares)

**Surprise moment:** The polynomial overfitting parade — R² keeps climbing as you increase degree, but the predictions become nonsensical (negative or wildly inflated prices for 10+ bedrooms). The model with the highest training R² is not the best model.

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

**Prerequisites:** Lec 5 (feature engineering, polynomial overfitting)

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

**Key vocabulary:**
- Logistic regression, sigmoid function
- Odds, odds ratio, log-odds (logit)
- Gradient descent, loss landscape, learning rate, convergence
- Local minimum, global minimum (for non-convex problems)
- Class imbalance, accuracy trap / accuracy paradox
- Confusion matrix
- True positive, false positive, true negative, false negative
- Precision, recall, F1 score
- ROC curve, AUC (Area Under Curve)
- Threshold

**Key formulas:**
- Sigmoid: p = 1 / (1 + e^(−z)) where z = β₀ + β₁x₁ + ⋯
- Logit (inverse sigmoid): log(p/(1−p)) = β₀ + β₁x₁ + ⋯
- Odds ratio: exp(βⱼ) = how odds multiply per unit increase in xⱼ
- Gradient descent update: β ← β − η · ∇L(β)
- ORIE 4741: logistic loss = log(1 + exp(−y·w^T x)) — connects to ERM framework

**Prerequisites:** Lec 4-6 (regression, feature engineering, validation)

**Connections:**
- Backward: Lec 4-5 (regression — OLS has closed form; logistic does not), Lec 6 (train/test, validation — apply to classification)
- Forward: Lec 12 (inference on logistic coefficients, calibration), Lec 13 (classification trees — trees handle both regression and classification), Lec 17 (gradient boosting uses gradient descent ideas)
- ORIE 4741: losses.tex — logistic loss section

**Surprise moment:** Overall AUC ~0.73 hides dramatic failures in subgroups — model fails for specific demographics

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
- Exchangeability: random assignment makes labels exchangeable under H₀
- Connection: bootstrap (Lec 8) = precision of estimate; permutation = significance of effect
- Conservative p-value estimator: (count + 1) / (n_perms + 1) (Phipson & Smyth 2010)
- CI/hypothesis test duality: a 95% CI excluding 0 is equivalent to rejecting H0 at alpha = 0.05

**Key vocabulary:**
- Permutation test (shuffle labels)
- Null distribution
- Null hypothesis (informal — formalized in Lec 10)
- p-value
- Exchangeability
- Simulation-based inference
- CI/hypothesis test duality

**Prerequisites:** Lec 8 (bootstrap — students know resampling)

**Connections:**
- Backward: Lec 8 (bootstrap)
- Forward: Lec 10 (formal hypothesis testing framework), Lec 11 (multiple testing)

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

## Lecture 11: Multiple Testing + Correlation

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
- $$ hook: NBA analytics intern "discovers" 30 players benefit from rest — but ~22 are expected by chance

**Aphorisms:** "If you torture the data long enough, it will confess to anything" (Coase); "Correlation is not causation"

**Surprise moment:** Simpson's paradox in NBA rest data — extended-rest players score *fewer* points overall because bench players dominate the extended-rest group

---

## Lecture 12: Regression Inference + Diagnostics

**Objectives addressed:** 10 (regression coefficient inference), 11 (evaluate models), 17 (regression causal vs. predictive)

**Key concepts:**
- Residual plots: the primary diagnostic for model validity (moved from old Lec 6)
- Heteroscedasticity: fan-shaped residuals mean unequal variance
- Q-Q plot: checking normality of residuals
- "Diagnostics first, inference second" — check model before testing coefficients
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

**Surprise moment:** REST_DAYS is statistically significant (p ~ 0.04) but the effect is only 0.3 points — practically negligible

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
- Backward: Lec 7 (classification model), Lec 8 (bootstrap), Lec 9 (permutation), Lec 10-11 (hypothesis testing, multiple testing), Lec 12 (regression inference, calibration)
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

---

## Lecture 15: Clustering (K-Means)

**Objectives addressed:** 15 (k-means, evaluate cluster quality)

**Key concepts:**
- Unsupervised learning: finding structure without labels
- K-means algorithm: assign points to nearest centroid, recompute centroids, repeat
- Choosing k: elbow method, silhouette score
- Standardization matters for clustering (same lesson as PCA)
- K-means is sensitive to initialization — different seeds → different clusters
- Local vs. global optima: k-means finds a local minimum, not necessarily the best
- Interpretation: what do the clusters mean?

**Key vocabulary:**
- Unsupervised learning
- K-means
- Centroid
- Cluster
- Silhouette score
- Elbow method
- Local optimum, initialization sensitivity
- Distance metrics (Euclidean, Manhattan, cosine)
- K-medoids
- Adjusted Rand Index (ARI)

**Key formulas:**
- K-means objective: minimize Σ_k Σ_{i∈C_k} ||x_i − μ_k||²
- ORIE 4741: k-means as GLRM with unit-one-sparse constraint on X

**Prerequisites:** Lec 14 (PCA, standardization)

**Connections:**
- Backward: Lec 14 (PCA, standardization)
- ORIE 4741: unsupervised.tex — k-means as special case of GLRM framework

**Surprise moment(s):** (1) Geography dominates clustering unless lat/lon are removed. (2) Different random seeds produce different clusters — k-means is not deterministic.

---

## Lecture 16: Backtesting + Time Series Validation

**Objectives addressed:** 11 (train/test/validate — temporal version), 12 (lag features)

**Key concepts:**
- Temporal structure means random train/test split leaks future information
- Backtesting: train on past, test on future (temporal split)
- Data leakage: using information from the future to predict the past
- Lag features: use past values (last 5 games, yesterday's AQI) as features for today
- Non-stationarity: the data-generating process changes over time
- Walk-forward validation: expanding or sliding window
- MAPE and MASE as forecast accuracy metrics
- Prediction intervals via bootstrap residual resampling
- Distribution shift: future data may not resemble past data
- Benchmark forecasting methods: naive, seasonal naive, drift

**Key vocabulary:**
- Backtesting, temporal split
- Data leakage
- Lag features
- Non-stationarity
- Walk-forward validation
- AQI (Air Quality Index)
- MAPE (Mean Absolute Percentage Error)
- MASE (Mean Absolute Scaled Error)
- Prediction interval
- Distribution shift
- Naive forecast, seasonal naive, drift

**Prerequisites:** Lec 5 (feature engineering), Lec 6 (train/test split, cross-validation)

**Connections:**
- Backward: Lec 5 (feature engineering), Lec 6 (train/test, cross-validation)
- Forward: Lec 17 (AutoML limitations with temporal data)
- FPP3 Ch 5 (the forecasting toolbox — train/test for time series)
- ORIE 4741: feature_engineering.tex (AR, ARMA, ARIMA, exponential smoothing); train-test-validate.tex ("can't randomly split time series")

**Aphorism:** "Prediction is very difficult, especially about the future" (attr. Bohr)

**Surprise moment:** Model trained on historical EPA data encounters an unprecedented wildfire smoke event — future doesn't look like the past

---

## Lecture 17: AutoML, LLMs, and the Future of Data Analysis

**Objectives addressed:** 3 (evaluate AI analyses), 19 (AI coding assistants), 20 (AI failure modes), 21 (prompt decomposition)

**Key concepts:**
- **How trees and forests work** (deepening the practical introduction from Lec 13) — Students learned trees and forests in Lec 13 — now they see the bigger picture:
  - Decision trees: recursive partitioning of feature space (split on one feature at a time)
  - Why trees handle missing values naturally (can split on "is this value missing?")
  - Why trees handle nonlinearities without feature engineering
  - Overfitting: deep trees memorize; shallow trees underfit
  - Random forests: grow many trees on bootstrap samples, average predictions → reduces variance
  - Gradient boosting: train weak learners sequentially, each correcting the previous one's errors (connects to gradient descent from Lec 7)
- AutoML: automated model selection and hyperparameter tuning
- What AutoML does well (trying many models, cross-validation) and what it cannot do (framing the question, evaluating assumptions, causal reasoning)
- LLM-generated data analyses: impressive but systematically flawed
- Selection bias from naively dropping missing data
- The human role: question formulation, assumption checking, interpretation, communication
- Comparing LLM analysis vs. course-trained analysis on the same problem
- Brief mention: additive models / splines / NAMs as "what's under the hood" in some AutoML systems

**Key vocabulary:**
- Decision tree, split, leaf, node
- Random forest, bagging (bootstrap aggregation)
- Gradient boosting
- AutoML
- Selection bias
- LLM (Large Language Model)

**Prerequisites:** All prior lectures (this is the synthesis); Lec 7 (gradient descent), Lec 13 (trees and forests)

**Connections:**
- Backward: **Lec 13 (trees and forests — now students see the deeper mechanics)**, Lec 3 (AI gotchas established early), Lec 7 (gradient descent → gradient boosting)
- Ties a bow on the AI theme threaded throughout the course
- ORIE 4741: trees.tex — decision trees, bagging, random forests, gradient boosting, feature importance

**Aphorism:** "Far better an approximate answer to the right question..." (Tukey) — revisited at course end

**Surprise moment:** Side-by-side comparison — LLM analysis of NBA rest data vs. what the course taught students to check (multiple testing, Simpson's paradox, practical significance)

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

**Prerequisites:** Lec 5 (regression), Lec 12 (regression coefficients, "controlling for")

**Connections:**
- Backward: Lec 2 (hospital data — "worst hospitals"), Lec 11 (correlation ≠ causation), Lec 12 (regression as partial control)
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

**Key vocabulary:**
- Counterfactual
- Randomized Controlled Trial (RCT), A/B test
- Natural experiment
- Difference-in-differences (DiD)
- Parallel trends assumption
- Treatment effect

**Key formulas:**
- DiD = (Ȳ_treated,after − Ȳ_treated,before) − (Ȳ_control,after − Ȳ_control,before)
- DiD regression: Y = β₀ + β₁·Treated + β₂·Post + β₃·Treated×Post + ε
- β₃ = the causal effect estimate

**Prerequisites:** Lec 18 (DAGs, confounding); Lec 8-10 (hypothesis testing for evaluating treatment effects)

**Connections:**
- Backward: Lec 8-10 (ACTG 175 clinical trial revisited with causal lens), Lec 18 (DAGs)
- The Effect Ch 16-18 (DiD, natural experiments)

**Surprise moment:** NBA play-in tournament introduction as a natural experiment affecting player usage patterns

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
| 22 | Reports with visualizations | **Lec 2** | Lec 13 |
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
