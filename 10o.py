import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def pca_scratch(X, n_components=2):
    X_centered = X - np.mean(X, axis=0)
    cov_matrix = np.cov(X_centered, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    sorted_indices = np.argsort(eigenvalues)[::-1]
    top_vectors = eigenvectors[:, sorted_indices[:n_components]]
    return np.dot(X_centered, top_vectors)

def lda_scratch(X, y, n_components=2):
    n_features = X.shape[1]
    class_labels = np.unique(y)
    mean_overall = np.mean(X, axis=0)

    S_W = np.zeros((n_features, n_features))
    S_B = np.zeros((n_features, n_features))

    for c in class_labels:
        X_c = X[y == c]
        mean_c = np.mean(X_c, axis=0)
        S_W += np.dot((X_c - mean_c).T, (X_c - mean_c))

        n_c = X_c.shape[0]
        mean_diff = (mean_c - mean_overall).reshape(-1, 1)
        S_B += n_c * np.dot(mean_diff, mean_diff.T)

    A = np.linalg.pinv(S_W).dot(S_B)
    eigenvalues, eigenvectors = np.linalg.eig(A)

    sorted_indices = np.argsort(np.real(eigenvalues))[::-1]
    top_vectors = np.real(eigenvectors[:, sorted_indices[:n_components]])

    return np.dot(X, top_vectors)

iris = load_iris()
X = iris.data
y = iris.target

X_pca = pca_scratch(X, n_components=2)
X_lda = lda_scratch(X, y, n_components=2)

def plot_scatter(data, title, position):
    plt.subplot(1, 2, position)
    plt.scatter(data[:, 0], data[:, 1], c=y, cmap='viridis')
    plt.title(title)

plot_scatter(X_pca, 'PCA of Iris dataset (Scratch)', 1)
plot_scatter(X_lda, 'LDA of Iris dataset (Scratch)', 2)

plt.show()
