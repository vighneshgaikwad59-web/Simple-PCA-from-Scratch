# Simple PCA from Scratch

A minimal implementation of Principal Component Analysis (PCA) using
only **NumPy**, with no `sklearn` and no black-box magic.

## Why PCA?

Imagine a gene expression dataset: each row is a sample (patient) and each
column is the expression level of one gene. With 500 genes, you can't
visualize the data directly.

PCA finds the directions along which the data varies the most, like a
photographer looking for the angle that shows the subject most clearly.
By projecting the data onto those top directions (the **Principal
Components**), you can bring high-dimensional data down to 2D or 3D
without losing much information.

## How it works

1. **Center the data**: shift each feature so its mean is zero
2. **Covariance matrix**: measure how features vary together
3. **Eigen decomposition**: extract the main directions of the covariance matrix
4. **Sort by eigenvalue**: the direction with the most variance comes first
5. **Project**: map the original data onto the top directions


Cloning an existing copy of this repo? Just run:

```bash
uv sync
```

## Usage

```python
from simple_pca_short import pca
import numpy as np

data = np.random.rand(10, 5)  # 10 samples, 5 features
reduced, variance_ratio = pca(data, n_components=2)

print(reduced)
print("Variance explained:", variance_ratio)
```

Run it with:

```bash
uv run python your_script.py
```

## Requirements

- Python 3.x
- NumPy
- [uv](https://docs.astral.sh/uv/) (optional, but recommended)

## Author

Vighnesh Anand Gaikwad
