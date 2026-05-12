#!/usr/bin/env bash
# Download large data files from the GitHub Release (data-v1).
# These files are too large for Git LFS free tier, so they're hosted as release assets.
# Run this once after cloning the repo: bash scripts/download-data.sh

set -euo pipefail

REPO="stanford-mse-125/book"
TAG="data-v1"

# Map: release asset name → local path
declare -A FILES=(
  ["listings.csv"]="data/airbnb/listings.csv"
  ["daily_aqi_by_county_2021.csv"]="data/epa-air-quality/daily_aqi_by_county_2021.csv"
  ["daily_aqi_by_county_2022.csv"]="data/epa-air-quality/daily_aqi_by_county_2022.csv"
  ["daily_aqi_by_county_2023.csv"]="data/epa-air-quality/daily_aqi_by_county_2023.csv"
  ["daily_aqi_by_county_2024.csv"]="data/epa-air-quality/daily_aqi_by_county_2024.csv"
  ["nba_load_management.csv"]="data/nba/nba_load_management.csv"
  ["nba_game_logs_2022_2024.csv"]="data/nba/nba_game_logs_2022_2024.csv"
  ["sp100_daily_returns_2014_2024.csv"]="data/stocks/sp100_daily_returns_2014_2024.csv"
  ["description_embeddings.npy"]="data/airbnb/description_embeddings.npy"
)

downloaded=0
skipped=0

for asset in "${!FILES[@]}"; do
  dest="${FILES[$asset]}"
  if [[ -f "$dest" ]]; then
    echo "  skip: $dest (already exists)"
    ((skipped++))
    continue
  fi
  mkdir -p "$(dirname "$dest")"
  echo "  downloading: $asset → $dest"
  gh release download "$TAG" --repo "$REPO" --pattern "$asset" --output "$dest"
  ((downloaded++))
done

echo ""
echo "Done: $downloaded downloaded, $skipped skipped."
