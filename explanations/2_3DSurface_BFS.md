# Program 2: 3D Surface Plots & Best First Search (BFS)

## Part A: Visualize n-dimensional data using 3D Surface Plots

### 1. Conceptual Overview
A **3D Surface Plot** visualizes the relationship between three variables. It plots data points on three axes (X, Y, and Z) and connects them to create a continuous "sheet" or "surface" using interpolation.

### 2. What to Look For (Interpretation)
*   **Topography:** You are looking for the "peaks" (highest Z values) and "valleys" (lowest Z values). 
*   **Color Gradients:** Most surface plots use a colormap (like 'viridis') where dark colors represent deep valleys and bright colors (yellows) represent high peaks. This makes it instantly obvious where the maximum and minimum values lie in relation to the X and Y inputs.

### 3. Real-World Application
*   **Aerodynamics & Engineering:** Visualizing how the *Drag Coefficient* (Z-axis) of a car changes simultaneously with *Speed* (X-axis) and *Wind Angle* (Y-axis).
*   **Geographical Mapping:** Creating digital elevation models where X and Y are GPS coordinates and Z is the altitude above sea level.

---

## Part B: Best First Search (Greedy BFS)

### 1. Conceptual Overview
**Best First Search (Greedy)** is an informed AI search algorithm. Unlike blind searches (like standard Breadth-First or Depth-First Search), BFS uses a **Heuristic Function ($h(n)$)** to actively estimate how far the current node is from the goal. It is "greedy" because it always chooses the path that *appears* to be the closest to the goal right now, without worrying about the past.

### 2. Step-by-Step Logic
1.  Initialize a **Priority Queue** (which automatically sorts items by lowest heuristic cost).
2.  Put the starting node in the queue.
3.  **Loop:**
    *   Pop the node with the lowest $h(n)$ value.
    *   If it is the goal, stop and return the path.
    *   Otherwise, add the node to the `visited` set so we don't loop infinitely.
    *   Expand the node by looking at all its neighbors. For any neighbor not in `visited`, calculate its $h(n)$ and put it in the priority queue.

### 3. Key Concepts to Mention in Exams
*   **The Heuristic $h(n)$:** An educated guess. For example, the straight-line ("as the crow flies") distance between a city and the destination.
*   **Optimality:** Greedy BFS is **NOT optimal**. Because it ignores the distance already traveled, it can be easily tricked by obstacles into taking a longer overall path, just because the initial steps looked closer to the goal.

### 4. Real-World Application
*   **Basic GPS Routing:** When computational power is extremely limited, calculating the absolute perfect route might take too long. A GPS might use a greedy approach to quickly output a "good enough" route by constantly forcing you to take roads that head in the general compass direction of your destination.
*   **Video Game AI:** A zombie in a game trying to reach the player. It doesn't calculate a complex maze route; it just continuously moves in the straight-line direction of the player until it hits a wall.
