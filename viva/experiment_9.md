# Experiment 9: Hierarchical Agglomerative Clustering

This document covers the theoretical concepts (derived from our from-scratch implementation), the standard `scipy` code explanation, and viva questions for the ninth lab experiment: `9.py` and `9o.py`.

---

## Theoretical Background (Based on `9o.py`)
Hierarchical clustering groups data points into a tree of clusters called a **Dendrogram**. There are two types: Agglomerative (bottom-up) and Divisive (top-down). We are studying **Agglomerative**.

**How Agglomerative Clustering works:**
1. **Start**: Treat every single data point as its own independent cluster (if you have N points, you have N clusters).
2. **Proximity Matrix**: Calculate the distance (usually Euclidean) between all clusters.
3. **Merge**: Find the two clusters that are closest to each other and merge them into a single, new cluster.
4. **Update**: Update the proximity matrix to reflect the distance between the newly formed cluster and all remaining clusters.
5. **Repeat**: Repeat steps 3 and 4 until all data points are merged into a single, massive root cluster.

**Linkage Methods (How to measure distance between *clusters*):**
- **Single Linkage**: The distance between two clusters is defined as the *shortest* distance between any point in cluster A and any point in cluster B. (Tends to create long, chain-like clusters).
- **Complete Linkage**: The distance between two clusters is defined as the *longest* (maximum) distance between any point in cluster A and any point in cluster B. (Tends to create compact, spherical clusters).

---

## Code Walkthrough (`9.py` - Built-in Implementation)
1. **Data Subset**: `X = load_iris().data[:6]`. To make the dendrogram and proximity matrix readable, the code only takes the first 6 data points of the Iris dataset.
2. **Proximity Matrix**: 
   - `pdist(X, 'euclidean')` calculates the pairwise Euclidean distances between all 6 points. It returns a condensed 1D array.
   - `squareform(...)` converts that 1D array into a symmetric 2D matrix (where diagonal is 0, since distance from a point to itself is 0).
3. **Linkage & Dendrograms**:
   - `linkage(X, 'single')` performs the agglomerative clustering math using Single Linkage. It returns an array `Z` containing the hierarchical merge sequence.
   - `dendrogram(...)` takes the `Z` array and physically draws the tree-like diagram.
   - This process is repeated for `'complete'` linkage, and both are plotted side-by-side using `plt.subplot`.

---

## Viva Questions

### Program-Specific Questions
**Q1: Why is `load_iris().data[:6]` used instead of the full dataset?**
*Answer:* Hierarchical clustering on 150 points creates a very dense, unreadable dendrogram. By slicing the array to `[:6]`, we limit it to 6 points, allowing us to clearly see the mathematical merge steps and the proximity matrix structure in an educational setting.

**Q2: What is the difference between `pdist` and `squareform` in `9.py`?**
*Answer:* `pdist` calculates the distances but returns a flattened 1D array to save memory (since the matrix is symmetric and the diagonal is zero). `squareform` converts this flattened array into the traditional N x N 2D matrix format.

**Q3: Looking at `9o.py`'s `cluster_distance` function, how is single linkage calculated?**
*Answer:* It calculates the Euclidean distance between every combination of points across the two clusters (`pts1` and `pts2`) and simply returns the `min(dists)`—the absolute shortest distance found.

**Q4: How does the `Z` array (the linkage matrix) represent the merges?**
*Answer:* As seen in `9o.py`, when two clusters `c1` and `c2` merge, a row is appended to `Z` containing: `[c1, c2, min_dist, new_cluster_size]`. `scipy`'s `dendrogram` function reads this exact 4-column format to draw the tree.

**Q5: What do the vertical and horizontal lines in a dendrogram represent?**
*Answer:* The horizontal lines represent the merging of two clusters. The height (vertical position on the Y-axis) of that horizontal line represents the mathematical distance between the two clusters at the moment they were merged.

### General Theory Questions
**Q6: What is a Dendrogram?**
*Answer:* A dendrogram is a tree-like diagram that records the sequences of merges or splits in hierarchical clustering. The leaves of the tree are individual data points, and the root is the single cluster containing all data points.

**Q7: What is the main advantage of Hierarchical Clustering over K-Means?**
*Answer:* In Hierarchical Clustering, you do not need to specify the number of clusters (`K`) in advance. You can look at the generated dendrogram and "cut" the tree at whatever height makes the most sense for your problem.

**Q8: Explain the difference between Single Linkage and Complete Linkage.**
*Answer:* Single linkage defines cluster distance based on the two closest points (minimum distance), often causing a "chaining" effect. Complete linkage defines cluster distance based on the two furthest points (maximum distance), resulting in more compact clusters.

**Q9: What is Average Linkage?**
*Answer:* Average linkage is a middle-ground approach where the distance between two clusters is defined as the average distance between all pairs of points across the two clusters.

**Q10: What is the time complexity of Agglomerative Hierarchical Clustering?**
*Answer:* Standard agglomerative clustering is very slow, with a time complexity of `O(N^3)` (or `O(N^2 log N)` with optimized priority queues), making it unsuitable for extremely large datasets compared to K-Means which is `O(N * K * iterations)`.
