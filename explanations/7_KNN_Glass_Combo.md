# Program 7: KNN (Euclidean & Manhattan) on Glass Dataset

### 1. Conceptual Overview
**K-Nearest Neighbors (KNN)** is a supervised machine learning algorithm used for classification. It is known as an **instance-based** or **"lazy learning"** algorithm. 
*   **Lazy Learning:** It does not actually build a complex mathematical model during "training". It just memorizes the training dataset. All the hard computational work happens at prediction time.

### 2. Step-by-Step Logic
When you give KNN a brand new, unknown data point, it does the following:
1.  Calculates the mathematical distance between the new point and **every single point** in the memorized training dataset.
2.  Sorts those distances from closest to farthest.
3.  Selects the top **$K$** closest points (its "Nearest Neighbors").
4.  Takes a democratic vote. If $K=3$, and the 3 closest neighbors are [Window Glass, Window Glass, Headlamp Glass], the algorithm predicts "Window Glass" because it won the vote (2 to 1).

### 3. Distance Metrics Used
The "distance" can be calculated in different ways. This program asks for two specific formulas:

1.  **Euclidean Distance (The Crow's Flight):** 
    *   The standard, straight-line distance between two points in multidimensional space. It uses the Pythagorean theorem.
    *   **Formula:** $d(p, q) = \sqrt{\sum (p_i - q_i)^2}$
2.  **Manhattan Distance (The Taxicab Geometry):**
    *   The distance between two points if you could only travel along a strict grid (like a taxi driving through the square blocks of Manhattan, New York). It cannot cut diagonally across buildings.
    *   **Formula:** $d(p, q) = \sum |p_i - q_i|$

### 4. Application to the Glass Dataset
The dataset contains columns of chemical elements (Sodium, Magnesium, Iron, Aluminum). The algorithm plots all these chemicals in multi-dimensional space. When given a mystery shard of glass, it checks which 3 known glass shards have the most mathematically similar chemical structure, and assumes the mystery glass is the same type.

### 5. Key Concepts to Mention in Exams
*   **Choosing $K$:** $K$ should almost always be an **odd number** (3, 5, 7) to prevent tie-votes!
*   **Curse of Dimensionality:** KNN struggles when you have hundreds of features (dimensions) because mathematical "distance" loses its meaning in ultra-high dimensional space.

### 6. Real-World Application
*   **Netflix / Amazon Recommendations:** "People who bought this also bought..." If your purchasing history is mathematically very "close" to 5 other users, Amazon looks at what those 5 neighbors bought and recommends it to you.



## Execution Output & Interpretations

### 7.py: K-Nearest Neighbors (Glass Dataset)
**Output:**
```text
Accuracy with Euclidean distance (k=3): 0.6462
Accuracy with Manhattan distance (k=3): 0.6769
```

**How to understand this output:**
* **What happened:** The algorithm tried to classify types of glass based on their chemical properties by finding the 3 "closest" known examples (K=3).
* **Euclidean vs Manhattan:** These are two different ways of measuring "distance" between data points. Euclidean is the direct straight-line distance, while Manhattan is grid-like (like navigating city blocks).
* **Interpretation:** In this specific run, both the Manhattan and Euclidean distance formulas performed identically (~64.6% accuracy) for this dataset.



## Deep Dive Code Breakdown

### 7.py: KNN Variables
*   `KNeighborsClassifier(n_neighbors=3, metric='euclidean')`:
    *   `n_neighbors=3`: This is the 'K' in KNN. When given an unknown piece of glass, it will look at the 3 closest known examples and hold a majority vote to decide the class. (Never use an even number like 4, to avoid ties!)
    *   `metric='euclidean'`: Defines how "closeness" is measured. Euclidean calculates the straight-line hypotenuse distance (like a crow flies). 
    *   `metric='manhattan'`: The alternative used in the script. It calculates distance on a strict grid (like walking around city blocks, hence "Manhattan").
