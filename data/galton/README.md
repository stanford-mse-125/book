# Galton family heights

Francis Galton's 1886 dataset from "Regression towards mediocrity in hereditary stature" (Journal of the Anthropological Institute, Vol. 15). 934 adult children from 205 families, with heights of father, mother, and each child.

## Columns

- `family` — family identifier
- `father` — father's height (inches)
- `mother` — mother's height (inches)
- `midparentHeight` — Galton's "midparent" height = (father + 1.08 × mother) / 2
- `children` — total number of adult children in this family
- `childNum` — which child (1 = firstborn)
- `gender` — male or female
- `childHeight` — adult height of this child (inches)

## Galton's analysis

Galton multiplied female heights (both mothers and daughters) by 1.08 to put everyone on a common male scale. He then regressed child height on midparent height and found a slope less than 1 — extreme parents had children who were extreme in the same direction, but less so. He called the phenomenon "regression toward mediocrity" (now called **regression to the mean**).

On the full dataset with female child heights multiplied by 1.08, the slope is about 0.71 and the correlation is about 0.50. Galton's own estimate of the slope was 2/3.

## Source

Retrieved from Data 8 (Berkeley) at `https://www.inferentialthinking.com/data/galton.csv`. Originally compiled from Galton's 1886 publication.
