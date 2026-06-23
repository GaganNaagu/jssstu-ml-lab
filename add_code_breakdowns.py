import os

breakdowns = {
    "1_Scatter_HillClimbing.md": """
## Deep Dive Code Breakdown

### 1a.py: Scatter Plot Variables
*   `iris.target`: This is the exact answer key (labels) for the dataset. For the Iris dataset, `target` is an array of 0s, 1s, and 2s representing the three flower species (Setosa, Versicolor, Virginica).
*   `scatter = plt.scatter(...)` Parameters:
    *   `X[:, 0], X[:, 1]`: The first two arguments are the X-axis and Y-axis coordinates. `X[:, 0]` means "all rows, 0th column" (Sepal Length), and `X[:, 1]` is the 1st column (Sepal Width).
    *   `c=y`: The "color" parameter. By passing the `iris.target` array (`y`), it assigns a unique color to the 0s, 1s, and 2s automatically.
    *   `cmap='viridis'`: The Color Map. Matplotlib maps the numbers 0, 1, 2 to a color gradient. `'viridis'` is a default color-blind friendly map that goes from dark purple to bright yellow. Other possible values: `'plasma'`, `'inferno'`, `'magma'`, `'coolwarm'`.
    *   `s=50`: Size of the scatter dots. Increasing this makes the dots larger.
    *   `alpha=0.8`: The transparency level, ranging from 0.0 (invisible) to 1.0 (solid). 0.8 makes dots slightly transparent so you can see if multiple dots overlap.

### 1b.py: Hill Climbing Variables
*   `def objective(x):`: The mathematical function creating the "hill" we are trying to climb.
*   `step_size`: How far the algorithm "steps" horizontally (on the X-axis) to check if the height (Y-axis) increases.
*   `max_iterations`: A safety cutoff to stop the loop from running forever if it gets stuck on a flat surface.
""",

    "2_3DSurface_BFS.md": """
## Deep Dive Code Breakdown

### 2a.py: 3D Plot Variables
*   `np.meshgrid(x, y)`: To plot a 3D surface, you can't just use 1D lines of X and Y. You need a full 2D grid covering the entire floor (the X-Y plane). `meshgrid` multiplies the X and Y arrays to create this flat grid, which the Z-function then pulls up into a 3D shape.
*   `ax.plot_surface(X, Y, Z, cmap='plasma')`: The function that stretches a colored skin over your X, Y, and Z points. The `'plasma'` cmap paints the lowest points purple and the highest points yellow.

### 2b.py: BFS Variables
*   `queue = deque([start])`: `deque` stands for Double-Ended Queue. BFS requires a First-In, First-Out (FIFO) structure. While a normal Python list can act like a queue using `.pop(0)`, it is extremely slow for large lists. `deque.popleft()` is blazingly fast and is the industry standard for BFS.
""",

    "3_Contour_AStar.md": """
## Deep Dive Code Breakdown

### 3a.py: Contour Plot Variables
*   `plt.contourf(X, Y, Z, levels=50, cmap='inferno')`: 
    *   `contourf`: The 'f' stands for fill. It draws contour lines and fills the gaps between them with solid color.
    *   `levels=50`: Tells the plot to draw 50 distinct color bands (elevation levels). The higher this number, the smoother the gradient looks.
    *   `cmap='inferno'`: A color map that goes from black/dark purple to glowing white/yellow, making the "hot" peaks stand out clearly.

### 3b.py: A* Search Variables
*   `heapq.heappush(open_list, (f_score, start))`: A* doesn't use a normal list or queue; it uses a **Priority Queue** (min-heap). `heapq` automatically sorts the queue every time you add an item. 
*   `f_score`: This is the priority weight. It's the sum of `g` (actual cost from start to current) + `h` (estimated cost from current to goal). The Priority Queue always pops the node with the lowest `f_score` first, guaranteeing the smartest search.
""",

    "4_Heatmap_MinMax.md": """
## Deep Dive Code Breakdown

### 4a.py: Heatmap Variables
*   `sns.heatmap(data, annot=True, cmap='coolwarm', fmt=".2f")`:
    *   `annot=True`: Forces the heatmap to physically write the underlying numerical value directly onto each colored square.
    *   `fmt=".2f"`: String formatting. It tells the annotator to round the numbers to a floating-point with exactly 2 decimal places.
    *   `cmap='coolwarm'`: The perfect color map for diverging data (like correlations ranging from -1 to 1). The middle is white/neutral, negative numbers fade to dark blue, and positive numbers fade to dark red.

### 4b.py: Min-Max Variables
*   `is_maximizing_player`: A boolean flag (True/False) passed down the recursion tree. When True, it's the Max player's turn, so the algorithm uses `max()` to pick the highest score. When False, it's the Min player's turn, so it uses `min()` to pick the lowest score.
""",

    "5_Boxplot_AlphaBeta.md": """
## Deep Dive Code Breakdown

### 5a.py: Box Plot Variables
*   `sns.boxplot(x='species', y='sepal_length', data=df, palette='Set2')`:
    *   `data=df`: Tells Seaborn to pull variables directly from a Pandas DataFrame.
    *   `palette='Set2'`: A predefined set of aesthetic pastel colors. Other palettes include `'pastel'`, `'muted'`, `'deep'`, or `'dark'`.
    *   *Note on the "candles":* Unlike financial candlestick charts (which show Open, High, Low, Close over time), a boxplot shows purely statistical spread (25th percentile, Median, 75th percentile).

### 5b.py: Alpha-Beta Variables
*   `alpha`: Passed down the recursive tree. It keeps track of the absolute highest score the Maximizer has secured so far along the current path.
*   `beta`: Keeps track of the absolute lowest score the Minimizer has secured so far.
*   `if beta <= alpha: break`: The actual pruning trigger. If the lowest score the Minimizer can force (`beta`) becomes worse than or equal to a score the Maximizer already secured elsewhere (`alpha`), the Minimizer will simply never allow play to reach this branch, so we stop evaluating it (`break`).
""",

    "6_NaiveBayes_Titanic.md": """
## Deep Dive Code Breakdown

### 6.py: Naive Bayes Variables
*   `GaussianNB()`: The exact type of Naive Bayes model being used. "Gaussian" means it mathematically assumes that the continuous features (like Age or Fare) follow a normal, bell-curve distribution.
*   `train_test_split(X, y, test_size=0.3, random_state=42)`: 
    *   `test_size=0.3`: Tells the function to hide 30% of the dataset to be used later as a final exam for the model. The model is trained on the remaining 70%.
    *   `random_state=42`: Seeds the random number generator. The data is shuffled randomly before splitting, but using a seed ensures it shuffles the *exact same way* every time you run the code. (42 is just a classic programmer's joke number).
""",

    "7_KNN_Glass_Combo.md": """
## Deep Dive Code Breakdown

### 7.py: KNN Variables
*   `KNeighborsClassifier(n_neighbors=3, metric='euclidean')`:
    *   `n_neighbors=3`: This is the 'K' in KNN. When given an unknown piece of glass, it will look at the 3 closest known examples and hold a majority vote to decide the class. (Never use an even number like 4, to avoid ties!)
    *   `metric='euclidean'`: Defines how "closeness" is measured. Euclidean calculates the straight-line hypotenuse distance (like a crow flies). 
    *   `metric='manhattan'`: The alternative used in the script. It calculates distance on a strict grid (like walking around city blocks, hence "Manhattan").
""",

    "8_KMeans.md": """
## Deep Dive Code Breakdown

### 8.py & 8o.py: K-Means Variables
*   `KMeans(n_clusters=3, random_state=42)`:
    *   `n_clusters=3`: This is the 'K' in K-Means. You must hardcode how many groups you want the algorithm to divide the data into.
*   `plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, c='red')`:
    *   `centroids[:, 0]`: The X-coordinates of the calculated center-points of the clusters.
    *   `marker='x'`: Changes the shape of the point from a standard dot to an 'X' so it is easily distinguished from normal data points.
    *   `s=200`: Makes the 'X' massive (size 200) so it's highly visible.
""",

    "8o_KMeans.md": """
## Deep Dive Code Breakdown
*(See 8_KMeans.md for deep dive code breakdowns, as both cover K-Means parameters.)*
""",

    "9_Agglomerative.md": """
## Deep Dive Code Breakdown

### 9.py: Agglomerative Variables
*   `linkage(X, 'single')` vs `linkage(X, 'complete')`:
    *   `linkage` is the mathematical rule used to decide the distance between two distinct clusters.
    *   `'single'`: Looks at the distance between the *two closest points* in the two clusters. (Tends to create long, chain-like clusters).
    *   `'complete'`: Looks at the distance between the *two furthest points* in the two clusters. (Tends to create tight, compact clusters).
*   `AgglomerativeClustering(n_clusters=3)`: Tells the algorithm to keep merging clusters up the tree until exactly 3 distinct clusters remain.
""",

    "10_PCA_LDA.md": """
## Deep Dive Code Breakdown

### 10.py: PCA & LDA Variables
*   `PCA(n_components=2)`: The `n_components` parameter forces the algorithm to squish the 4-dimensional Iris data down to exactly 2 dimensions (components) so we can plot it on an X-Y graph.
*   `pca.fit_transform(X)`: A convenience function that does two steps at once. First, it `fit`s (does the heavy math to find the principal components of variance), and then it `transform`s (actually multiplies the data to project it onto the new 2D plane).
*   `lda.fit_transform(X, y)`: Notice LDA requires `y` (the answers/labels) as a parameter, while PCA only requires `X`. This is because PCA is blind (unsupervised), while LDA actively looks at the answers to figure out how to best pull the distinct classes apart (supervised).
""",

    "11_Perceptron.md": """
## Deep Dive Code Breakdown

### 11.py: Perceptron Variables
*   `linear_output = np.dot(X, self.weights) + self.bias`: This is the absolute core math of all Neural Networks.
    *   `np.dot(X, self.weights)`: The dot product. It multiplies every input feature by its assigned importance (weight) and sums them all together.
    *   `self.bias`: A constant number added to shift the result left or right. It's like the y-intercept (`b`) in the line equation `y = mx + b`.
*   `y_pred = np.where(linear_output >= 0, 1, 0)`: The "Step" Activation Function. It acts as the brain's decision gate. `np.where` checks a condition: if the math output is >= 0, the neuron "fires" and predicts a 1. Otherwise, it stays quiet and predicts a 0.
"""
}

for filename, content in breakdowns.items():
    path = os.path.join("explanations", filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            existing_content = f.read()
        if "Deep Dive Code Breakdown" not in existing_content:
            with open(path, "a", encoding="utf-8") as f:
                f.write("\n\n" + content)

print("Code breakdowns added to markdown files successfully.")
