# K-Means Clustering (Vectorized Implementation)

This folder contains the explanation of the `8o.py` script. The script is based on your friend's implementation, but two critical bugs had to be fixed for it to actually work on the Iris dataset.

## The Bugs in Your Friend's Code

Your friend's code had two major flaws that would cause it to break silently or throw errors when run on the Iris dataset:

### 1. The Initialization Bug (The "Setosa Trap")
Your friend initialized the centroids like this:
```python
centroids = X[:K]
```
**Why it fails:** The `load_iris()` dataset returns 150 rows perfectly sorted by class (Rows 0-49 are Setosa, 50-99 are Versicolor, 100-149 are Virginica). Taking `X[:3]` grabs the first three rows of the dataset, which are all Setosa flowers that are nearly identical. 
Because all three starting points were clustered closely together, other points on the far side of the graph would "pull" one centroid, while the other two centroids would end up completely empty because no points were closest to them.

**The Fix:** Random initialization.
```python
np.random.seed(42)
centroids = X[np.random.choice(X.shape[0], K, replace=False)]
```
This randomly picks 3 distinct points across the entire dataset to ensure they are spread out.

### 2. The Empty Cluster Bug (The NaN Error)
Your friend updated the centroids using this line:
```python
new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])
```
**Why it fails:** If a cluster ever becomes empty (which happens frequently due to the bug mentioned above), `X[labels == k]` becomes an empty array. Calculating `.mean()` on an empty array results in `nan` (Not a Number). 
Once a centroid becomes `nan`, its distance to all points becomes `nan`. The convergence check `np.all(centroids == new_centroids)` will then fail because `nan == nan` evaluates to `False` in Python. The loop would get stuck and run until `max_iters` was reached, outputting broken data.

**The Fix:** Adding an `if len(points) > 0` check.
```python
new_centroids = []
for k in range(K):
    points = X[labels == k]
    if len(points) > 0:
        new_centroids.append(points.mean(axis=0))
    else:
        new_centroids.append(centroids[k]) # Keep the old centroid if empty
new_centroids = np.array(new_centroids)
```

## How the Rest of the Code Works (Vectorization)
* **`expanded_x = X[:, np.newaxis]`**: Reshapes the data to allow computing the distance between all 150 points and all 3 centroids simultaneously without any loops.
* **`euc_dist = np.linalg.norm(...)`**: Calculates the Euclidean distance across the feature axis.
* **`labels = np.argmin(euc_dist, axis=1)`**: Assigns each point to the centroid with the minimum distance.



## Execution Output & Interpretations
*(See 8_KMeans.md for outputs and interpretations, as they cover the same concept and the graphs are generated successfully there.)*



## Deep Dive Code Breakdown
*(See 8_KMeans.md for deep dive code breakdowns, as both cover K-Means parameters.)*
