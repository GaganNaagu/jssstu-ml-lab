# Program 3: Contour Plots & A* Search

## 3(a): Contour Plot
**What it does:** Represents 3D surface data on a 2D plane using "contour lines" (like rings). Everywhere on a single ring has the exact same Z-value.
**What to look for:** Tight rings indicate steep changes (a sharp hill), while spread-out rings indicate flat areas.
**Real-World Example:** Weather maps on the news! The lines (isobars) show areas of equal atmospheric pressure.

## 3(b): A* (A-Star) Algorithm
**Logic / Algorithm:** The gold standard of pathfinding. It calculates $f(n) = g(n) + h(n)$. 
- $g(n)$: The actual cost to reach node $n$ from the start.
- $h(n)$: The estimated (heuristic) cost from node $n$ to the goal.
By combining both, A* avoids the traps that Greedy BFS falls into, guaranteeing the shortest path (as long as $h(n)$ never overestimates the distance).
**Real-World Example:** Google Maps routing. It calculates the actual distance driven so far ($g$) plus the straight-line distance to the destination ($h$) to find the fastest driving route.
