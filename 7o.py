import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split

class KNNScratch:
    def __init__(self, k=3, metric='euclidean'):
        self.k = k
        self.metric = metric

    def fit(self, X, y):
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def _compute_distance(self, x1, x2):
        if self.metric == 'euclidean':
            return np.sqrt(np.sum((x1 - x2) ** 2))
        elif self.metric == 'manhattan':
            return np.sum(np.abs(x1 - x2))
        else:
            raise ValueError("Unsupported metric")

    def predict(self, X):
        X = np.array(X)
        y_pred = [self._predict_one(x) for x in X]
        return np.array(y_pred)

    def _predict_one(self, x):
        distances = [self._compute_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

glass_data = pd.read_csv('glass.csv')

X = glass_data.drop('Type', axis=1)
y = glass_data['Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

def evaluate_knn_scratch(metric_type):
    knn = KNNScratch(k=3, metric=metric_type)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = np.mean(y_pred == np.array(y_test))
    return accuracy

print("K-Nearest Neighbors (From Scratch)")
print(f"Accuracy with Euclidean distance (k=3): {evaluate_knn_scratch('euclidean'):.4f}")
print(f"Accuracy with Manhattan distance (k=3): {evaluate_knn_scratch('manhattan'):.4f}")
