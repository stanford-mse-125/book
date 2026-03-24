# MSE 125 Course Book

## Structure
- 19 lectures as .qmd files at repo root, rendered as Quarto book
- `_quarto.yml` — book config (3 acts: Build Models, Trust Models, See Further)
- `data/` — datasets (large CSVs via Git LFS)
- `DATA_DIR = 'data'` in all .qmd files

## Rendering
- `quarto render lecNN-slug.qmd` to verify a single lecture
- `quarto render` to build the full book

## Callout syntax
- `:::{.callout-important}` — definitions and key results (styled blue via custom.scss)
- `:::{.callout-tip}` — "Think about it" discussion prompts
- `:::{.callout-note}` — historical asides, conceptual previews (title = story/concept name)
- `:::{.callout-warning}` — pitfalls and common errors

## CI/CD
- GitHub Actions renders book, generates .ipynb notebooks, deploys to Pages
- Notebooks patched for Colab (DATA_DIR → raw GitHub URL)
- `_notebook-links.lua` adds Colab badge to each chapter

## For style guide, course plan, review pipeline, and all design decisions
See the dev repo: mse125-dev/docs/
