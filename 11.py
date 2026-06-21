import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size + 1) # +1 for bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        z = self.weights.T.dot(np.insert(x, 0, 1)) # insert 1 for bias
        return self.activation(z)

    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(y.shape[0]):
                x_i = np.insert(X[i], 0, 1)
                y_hat = self.activation(self.weights.T.dot(x_i))
                self.weights = self.weights + self.learning_rate * (y[i] - y_hat) * x_i

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# AND function
y_and = np.array([0, 0, 0, 1])
perceptron_and = Perceptron(input_size=2)
perceptron_and.train(X, y_and)

print("AND Function Predictions:")
for x in X:
    print(f"{x} -> {perceptron_and.predict(x)}")
    
print("\n-----------------------\n")

# OR function
y_or = np.array([0, 1, 1, 1])
perceptron_or = Perceptron(input_size=2)
perceptron_or.train(X, y_or)

print("OR Function Predictions:")
for x in X:
    print(f"{x} -> {perceptron_or.predict(x)}")

