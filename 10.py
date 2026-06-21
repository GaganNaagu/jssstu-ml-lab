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

plt.subplot(1, 2, 1)
for c, i, target_name in zip(['r', 'g', 'b'], [0, 1, 2], iris.target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], c=c, label=target_name)
plt.title('PCA of Iris dataset')
plt.legend()

plt.subplot(1, 2, 2)
for c, i, target_name in zip(['r', 'g', 'b'], [0, 1, 2], iris.target_names):
    plt.scatter(X_lda[y == i, 0], X_lda[y == i, 1], c=c, label=target_name)
plt.title('LDA of Iris dataset')
plt.legend()

plt.show()

