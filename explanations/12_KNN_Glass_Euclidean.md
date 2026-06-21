# Program 12: KNN Euclidean on Glass Dataset

### 1. Conceptual Overview
*(Note: Be sure to read the general KNN logic in the explanation for Program 7).*

This program strictly focuses on utilizing the **Euclidean Distance** metric within the K-Nearest Neighbors classification algorithm.

### 2. Deep Dive: Euclidean Distance
Euclidean distance is the "ordinary" or natural straight-line distance between two points in multidimensional Euclidean space. It is exactly what you would measure if you laid a physical ruler down between two dots on a piece of paper.

It is derived directly from the **Pythagorean Theorem** ($a^2 + b^2 = c^2$).
**Mathematical Formula:**
$$d(p, q) = \sqrt{(p_1 - q_1)^2 + (p_2 - q_2)^2 + ... + (p_n - q_n)^2}$$

### 3. Step-by-Step Logic for the Glass Dataset
The Glass dataset contains varying levels of chemicals like Sodium, Magnesium, and Iron. 
1.  We split the dataset: 70% of the data is given to the algorithm to "memorize" (Training). The remaining 30% is kept completely secret (Testing).
2.  We take one piece of glass from the 30% secret pile.
3.  The algorithm calculates the Euclidean distance from this mystery glass to all the glasses in the 70% training pile based on their chemical numbers.
4.  Because $K=3$, it looks at the 3 closest glasses in the training pile.
5.  If 2 of those neighbors are "Car Headlamp Glass" and 1 is "Tableware Glass", the algorithm predicts that our mystery glass is a Car Headlamp.

### 4. Key Concepts to Mention in Exams
*   **Sensitivity to Scale:** Because Euclidean distance squares the differences, a feature with massive numbers (like a chemical measured in the thousands) will completely overpower a feature with small numbers (like a chemical measured in decimals). Therefore, you **must normalize or standardize** your data before using Euclidean distance!

### 5. Real-World Application
*   **Aviation / Drones:** If you are programming a drone to fly to the nearest charging station, you use Euclidean distance because the drone can fly in a perfect straight line over buildings and obstacles.
