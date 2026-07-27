# Experiment 4: Data Visualization (Heatmap) and Minimax Algorithm

This document covers the theoretical concepts, code explanation, and viva questions for the fourth lab experiment:
1. `4a.py`: Data Visualization using Correlation Heatmaps.
2. `4b.py`: The Minimax Algorithm.

---

## Part A: Data Visualization (Correlation Heatmap) - `4a.py`

### Theoretical Background
A heatmap is a two-dimensional graphical representation of data where individual values contained in a matrix are represented as colors. In Machine Learning, heatmaps are most frequently used to visualize the **Correlation Matrix**.

**Correlation** measures how strongly two variables are related to each other. Values range from -1 to 1:
- **1**: Perfect positive correlation (as one increases, the other increases).
- **0**: No correlation.
- **-1**: Perfect negative correlation (as one increases, the other decreases).

Visualizing this helps in Feature Selection. If two features are highly correlated (e.g., 0.95), they carry almost the same information, meaning we can drop one to simplify our model (dimensionality reduction).

### Code Walkthrough
1. **Load Data**: The code loads the Iris dataset and converts it into a pandas DataFrame.
2. **Correlation Calculation**: `df.corr()` calculates the pairwise Pearson correlation of all columns in the DataFrame.
3. **Plotting**: 
   - `sns.heatmap(...)` creates the colored grid.
   - `annot=True` writes the actual correlation number inside each colored cell.
   - `cmap='coolwarm'` sets the color theme. High correlations will be warm (red), and low/negative correlations will be cool (blue).

---

## Part B: Minimax Algorithm - `4b.py`

### Theoretical Background
Minimax is a decision-making and game theory algorithm used in artificial intelligence for finding the optimal move in a two-player, turn-based, zero-sum game (like Tic-Tac-Toe or Chess).

In these games, what is good for Player A is equally bad for Player B. 
- **Maximizer (Max)** tries to get the highest possible score.
- **Minimizer (Min)** tries to get the lowest possible score.

The algorithm uses Depth-First Search (DFS) to explore the entire game tree down to the terminal nodes (leaves). It then evaluates these leaves and propagates the values back up the tree. Max will always pick the child branch with the highest value, while Min will pick the branch with the lowest value.

### Code Walkthrough
1. **TreeNode Class**: A simple class to build the tree. Each node has a `value` and a list of `children`.
2. **Minimax Function**:
   - **Base Case**: If we reach `depth == 0` or a leaf node (`not node.children`), it returns the node's value and the path (which is just the node itself).
   - **Maximizing Player**: If it's Max's turn, it initializes `best_val = float("-inf")`. It recursively calls `minimax` for all children (passing `False` for the next turn to make it Min's turn). It updates `best_val` if a child returns a higher value, and appends the current node to the winning `best_path`.
   - **Minimizing Player**: If it's Min's turn, it initializes `best_val = float("inf")`. It recursively calls `minimax` on children (passing `True` to make it Max's turn). It updates `best_val` if a child returns a lower value.
3. **Game Tree**: The code builds a small tree with leaf nodes: 3, 5, 2, 9. Max goes first at the root.

---

## Viva Questions

### Program-Specific Questions
**Q1: What does `df.corr()` compute in `4a.py`?**
*Answer:* It computes the Pearson correlation coefficient between every pair of numerical columns in the DataFrame. 

**Q2: Why do we use `annot=True` in the seaborn heatmap?**
*Answer:* `annot=True` forces seaborn to print the exact mathematical correlation values inside each square of the heatmap, making it easier to read the precise numbers rather than just guessing based on the color.

**Q3: How does the minimax algorithm represent the starting worst-case scenarios for Max and Min?**
*Answer:* It initializes `best_val` as `float("-inf")` (negative infinity) for the Maximizer so any real score will be higher. It uses `float("inf")` (positive infinity) for the Minimizer so any real score will be lower.

**Q4: How does `4b.py` keep track of whose turn it is?**
*Answer:* It uses the boolean parameter `is_maximizing`. When making a recursive call to a child node, it passes the opposite boolean value (`not is_maximizing`), effectively alternating turns at each level of depth in the tree.

**Q5: In the provided game tree, what are the choices Min will make at depth 1?**
*Answer:* The left Min node has children 3 and 5, so it will choose 3. The right Min node has children 2 and 9, so it will choose 2.

### General Theory Questions
**Q6: What is a Zero-Sum game?**
*Answer:* A game where one player's gain is exactly equal to the other player's loss. If Player A gets +10 points, Player B effectively gets -10 points. Chess and Tic-Tac-Toe are zero-sum games.

**Q7: Is the Minimax algorithm a Breadth-First or Depth-First search?**
*Answer:* It is a Depth-First Search (DFS). It explores a branch all the way down to a leaf node to find the terminal utility value before backtracking to evaluate other branches.

**Q8: What is the main drawback of the standard Minimax algorithm?**
*Answer:* The biggest drawback is its time complexity, which is `O(b^m)` (where `b` is branching factor and `m` is maximum depth). For games with large branching factors like Chess, the tree becomes too massive to explore completely.

**Q9: Why is checking for highly correlated features important in ML?**
*Answer:* Highly correlated features provide redundant information. This can cause the "curse of dimensionality", increase model training time, and cause multicollinearity issues in models like Linear Regression. Dropping redundant features simplifies and often improves the model.

**Q10: Can Minimax be used for games with randomness, like Poker or Backgammon?**
*Answer:* Standard Minimax assumes perfect information and deterministic moves. For games with chance, a variation called the Expectiminimax algorithm is used, which introduces "chance nodes" that calculate the expected utility based on probabilities.
