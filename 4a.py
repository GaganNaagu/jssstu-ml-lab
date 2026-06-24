import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Step 1: Load Data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Step 2: Setup Canvas
plt.figure(figsize=(8, 6))

# Step 3: THE PLOT SPECIFIC CODE GOES HERE
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')

# Step 4: Add Labels & Show
plt.title('Heat-map of Iris Data Correlation')
plt.show()