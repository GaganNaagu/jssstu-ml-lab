import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Step 1: Load Data
iris = load_iris()
X = iris.data
y = iris.target

# Step 2: Setup Canvas
plt.figure(figsize=(8, 6))

# Step 3: THE PLOT SPECIFIC CODE GOES HERE
scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=50, alpha=0.8)

# Step 4: Add Labels & Show
plt.title('Scatter Plot of Iris Data (Sepal Length vs Sepal Width)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# Add a legend
handles, _ = scatter.legend_elements()
plt.legend(handles, iris.target_names, title="Classes")

plt.show()