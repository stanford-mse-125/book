# MSE 125 Book — Process Journal

## 2026-03-24: Scholarly tone revision + structural fixes + feeder/feedee analysis

### Major changes
- **Scholarly tone overhaul**: Applied new grammar rules across all 19 lectures — "This"+noun rule, no "because" constructions, show-before-tell, define-before-namedrop. Tone elevated to Cambridge University Press level.
- **Classification moved to Act 3**: `_quarto.yml` updated. Lec 13 reframed (removed "Act 2 capstone"). Act 2 is now Lec 8-12, Act 3 is Lec 13-19.
- **Custom definition callouts**: Created `custom.scss` to restyle `.callout-important` as blue with book icon (replacing red exclamation). Added to `_quarto.yml` theme.
- **"Consequential decisions" terminology**: Replaced "$$ decisions" / "dollar-sign decisions" throughout all lectures and CLAUDE.md.
- **Plot widths reduced ~20%**: Default figsize changed to (7, 4.5). Side-by-side plots reduced from (14, 5) to (11, 4) across 15 lectures.

### Per-lecture fixes
- Lec 1: Positive framing, AI reframed as skepticism
- Lec 3: Joins defined before questions, correlation-based leakage demo
- Lec 4: Span/projection visualization fixed (target vector in rendered plane)
- Lec 6: Polynomial overfitting/extrapolation (negative prices at 9+ bedrooms), regularization callout for collinearity
- Lec 7: Fintech credit-scoring opening, double descent section
- Lec 10: $1.3B opener, uniform p-values, ACTG 175 simplification note
- Lec 11: Ioannidis (2005) "Why Most Published Research Findings Are False" added
- Lec 12: Major restructure — regression first then inference (bootstrap → formula → statsmodels), LINE diagnostics 2x2 panel, Q-Q scale fix, format_pvalue() helper, rest-days covariates (BACK_TO_BACK, PREV_MIN), Occam's razor
- Lec 13: Act 3 reframing
- Lec 16: Fixed 'County Name' → 'county Name' (matching actual CSV column)
- Lec 19: NBA reframed as descriptive comparison

### Feeder/feedee analysis
- **MS&E 120 (feeder)**: MSE 125 is well-calibrated. CLT/LLN covered on last day of 120 — book's thorough re-introduction is justified. ~8 probability callbacks being added (abstract framing, not course-specific).
- **MS&E 226 (feedee)**: Good alignment. MSE 125 feeds directly into 226's regression, validation, bootstrap, testing, classification, and causal inference modules. ~6 forward-references being added. Small content additions identified: MLE connection, regularization preview, Bayesian mention, potential outcomes notation.

### Infrastructure
- `key-concepts.md` synced with vocabulary from all lecture revisions
- `index.qmd` created (was missing)
- All 19 lectures render successfully
- Pushed to main

### Open items
- Lec 7: trees/features unification (design question, deferred)
- Homeworks and quizzes development (next major phase)
- Feeder/feedee cross-references being applied (in progress)
