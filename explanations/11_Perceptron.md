# Program 11: Single Layer Perceptron (AND / OR Gates)

**Logic / Algorithm:** The Perceptron is the fundamental building block of Neural Networks. It takes inputs, multiplies them by weights, adds a bias, and passes the result through an activation function (like a simple step function: if total > 0, output 1; else 0).
- It is a **Linear Classifier**. It can only solve problems where a straight line can separate the 0s from the 1s.

**Application:** Simulating boolean logic gates. 
- For an `AND` gate, it learns weights so that only [1, 1] crosses the threshold to output 1.

**Real-World Example:** A simple loan approval system. 
Input 1: Income (weight: high). Input 2: Debt (weight: negative). If `(Income * w1) + (Debt * w2) > Threshold`, the loan is approved (1), else denied (0).

**Exam Tip:** Mention that a Single Layer Perceptron **cannot** solve the XOR problem because XOR is not linearly separable. You need a Multi-Layer Perceptron (deep learning) for that!
