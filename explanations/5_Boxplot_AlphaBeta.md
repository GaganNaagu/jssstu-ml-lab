# Program 5: Box-plots & Alpha-Beta Pruning

## Part A: Visualize n-dimensional data using Box-plots

### 1. Conceptual Overview
A **Box-plot (or Whisker Plot)** is a standardized way of displaying the distribution of data based on a five-number mathematical summary. Unlike scatter plots that show every single point, box-plots abstract the data to show its statistical spread.

### 2. What to Look For (Interpretation)
When reading a box-plot, an examiner expects you to identify:
1.  **The Box (Interquartile Range - IQR):** Contains the middle 50% of the data (from Q1 to Q3).
2.  **The Median (Line inside the box):** The exact mathematical middle of the dataset.
3.  **The Whiskers (Lines extending from the box):** Represent the upper and lower 25% of the data, excluding outliers.
4.  **Outliers (Dots outside the whiskers):** Data points that are statistically abnormal. They sit significantly far away from the rest of the data.

### 3. Real-World Application
*   **Corporate Analytics:** Analyzing the salaries of a company. The box shows where the vast majority of regular employees sit. The massive outlier dot at the very top instantly highlights the CEO's salary, proving it is a statistical anomaly compared to the rest of the workforce.

---

## Part B: Alpha-Beta Pruning Algorithm

### 1. Conceptual Overview
**Alpha-Beta Pruning** is an optimization technique specifically designed for the **Min-Max algorithm**. 
In complex games like Chess, the game tree is so massively huge that evaluating every single possible future move takes too long. Alpha-Beta Pruning solves this by "pruning" (ignoring/cutting off) branches of the tree that **cannot possibly influence the final decision**. 

### 2. Step-by-Step Logic
It maintains two values as it explores the tree:
*   **Alpha ($\alpha$):** The best (highest) value that the Maximizer can guarantee so far. (Initializes at $-\infty$)
*   **Beta ($\beta$):** The best (lowest) value that the Minimizer can guarantee so far. (Initializes at $+\infty$)

**The Pruning Rule:** If at any point the algorithm finds that $\beta \le \alpha$, it immediately stops evaluating that branch. Why? Because the opponent will simply never allow you to reach that part of the tree anyway, so calculating it is a waste of time!

### 3. Key Concepts to Mention in Exams
*   **Efficiency:** Alpha-Beta pruning does *not* change the final decision of the Min-Max algorithm. It simply arrives at the exact same mathematically perfect decision much, much faster.
*   **Node Ordering:** The efficiency of pruning relies heavily on the order nodes are checked. If you check the best moves first, you can prune almost half the entire tree!

### 4. Real-World Application
*   **IBM's Deep Blue:** The chess supercomputer that famously defeated human world champion Garry Kasparov. By aggressively pruning terrible moves early, the computer was able to calculate 10 to 14 moves deep into the future in fractions of a second.



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



## Deep Dive Code Breakdown

### 5a.py: Box Plot Variables
*   `plt.boxplot(data, vert=True, patch_artist=True, tick_labels=iris.feature_names)`:
    *   `vert=True`: Draws the boxes vertically rather than horizontally.
    *   `patch_artist=True`: Tells matplotlib to fill the boxes with color, rather than just drawing hollow outlines.
    *   `tick_labels=iris.feature_names`: Assigns the proper names of the features (like 'sepal length (cm)') to the bottom X-axis.

### 5b.py: Alpha-Beta Variables
*   `alpha`: Passed down the recursive tree. It keeps track of the absolute highest score the Maximizer has secured so far along the current path.
*   `beta`: Keeps track of the absolute lowest score the Minimizer has secured so far.
*   `if beta <= alpha: break`: The actual pruning trigger. If the lowest score the Minimizer can force (`beta`) becomes worse than or equal to a score the Maximizer already secured elsewhere (`alpha`), the Minimizer will simply never allow play to reach this branch, so we stop evaluating it (`break`).


### Important Notes
- The leaf values evaluated for the Alpha-Beta Pruning tree in 5b.py from left to right are: 3, 5, 6, 9, 1, 2, 0, -1.
