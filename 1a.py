import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target


scatter = plt.scatter(X[:, 0], X[:, 1], c=y)

plt.title('Scatter Plot of Iris Data (Sepal Length vs Sepal Width)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.show()