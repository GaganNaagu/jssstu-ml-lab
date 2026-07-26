import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def proximity_matrix_from_scratch(X):
    n = len(X)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = euclidean_distance(X[i], X[j])
    return matrix

def linkage_from_scratch(X, method='single'):
    n = len(X)
    clusters = {i: [i] for i in range(n)}
    current_clusters = list(range(n))
    next_cluster_id = n
    Z = []

    def cluster_distance(c1, c2):
        pts1 = [X[idx] for idx in clusters[c1]]
        pts2 = [X[idx] for idx in clusters[c2]]
        dists = [euclidean_distance(p1, p2) for p1 in pts1 for p2 in pts2]
        if method == 'single':
            return min(dists)
        elif method == 'complete':
            return max(dists)
        else:
            raise ValueError("Unknown method")

    while len(current_clusters) > 1:
        min_dist = float('inf')
        best_pair = (None, None)

        for i in range(len(current_clusters)):
            for j in range(i + 1, len(current_clusters)):
                c1, c2 = current_clusters[i], current_clusters[j]
                d = cluster_distance(c1, c2)
                if d < min_dist:
                    min_dist = d
                    best_pair = (c1, c2)

        c1, c2 = best_pair
        new_cluster_id = next_cluster_id
        next_cluster_id += 1

        new_cluster_members = clusters[c1] + clusters[c2]
        clusters[new_cluster_id] = new_cluster_members

        Z.append([c1, c2, min_dist, len(new_cluster_members)])

        current_clusters.remove(c1)
        current_clusters.remove(c2)
        current_clusters.append(new_cluster_id)

    return np.array(Z, dtype=float)

X = load_iris().data[:6]

prox_matrix = proximity_matrix_from_scratch(X)
print("Proximity Matrix (From Scratch):\n", np.round(prox_matrix, 2))

Z_single = linkage_from_scratch(X, method='single')
Z_complete = linkage_from_scratch(X, method='complete')

plt.subplot(1, 2, 1)
dendrogram(Z_single)
plt.title('Single-Linkage (Scratch)')

plt.subplot(1, 2, 2)
dendrogram(Z_complete)
plt.title('Complete-Linkage (Scratch)')

plt.show()
