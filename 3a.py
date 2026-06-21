import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

plt.figure(figsize=(8, 6))
# Correlation heatmap is a great way to visualize n-dimensional data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heat-map of Iris Data Correlation')
plt.show()
