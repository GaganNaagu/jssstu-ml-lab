# Experiment 8: K-Means Clustering

This document covers the theoretical concepts, code explanation, and viva questions for the eighth lab experiment: `8o.py` (K-Means from scratch). As requested, we will focus entirely on the from-scratch implementation for both theory and code.

---

## Theoretical Background
K-Means is one of the simplest and most popular **unsupervised machine learning** algorithms. Unsupervised means it works on data without predefined labels or targets; it attempts to find underlying patterns (clusters) on its own.

**The goal:** Group similar data points together into `K` distinct non-overlapping subgroups (clusters), where each data point belongs to the cluster with the nearest mean (centroid).

**How it works (The Algorithm):**
1. **Initialization**: Choose the number of clusters `K`. Randomly pick `K` data points from the dataset to act as the initial cluster centers (centroids).
2. **Assignment Step**: Calculate the Euclidean distance from every data point to all `K` centroids. Assign each data point to the cluster of the centroid it is closest to.
3. **Update Step**: Now that points are assigned, calculate the new mean (average) of all points belonging to each cluster. Move the centroid to this new mean location.
4. **Repeat**: Repeat steps 2 and 3 until the centroids no longer move (convergence) or a maximum number of iterations is reached.

---

## Code Walkthrough (`8o.py` - From Scratch Implementation)
1. **Data Preparation & Scaling**: 
   - Loads the Iris dataset.
   - `StandardScaler()` is used to scale `X`. Because K-Means relies entirely on distance calculations, scaling is crucial to ensure all features are weighted equally.
2. **The `kmeans(X, K, max_iters)` Function**:
   - `np.random.seed(42)` ensures reproducibility.
   - **Initialization**: `centroids = X[:K]`. It initializes the first `K` centroids using the first `K` points in the dataset. *(Note: While simple, this is not robust in practice. Algorithms like K-means++ are better as they spread out the initial centroids).*
3. **The Iteration Loop**:
   - `expanded_x = X[:, np.newaxis]`: This cleverly reshapes the array to allow for fast, vectorized calculation of distances between all points and all centroids simultaneously without using slow Python `for` loops.
   - `euc_dist = np.linalg.norm(expanded_x - centroids, axis=2)`: Calculates the Euclidean distance.
   - `labels = np.argmin(euc_dist, axis=1)`: Finds the index of the minimum distance (the closest centroid) for each point, assigning it a cluster label (0, 1, or 2).
4. **Updating Centroids**:
   - `new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(K)])`: For each cluster `k`, this grabs all points assigned to `k` and calculates their new average position along all axes (`axis=0`).
5. **Convergence Check**:
   - `if np.all(centroids == new_centroids): break`. If the newly calculated centroids are in the exact same mathematical position as the old ones, the algorithm has converged, and the loop stops early.

---

## Viva Questions

### Program-Specific Questions
**Q1: Why is `StandardScaler` used before applying K-Means?**
*Answer:* K-Means groups points based on Euclidean distance. If features are on vastly different scales (e.g., one in thousands, another in decimals), the larger feature will dominate the distance calculation. Standard scaling ensures all features have a mean of 0 and a standard deviation of 1, allowing them to contribute equally.

**Q2: What is the purpose of `X[:, np.newaxis]`?**
*Answer:* It adds a new, empty dimension to the numpy array, converting it from a 2D array to a 3D array. This allows numpy to "broadcast" the subtraction operation across the centroids array, calculating the distance between *every* point and *every* centroid simultaneously without writing explicit nested loops.

**Q3: How does `np.argmin(euc_dist, axis=1)` determine the cluster label?**
*Answer:* `euc_dist` contains the distances from a point to all `K` centroids. `np.argmin` finds the index (0, 1, or 2) of the smallest value in that list. This index acts as the cluster label, meaning the point is assigned to the nearest centroid.

**Q4: How does the code calculate the new centroid position?**
*Answer:* It uses a list comprehension: `X[labels == k].mean(axis=0)`. `X[labels == k]` filters the dataset to only include points assigned to cluster `k`. Then, `.mean(axis=0)` calculates the average value across each feature column for those specific points.

**Q5: What happens if you run the custom `kmeans` function with an un-shuffled Iris dataset without scaling?**
*Answer:* The Iris dataset is ordered by class (first 50 are Setosa, etc.). If we initialize centroids using `X[:3]`, we are picking 3 points that are almost identical and belong to the same class. The algorithm will likely get stuck in a terrible local minimum, resulting in very inaccurate clusters.

### General Theory Questions
**Q6: What is the difference between supervised and unsupervised learning?**
*Answer:* Supervised learning uses labeled datasets to train algorithms (like predicting house prices based on known past prices). Unsupervised learning analyzes and clusters unlabeled datasets, discovering hidden patterns or groupings without human intervention (like grouping customers by purchasing behavior).

**Q7: How do you choose the optimal value of K?**
*Answer:* The most common technique is the **Elbow Method**. You run K-Means for a range of K values and calculate the Within-Cluster Sum of Squares (WCSS). You plot WCSS against K, and the "elbow" of the curve (where the rate of decrease sharply slows down) indicates the optimal K.

**Q8: What is the "Local Minimum" problem in K-Means?**
*Answer:* Depending on where the initial centroids are placed, the algorithm might converge to a configuration that is mathematically stable but practically incorrect (a local minimum). This is why standard K-Means is usually run multiple times with different random initializations.

**Q9: Explain the K-Means++ initialization strategy.**
*Answer:* K-Means++ is an improvement over random initialization. It picks the first centroid randomly, but for subsequent centroids, it selects data points that are furthest away from the already chosen centroids. This spreads the initial centroids out, dramatically improving the chances of finding the global optimum.

**Q10: Is K-Means sensitive to outliers?**
*Answer:* Yes, highly sensitive. Because it relies on calculating the mathematical mean, a single extreme outlier can drastically pull the centroid away from the true center of the data mass.
