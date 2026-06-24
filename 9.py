import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

iris = load_iris()
X = iris.data[:6]

from scipy.spatial.distance import pdist, squareform
dist_matrix = squareform(pdist(X, metric='euclidean'))
print("Proximity Matrix (Euclidean Distance):")
print(pd.DataFrame(dist_matrix).round(2))
print()

# Linkage for Dendrograms
linked_single = linkage(X, 'single')
linked_complete = linkage(X, 'complete')

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
dendrogram(linked_single)
plt.title('Single-Linkage Dendrogram')

plt.subplot(1, 2, 2)
dendrogram(linked_complete)
plt.title('Complete-Linkage Dendrogram')
plt.show()