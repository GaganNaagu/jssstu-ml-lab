import numpy as np

def train_perceptron(X, y, epochs=10, lr=0.1):
    weights = np.zeros(X.shape[1])
    bias = 0
    
    for _ in range(epochs):
        for i in range(len(X)):
            # Step 1: Calculate prediction (1 if w*x + b >= 0 else 0)
            y_hat = 1 if np.dot(X[i], weights) + bias >= 0 else 0
            
            # Step 2: Update weights and bias based on error
            error = y[i] - y_hat
            weights += lr * error * X[i]
            bias += lr * error
            
    return weights, bias

def predict(X, weights, bias):
    return [1 if np.dot(x, weights) + bias >= 0 else 0 for x in X]

# Dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# 1. AND Function
y_and = np.array([0, 0, 0, 1])
w_and, b_and = train_perceptron(X, y_and)

print("AND Function Predictions:")
for x, p in zip(X, predict(X, w_and, b_and)):
    print(f"{x} -> {p}")

print("\n-----------------------\n")

# 2. OR Function
y_or = np.array([0, 1, 1, 1])
w_or, b_or = train_perceptron(X, y_or)

print("OR Function Predictions:")
for x, p in zip(X, predict(X, w_or, b_or)):
    print(f"{x} -> {p}")