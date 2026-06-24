import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform

X = load_iris().data[:6]

print("Proximity Matrix:\n", np.round(squareform(pdist(X, 'euclidean')), 2))

plt.subplot(1, 2, 1)
dendrogram(linkage(X, 'single'))
plt.title('Single-Linkage')

plt.subplot(1, 2, 2)
dendrogram(linkage(X, 'complete'))
plt.title('Complete-Linkage')

plt.show()