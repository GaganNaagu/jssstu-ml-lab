import numpy as np

def activation(x):
    return 1 if x > 0 else 0

def perceptron(inputs, weights, bias):
    sum_val = np.dot(inputs, weights) + bias
    return activation(sum_val)

inputs = np.array([[0,0], [0,1], [1,0], [1,1]])

print("AND Gate")
weights_and = np.array([1, 1])
bias_and = -1.5

for x in inputs:
    output = perceptron(x, weights_and, bias_and)
    print(f"Input: {x} -> Output: {output}")

print("\nOR Gate")
weights_or = np.array([1, 1])
bias_or = -0.5

for x in inputs:
    output = perceptron(x, weights_or, bias_or)
    print(f"Input: {x} -> Output: {output}")