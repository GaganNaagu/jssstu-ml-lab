# Experiment 5: Data Visualization (Boxplot) and Alpha-Beta Pruning

This document covers the theoretical concepts, code explanation, and viva questions for the fifth lab experiment:
1. `5a.py`: Data Visualization using Boxplots.
2. `5b.py`: The Alpha-Beta Pruning Algorithm.

---

## Part A: Data Visualization (Boxplot) - `5a.py`

### Theoretical Background
A **Boxplot** (or box-and-whisker plot) is a standardized way of displaying the distribution of data based on a five-number summary:
1. **Minimum**: The lowest data point excluding outliers.
2. **First Quartile (Q1)**: The 25th percentile (lower edge of the box).
3. **Median**: The 50th percentile (the line inside the box).
4. **Third Quartile (Q3)**: The 75th percentile (upper edge of the box).
5. **Maximum**: The highest data point excluding outliers.

Boxplots are excellent for visually identifying **outliers** (plotted as individual dots outside the "whiskers") and understanding the variance and skewness of the data.

### Code Walkthrough
1. **Load Data**: The code loads the numerical feature data `X` from the Iris dataset.
2. **Plotting**: 
   - `plt.boxplot(X, tick_labels=iris.feature_names)` generates a box plot for each column (feature) in `X`.
   - `tick_labels` assigns the actual names (e.g., 'sepal length (cm)') to the X-axis so we know which box belongs to which feature.

---

## Part B: Alpha-Beta Pruning - `5b.py`

### Theoretical Background
Alpha-Beta Pruning is an optimization technique for the Minimax algorithm. As seen in Experiment 4, standard Minimax explores the entire game tree, which is impossible for complex games. 

Alpha-Beta Pruning significantly reduces the number of nodes evaluated in the search tree by "pruning" (cutting off) branches that cannot possibly influence the final decision.

It uses two parameters:
- **Alpha (α)**: The best (highest) value that the Maximizer can guarantee at that level or above. Initially `-infinity`.
- **Beta (β)**: The best (lowest) value that the Minimizer can guarantee at that level or above. Initially `+infinity`.

**Pruning Condition**: If at any point **`beta <= alpha`**, the current branch evaluation stops, and the algorithm returns immediately (prunes the rest of the children). This happens because we've found a path that the opponent will avoid anyway, so there's no need to evaluate its remaining options.

### Code Walkthrough
1. **Function Signature**: The `alpha_beta` function takes two extra parameters compared to minimax: `alpha` and `beta`.
2. **Maximizer Logic**:
   - Recursively calls children to get `val`.
   - Updates `best_val = max(best_val, val)`.
   - Updates `alpha = max(alpha, best_val)`.
   - **Prune Check**: `if beta <= alpha: break`. If this condition is met, it stops checking the remaining siblings in `node.children` and returns the `best_val`.
3. **Minimizer Logic**:
   - Recursively calls children to get `val`.
   - Updates `best_val = min(best_val, val)`.
   - Updates `beta = min(beta, best_val)`.
   - **Prune Check**: `if beta <= alpha: break`. Cuts off remaining sibling evaluations.

---

## Viva Questions

### Program-Specific Questions
**Q1: In `5a.py`, what do the lines (whiskers) extending from the boxes represent?**
*Answer:* The whiskers represent the range of the data, extending from the first and third quartiles (the box) to the minimum and maximum values, excluding statistical outliers.

**Q2: How are outliers typically represented in a matplotlib boxplot?**
*Answer:* Outliers—data points that fall significantly far from the median (usually defined as beyond 1.5 * Interquartile Range)—are plotted as individual dots or circles beyond the ends of the whiskers.

**Q3: In `5b.py`, what are the initial values passed for alpha and beta?**
*Answer:* When initially calling the function, `alpha` is set to `-infinity` (`float('-inf')`) and `beta` is set to `+infinity` (`float('inf')`).

**Q4: Explain the line `if beta <= alpha: break` inside the Maximizer block.**
*Answer:* This is the pruning condition. If `beta <= alpha`, it means the Minimizer higher up in the tree already has a better or equal option elsewhere, and will never allow the game to reach this state. Therefore, it is useless to evaluate any more children of this node, and the loop breaks.

**Q5: Does Alpha-Beta pruning change the final optimal value compared to standard Minimax?**
*Answer:* No. Alpha-Beta pruning is guaranteed to return the exact same optimal value and move as standard Minimax. It just does so much faster by skipping irrelevant branches.

### General Theory Questions
**Q6: What is the Interquartile Range (IQR)?**
*Answer:* The IQR is the distance between the first quartile (Q1) and the third quartile (Q3) in a boxplot. It represents the middle 50% of the data and is used as a measure of statistical dispersion.

**Q7: What is the best-case time complexity of Alpha-Beta Pruning?**
*Answer:* If the tree is perfectly ordered (meaning the best move is always evaluated first at every node), the time complexity drops from `O(b^m)` (Minimax) to `O(b^(m/2))`. This allows the algorithm to search twice as deep in the same amount of time.

**Q8: What is "node ordering" and why is it important in Alpha-Beta pruning?**
*Answer:* Node ordering is the practice of attempting to evaluate the most promising moves first. Good node ordering maximizes the number of branches pruned, pushing performance closer to the best-case scenario of `O(b^(m/2))`.

**Q9: If the pruning condition is met, are the pruned nodes evaluated?**
*Answer:* No. The algorithm immediately breaks out of the loop and returns the current best value, completely ignoring and not exploring any remaining child nodes of that state.

**Q10: Can Alpha-Beta pruning be used in games with more than two players?**
*Answer:* No. Alpha-Beta pruning relies strictly on the zero-sum, two-player nature of games where one's gain is the other's loss (max vs min). For multi-player games, an algorithm like `Max^n` is used, where pruning is generally not possible in the same way.
