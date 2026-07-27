# Experiment 2: Data Visualization (3D Surface) and Best First Search

This document covers the theoretical concepts, code explanation, and viva questions for the second lab experiment:
1. `2a.py`: Data Visualization using 3D Surface Plots.
2. `2b.py`: Best First Search (Greedy Best-First Search) Algorithm.

---

## Part A: Data Visualization (3D Surface Plot) - `2a.py`

### Theoretical Background
A 3D Surface Plot is a three-dimensional graph that is useful for exploring the relationship between three variables. While scatter plots show discrete data points, surface plots connect these points to form a continuous surface, which is particularly useful for finding optimum combinations of variables or visualizing complex mathematical functions.

### Code Walkthrough
1. **Load Data**: The code loads the Iris dataset.
2. **Setup 3D Axes**: `ax = plt.axes(projection='3d')` initializes a 3-dimensional plotting area.
3. **Plotting the Surface**: 
   - `ax.plot_trisurf(...)` creates a 3D surface using triangular meshing.
   - It takes the first three features of the dataset: `X[:, 0]` (Sepal Length) as X, `X[:, 1]` (Sepal Width) as Y, and `X[:, 2]` (Petal Length) as Z.
   - `cmap="jet"` applies a color map to the surface, representing depth/height through color gradients.

---

## Part B: Best First Search (Greedy) - `2b.py`

### Theoretical Background
Best First Search is an informed search algorithm that uses an evaluation function to decide which node to expand next. In **Greedy Best-First Search**, the evaluation function `f(n)` is solely based on a heuristic function `h(n)`.

**Formula:** `f(n) = h(n)`
- `h(n)` is the estimated cost from node `n` to the goal.

The algorithm expands the node that appears to be closest to the goal based on the heuristic. It is called "greedy" because at each step, it tries to get as close to the goal as possible without considering the cost already spent to reach the current node.

**Properties:**
- It is **not guaranteed** to find the shortest path (not optimal).
- It can get stuck in loops if not keeping track of visited nodes.

### Code Walkthrough
1. **Priority Queue**: The algorithm uses a `PriorityQueue` from python's `queue` module. The queue automatically sorts items based on the first element of the tuple inserted.
2. **Queue Contents**: The queue stores tuples in the format `(heuristic[node], node, accumulated_cost)`. Because the heuristic value is the first element, the Priority Queue will always pop the node with the lowest heuristic value (i.e., the one deemed closest to the goal).
3. **Loop Logic**:
   - Dequeue the node with the lowest heuristic.
   - If it's already visited, skip it.
   - If it's the goal node, return the path and cost.
   - Otherwise, iterate through its neighbors. If a neighbor hasn't been visited, push it into the priority queue with its heuristic value and the updated accumulated cost.

---

## Viva Questions

### Program-Specific Questions
**Q1: Why do we use `projection='3d'` in `2a.py`?**
*Answer:* It tells matplotlib to create a three-dimensional axis (Axes3D) instead of the default 2D Cartesian axis, allowing us to plot X, Y, and Z coordinates.

**Q2: What does `cmap="jet"` do in the 3D surface plot?**
*Answer:* It applies a specific color map named "jet" to the surface. It helps visualize the depth or Z-value of the surface, with lower values typically appearing blue and higher values appearing red.

**Q3: How does the Priority Queue in `2b.py` know to sort by the heuristic value?**
*Answer:* In Python, when tuples are put into a Priority Queue, it sorts them based on the first element of the tuple. In the code, the tuple is structured as `(heuristic[node], node, accumulated_cost)`, so it automatically prioritizes the lowest heuristic.

**Q4: Does the Best First Search implementation in `2b.py` use the edge costs to decide which path to take?**
*Answer:* No. It calculates the `accumulated_cost` for tracking purposes, but the priority queue sorting (the decision-making part) relies *only* on `heuristic[node]`.

**Q5: Why do we need a `visited` set in the Best First Search implementation?**
*Answer:* The `visited` set keeps track of nodes that have already been expanded. This prevents the algorithm from processing the same node multiple times and getting stuck in an infinite loop if the graph has cycles.

### General Theory Questions
**Q6: What is the difference between uninformed and informed search algorithms?**
*Answer:* Uninformed search algorithms (like BFS, DFS) have no additional information about states beyond that provided in the problem definition. Informed search algorithms (like Best First Search, A*) use a heuristic function that estimates how close a state is to the goal.

**Q7: What is a heuristic function?**
*Answer:* A heuristic function `h(n)` estimates the cost of the cheapest path from node `n` to the goal node. It is an informed guess based on domain knowledge.

**Q8: Is Greedy Best-First Search optimal and complete?**
*Answer:* It is **not optimal** because it can easily be led down a suboptimal path by a misleading heuristic. It is **complete** only if the state space is finite and we keep track of visited nodes to avoid loops.

**Q9: How is Greedy Best-First Search different from A* Search?**
*Answer:* Greedy Best-First Search only considers the estimated distance to the goal `h(n)`. A* Search considers both the cost already incurred to reach the node `g(n)` and the estimated distance to the goal `h(n)`, using the evaluation function `f(n) = g(n) + h(n)`.

**Q10: Give an example of a heuristic that could be used for finding routes on a map.**
*Answer:* Straight-line distance (Euclidean distance) is a common heuristic. It estimates the distance between a city and the destination as a straight line, which is always less than or equal to the actual road distance.
