import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

glass_data = pd.read_csv('glass.csv')

X = glass_data.drop('Type', axis=1)
y = glass_data['Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

def custom_euclidean(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def custom_manhattan(x1, x2):
    return np.sum(np.abs(x1 - x2))

def evaluate_knn(metric_type):
    knn = KNeighborsClassifier(n_neighbors=3, metric=metric_type)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return accuracy_score(y_test, y_pred)

print(f"Accuracy with Euclidean distance (k=3): {evaluate_knn(custom_euclidean):.4f}")
print(f"Accuracy with Manhattan distance (k=3): {evaluate_knn(custom_manhattan):.4f}")