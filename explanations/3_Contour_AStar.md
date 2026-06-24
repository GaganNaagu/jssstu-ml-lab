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



## Execution Output & Interpretations

### 3a.py: Contour Plot
**Graph:**
![3a.py](../outputs/3a.png)

**How to understand this graph:**
* **What it shows:** A contour plot is a 2D representation of a 3D surface, just like a topographic map used by hikers.
* **The Rings/Lines:** Each line connects points of equal Z-value (height). 
* **Interpretation:** 
  * If the rings are packed very closely together, the slope is extremely steep. 
  * If the rings are far apart, the terrain is relatively flat. 
  * The center of a series of concentric rings represents a local minimum (valley bottom) or maximum (mountain peak).

### 3b.py: A* Search
**Output:**
```text
A* Path: ['S', 'A', 'C', 'G']
Total Cost: 9
```
**Interpretation:** A* search smartly uses heuristics (estimated distance to goal) to find the absolute best path. The output confirms the shortest path found is S -> A -> C -> G, and tells us the total accumulated cost (distance/effort) to travel that path is 9.



## Deep Dive Code Breakdown

### 3a.py: Contour Plot Variables
*   `plt.tricontourf(X[:, 0], X[:, 1], X[:, 2], levels=14, cmap='viridis')`: 
    *   `tricontourf`: Similar to `plot_trisurf`, this creates a filled contour plot from unstructured data by calculating triangles between the points.
    *   `levels=14`: Tells the plot to draw 14 distinct color bands (elevation levels).
    *   `cmap='viridis'`: Maps the Z-values to a color scale ranging from dark purple (low) to yellow (high).

### 3b.py: A* Search Variables
*   `pq = PriorityQueue()`: A* uses a Priority Queue so it can always expand the most promising path first.
*   `new_cost = g_cost + cost`: This calculates the exact distance traveled from the start node to the current neighbor (`g`).
*   `pq.put((new_cost + heuristic[neighbor], ...))`: The priority is the `f_score`, which is the sum of `g` (actual cost so far) + `h` (heuristic estimate to the goal). The node with the lowest `f_score` is explored first.


### Important Notes
- In A* search (3b.py), the priority queue stores tuples in the format: (Cost, current_node, path).
