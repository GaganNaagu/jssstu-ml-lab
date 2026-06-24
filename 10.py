from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

lda = LDA(n_components=2)
X_lda = lda.fit_transform(X, y)

plt.figure(figsize=(12, 5))

# Helper function to modularize the repetitive plotting
def plot_scatter(data, title, position):
    plt.subplot(1, 2, position)
    for c, i, target_name in zip(['r', 'g', 'b'], [0, 1, 2], iris.target_names):
        plt.scatter(data[y == i, 0], data[y == i, 1], c=c, label=target_name)
    plt.title(title)
    plt.legend()

plot_scatter(X_pca, 'PCA of Iris dataset', 1)
plot_scatter(X_lda, 'LDA of Iris dataset', 2)

plt.show()