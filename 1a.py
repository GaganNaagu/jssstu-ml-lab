import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

plt.figure(figsize=(8, 6))

# Scatter plot of the first two dimensions (Sepal Length vs Sepal Width)
scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=50, alpha=0.8)

plt.title('Scatter Plot of Iris Data (Sepal Length vs Sepal Width)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# Add a legend
handles, _ = scatter.legend_elements()
plt.legend(handles, iris.target_names, title="Classes")

plt.show()

