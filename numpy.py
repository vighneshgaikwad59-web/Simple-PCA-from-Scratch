

import numpy as np


def pca(X, n_components=2):
    X = np.asarray(X, dtype=float)

    # Step 1: Center the data (har gene ko apne mean ke around laao)
    mean = X.mean(axis=0)
    X_centered = X - mean

    # Step 2: Covariance matrix — genes aapas mein kaise vary karte hain
    cov_matrix = np.cov(X_centered, rowvar=False)

    # Step 3: Eigen decomposition — main directions (PCs) nikalo
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # Step 4: Sabse zyada variance wali direction pehle
    order = np.argsort(eigenvalues)[::-1]
    top_vectors = eigenvectors[:, order][:, :n_components]
    top_values = eigenvalues[order][:n_components]

    # Step 5: Data ko un top directions pe project karo
    X_reduced = X_centered @ top_vectors
    explained_ratio = top_values / eigenvalues.sum()

    return X_reduced, explained_ratio


if __name__ == "__main__":
    # Demo: 3 healthy + 3 disease samples, 4 genes
    np.random.seed(42)
    healthy = np.random.normal(5, 1, (3, 4))
    disease = np.random.normal(9, 1, (3, 4))
    data = np.vstack([healthy, disease])

    reduced, variance_ratio = pca(data, n_components=2)

    print("Reduced data (2D):\n", reduced.round(2))
    print("Variance explained by PC1, PC2:", variance_ratio.round(3))
