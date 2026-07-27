# Experiment 1: Data Visualization (Scatter Plot) and Hill Climbing Algorithm

This document covers the theoretical concepts, code explanation, and viva questions for the first lab experiment, which is divided into two parts:
1. `1a.py`: Data Visualization using Scatter Plots.
2. `1b.py`: The Hill Climbing Search Algorithm.

---

## Part A: Data Visualization (Scatter Plot) - `1a.py`

### Theoretical Background
Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.

A **Scatter Plot** uses dots to represent values for two different numeric variables. The position of each dot on the horizontal and vertical axis indicates values for an individual data point. Scatter plots are used to observe relationships (correlations) between variables.

### Code Walkthrough
1. **Load Data**: The code uses `load_iris()` from `sklearn.datasets` to load the famous Iris dataset.
2. **Features and Target**: 
   - `X = iris.data`: The feature matrix (sepal length, sepal width, petal length, petal width).
   - `y = iris.target`: The target classes (0: Setosa, 1: Versicolor, 2: Virginica).
3. **Plotting**: 
   - `plt.scatter(X[:, 0], X[:, 1], c=y)`: This plots the first feature (sepal length) on the X-axis and the second feature (sepal width) on the Y-axis. The `c=y` argument colors the data points based on their target class, making it easy to visually separate the classes.
4. **Formatting**: Labels and titles are added for readability before calling `plt.show()`.

---

## Part B: Hill Climbing Algorithm - `1b.py`

### Theoretical Background
Hill Climbing is a mathematical optimization technique which belongs to the family of local search algorithms. It is an iterative algorithm that starts with an arbitrary solution to a problem, then attempts to find a better solution by making an incremental change to the solution. If the change produces a better solution, another incremental change is made to the new solution, and so on until no further improvements can be found.

**Types of Hill Climbing:**
- Simple Hill Climbing
- Steepest-Ascent Hill Climbing (implemented in `1b.py`)
- Stochastic Hill Climbing

**Limitations:**
- **Local Maxima:** A state that is better than all its neighbors but is not better than some other states farther away. The algorithm stops here.
- **Plateau:** A flat area of the search space where all neighboring states have the same value.
- **Ridge:** A sequence of local maxima that is very difficult for greedy algorithms to navigate.

### Code Walkthrough
1. **Objective Function**: `return -x**2 + 4*x`. This is the mathematical function the algorithm is trying to maximize. In this case, it's a downward opening parabola with a global maximum.
2. **Get Neighbors**: The `get_neighbors` function generates the adjacent states by moving a small `step_size` (0.1) to the left and right of the current state.
3. **Hill Climbing Logic**:
   - The loop runs for a maximum number of iterations.
   - It evaluates all neighbors of the current state.
   - It picks the neighbor with the highest objective value (`max(neighbor_evals, ...)`).
   - If the best neighbor's value is **less than or equal** to the current value, it means we have reached a peak (local/global maximum) and the loop `break`s.
   - Otherwise, it updates the `current_state` to the `best_neighbor` and continues.

---

## Viva Questions

### Program-Specific Questions
**Q1: What does `X[:, 0]` and `X[:, 1]` mean in the scatter plot code?**
*Answer:* In numpy array slicing, `:` means "all rows", and `0` means the first column. So `X[:, 0]` extracts the first feature (sepal length) for all samples, and `X[:, 1]` extracts the second feature (sepal width).

**Q2: What is the purpose of `c=y` in `plt.scatter`?**
*Answer:* It maps the color of the scatter points to the target array `y`. Since `y` contains values 0, 1, and 2 (representing the three Iris species), the points will be plotted in three distinct colors.

**Q3: What type of Hill Climbing is implemented in `1b.py`?**
*Answer:* It is Steepest-Ascent Hill Climbing because it evaluates *all* generated neighbors and chooses the absolute best one before making a move.

**Q4: How does the algorithm know when to stop climbing?**
*Answer:* It stops when `best_value <= current_value`. This means that none of the neighboring states offer a better objective value than the current state, implying the algorithm has reached a peak.

**Q5: Will the algorithm in `1b.py` always find the global maximum for the given function?**
*Answer:* Yes, for the specific function `-x^2 + 4x`, there is only one peak (a global maximum at x=2). Because there are no local maxima traps, the hill climbing algorithm will successfully find it regardless of the starting point.

### General Theory Questions
**Q6: What is a local maximum in Hill Climbing?**
*Answer:* A local maximum is a state that is better than all of its immediate neighbors, but is not the overall best state (global maximum) in the entire search space.

**Q7: How can we overcome the problem of local maxima in Hill Climbing?**
*Answer:* Techniques like Random-Restart Hill Climbing (running the algorithm multiple times from random initial states) or Simulated Annealing (allowing occasional "bad" moves to escape local peaks) are commonly used.

**Q8: Explain the "Plateau" problem in Hill Climbing.**
*Answer:* A plateau is a flat region in the state space landscape where all neighboring states have the same value. The algorithm gets stuck because it cannot determine which direction leads to improvement.

**Q9: What is the difference between Simple Hill Climbing and Steepest Ascent Hill Climbing?**
*Answer:* Simple Hill Climbing evaluates neighbors one by one and moves to the *first* neighbor that is better than the current state. Steepest Ascent evaluates *all* neighbors and moves to the *best* neighbor among them.

**Q10: Why do we use data visualization in Machine Learning?**
*Answer:* Data visualization helps in exploratory data analysis (EDA). It allows us to intuitively spot patterns, outliers, correlations, and the general distribution of the data before applying complex mathematical algorithms.
