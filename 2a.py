import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

ax = plt.subplot(111, projection='3d')

surf = ax.plot_trisurf(X[:, 0], X[:, 1], X[:, 2], cmap='viridis')

plt.title('3D Surface Plot of Iris Data (3 Features)')
ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
ax.set_zlabel(iris.feature_names[2])
plt.colorbar(surf)
plt.show()