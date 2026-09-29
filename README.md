# Simple PCA from Scratch

A minimal implementation of Principal Component Analysis (PCA) using
only **NumPy** — no `sklearn`, no black-box magic.

## Why PCA?

Socho tumhare paas ek gene expression dataset hai — har row ek sample
(patient), har column ek gene ka expression level. Agar 500 genes hain,
toh data ko visualize karna impossible hai.

PCA data mein sabse zyada **variation** (spread) kis direction mein hai
woh dhundta hai — jaise photographer best angle dhundta hai jahan se
subject sabse clearly dikhe. Un top directions (**Principal Components**)
pe data ko project karke hum high-dimensional data ko 2D/3D mein la
sakte hain, bina zyada information khoye.

## How it works

1. **Center the data** — har feature ko apne mean ke around laao
2. **Covariance matrix** — dekho features aapas mein kaise vary karte hain
3. **Eigen decomposition** — covariance matrix ki main directions nikalo
4. **Sort by eigenvalue** — sabse zyada variance wali direction pehle
5. **Project** — original data ko un top directions pe daalo

## Usage

```python
from simple_pca_short import pca
import numpy as np

data = np.random.rand(10, 5)  # 10 samples, 5 features
reduced, variance_ratio = pca(data, n_components=2)

print(reduced)
print("Variance explained:", variance_ratio)
```

## Demo

Running the script directly gives a toy example: 3 "healthy" + 3
"disease" samples across 4 genes, reduced to 2D.



PC1 alone captures ~88% of the variance — clearly separating healthy vs
disease samples.

## Requirements

- Python 3.x
- NumPy

## Author

Vighnesh Anand Gaikwad
