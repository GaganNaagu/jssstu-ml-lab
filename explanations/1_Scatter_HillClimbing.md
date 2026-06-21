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
