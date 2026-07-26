# Program 1: Scatter Plots & Hill Climbing Algorithm

## Part A: Visualize n-dimensional data using Scatter Plots

### 1. Conceptual Overview
A **Scatter Plot** is a fundamental two-dimensional data visualization technique that uses dots to represent the values obtained for two different variables - one plotted along the x-axis and the other plotted along the y-axis. 

### 2. What to Look For (Interpretation)
When looking at a scatter plot, an examiner will expect you to identify the relationship (correlation) between the variables:
*   **Positive Correlation:** As X increases, Y increases (dots form a line sloping upwards).
*   **Negative Correlation:** As X increases, Y decreases (dots slope downwards).
*   **No Correlation:** Dots are scattered completely randomly with no discernible pattern.
*   **Clusters:** If dots of the same class (color) group tightly together, it proves that the chosen X and Y features are excellent at distinguishing between classes.

### 3. Real-World Application
*   **Real Estate:** Plotting *House Price* (Y-axis) vs *Square Footage* (X-axis) to see if bigger houses are strictly more expensive, or if there are massive outliers (e.g., a tiny house that costs a fortune because it is in a prime location).

---

## Part B: Hill Climbing Algorithm

### 1. Conceptual Overview
**Hill Climbing** is a heuristic search used for mathematical optimization problems. It belongs to the family of **Local Search algorithms**. It starts with a random arbitrary solution to a problem and iteratively attempts to make a small change to the solution. If the change results in a *better* state (a higher value on the objective function), the algorithm makes the change and continues. If the change is worse, it discards it. It stops when no neighboring state is better than the current state.

### 2. Step-by-Step Logic
1.  **Evaluate the initial state.** If it is the goal state, return it and quit.
2.  **Loop until a solution is found or no further improvements can be made:**
    *   Generate neighbors of the current state.
    *   Evaluate all neighbors.
    *   Select the neighbor with the highest objective value.
    *   If this neighbor is *strictly better* than the current state, move to it. Otherwise, stop and return the current state as the "peak".

### 3. Key Limitations to Mention in Exams
Examiners love asking about the pitfalls of Hill Climbing. Always mention these three:
*   **Local Maxima:** The algorithm reaches a state that is better than all its immediate neighbors, but it is not the best possible state overall (the Global Maximum). It gets stuck on a "foothill" and misses the "mountain".
*   **Plateaus:** A flat area where all neighbors have the exact same value. The algorithm has no idea which way to step to go "up".
*   **Ridges:** A steep slope where the highest point is at an angle, forcing the algorithm to aggressively zig-zag inefficiently.

### 4. Real-World Application
*   **Antenna Tuning / Signal Processing:** Turning a radio dial or a TV antenna. You make small adjustments; if the static gets quieter, you keep moving in that direction. Once moving in *any* direction makes the static worse, you stop, assuming you have the best signal.
*   **Gradient Descent:** The underlying concept is identical to Gradient Descent in Neural Networks (which is just hill climbing in reverse—trying to find the lowest valley of error instead of the highest peak of accuracy).



## Execution Output & Interpretations

### 1a.py: Scatter Plot
**Graph:**
![1a.py](../outputs/1a.png)

**How to understand this graph:**
* **What it shows:** A scatter plot displays individual data points on a 2D coordinate system. Here, the X and Y axes represent two features of the Iris dataset (Sepal Length and Sepal Width).
* **Colors:** Different colors represent different classes (species of Iris flowers).
* **Interpretation:** By looking at the spread and overlap of colors, you can easily see if certain classes are naturally grouped together or if they are mixed. If the colors are well-separated, a machine learning model will have an easy time classifying them!

### 1b.py: Hill Climbing
**Output:**
```text
Starting state: 3.1854
Local maximum found at x = 1.9854
Objective value: 3.9998
```
**Interpretation:** The algorithm starts at a random negative coordinate and iteratively takes steps uphill. It successfully finds the peak (local maximum) at x ≈ 2.02, where the mathematical function reaches its highest value of ≈ 3.99.



## Deep Dive Code Breakdown

### 1a.py: Scatter Plot Variables
*   `iris.target`: This is the exact answer key (labels) for the dataset. For the Iris dataset, `target` is an array of 0s, 1s, and 2s representing the three flower species (Setosa, Versicolor, Virginica).
*   `scatter = plt.scatter(...)` Parameters:
    *   `X[:, 0], X[:, 1]`: The first two arguments are the X-axis and Y-axis coordinates. `X[:, 0]` means "all rows, 0th column" (Sepal Length), and `X[:, 1]` is the 1st column (Sepal Width).
    *   `c=y`: The "color" parameter. By passing the `iris.target` array (`y`), it assigns a unique color to the 0s, 1s, and 2s automatically.
    *   `cmap='viridis'`: The Color Map. Matplotlib maps the numbers 0, 1, 2 to a color gradient. `'viridis'` is a default color-blind friendly map that goes from dark purple to bright yellow. Other possible values: `'plasma'`, `'inferno'`, `'magma'`, `'coolwarm'`.
    *   `s=50`: Size of the scatter dots. Increasing this makes the dots larger.
    *   `alpha=0.8`: The transparency level, ranging from 0.0 (invisible) to 1.0 (solid). 0.8 makes dots slightly transparent so you can see if multiple dots overlap.

### 1b.py: Hill Climbing Variables
*   `def objective(x):`: The mathematical function creating the "hill" we are trying to climb.
*   `step_size`: How far the algorithm "steps" horizontally (on the X-axis) to check if the height (Y-axis) increases.
*   `max_iterations`: A safety cutoff to stop the loop from running forever if it gets stuck on a flat surface.


### Important Notes
- The objective function used for Hill Climbing in 1b.py is (x) = -x^2 + 4x (a parabola facing down, with its maximum at x=2).
