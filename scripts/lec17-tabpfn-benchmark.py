#!/usr/bin/env python
"""TabPFN v2 benchmark on the Lec 17 Airbnb pricing task.

Runs 5-fold CV with RandomForest, GradientBoosting, and TabPFN on a
10K-row subsample of the Airbnb listings (TabPFN v2 caps near 10K rows /
500 features). The Lec 17 chapter quotes the TabPFN result without
running TabPFN in CI, because the model needs a GPU for tractable
inference time and adds a non-CI-friendly dependency.

Run from book/:  python scripts/lec17-tabpfn-benchmark.py
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score

DATA_DIR = "data"

# --- preprocessing matches the Lec 17 chapter exactly ---
listings = pd.read_csv(f"{DATA_DIR}/airbnb/listings.csv", low_memory=False)
listings["price"] = pd.to_numeric(
    listings["price"].astype(str).str.replace(r"[$,]", "", regex=True),
    errors="coerce",
)
listings = listings[listings["price"].between(10, 500)]

num_cols = [
    "bedrooms", "bathrooms", "accommodates", "number_of_reviews",
    "latitude", "longitude",
]
cat_cols = ["room_type", "neighbourhood_group_cleansed"]
listings_clean = listings[num_cols + cat_cols + ["price"]].dropna()

X_full = pd.concat(
    [
        listings_clean[num_cols],
        pd.get_dummies(listings_clean[cat_cols], drop_first=True),
    ],
    axis=1,
)
y_full = listings_clean["price"]

# Subsample to TabPFN's row cap
SUBSAMPLE = 10_000
rng = np.random.default_rng(42)
idx = rng.choice(len(X_full), size=SUBSAMPLE, replace=False)
X_sub = X_full.iloc[idx].reset_index(drop=True)
y_sub = y_full.iloc[idx].reset_index(drop=True)

print(f"Subsample: {len(X_sub):,} rows x {X_sub.shape[1]} features")

kf = KFold(n_splits=5, shuffle=True, random_state=42)

print("\nRandomForest (n=200)...")
rf = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
rf_cv = cross_val_score(rf, X_sub, y_sub, cv=kf, scoring="r2", n_jobs=1)
print(f"  CV R-sq = {rf_cv.mean():.3f} +/- {rf_cv.std():.3f}")

print("\nGradientBoosting (sklearn, n=200, depth=4)...")
gb = GradientBoostingRegressor(n_estimators=200, max_depth=4, random_state=42)
gb_cv = cross_val_score(gb, X_sub, y_sub, cv=kf, scoring="r2", n_jobs=1)
print(f"  CV R-sq = {gb_cv.mean():.3f} +/- {gb_cv.std():.3f}")

print("\nTabPFN v2 (no per-dataset tuning)...")
from tabpfn import TabPFNRegressor

tabpfn = TabPFNRegressor(device="cpu", ignore_pretraining_limits=True)  # CPU + bypass 1000-sample guard
tabpfn_cv = cross_val_score(tabpfn, X_sub, y_sub, cv=kf, scoring="r2", n_jobs=1)
print(f"  CV R-sq = {tabpfn_cv.mean():.3f} +/- {tabpfn_cv.std():.3f}")

print("\n--- Summary (5-fold CV R-sq on 10K Airbnb subsample) ---")
print(f"  RandomForest (n=200):              {rf_cv.mean():.3f}")
print(f"  GradientBoosting (sklearn, n=200): {gb_cv.mean():.3f}")
print(f"  TabPFN v2 (zero tuning):           {tabpfn_cv.mean():.3f}")
