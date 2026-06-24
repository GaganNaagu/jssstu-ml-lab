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

# Helper function to modularize the repetitive plotting
def plot_scatter(data, title, position):
    plt.subplot(1, 2, position)
    # c=y automatically colors the points based on their class (0, 1, or 2)
    plt.scatter(data[:, 0], data[:, 1], c=y)
    plt.title(title)

plot_scatter(X_pca, 'PCA of Iris dataset', 1)
plot_scatter(X_lda, 'LDA of Iris dataset', 2)

plt.show()