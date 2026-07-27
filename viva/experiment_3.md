# Experiment 3: Data Visualization (Contour Plot) and A* Search

This document covers the theoretical concepts, code explanation, and viva questions for the third lab experiment:
1. `3a.py`: Data Visualization using Contour Plots.
2. `3b.py`: The A* Search Algorithm.

---

## Part A: Data Visualization (Contour Plot) - `3a.py`

### Theoretical Background
A contour plot is a graphical technique for representing a 3-dimensional surface by plotting constant Z slices, called contours, on a 2-dimensional format. It is like a topographical map where lines represent equal elevation. Contour plots are excellent for identifying local maxima, minima, and saddle points in data.

### Code Walkthrough
1. **Load Data**: The code loads the Iris dataset.
2. **Plotting the Contour**: 
   - `cp = plt.tricontourf(X[:, 0], X[:, 1], X[:, 2], levels=14)`: This creates a filled contour plot (`tricontourf` uses unstructured triangular grids). 
   - It maps Sepal Length (X) and Sepal Width (Y) to the Petal Length (Z).
   - `levels=14` indicates that the plot should be divided into 14 distinct color/contour levels based on the Z values.
3. **Colorbar**: `plt.colorbar(cp)` adds a legend scale on the side that shows which colors correspond to which Z values (Petal Length).

---

## Part B: A* Search Algorithm - `3b.py`

### Theoretical Background
A* (A-star) is one of the most popular and widely used informed search algorithms. It combines the advantages of Dijkstra's Algorithm (which favors nodes close to the start) and Greedy Best-First Search (which favors nodes close to the goal).

**Formula:** `f(n) = g(n) + h(n)`
- `g(n)`: The exact, accumulated cost to reach node `n` from the start node.
- `h(n)`: The heuristic estimated cost to reach the goal from node `n`.
- `f(n)`: The total estimated cost of the path through node `n`.

A* is **optimal** and **complete** provided that the heuristic function is **admissible** (it never overestimates the actual cost to reach the goal).

### Code Walkthrough
1. **Priority Queue Structure**: The `PriorityQueue` stores tuples in the format `(f_cost, g_cost, node, path)`. 
   - The first element is `f_cost` (`g_cost + heuristic[start]`), so the queue prioritizes nodes with the lowest overall estimated cost `f(n)`.
2. **Loop Logic**:
   - Pop the node with the lowest `f_cost`.
   - Mark it as visited.
   - If it is the goal node, return the path taken and the `g_cost` (total actual cost to reach the goal).
   - For every neighbor, calculate the `new_cost` (which is `current g_cost + edge_cost`).
   - Push the neighbor into the queue with the newly calculated `f_cost` (`new_cost + heuristic[neighbor]`).
3. **Graph and Heuristic**: The script defines an adjacency list `graph` with costs, and a dictionary `heuristic` with the estimated distances to the goal 'Z'.

---

## Viva Questions

### Program-Specific Questions
**Q1: What is the purpose of `levels=14` in the `tricontourf` function?**
*Answer:* It specifies the number of contour regions (color bands) to draw. By dividing the Z-axis data range into 14 levels, the plot creates a smoother gradient between regions of different values.

**Q2: What does the color bar (`plt.colorbar(cp)`) signify in `3a.py`?**
*Answer:* The color bar provides a visual key that maps the colors in the contour plot to actual numerical values of the Z-axis (which represents Petal Length in this program).

**Q3: How does the priority queue in `3b.py` prioritize nodes?**
*Answer:* The priority queue sorts based on the first element of the tuple, which is `new_cost + heuristic[neighbor]`. This represents the `f(n)` value (total estimated cost), so it explores the node with the lowest `f(n)` first.

**Q4: Why is `g_cost` stored inside the priority queue alongside `f_cost`?**
*Answer:* Because `g_cost` is needed to calculate the cost for subsequent neighbor expansions. When expanding a node, the new `g_cost` for a neighbor is the current node's `g_cost` plus the edge cost to the neighbor.

**Q5: What will `3b.py` return if there is no valid path to the goal?**
*Answer:* If the queue becomes empty and the goal hasn't been found, the function returns `None, float('inf')`, indicating no path exists.

### General Theory Questions
**Q6: What makes A* search optimal?**
*Answer:* A* is optimal if its heuristic is **admissible**. An admissible heuristic never overestimates the true cost to the goal. Because it assumes the goal is closer than it actually is, A* will safely explore all promising paths before settling on the final one, guaranteeing the shortest path is found.

**Q7: Explain the difference between `g(n)` and `h(n)` in A*.**
*Answer:* `g(n)` is the actual backward cost (the exact cost incurred to get from the start node to the current node). `h(n)` is the estimated forward cost (the guessed cost to get from the current node to the goal).

**Q8: If `h(n) = 0` for all nodes in A*, what algorithm does it become?**
*Answer:* If `h(n) = 0`, the evaluation function becomes `f(n) = g(n)`. This makes A* behave exactly like Dijkstra's Algorithm (Uniform Cost Search).

**Q9: What happens if `h(n)` overestimates the cost to the goal?**
*Answer:* If `h(n)` overestimates, the heuristic is no longer admissible. The algorithm may run faster by acting greedier, but it loses its guarantee of finding the optimal (shortest) path.

**Q10: Why might A* struggle with memory in very large graphs?**
*Answer:* A* keeps all generated, unexpanded nodes in memory (in the priority queue or open list). For problems with high branching factors, the number of nodes stored grows exponentially, which can quickly consume all available RAM.
