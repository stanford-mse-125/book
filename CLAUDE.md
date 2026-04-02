# Applied Statistics: From Data to Decisions

## Structure
- 19 chapters as .qmd files at repo root, plus `appendix-probability.qmd`
- `_quarto.yml` — book config (3 acts: Build Models, Trust Models, See Further)
- `key-concepts.md` — learning objectives, vocabulary, prerequisites per chapter
- `data/` — datasets (large CSVs via Git LFS)
- `DATA_DIR = 'data'` in all .qmd files
- Chapter titles are topic only (no "Lecture N:" prefix)
- Four modes of reasoning thread the book: summary, prediction, inference, causation

## Rendering
- `quarto render lecNN-slug.qmd` to verify a single chapter
- `quarto render` to build the full book
- `quarto convert lecNN-slug.qmd --output notebooks/lecNN-slug.ipynb` to regenerate a notebook

## Notebooks
- `notebooks/` contains .ipynb versions of each chapter, generated from .qmd via `quarto convert`
- CI/CD regenerates these automatically; to sync locally, run the convert command above for each file

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
