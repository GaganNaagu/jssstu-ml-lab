import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# If your local dataset has different column names, you MUST update this list 
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