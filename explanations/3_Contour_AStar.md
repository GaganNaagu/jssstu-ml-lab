# Program 3: Contour Plots & A* Search

## Part A: Visualize n-dimensional data using Contour Plots

### 1. Conceptual Overview
A **Contour Plot** is a way to represent 3D surface data on a flat 2D plane. It uses "contour lines" (rings). Every point on a single continuous line has the exact same Z-value. 

### 2. What to Look For (Interpretation)
*   **Spacing of Lines:** If the contour rings are grouped very tightly together, it represents a steep gradient (a cliff). If the rings are spread far apart, it represents a very gradual, flat slope.
*   **Concentric Circles:** A series of closed rings shrinking into a center point represents either a local maximum (a hilltop) or a local minimum (a bowl/crater). The colorbar tells you which it is.

### 3. Real-World Application
*   **Meteorology:** Weather maps use contour lines (called *isobars*) to connect areas of equal atmospheric pressure. Tightly packed isobars mean high winds.
*   **Hiking / Topography:** Hikers use 2D contour maps to plan routes, actively avoiding areas where the contour lines are packed too tightly together (as that indicates a cliff too steep to climb).

---

## Part B: A* (A-Star) Algorithm

### 1. Conceptual Overview
**A*** is arguably the most famous and widely used pathfinding algorithm in computer science. It is an informed search algorithm that solves the massive flaw of Greedy BFS. Instead of just looking blindly at the future, A* considers both the **past** and the **future**.

It evaluates nodes by combining two values:
$$f(n) = g(n) + h(n)$$
*   **$g(n)$:** The exact, actual cost of the path from the starting node to node $n$ (the past).
*   **$h(n)$:** The estimated (heuristic) cost from node $n$ to the goal (the future).
*   **$f(n)$:** The total estimated cost of the cheapest solution through node $n$.

### 2. Step-by-Step Logic
1.  Initialize a Priority Queue with the start node, sorting by $f(n)$.
2.  **Loop:**
    *   Pop the node with the lowest $f(n)$.
    *   If it is the goal, the optimal path is found.
    *   Expand neighbors. Calculate the exact $g(n)$ to reach the neighbor (current $g$ + edge cost).
    *   Calculate $f(n) = g(n) + h(\text{neighbor})$.
    *   Push the neighbor into the queue with this new $f(n)$.

### 3. Key Concepts to Mention in Exams
*   **Admissibility:** For A* to guarantee finding the shortest possible path (optimality), the heuristic $h(n)$ **must be admissible**. This means the heuristic must *never overestimate* the true cost to reach the goal. (e.g., A straight line distance is admissible because you can never travel faster than a straight line).
*   **Completeness:** A* is complete, meaning if a path exists, A* will absolutely find it.

### 4. Real-World Application
*   **Google Maps / Routing:** Calculating the absolute fastest driving route. The $g(n)$ is the miles you have already driven, and the $h(n)$ is the straight-line distance to your destination. 
*   **Network Routing:** Finding the shortest path to send a packet of data across a global network of servers while minimizing latency.
