import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
X = iris.data

# Use 3 features for 3D surface (trisurf) plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_trisurf(X[:, 0], X[:, 1], X[:, 2], cmap='viridis', edgecolor='none')

plt.title('3D Surface Plot of Iris Data (3 Features)')
ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
ax.set_zlabel(iris.feature_names[2])
fig.colorbar(surf)
plt.show()
