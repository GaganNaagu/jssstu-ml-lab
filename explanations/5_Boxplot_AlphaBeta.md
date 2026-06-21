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
