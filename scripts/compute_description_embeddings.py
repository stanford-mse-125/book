"""
Precompute sentence-embedding vectors for the `description` field of every
Airbnb listing that survives the chapter's numeric-feature dropna() filter.

Outputs (relative to repo root):
  - data/airbnb/description_embeddings.npy
  - data/airbnb/description_embeddings_index.csv
  - data/airbnb/description_embeddings_meta.json

Run once offline. Students never run this. Total runtime on Apple Silicon MPS
with all-mpnet-base-v2 is a few minutes.

Spec preference: intfloat/e5-mistral-7b-instruct (4096-d). Fallback used here:
sentence-transformers/all-mpnet-base-v2 (768-d) -- chosen because the spec
model is ~14 GB and does not fit comfortably on Apple Silicon unified memory.
See chapter prose for narrative implications.
"""

import json
import os
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer


# Match the chapter's numeric column list exactly so embeddings align with df.
NUMERIC_COLS = [
    "accommodates", "bathrooms", "bedrooms", "beds", "price",
    "minimum_nights", "maximum_nights", "number_of_reviews",
    "reviews_per_month", "review_scores_rating", "review_scores_accuracy",
    "review_scores_cleanliness", "review_scores_checkin",
    "review_scores_communication", "review_scores_location",
    "review_scores_value", "availability_30", "availability_60",
    "availability_90", "availability_365",
    "calculated_host_listings_count", "latitude", "longitude",
]

MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
# all-mpnet-base-v2 does not require an instruction prefix.
INSTRUCTION_PREFIX = ""
NORMALIZE = True
DTYPE = "float32"


def clean_listings(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, low_memory=False)
    if df["price"].dtype == object:
        df["price"] = (
            df["price"].replace(r"[\$,]", "", regex=True).astype(float)
        )
    if "bathrooms" not in df.columns and "bathrooms_text" in df.columns:
        df["bathrooms"] = (
            df["bathrooms_text"].str.extract(r"(\d+\.?\d*)")[0].astype(float)
        )
    return df


def main():
    here = Path(__file__).resolve().parent.parent
    listings_path = here / "data" / "airbnb" / "listings.csv"
    out_dir = here / "data" / "airbnb"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading {listings_path} ...")
    airbnb = clean_listings(listings_path)
    print(f"Raw: {len(airbnb):,} rows")

    # Match chapter: keep rows where all NUMERIC_COLS are present.
    df = airbnb.dropna(subset=NUMERIC_COLS).copy()
    print(f"After numeric dropna: {len(df):,} rows")

    # Use description; fall back to name when description is missing/empty.
    text = df["description"].fillna("").astype(str)
    fallback = df["name"].fillna("").astype(str)
    text = text.where(text.str.strip().str.len() > 0, fallback)
    # Drop rows with empty text after fallback.
    keep = text.str.strip().str.len() > 0
    df = df.loc[keep].copy()
    text = text.loc[keep]
    print(f"After text-availability filter: {len(df):,} rows")

    device = "mps" if torch.backends.mps.is_available() else (
        "cuda" if torch.cuda.is_available() else "cpu"
    )
    print(f"Device: {device}")
    print(f"Loading model {MODEL_NAME} ...")
    model = SentenceTransformer(MODEL_NAME, device=device)

    inputs = ([INSTRUCTION_PREFIX + t for t in text]
              if INSTRUCTION_PREFIX else text.tolist())
    print(f"Encoding {len(inputs):,} descriptions ...")
    emb = model.encode(
        inputs,
        batch_size=64,
        show_progress_bar=True,
        normalize_embeddings=NORMALIZE,
        convert_to_numpy=True,
    ).astype(np.float32)

    print(f"Embeddings shape: {emb.shape}, dtype {emb.dtype}")

    np.save(out_dir / "description_embeddings.npy", emb)
    pd.DataFrame({"listing_id": df["id"].values}).to_csv(
        out_dir / "description_embeddings_index.csv", index=False
    )

    meta = {
        "model": MODEL_NAME,
        "revision": "main",
        "instruction_prefix": INSTRUCTION_PREFIX,
        "normalize": NORMALIZE,
        "dtype": DTYPE,
        "dimension": int(emb.shape[1]),
        "n_rows": int(emb.shape[0]),
        "date": str(date.today()),
        "fallback_note": (
            "Spec calls for intfloat/e5-mistral-7b-instruct (4096-d); "
            "used all-mpnet-base-v2 (768-d) because spec model exceeds "
            "available VRAM/unified memory on consumer Apple Silicon."
        ),
    }
    with open(out_dir / "description_embeddings_meta.json", "w") as f:
        json.dump(meta, f, indent=2)

    print("Wrote:")
    print(f"  {out_dir / 'description_embeddings.npy'}")
    print(f"  {out_dir / 'description_embeddings_index.csv'}")
    print(f"  {out_dir / 'description_embeddings_meta.json'}")


if __name__ == "__main__":
    main()
