import numpy as np

def activation(x):
    return 1 if x > 0 else 0

inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
targets = np.array([0, 0, 0, 1])

weights = np.random.rand(2)
bias = np.random.rand(1)[0]
learning_rate = 0.1

for epoch in range(15):
    total_error = 0
    for x, target in zip(inputs, targets):
        prediction = activation(np.dot(x, weights) + bias)
        error = target - prediction
        total_error += abs(error)
        weights += learning_rate * error * x
        bias += learning_rate * error
        
    print(f"Epoch {epoch+1} - Errors: {total_error} | Weights: {weights}, Bias: {bias:.2f}")
    if total_error == 0:
        break

print(f"\nFinal Learned Weights: {weights}, Final Learned Bias: {bias:.2f}")
for x in inputs:
    print(f"Input: {x} -> Output: {activation(np.dot(x, weights) + bias)}")
