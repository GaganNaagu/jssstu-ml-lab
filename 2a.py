import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Step 1: Load Data
iris = load_iris()
X = iris.data

# Step 2: Setup Canvas
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Step 3: THE PLOT SPECIFIC CODE GOES HERE
surf = ax.plot_trisurf(X[:, 0], X[:, 1], X[:, 2], cmap='viridis', edgecolor='none')

# Step 4: Add Labels & Show
plt.title('3D Surface Plot of Iris Data (3 Features)')
ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
ax.set_zlabel(iris.feature_names[2])
fig.colorbar(surf)
plt.show()