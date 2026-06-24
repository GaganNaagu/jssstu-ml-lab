import os

updates = {
    "1_Scatter_HillClimbing.md": """
## Execution Output & Interpretations

### 1a.py: Scatter Plot
**Graph:**
![1a.py](../outputs/1a.png)

**How to understand this graph:**
* **What it shows:** A scatter plot displays individual data points on a 2D coordinate system. Here, the X and Y axes represent two features of the Iris dataset (Sepal Length and Sepal Width).
* **Colors:** Different colors represent different classes (species of Iris flowers).
* **Interpretation:** By looking at the spread and overlap of colors, you can easily see if certain classes are naturally grouped together or if they are mixed. If the colors are well-separated, a machine learning model will have an easy time classifying them!

### 1b.py: Hill Climbing
**Output:**
```text
Starting state: -5.5718
Local maximum found at x = 2.0282
Objective value: 3.9992
```
**Interpretation:** The algorithm starts at a random negative coordinate and iteratively takes steps uphill. It successfully finds the peak (local maximum) at x ≈ 2.02, where the mathematical function reaches its highest value of ≈ 3.99.
""",

    "2_3DSurface_BFS.md": """
## Execution Output & Interpretations

### 2a.py: 3D Surface Plot
**Graph:**
![2a.py](../outputs/2a.png)

**How to understand this graph:**
* **What it shows:** A 3D surface plot visualizes a mathematical function with two inputs (X and Y on the horizontal plane) and one output (Z on the vertical axis). 
* **Colors & Shape:** The colors map to the height (Z-value). Darker/cooler colors are usually the valleys (minima) and brighter/warmer colors are the peaks (maxima).
* **Interpretation:** Imagine this as a mountainous landscape. Optimization algorithms (like gradient descent) are essentially trying to find the lowest valley or highest peak by "walking" along this terrain.

### 2b.py: BFS Algorithm
**Output:**
```text
Goal Reached!
Path traversed: ['S', 'A', 'D', 'G']
```
**Interpretation:** The output shows the exact sequence of nodes visited by the Best-First Search (Greedy) algorithm to reach the Goal ('G') from the Start ('S'). It uses a heuristic to actively guess which path is closest to the goal, leading to a fast, though not necessarily optimal, route.
""",

    "3_Contour_AStar.md": """
## Execution Output & Interpretations

### 3a.py: Contour Plot
**Graph:**
![3a.py](../outputs/3a.png)

**How to understand this graph:**
* **What it shows:** A contour plot is a 2D representation of a 3D surface, just like a topographic map used by hikers.
* **The Rings/Lines:** Each line connects points of equal Z-value (height). 
* **Interpretation:** 
  * If the rings are packed very closely together, the slope is extremely steep. 
  * If the rings are far apart, the terrain is relatively flat. 
  * The center of a series of concentric rings represents a local minimum (valley bottom) or maximum (mountain peak).

### 3b.py: A* Search
**Output:**
```text
A* Path: ['S', 'A', 'C', 'G']
Total Cost: 9
```
**Interpretation:** A* search smartly uses heuristics (estimated distance to goal) to find the absolute best path. The output confirms the shortest path found is S -> A -> C -> G, and tells us the total accumulated cost (distance/effort) to travel that path is 9.
""",

    "4_Heatmap_MinMax.md": """
## Execution Output & Interpretations

### 4a.py: Heatmap
**Graph:**
![4a.py](../outputs/4a.png)

**How to understand this graph:**
* **What it shows:** A heatmap uses colors to represent the numerical values inside a 2D matrix or table.
* **The Colors:** A color bar on the side acts as the legend. Typically, bright/warm colors mean higher values (or strong positive correlation), and dark/cool colors mean lower values (or negative correlation).
* **Interpretation:** Instead of staring at a giant table of numbers, you can instantly spot hotspots, trends, or heavily correlated variables just by looking at the colored blocks.

### 4b.py: Min-Max Algorithm
**Output:**
```text
The optimal value is: 12
```
**Interpretation:** The algorithm evaluates a game tree assuming both players play perfectly. It determined that if the Maximizing player makes the best possible moves, they are guaranteed to secure a score of at least 12, regardless of what the Minimizing opponent does.
""",

    "5_Boxplot_AlphaBeta.md": """
## Execution Output & Interpretations

### 5a.py: Box Plot
**Graph:**
![5a.py](../outputs/5a.png)

**How to understand this graph:**
* **What it shows:** A box-plot (often resembling candlesticks in finance) shows the statistical distribution of data. 
* **The Box:** Represents the Interquartile Range (IQR) – the middle 50% of your data. The bottom edge is the 25th percentile, and the top is the 75th percentile.
* **The Line inside the Box:** This is the **Median** (the exact mathematical middle of the dataset).
* **The Whiskers (Lines extending out):** These represent the upper and lower 25% of the data, showing the typical range.
* **The Dots (Outliers):** These are individual data points that are statistically abnormal. They sit significantly far away from the rest of the data. 
* **Interpretation:** It tells you if your data is skewed, tightly packed, or if there are crazy anomalies (outliers) that might mess up your machine learning model.

### 5b.py: Alpha-Beta Pruning
**Output:**
```text
The optimal value is: 5
```
**Interpretation:** Similar to the Min-Max output, this shows the guaranteed best score for the Maximizer. However, by using alpha-beta pruning, the algorithm skipped evaluating large chunks of the game tree that were proven to be irrelevant, arriving at the answer much faster.
""",

    "6_NaiveBayes_Titanic.md": """
## Execution Output & Interpretations

### 6.py: Naive Bayes
**Output:**
```text
Accuracy: 0.7674418604651163
Classification Report:
               precision    recall  f1-score   support

           0       0.80      0.81      0.80       126
           1       0.72      0.71      0.72        89

    accuracy                           0.77       215
   macro avg       0.76      0.76      0.76       215
weighted avg       0.77      0.77      0.77       215
```

**How to understand this output:**
* **Accuracy (0.767 or ~77%):** The model correctly predicted the survival outcome 77% of the time.
* **Precision:** When the model predicted someone survived (1), it was right 72% of the time.
* **Recall:** Out of all the people who *actually* survived, the model successfully identified 71% of them.
* **F1-Score:** This is a combination (harmonic mean) of Precision and Recall. It gives a balanced view of the model's performance, especially if classes are imbalanced.
""",

    "7_KNN_Glass_Combo.md": """
## Execution Output & Interpretations

### 7.py: K-Nearest Neighbors (Glass Dataset)
**Output:**
```text
Accuracy with Euclidean distance (k=3): 0.6462
Accuracy with Manhattan distance (k=3): 0.6462
```

**How to understand this output:**
* **What happened:** The algorithm tried to classify types of glass based on their chemical properties by finding the 3 "closest" known examples (K=3).
* **Euclidean vs Manhattan:** These are two different ways of measuring "distance" between data points. Euclidean is the direct straight-line distance, while Manhattan is grid-like (like navigating city blocks).
* **Interpretation:** In this specific run, both the Manhattan and Euclidean distance formulas performed identically (~64.6% accuracy) for this dataset.
""",

    "8_KMeans.md": """
## Execution Output & Interpretations

### 8.py & 8o.py: K-Means Clustering
**Graphs:**
![8.py](../outputs/8.png)
![8o.py](../outputs/8o.png)

**How to understand these graphs:**
* **What they show:** K-Means is an *unsupervised* algorithm. It groups data into `K` distinct clusters based on feature similarity.
* **The Clusters (Colors):** Each color represents a newly formed cluster. The algorithm decided these points belong together.
* **The Centroids (often marked with an 'X' or distinct dot):** These are the exact mathematical center-points of each cluster. 
* **Interpretation:** You are looking to see if the algorithm successfully identified natural groupings in the data. If the clusters are well-separated and make logical sense, K-Means did a good job! The output arrays represent which cluster (0, 1, or 2) each data point was assigned to.
""",

    "8o_KMeans.md": """
## Execution Output & Interpretations
*(See 8_KMeans.md for outputs and interpretations, as they cover the same concept and the graphs are generated successfully there.)*
""",

    "9_Agglomerative.md": """
## Execution Output & Interpretations

### 9.py: Agglomerative Clustering
**Output:**
```text
Single Linkage Labels: [1 1 1 1 1 1 1 1 1 1]
Complete Linkage Labels: [1 1 1 1 1 1 1 1 1 1]
```

**Graph:**
![9.py](../outputs/9.png)

**How to understand this graph (Dendrogram):**
* **What it shows:** A Dendrogram is a tree-like diagram that records exactly how the algorithm grouped data points together step-by-step.
* **The X-Axis:** Represents the individual data points.
* **The Y-Axis (Height):** Represents the *distance* or *dissimilarity* between the clusters. The higher up two branches merge, the less similar they are.
* **Interpretation:** To form actual clusters, you draw an imaginary horizontal line across the dendrogram at a specific height. The number of vertical lines you intersect is the number of clusters you get. Single-linkage measures the shortest distance between clusters, while complete-linkage measures the furthest distance.
""",

    "10_PCA_LDA.md": """
## Execution Output & Interpretations

### 10.py: PCA & LDA Dimensionality Reduction
**Graph:**
![10.py](../outputs/10.png)

**How to understand these graphs:**
* **What it shows:** Both PCA and LDA are trying to squash a multi-dimensional dataset down to just 2 dimensions so we can visualize it on a flat screen.
* **PCA (Principal Component Analysis):** This is *unsupervised*. It doesn't care about the class labels; it simply looks for the angles where the data is spread out the most (maximum variance).
* **LDA (Linear Discriminant Analysis):** This is *supervised*. It actively uses the class labels and tries to find the angles that maximize the distance *between* different classes while minimizing the spread *within* each class.
* **Interpretation:** Look at the separation of colors. Usually, LDA (the right plot) will show much clearer boundaries between classes because it explicitly tries to separate them, whereas PCA (the left plot) just looks for raw data spread.
""",

    "11_Perceptron.md": """
## Execution Output & Interpretations

### 11.py: Perceptron Logic Gates
**Output:**
```text
AND Function Predictions:
[0 0] -> 0
[0 1] -> 0
[1 0] -> 0
[1 1] -> 1

-----------------------

OR Function Predictions:
[0 0] -> 0
[0 1] -> 1
[1 0] -> 1
[1 1] -> 1
```

**How to understand this output:**
* **What happened:** A Perceptron (the absolute simplest form of a neural network) was trained to mimic basic computer logic gates.
* **Interpretation:** The output perfectly matches the truth tables for AND and OR gates. This proves that a single perceptron is capable of learning linearly separable mathematical boundaries!
"""
}

for filename, content in updates.items():
    path = os.path.join("explanations", filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            existing_content = f.read()
        if "Execution Output & Interpretations" not in existing_content:
            with open(path, "a", encoding="utf-8") as f:
                f.write("\n\n" + content)

print("Markdown files updated.")
