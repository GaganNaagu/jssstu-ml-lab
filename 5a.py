import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data


plt.boxplot(X, tick_labels=iris.feature_names)

plt.title('Box-plot of Iris Dataset Features')
plt.ylabel('Centimeters')
plt.show()