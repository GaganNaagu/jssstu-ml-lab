import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

iris = load_iris()
X = iris.data

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

# Agglomerative Clustering
agg_single = AgglomerativeClustering(n_clusters=3, linkage='single')
labels_single = agg_single.fit_predict(X)

agg_complete = AgglomerativeClustering(n_clusters=3, linkage='complete')
labels_complete = agg_complete.fit_predict(X)

print("Single Linkage Labels:", labels_single[:10])
print("Complete Linkage Labels:", labels_complete[:10])

