# Program 9: Agglomerative Clustering

### 1. Conceptual Overview
**Agglomerative Clustering** is an **unsupervised** machine learning algorithm, specifically a type of **Hierarchical Clustering**. 
While K-Means forces you to guess the number of clusters ($K$) from the very beginning, Hierarchical Clustering builds a massive tree (called a **Dendrogram**) showing how every single data point relates to every other point. 

"Agglomerative" specifically means a **Bottom-Up** approach. 

### 2. Step-by-Step Logic
1.  **Start:** Every single data point in your dataset is considered its own completely separate cluster. (If you have 100 points, you start with 100 clusters).
2.  **Find the Closest:** The algorithm calculates the distance between all clusters and finds the two clusters that are closest together.
3.  **Merge:** It merges those two clusters into one slightly larger cluster.
4.  **Repeat:** It repeats steps 2 and 3 continuously. As it runs, the clusters get bigger and bigger until, eventually, all data points are merged into one massive, single cluster.
5.  **Cut the Tree:** You look at the resulting Dendrogram tree and draw a horizontal line across it to "cut" the tree into the desired number of clusters.

### 3. Linkage Criteria (How do we measure distance?)
How do you measure the distance between two clusters if they both contain multiple points?
*   **Single Linkage:** Calculates the distance between the two *closest* points of the two clusters. (Tends to create long, chain-like clusters).
*   **Complete Linkage:** Calculates the distance between the two *farthest* points of the two clusters. (Tends to create tight, compact, spherical clusters).
*   **Average Linkage:** Calculates the average distance of all points in cluster A to all points in cluster B.

### 4. Key Concepts to Mention in Exams
*   **Dendrogram:** Make sure to explain that the output is a tree diagram. The Y-axis represents the mathematical distance between the clusters when they were merged. 
*   **No "K" Needed Initially:** You don't have to guess $K$ like in K-Means. You just build the tree and decide $K$ later by looking at the visual result.

### 5. Real-World Application
*   **Evolutionary Biology / Taxonomy:** Building the "Tree of Life" (phylogeny). You start with individual animal species at the bottom. You group lions and tigers into 'felines', then group felines and canines into 'carnivores', merging upwards until you reach the common ancestor of all mammals.
