import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform

# Load just 6 samples for a clean dendrogram
X = load_iris().data[:6]

# Print distance matrix
print("Proximity Matrix:\n", squareform(pdist(X, 'euclidean')), 2))

plt.figure(figsize=(12, 5))

# Single Linkage
plt.subplot(1, 2, 1)
dendrogram(linkage(X, 'single'))
plt.title('Single-Linkage')

# Complete Linkage
plt.subplot(1, 2, 2)
dendrogram(linkage(X, 'complete'))
plt.title('Complete-Linkage')

plt.show()