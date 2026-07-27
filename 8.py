import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = iris.data

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
K = 3

kmeans = KMeans(n_clusters=K, random_state=42)
kmeans.fit(X_scaled)
labels = kmeans.predict(X_scaled)
centroids = kmeans.cluster_centers_

print("K-Means clustering completed.")
print("Cluster Centers:\n", centroids)

plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', color='red', s=200, alpha=0.75)
plt.title('K-Means Clustering on Iris Dataset')
plt.xlabel('Sepal Length (scaled)')
plt.ylabel('Sepal Width (scaled)')
plt.show()