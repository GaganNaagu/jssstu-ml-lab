import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


glass_data = pd.read_csv('glass.csv', header=None)
X = glass_data.iloc[:, 1:-1]
y = glass_data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

def evaluate_knn(metric_type):
    knn = KNeighborsClassifier(n_neighbors=3, metric=metric_type)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return accuracy_score(y_test, y_pred)

print(f"Accuracy with Euclidean distance (k=3): {evaluate_knn('euclidean'):.4f}")
print(f"Accuracy with Manhattan distance (k=3): {evaluate_knn('manhattan'):.4f}")