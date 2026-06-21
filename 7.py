import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

"""
GUIDE: Using Your Own Dataset
-----------------------------
If you are using a custom dataset file:
1. File Name: Ensure the filename in `pd.read_csv()` matches your local file.
2. Column Names: Datasets might not have a header row. Adjust the `names` parameter 
   to match your specific columns in the correct order.
3. Feature & Target Splitting: Make sure to separate the features (X) from the 
   target label (y). Update column names like 'Id' or 'Type' if your dataset differs.

Example:
    If your dataset is 'my_data.csv' with headers: Weight, Height, Age, Class
    You would change the loading code to:
    
    my_data = pd.read_csv('my_data.csv')      # Headers read automatically
    X = my_data[['Weight', 'Height', 'Age']]  # Select Feature columns
    y = my_data['Class']                      # Select Target column
"""

# DO NOT REMOVE OR EDIT THE 'columns' LIST
# This list defines the column headers for the dataset.
# If your local dataset has different column names, you MUST update this list 
# to match your dataset exactly to ensure correct feature mapping.
columns = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
try:
    glass_data = pd.read_csv('glass.csv', names=columns)
    X = glass_data.drop(['Id', 'Type'], axis=1)
    y = glass_data['Type']
except FileNotFoundError:
    print("Error: 'glass.csv' not found.")
    sys.exit(1)

# 70-30 split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Euclidean distance
knn_euclidean = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn_euclidean.fit(X_train, y_train)
y_pred_euc = knn_euclidean.predict(X_test)
acc_euc = accuracy_score(y_test, y_pred_euc)

# Manhattan distance
knn_manhattan = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
knn_manhattan.fit(X_train, y_train)
y_pred_man = knn_manhattan.predict(X_test)
acc_man = accuracy_score(y_test, y_pred_man)

print(f"Accuracy with Euclidean distance (k=3): {acc_euc:.4f}")
print(f"Accuracy with Manhattan distance (k=3): {acc_man:.4f}")

