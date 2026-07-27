import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
K = 3

def kmeans(X, K, max_iters=100, metric='euclidean'):
    np.random.seed(42)
    centroids = X[:K]

    for _ in range(max_iters):
        expanded_x = X[:, np.newaxis]
        
        if metric == 'euclidean':
            dist = np.linalg.norm(expanded_x - centroids, axis=2)
        elif metric == 'manhattan':
            dist = np.sum(np.abs(expanded_x - centroids), axis=2)
        else:
            raise ValueError("Unsupported metric")
            
        labels = np.argmin(dist, axis=1)

        new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])

        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return labels, centroids

labels_euc, centroids_euc = kmeans(X_scaled, K, metric='euclidean')
labels_man, centroids_man = kmeans(X_scaled, K, metric='manhattan')

print("K-Means (Euclidean) completed.")
print("Cluster Centers (Euclidean):\n", centroids_euc)
print("\nK-Means (Manhattan) completed.")
print("Cluster Centers (Manhattan):\n", centroids_man)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_euc, s=50, cmap='viridis')
plt.scatter(centroids_euc[:, 0], centroids_euc[:, 1], marker='X', color='red', s=200, alpha=0.75)
plt.title('K-Means Clustering (Euclidean)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.subplot(1, 2, 2)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_man, s=50, cmap='viridis')
plt.scatter(centroids_man[:, 0], centroids_man[:, 1], marker='X', color='red', s=200, alpha=0.75)
plt.title('K-Means Clustering (Manhattan)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.tight_layout()
plt.show()