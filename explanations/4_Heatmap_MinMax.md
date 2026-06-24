# Program 4: Heat-maps & Min-Max Algorithm

## Part A: Visualize n-dimensional data using Heat-maps

### 1. Conceptual Overview
A **Heat-map** uses a color-coding system to represent different values in a matrix (a 2D grid). In machine learning, heat-maps are most commonly used to visualize a **Correlation Matrix**, which shows how strongly every feature in a dataset relates to every other feature.

### 2. What to Look For (Interpretation)
Correlation values range from -1 to 1.
*   **Value near 1 (Deep Red/Warm):** Perfect positive correlation. When Feature A goes up, Feature B always goes up.
*   **Value near -1 (Deep Blue/Cool):** Perfect negative correlation. When Feature A goes up, Feature B always goes down.
*   **Value near 0 (White/Neutral):** No relationship whatsoever.
*   **The Diagonal:** The diagonal line from top-left to bottom-right will always be 1, because a feature is always perfectly correlated with itself.

### 3. Real-World Application
*   **Data Science Feature Selection:** If two features have a correlation of 0.99, they are essentially providing the exact same information to the model. You can safely drop one of them to save computational power without losing accuracy.
*   **Stock Market Analytics:** Visualizing the S&P 500. Green squares show stocks going up, red shows stocks going down. You can instantly see if the "Tech Sector" as a whole is bleeding while "Healthcare" is rising.

---

## Part B: Min-Max Algorithm

### 1. Conceptual Overview
**Min-Max** is an artificial intelligence algorithm used heavily in **Game Theory** for two-player, zero-sum games (games where one player's gain is exactly equal to the other player's loss). 

The algorithm assumes both players are playing perfectly. 
*   **The Maximizer (You):** Tries to choose a move that results in the highest possible score (+ infinity).
*   **The Minimizer (Opponent):** Tries to choose a move that results in the lowest possible score (- infinity).

### 2. Step-by-Step Logic
1.  Generate the entire game tree from the current position all the way down to the terminal states (win, lose, or draw).
2.  Assign a mathematical utility value to the terminal states (e.g., Win = +10, Lose = -10, Draw = 0).
3.  **Work Backwards (Bottom-Up):**
    *   If it is the Minimizer's turn, they look at the available nodes and "pull up" the *smallest* value.
    *   If it is the Maximizer's turn, they look at the available nodes and "pull up" the *largest* value.
4.  The root node eventually gets the optimal value, revealing the best guaranteed move you can make.

### 3. Key Concepts to Mention in Exams
*   **Depth Limit:** In complex games like Chess, the game tree is infinitely large. You cannot reach terminal states. Instead, you stop at a specific "Depth Limit" (e.g., 5 moves ahead) and use a heuristic function to estimate the board's value (e.g., counting the value of pieces left on the board).

### 4. Real-World Application
*   **Classic Board Games AI:** The fundamental backbone of computers playing Tic-Tac-Toe, Checkers, Connect Four, and Chess. The computer looks ahead at all possible outcomes, assumes you will play your best counter-move, and selects the path that minimizes your ability to hurt them.



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



## Deep Dive Code Breakdown

### 4a.py: Heatmap Variables
*   `sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")`:
    *   `df.corr()`: Calculates the pairwise correlation matrix of all columns. This matrix is what the heatmap actually visualizes.
    *   `annot=True`: Forces the heatmap to physically write the underlying numerical value directly onto each colored square.
    *   `fmt=".2f"`: String formatting. It tells the annotator to round the numbers to a floating-point with exactly 2 decimal places.
    *   `cmap='coolwarm'`: A diverging color map perfectly suited for correlations ranging from -1 to 1. 

### 4b.py: Min-Max Variables
*   `isMax`: A boolean flag (True/False) passed down the recursion tree. When True, it's the Max player's turn, so the algorithm uses `max()` to pick the highest score from the recursive calls. When False, it's the Min player's turn, so it uses `min()` to pick the lowest score.
