# Experiment 11: Single-Layer Perceptron (AND & OR Gates)

This document covers the theoretical concepts, code explanation, and viva questions for the eleventh and final lab experiment: `11.py`.

---

## Theoretical Background
The **Perceptron** is the simplest form of an Artificial Neural Network, invented in 1957 by Frank Rosenblatt. It is a single-layer neural network used for binary classification. It models how a biological neuron works.

**How a Perceptron works:**
1. **Inputs**: It takes a vector of inputs `(x1, x2, ..., xn)`.
2. **Weights**: Each input is multiplied by a corresponding weight `(w1, w2, ..., wn)`. Weights determine the importance of an input.
3. **Bias**: A bias term `(b)` is added to the weighted sum. The bias acts as a threshold shifter, allowing the activation function to shift left or right.
4. **Summation**: Compute the weighted sum: `S = (x1*w1 + x2*w2 + ... + xn*wn) + b` or mathematically `S = (w • x) + b`.
5. **Activation Function**: The sum `S` is passed through an activation function (often a Step Function) to constrain the output to binary values (0 or 1).

**Limitations:**
A single-layer perceptron can only solve **linearly separable** problems. Linearly separable means you can draw a single straight line on a graph to separate the 0 outputs from the 1 outputs. It works perfectly for AND and OR gates, but it **cannot solve the XOR problem**.

---

## Code Walkthrough (`11.py`)
1. **Inputs and Weights**:
   - `inputs = [[0,0], [0,1], [1,0], [1,1]]`: Represents the four possible boolean combinations for a 2-input logic gate.
   - `weights = np.array([1, 1])`: The perceptron applies a weight of 1 to both inputs.
2. **The Perceptron Function**:
   - `sum_val = np.dot(inputs, weights) + bias`: Uses numpy's dot product to multiply each input by its weight and add them together, then adds the bias.
   - `return activation(sum_val)`: Passes the sum to the activation function.
3. **Activation Function**:
   - `return 1 if x > 0 else 0`: A simple binary step function. If the weighted sum + bias is greater than zero, the neuron "fires" (returns 1). Otherwise, it stays dormant (returns 0).
4. **Simulating the Gates (The magic of Bias)**:
   - **AND Gate**: The bias is set to `-1.5`. 
     - If input is [1,1], sum is (1*1 + 1*1) - 1.5 = 0.5. (Fires -> 1)
     - If input is [1,0], sum is (1*1 + 0*1) - 1.5 = -0.5. (Doesn't fire -> 0)
   - **OR Gate**: The bias is set to `-0.5`.
     - If input is [1,0], sum is (1*1 + 0*1) - 0.5 = 0.5. (Fires -> 1)
     - If input is [0,0], sum is (0*1 + 0*1) - 0.5 = -0.5. (Doesn't fire -> 0)

*Note: By simply changing the bias threshold, the exact same neural network structure completely changes its logical behavior from AND to OR.*

---

## Viva Questions

### Program-Specific Questions
**Q1: What does `np.dot(inputs, weights)` do in this program?**
*Answer:* It calculates the dot product between the input array and the weight array. Mathematically, it multiplies the first input by the first weight, the second input by the second weight, and adds those products together.

**Q2: What type of activation function is used in `11.py`?**
*Answer:* It uses a **Binary Step Function** (also known as a Heaviside step function). It outputs a 1 if the input is greater than 0, and a 0 otherwise.

**Q3: How does changing the bias from `-1.5` to `-0.5` change the gate from AND to OR?**
*Answer:* The weights are both 1. For an AND gate, we only want the neuron to fire if *both* inputs are 1 (sum = 2). A bias of `-1.5` means the sum must overcome 1.5 to be > 0. For an OR gate, we want it to fire if *at least one* input is 1 (sum = 1). A bias of `-0.5` lowers the threshold, allowing a sum of 1 to easily surpass 0.

**Q4: What are the predetermined weights used in this program?**
*Answer:* The weights for both inputs are hardcoded to `1` (`np.array([1, 1])`). This is a demonstration of inference; a real perceptron algorithm would start with random weights and learn these values via backpropagation or the perceptron learning rule.

**Q5: Why does this program not have a `.fit()` or training function?**
*Answer:* Because the weights and biases have been manually calculated and hardcoded by the programmer. The program only demonstrates the forward pass (inference) of a perceptron, not the training phase.

### General Theory Questions
**Q6: What is a biological analog to the weights in a perceptron?**
*Answer:* The weights represent the strength of the synapses (connections) between biological neurons. A higher weight means the incoming signal has a stronger influence on whether the receiving neuron will fire.

**Q7: Can a single-layer perceptron learn the XOR logic gate?**
*Answer:* No. The XOR (Exclusive OR) problem is not linearly separable. You cannot draw a single straight line on a 2D graph to separate the positive cases from the negative cases of XOR.

**Q8: How do you solve the XOR problem?**
*Answer:* To solve non-linearly separable problems like XOR, you need a Multi-Layer Perceptron (MLP)—a neural network with at least one hidden layer and non-linear activation functions.

**Q9: What is the purpose of the Bias in a neural network?**
*Answer:* The bias allows the activation function to be shifted to the left or right, independently of the inputs. Without a bias, the separating decision boundary line would always be forced to pass exactly through the origin (0,0), which severely limits what the network can learn.

**Q10: What are some other common activation functions besides the Step function?**
*Answer:* Sigmoid (maps values between 0 and 1, used for probability), ReLU (Rectified Linear Unit, standard for modern deep learning), and Tanh (maps values between -1 and 1).
