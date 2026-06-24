import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Step 1: Load Data
iris = load_iris()
X = iris.data

# Step 2: Setup Canvas

# Step 3: THE PLOT SPECIFIC CODE GOES HERE
cp = plt.tricontourf(X[:, 0], X[:, 1], X[:, 2], levels=14, cmap='viridis')

# Step 4: Add Labels & Show
plt.title('Contour Plot of Iris Data (Sepal L vs Sepal W vs Petal L)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.colorbar(cp)
plt.show()