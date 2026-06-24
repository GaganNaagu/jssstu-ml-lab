import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def kmeans(X, K):
    np.random.seed(42)
    centroids = X[np.random.choice(len(X), K, replace=False)]
    
    for _ in range(100):
        # 1. Assign each point to the closest centroid
        labels = np.argmin(np.linalg.norm(X[:, None] - centroids, axis=2), axis=1)
        
        # 2. Calculate new centroids from the points
        new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])
        
        # 3. Stop if centroids haven't changed
        if np.array_equal(centroids, new_centroids): 
            break
        centroids = new_centroids
        
    return labels, centroids

X = load_iris().data
labels, centroids = kmeans(X, 3)

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='red', s=200)
plt.show()