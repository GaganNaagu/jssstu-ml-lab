import numpy as np

def activation(x):
    return 1 if x > 0 else 0

def perceptron(inputs, weights, bias):
    sum_val = np.dot(inputs, weights) + bias
    return activation(sum_val)

inputs = np.array([[0,0], [0,1], [1,0], [1,1]])

print("AND Gate")
weights = np.array([1, 1])

for x in inputs:
    output = perceptron(x, weights, -1.5)
    print(f"Input: {x} -> Output: {output}")

print("\nOR Gate")

for x in inputs:
    output = perceptron(x, weights, -0.5)
    print(f"Input: {x} -> Output: {output}")