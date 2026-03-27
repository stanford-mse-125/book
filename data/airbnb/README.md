# NYC Airbnb Listings

## Data Source

- **Origin**: Inside Airbnb (http://insideairbnb.com), via Cornell ORIE 4741 course materials
- **File**: `listings.csv`
- **Scope**: New York City Airbnb listings, scraped March 2018
- **Size**: 29,142 rows x 96 columns

## Schema

### Key Columns

| Column | Type | Description |
|--------|------|-------------|
| `id` | int | Unique listing identifier |
| `name` | str | Listing title |
| `host_id` | int | Unique host identifier |
| `host_name` | str | Host name |
| `host_since` | date | Date host joined Airbnb |
| `host_is_superhost` | bool (t/f) | Superhost status |
| `neighbourhood_cleansed` | str | Neighbourhood name (221 unique) |
| `neighbourhood_group_cleansed` | str | Borough (Manhattan, Brooklyn, Queens, Bronx, Staten Island) |
| `latitude` | float | Listing latitude |
| `longitude` | float | Listing longitude |
| `property_type` | str | Apartment, House, etc. |
| `room_type` | str | Entire home/apt, Private room, Shared room |
| `accommodates` | int | Max number of guests |
| `bathrooms` | float | Number of bathrooms |
| `bedrooms` | int | Number of bedrooms |
| `beds` | float | Number of beds |
| `price` | str -> int | Nightly price in USD (stored as "$X,XXX" string, needs parsing) |
| `weekly_price` | str | Weekly price (87% missing) |
| `monthly_price` | str | Monthly price (99% missing) |
| `cleaning_fee` | str | Cleaning fee (41% missing) |
| `security_deposit` | str | Security deposit (41% missing) |
| `minimum_nights` | int | Minimum booking length |
| `maximum_nights` | int | Maximum booking length |
| `number_of_reviews` | int | Total review count |
| `reviews_per_month` | float | Average reviews per month |
| `review_scores_rating` | int | Overall rating (0-100 scale) |
| `review_scores_accuracy` | int | Accuracy sub-score (0-10) |
| `review_scores_cleanliness` | int | Cleanliness sub-score (0-10) |
| `review_scores_checkin` | int | Check-in sub-score (0-10) |
| `review_scores_communication` | int | Communication sub-score (0-10) |
| `review_scores_location` | int | Location sub-score (0-10) |
| `review_scores_value` | int | Value sub-score (0-10) |
| `availability_365` | int | Days available in next year |
| `calculated_host_listings_count` | int | Number of listings by this host |
| `amenities` | str | Set of amenities (stored as string, needs parsing) |

### Columns That Are Entirely Missing (100% NaN)

`thumbnail_url`, `medium_url`, `xl_picture_url`, `host_acceptance_rate`, `license`, `jurisdiction_names`

## Key Statistics

| Statistic | Value |
|-----------|-------|
| Rows | 29,142 |
| Columns | 96 |
| Median price | $100/night |
| Mean price | $133/night |
| Price range | $0 -- $999 |
| Zero-price listings | 25 |
| Room types | Entire home/apt (52%), Private room (46%), Shared room (2%) |
| Top borough | Manhattan (45%), Brooklyn (42%), Queens (10%) |
| Listings with 0 reviews | ~25% (these lack all review_scores_* data) |

## Naive Analysis Traps

This dataset is specifically chosen because a naive analysis will produce confident but misleading results. Here are the traps:

### 1. Outliers Destroy Regression
Price has a heavy right tail (up to $999/night) and 25 listings at $0. A naive OLS regression on raw prices produces an R^2 of ~0.46 with an RMSE of $76. The model is heavily influenced by expensive listings. Filtering to $1--$500 changes the coefficient estimates substantially but R^2 stays similar (~0.44), revealing the model is poorly specified regardless.

### 2. Missing Data Is Not Random
About 25% of listings have zero reviews and therefore have NaN for all `review_scores_*` columns. Dropping rows with any NaN silently removes all new/unreviewed listings, biasing the sample toward established listings. `weekly_price` (87% missing) and `monthly_price` (99% missing) should not be imputed from `price` because real weekly/monthly discounts vary.

### 3. Spatial Confounding
Latitude and longitude are numeric and will be happily consumed by any regression or PCA. But the relationship between location and price is highly nonlinear: Manhattan listings cost 2--3x more than outer-borough listings at similar distances. A linear function of lat/lon cannot capture borough boundaries, subway proximity, or neighborhood desirability. A naive model will include lat/lon as features without noting this.

### 4. Multicollinearity Among Review Scores
The six `review_scores_*` sub-scores are all correlated > 0.6 with each other and with the overall `review_scores_rating`. Including all of them as features inflates coefficient variance and makes individual coefficients uninterpretable.

### 5. Confident Garbage
A naive analysis that fits OLS, reports R^2, prints coefficients, and declares success will miss that the residual plot shows severe heteroscedasticity (variance increases with predicted price), that the model is misspecified (categorical variables like room_type and neighbourhood are omitted), and that the coefficients are unreliable due to multicollinearity.

### 6. PCA Mixes Geography With Amenities
PCA on numeric features blends lat/lon with accommodates/bedrooms/price into single components. The first PC explains only 26% of variance, and 9 components are needed for 90%. The mixed components are uninterpretable -- what does "0.3*latitude + 0.4*bedrooms" mean?

### 7. K-Means Rediscovers Boroughs
K-Means clustering on features including lat/lon is dominated by spatial separation. Clusters largely correspond to Manhattan vs Brooklyn vs Queens -- information already available in the `neighbourhood_group_cleansed` column. A naive analysis will present these clusters as novel insights.

## Suggested Uses by Lecture

| Lecture | Topic | Suggested Exercise |
|---------|-------|--------------------|
| Lec 5 | Linear Regression | Predict price from numeric features. Compare naive model (all data) vs filtered model (remove outliers). Show that omitting room_type and neighbourhood hurts R^2. Discuss residual plots and heteroscedasticity. |
| Lec 7 | Feature Engineering | Parse amenities string into binary features. Create interaction terms (room_type x borough). Log-transform price. One-hot encode neighbourhood. Show that engineered features dramatically improve R^2. |
| Lec 14 | PCA | Run PCA on numeric features. Discuss why scaling matters (price range vs latitude range). Show that mixing geographic and listing features produces uninterpretable components. Try PCA separately on listing features vs geographic features. |
| Lec 15 | Clustering | Run K-Means with different k. Show that clusters are dominated by geography. Try clustering without lat/lon to find listing-type clusters (budget/mid/luxury). Compare cluster profiles to known room_type categories. |

## Files

- `listings.csv` -- Raw data (29,142 listings x 96 columns)
- `eda.py` -- Exploratory data analysis script (run with `python3 eda.py`)
- `price_dist.png` -- Price distribution histograms (raw and capped at $500)
- `correlations.png` -- Correlation matrix heatmap of numeric features
- `residuals.png` -- Residual plots for naive OLS (all data vs filtered)
