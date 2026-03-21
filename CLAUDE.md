# MSE 125 Course Book

## Structure
- 19 lectures as .qmd files at repo root, rendered as Quarto book
- `_quarto.yml` — book config (3 acts: Build Models, Trust Models, See Further)
- `data/` — datasets (large CSVs via Git LFS: airbnb, EPA, NBA)
- `DATA_DIR = 'data'` in all .qmd files (not '../data')

## Editing lectures
- Always `quarto render lecNN-slug.qmd` after editing to verify
- Callout syntax: `:::{.callout-important}`, `:::{.callout-tip}`, `:::{.callout-note}`, `:::{.callout-warning}`
- Definitions and key results use `.callout-important`
- "Think about it" prompts use `.callout-tip`
- Historical asides use `.callout-note` (title = story name, not "History")
- Warnings/pitfalls use `.callout-warning`
- Don't label surprises — let the narrative deliver them
- Study guide has 3 parts: `### Key ideas`, `### Computational tools`, `### For the quiz`
- See STYLE_GUIDE.md for tone and cell patterns

## Code conventions
- Setup cell: numpy, pandas, matplotlib, seaborn, warnings suppressed, sns.set_style('whitegrid')
- 5-15 lines per code cell, clear variable names (not x/y)
- Figures: `fig, ax = plt.subplots(figsize=(8, 5))`, seaborn, labeled axes

## CI/CD
- GitHub Actions renders book, generates .ipynb notebooks, deploys to Pages
- Notebooks patched for Colab (DATA_DIR → raw GitHub URL)
- `_notebook-links.lua` adds Colab badge to each chapter
- `code-tools-fix.html` works around Quarto 1.8 code-tools bug

## Course design principles
- Act 1 (Lec 1-7): prediction. Act 2 (Lec 8-13): inference. Don't mix.
- Every hypothesis test needs a concrete $$ decision
- Topics must earn their place — practical utility over textbook completeness
- Real datasets only, no synthetic data
