import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Step 1: Load Data
iris = load_iris()
X = iris.data

# Step 2: Setup Canvas
plt.figure(figsize=(8, 6))

# Step 3: THE PLOT SPECIFIC CODE GOES HERE
plt.boxplot(X, tick_labels=iris.feature_names)

# Step 4: Add Labels & Show
plt.title('Box-plot of Iris Dataset Features')
plt.ylabel('Centimeters')
plt.show()