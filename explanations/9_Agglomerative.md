# Program 9: Agglomerative Clustering

**Logic / Algorithm:** This is a type of Hierarchical Clustering. It uses a "bottom-up" approach.
1. Initially, every single data point is considered its own cluster.
2. The two closest clusters are merged into one.
3. This repeats until all points are merged into a single giant cluster (forming a tree structure called a Dendrogram).

**Linkage Criteria (How do we measure distance between clusters?):**
- **Single Linkage:** Distance between the two *closest* points of the clusters.
- **Complete Linkage:** Distance between the two *farthest* points of the clusters.

**Real-World Example:** Evolutionary Biology. Organizing species into a family tree (phylogeny). You start with individual species and group them by genetic similarity until you reach the common ancestor of all life.
