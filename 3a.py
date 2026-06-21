import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
X = iris.data

# Use 2 features for Contour plot (tricontourf) with 3rd feature as Z
plt.figure()
cp = plt.tricontourf(X[:, 0], X[:, 1], X[:, 2], levels=14, cmap='viridis')
plt.colorbar(cp)
plt.title('Contour Plot of Iris Data (Sepal L vs Sepal W vs Petal L)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()
