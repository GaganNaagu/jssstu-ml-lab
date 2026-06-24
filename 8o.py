import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def kmeans(X, K, max_iters=100):
  np.random.seed(42)
  centroids = X[np.random.choice(X.shape[0], K, replace=False)]

  for _ in range(max_iters):
    expanded_x = X[:, np.newaxis]
    euc_dist = np.linalg.norm(expanded_x - centroids, axis=2)
    labels = np.argmin(euc_dist, axis=1)

    new_centroids = []
    for k in range(K):
      points = X[labels == k]
      if len(points) > 0:
        new_centroids.append(points.mean(axis=0))
      else:
        new_centroids.append(centroids[k])
    
    new_centroids = np.array(new_centroids)

    if np.all(centroids == new_centroids):
      break

    centroids = new_centroids

  return labels, centroids

X = load_iris().data
K = 3
labels, centroids = kmeans(X, K)

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-means Clustering of Iris Dataset')
plt.show()