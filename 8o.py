import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
K = 3

def kmeans(X, K, max_iters=100):
    np.random.seed(42)
    centroids = X[:K]

    for _ in range(max_iters):
        expanded_x = X[:, np.newaxis]
        euc_dist = np.linalg.norm(expanded_x - centroids, axis=2) #dist = np.sum(np.abs(expanded_x - centroids), axis=2) # Manhattan distance
        labels = np.argmin(euc_dist, axis=1)

        new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])

        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return labels, centroids

labels, centroids = kmeans(X_scaled, K)

print("K-Means clustering completed.")
print("Cluster Centers:\n", centroids)

plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', color='red', s=200, alpha=0.75)
plt.title('K-Means Clustering on Iris Dataset')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()