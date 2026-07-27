import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

ax = plt.axes(projection='3d')
ax.plot_trisurf(X[:, 0], X[:, 1], X[:, 2], cmap="jet")
ax.set_title("3D Surface Plot")

plt.show()