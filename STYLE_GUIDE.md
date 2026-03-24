# MSE 125 Notebook Style Guide

## Format
Each lecture gets one unified Jupyter notebook (.ipynb) in `course-notes/` that serves as BOTH course notes AND in-class demo. Save as `lec{NN}-{slug}.ipynb` (e.g., `lec01-intro.ipynb`).

## Narrative structure

### Opening (1-2 cells)
Start with a real question that has stakes. Not "today we learn about regression" but "An Airbnb host wants to know: am I charging too much? too little? Let's find out."

### Build intuition (5-10 cells)
Show the data first. Let students see it, touch it, plot it. Build up the concept through concrete examples before any abstraction. Use the Data 8 pattern: concrete → visual → pattern → formalization.

### The method (5-10 cells)
Introduce the technique through the data, not abstractly. The formula appears AFTER you've seen it work. Walk through one worked example in detail. Code should be readable — favor clarity over cleverness.

### The surprise (2-5 cells)
The Big Messy Data moment. Something unexpected that a naive analysis (or an AI) would miss:
- Simpson's paradox in the hospital data
- Outliers destroying a regression on Airbnb
- Multiple comparisons producing "significant" results from noise on NBA data
- AI silently dropping rows and producing plausible-looking nonsense

This is what makes the course memorable. Every notebook needs at least one genuine surprise.

### Key takeaway (1-2 cells)
What did we learn? What should you check next time? Keep it short — 3-5 bullet points max.

## Cell patterns

### Markdown cells
- Conversational, second person ("you", "let's", "notice that...")
- Short paragraphs (2-3 sentences max)
- **Bold** key terms when first introduced
- Use questions to drive the narrative: "What happens if we remove the outliers?"
- Include "Think about it" prompts for in-class discussion
- LaTeX math inline ($x$) and display ($$) where needed, but always AFTER intuition

### Code cells
- 5-15 lines per cell (never walls of code)
- Clear variable names (not `x`, `y` — use `prices`, `readmission_rate`)
- Comments only where non-obvious
- Print/display intermediate results so students can follow along
- Use pandas, numpy, matplotlib, seaborn, sklearn (NOT the Data 8 `datascience` library)
- Suppress warnings in the setup cell

### Figure cells
- Use seaborn with clear axis labels and titles
- Figures should be self-explanatory
- Add annotations for key features (outliers, trends, thresholds)
- Prefer `fig, ax = plt.subplots(figsize=(8, 5))` for consistent sizing

## Setup cell (first cell of every notebook)
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (8, 5)
plt.rcParams['font.size'] = 12

# Load data
DATA_DIR = 'data'  # For .qmd files at repo root; '../data' for .ipynb in course-notes/
```

## Tone and prose style
- Scholarly but accessible. Aim for Cambridge University Press, not clickbait.
- Every sentence must communicate a new idea. No filler, no fluff, no bombast.
- Show before tell: demonstrate ideas computationally, then name them.
- Mathematical concepts (even simple ones like correlation) must be defined and demonstrated.
- Do not namedrop concepts without explaining them.
- Minimal words; each one should carry meaning.
- Credit the data. Real datasets have stories; tell them briefly.

### Grammar rules
- "This" must ALWAYS be followed by a noun. Never "This means..." or "This happens because..." — instead "This technique improves..." or "This pattern suggests..."
- Avoid "because" constructions — rephrase for flow. Prefer causal structure in the sentence itself.
- Vary sentence structure. Do not overuse colon-fronted patterns ("Think about it: ...", "The key insight: ...").
- Prefer active voice. Prefer concrete subjects over abstract ones.

## Cross-references
- Reference previous notebooks: "Recall from Lecture 5 that regression finds the projection onto..."
- Reference MS&E 120: "You saw in probability that the CLT says..."
- Reference VMLS: "If you've taken EE103, you'll recognize this as..."
- Reference future topics: "We'll revisit this hospital data in Lecture 18 when we ask: is this causal?"

## Data paths
All datasets are in `../data/{dataset-name}/`:
- `../data/hospital-readmissions/` — Hospital readmissions (CMS)
- `../data/airbnb/` — Airbnb NYC listings
- `../data/clinical-trial/` — ACTG 175 clinical trial
- `../data/nba/` — NBA load management game logs
- `../data/college-scorecard/` — College Scorecard
- `../data/framingham/` — Framingham Heart Study
- `../data/epa-air-quality/` — EPA air quality (CA)
- `../data/john-snow/` — John Snow cholera
