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
