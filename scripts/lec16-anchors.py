"""Exploratory anchors for lec16 reorg: can retail carry the leakage demo?"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

DATA_DIR = 'data'

retail = pd.read_csv(f'{DATA_DIR}/retail-sales/fred_rsafsna_monthly.csv')
retail['date'] = pd.to_datetime(retail['date'])
retail = retail.sort_values('date').reset_index(drop=True)
print(f"retail: {len(retail)} months, {retail['date'].min().date()} to {retail['date'].max().date()}")

# ---- Features ----
r = retail.copy()
r['lag1']      = r['sales'].shift(1)
r['lag3_avg']  = r['sales'].rolling(3).mean().shift(1)
r['lag12']     = r['sales'].shift(12)
r['months']    = (r['date'] - r['date'].min()).dt.days / 30.44
r['sin']       = np.sin(2*np.pi*r['date'].dt.month/12)
r['cos']       = np.cos(2*np.pi*r['date'].dt.month/12)
r = r.dropna().reset_index(drop=True)

models = {
    'Lag features': ['lag1', 'lag3_avg'],
    'Linear trend': ['months'],
    'Seasonal':     ['sin', 'cos', 'lag12'],
}

# ---- Random vs temporal split ----
np.random.seed(42)
rmask = np.random.rand(len(r)) < 0.8
# avoid COVID weirdness: cut at a clean pre-covid point and also test full
for cutoff_str in ['2017-01-01', '2010-01-01']:
    cutoff = pd.Timestamp(cutoff_str)
    tr_t, te_t = r[r['date'] < cutoff], r[r['date'] >= cutoff]
    print(f"\n=== temporal cutoff {cutoff_str}  (train {len(tr_t)}, test {len(te_t)}) ===")
    print(f"{'Model':<15}{'rand R2':>9}{'temp R2':>9}{'temp MAE':>11}")
    for name, feats in models.items():
        m_r = LinearRegression().fit(r[rmask][feats], r[rmask]['sales'])
        r2r = r2_score(r[~rmask]['sales'], m_r.predict(r[~rmask][feats]))
        m_t = LinearRegression().fit(tr_t[feats], tr_t['sales'])
        pt = m_t.predict(te_t[feats])
        print(f"{name:<15}{r2r:>9.3f}{r2_score(te_t['sales'], pt):>9.3f}{mean_absolute_error(te_t['sales'], pt):>11,.0f}")
    # naive lag1 and lag12 on temporal test
    print(f"{'Naive lag1':<15}{'-':>9}{r2_score(te_t['sales'], te_t['lag1']):>9.3f}{mean_absolute_error(te_t['sales'], te_t['lag1']):>11,.0f}")
    print(f"{'Naive lag12':<15}{'-':>9}{r2_score(te_t['sales'], te_t['lag12']):>9.3f}{mean_absolute_error(te_t['sales'], te_t['lag12']):>11,.0f}")

# ---- Trend shape: is it linear or accelerating? ----
print("\n=== trend shape ===")
yr = retail.copy()
yr['year'] = yr['date'].dt.year
ann = yr.groupby('year')['sales'].mean()
print("decade-over-decade mean monthly sales ($M):")
for y in [1995, 2000, 2005, 2010, 2015, 2019, 2023]:
    if y in ann.index:
        print(f"  {y}: {ann[y]:,.0f}")

# ---- Clean pre-COVID leakage demo: train <2017, test 2017-2019 ----
print("\n=== CLEAN pre-COVID: train <2017-01, test 2017-01..2019-12 ===")
tr = r[r['date'] < '2017-01-01']
te = r[(r['date'] >= '2017-01-01') & (r['date'] <= '2019-12-01')]
print(f"train {len(tr)}, test {len(te)}")
print(f"{'Model':<15}{'rand R2':>9}{'temp R2':>9}{'temp MAE':>11}")
for name, feats in models.items():
    m_r = LinearRegression().fit(r[rmask][feats], r[rmask]['sales'])
    r2r = r2_score(r[~rmask]['sales'], m_r.predict(r[~rmask][feats]))
    m_t = LinearRegression().fit(tr[feats], tr['sales'])
    pt = m_t.predict(te[feats])
    print(f"{name:<15}{r2r:>9.3f}{r2_score(te['sales'], pt):>9.3f}{mean_absolute_error(te['sales'], pt):>11,.0f}")
print(f"{'Naive lag12':<15}{'-':>9}{r2_score(te['sales'], te['lag12']):>9.3f}{mean_absolute_error(te['sales'], te['lag12']):>11,.0f}")

# ---- Walk-forward across full history: where does error spike? ----
print("\n=== walk-forward yearly MAE (lag-feature model, expanding window) ===")
feats = ['lag1', 'lag3_avg', 'lag12']
for yr_test in range(2005, 2026):
    tr_wf = r[r['date'] < f'{yr_test}-01-01']
    te_wf = r[(r['date'] >= f'{yr_test}-01-01') & (r['date'] < f'{yr_test+1}-01-01')]
    if len(te_wf) < 6 or len(tr_wf) < 24: continue
    m = LinearRegression().fit(tr_wf[feats], tr_wf['sales'])
    mae = mean_absolute_error(te_wf['sales'], m.predict(te_wf[feats]))
    print(f"  {yr_test}: MAE {mae:>9,.0f}")
