# Program 13: KNN Manhattan on Fruit Dataset

### 1. Conceptual Overview
*(Note: Be sure to read the general KNN logic in the explanation for Program 7).*

This program strictly focuses on utilizing the **Manhattan Distance** metric within the K-Nearest Neighbors classification algorithm. It is also commonly known as the **L1 Norm** or **Taxicab Geometry**.

### 2. Deep Dive: Manhattan Distance
Manhattan distance calculates the distance between two points by summing the absolute differences of their individual Cartesian coordinates. You are NOT allowed to move diagonally. You can only move up, down, left, and right along a grid.

**Mathematical Formula:**
$$d(p, q) = |p_1 - q_1| + |p_2 - q_2| + ... + |p_n - q_n|$$

### 3. Step-by-Step Logic for the Fruit Dataset
The Fruit dataset contains measurements like Mass, Width, Height, and Color Score.
1.  We split the dataset: 80% is used for Training (memorization), and 20% is used for Testing.
2.  For a mystery fruit in the 20% testing pile, the algorithm calculates the Manhattan distance to all fruits in the 80% training pile.
3.  Because $K=5$, it grabs the 5 closest neighbors.
4.  If the neighbors are [Apple, Apple, Apple, Mandarin, Lemon], the majority vote wins, and the mystery fruit is classified as an Apple.

### 4. Key Concepts to Mention in Exams: Why Manhattan over Euclidean?
If an examiner asks why you would ever choose Manhattan over Euclidean, here is the answer:
*   **High Dimensionality:** In datasets with hundreds or thousands of columns, Euclidean distance mathematically breaks down and all points start to look like they are exactly the same distance apart. Manhattan distance holds up much better in high dimensions.
*   **Outlier Resistance:** Euclidean distance squares the differences. If you have a massive anomaly or outlier in your data, squaring it makes the error explode, ruining your predictions. Manhattan distance uses absolute values, so it is mathematically "robust" and largely ignores massive outliers.

### 5. Real-World Application
*   **City Logistics / Delivery:** If you are building a routing system for FedEx trucks in New York City (Manhattan), a straight-line Euclidean distance is useless because trucks cannot drive through skyscrapers. You must use Manhattan distance to calculate the actual drivable distance along the city's square street blocks.
