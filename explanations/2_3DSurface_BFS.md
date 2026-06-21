# Program 2: 3D Surface Plots & Best First Search (BFS)

## 2(a): 3D Surface Plot
**What it does:** Adds a third dimension (Z-axis) to a 2D plot, creating a continuous "sheet" or "surface" connecting the data points.
**What to look for:** Peaks and valleys in the data. It helps visualize how a target variable reacts to changes in *two* input variables simultaneously.
**Real-World Example:** Topographical elevation maps. The X and Y axes are GPS coordinates (longitude/latitude), and the Z axis is the height of the mountain.

## 2(b): Best First Search (Greedy BFS)
**Logic / Algorithm:** An AI search algorithm that uses a priority queue and a **Heuristic Function ($h(n)$)**. Unlike generic generic searches, BFS actively estimates "how far am I from the goal?" and always expands the node that *looks* closest to the goal.
**Real-World Example:** Imagine navigating a maze. Greedy BFS is like choosing the hallway that physically points in the compass direction of the exit, even if it might eventually lead to a dead end.
**Exam Tip:** Mention that Greedy BFS is *fast* but not *optimal* (it might not find the absolute shortest path, just a fast one).
