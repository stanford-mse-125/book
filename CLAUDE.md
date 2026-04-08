# Applied Statistics: From Data to Decisions

## Structure
- 19 chapters as .qmd files at repo root, plus `appendix-probability.qmd`
- `_quarto.yml` — book config (3 acts: Build Models, Trust Models, See Further)
- `key-concepts.md` — learning objectives, vocabulary, prerequisites per chapter
- `data/` — datasets (large CSVs hosted on GitHub Release `data-v1`, small files committed normally)
- `DATA_DIR = 'data'` in all .qmd files
- Run `bash scripts/download-data.sh` after cloning to fetch large data files
- For content standards, style rules, and authoring conventions, see the `/write-chapter` skill

## Rendering
- `quarto render lecNN-slug.qmd` to verify a single chapter
- `quarto render` to build the full book
- `quarto convert lecNN-slug.qmd --output notebooks/lecNN-slug.ipynb` to regenerate a notebook

## Notebooks
- `notebooks/` contains .ipynb versions of each chapter, generated from .qmd via `quarto convert`
- CI/CD regenerates these automatically; to sync locally, run the convert command above for each file

## Callout syntax
See `/write-chapter` skill for full details. Quick reference: important=definitions, tip=discussion, note=asides, warning=pitfalls.

## CI/CD
- GitHub Actions renders book, generates .ipynb notebooks, deploys to Pages
- CI downloads large data files from GitHub Release `data-v1` (no LFS needed)
- Notebooks patched for Colab (DATA_DIR → raw GitHub URL or release URL)
- `_notebook-links.lua` adds Colab badge to each chapter

## For style guide, course plan, review pipeline, and all design decisions
See the dev repo: mse125-dev/docs/
