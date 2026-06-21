import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
data = [iris.data[:, i] for i in range(iris.data.shape[1])]

plt.figure(figsize=(8, 6))
plt.boxplot(data, vert=True, patch_artist=True, tick_labels=iris.feature_names)
plt.title('Box-plot of Iris Dataset Features')
plt.ylabel('Centimeters')
plt.show()
