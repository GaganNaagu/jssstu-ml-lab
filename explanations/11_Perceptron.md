# Program 11: Single Layer Perceptron (AND / OR Gates)

### 1. Conceptual Overview
The **Perceptron** is the absolute simplest form of an Artificial Neural Network. Created in 1957, it is essentially a single "neuron" modeled after the human brain. It is a **Binary Linear Classifier**, meaning it can only separate data into two categories (0 or 1) by drawing a straight, rigid line through the data.

### 2. Step-by-Step Logic
1.  **Inputs ($X$):** The neuron receives input signals (e.g., $x_1$ and $x_2$).
2.  **Weights ($W$):** Every input is multiplied by a "weight", which represents how important that specific input is.
3.  **Summation ($Z$):** The neuron adds all the weighted inputs together. It also adds a **Bias ($b$)**, which shifts the activation threshold up or down.
    *   $Z = (x_1 \cdot w_1) + (x_2 \cdot w_2) + b$
4.  **Activation Function:** The sum $Z$ is passed through a simple mathematical filter (usually a Step Function).
    *   If $Z \ge 0$, the neuron "fires" and outputs 1.
    *   If $Z < 0$, the neuron stays quiet and outputs 0.

### 3. Simulating Logic Gates (AND / OR)
In this program, we train the Perceptron to act like a computer microchip.
*   **AND Gate:** The Perceptron automatically learns to adjust its weights so that the output is ONLY 1 if both $x_1=1$ **AND** $x_2=1$. 
*   **OR Gate:** It adjusts its weights so that the output is 1 if *either* $x_1=1$ **OR** $x_2=1$.

### 4. Key Concepts to Mention in Exams
*   **Linear Separability:** A Single Layer Perceptron can ONLY solve problems where you can take a pencil and draw a single straight line to separate the 1s from the 0s on a graph. 
*   **The XOR Problem:** If an examiner asks about the limitations of a Perceptron, tell them it **cannot solve the XOR (Exclusive OR) problem**. The XOR data points are arranged diagonally, making it physically impossible to separate them with one straight line. This fatal flaw is what caused the first "AI Winter" in the 1970s until Multi-Layer Perceptrons (Deep Learning) were invented!

### 5. Real-World Application
*   **Basic Approval Algorithms:** A simple banking algorithm for student loans. Input 1: Credit Score (High Weight). Input 2: Existing Debt (Negative Weight). If the calculated sum crosses the bias threshold, the output is 1 (Loan Approved).
