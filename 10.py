from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

lda = LDA(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

print("Original shape of data:", X.shape)

print("\nShape of PCA transformed data:", X_pca.shape)
print("\nShape of LDA transformed data:", X_lda.shape)

def plot_scatter(data, title, position):
    plt.subplot(1, 2, position)
    plt.scatter(data[:, 0], data[:, 1], c=y)
    plt.title(title)

plot_scatter(X_pca, 'PCA of Iris dataset (Scaled)', 1)
plot_scatter(X_lda, 'LDA of Iris dataset (Scaled)', 2)

plt.show()