# Experiment 10: Dimensionality Reduction (PCA vs LDA)

This document covers the theoretical concepts (derived from our from-scratch implementation), the standard `sklearn` code explanation, and viva questions for the tenth lab experiment: `10.py` and `10o.py`.

---

## Theoretical Background (Based on `10o.py`)
High-dimensional data can be difficult to visualize, compute, and can cause the "curse of dimensionality" in Machine Learning. **Dimensionality Reduction** techniques solve this by projecting data down into fewer dimensions (e.g., from 4D to 2D) while trying to retain as much meaningful information as possible.

### 1. Principal Component Analysis (PCA)
PCA is an **unsupervised** technique. It ignores class labels and focuses purely on finding the directions (Principal Components) where the data has the **maximum variance** (spread).

**How it works (from `pca_scratch`):**
1. **Centering**: Subtract the mean from the dataset so it is centered around zero.
2. **Covariance Matrix**: Calculate the covariance matrix of the centered data to understand how features vary together.
3. **Eigen Decomposition**: Calculate the Eigenvalues and Eigenvectors of the covariance matrix. 
   - *Eigenvectors* represent the directions of the new feature space.
   - *Eigenvalues* represent the magnitude (variance) along those directions.
4. **Projection**: Sort the eigenvectors by their eigenvalues in descending order. Pick the top `K` eigenvectors and multiply the original data by them to get the new, reduced-dimension dataset.

### 2. Linear Discriminant Analysis (LDA)
LDA is a **supervised** technique. It uses the class labels (`y`) to find the directions that **maximize the separation between multiple classes** while minimizing the scatter within each individual class.

**How it works (from `lda_scratch`):**
1. **Scatter Matrices**:
   - Calculate `S_W` (Within-class scatter matrix): How spread out the data is *inside* each individual class.
   - Calculate `S_B` (Between-class scatter matrix): How spread out the class means are from the overall dataset mean.
2. **Eigen Decomposition**: Solve the generalized eigenvalue problem for the matrix `(S_W^-1 * S_B)`. 
3. **Projection**: Similar to PCA, pick the top `K` eigenvectors that correspond to the largest eigenvalues and project the data onto them.

---

## Code Walkthrough (`10.py` - Built-in Implementation)
1. **Data Loading & Scaling**:
   - The Iris dataset (4 features) is loaded.
   - `StandardScaler()` is applied. Scaling is critical for PCA because it is sensitive to the variance of initial variables. If one variable has a much larger scale, PCA will mistakenly prioritize it.
2. **Applying PCA**:
   - `pca = PCA(n_components=2)`: Initializes PCA to reduce the 4D data down to 2 dimensions.
   - `X_pca = pca.fit_transform(X_scaled)`: Fits the model and transforms the data simultaneously. Note that it does **not** take the target `y` as an argument because PCA is unsupervised.
3. **Applying LDA**:
   - `lda = LDA(n_components=2)`: Initializes LDA.
   - `X_lda = lda.fit_transform(X_scaled, y)`: Fits and transforms the data. Note that it **does** require the target `y` as an argument because LDA needs to know the class labels to maximize class separation.
4. **Visualization**:
   - The original 4D data is transformed into two different 2D datasets (`X_pca` and `X_lda`), which are then plotted side-by-side using `plt.scatter`.

---

## Viva Questions

### Program-Specific Questions
**Q1: What is the shape of the Iris dataset before and after PCA/LDA?**
*Answer:* Before PCA/LDA, the shape is `(150, 4)` because there are 150 samples and 4 features. After running `fit_transform` with `n_components=2`, the shape becomes `(150, 2)`.

**Q2: In `10.py`, why do we pass `y` to `lda.fit_transform` but not to `pca.fit_transform`?**
*Answer:* LDA is a supervised algorithm, meaning it requires the target class labels (`y`) to calculate the between-class and within-class scatter matrices. PCA is unsupervised and only cares about the variance of the features (`X`), ignoring the labels completely.

**Q3: What does `np.linalg.eigh(cov_matrix)` do in the from-scratch PCA implementation?**
*Answer:* It calculates the eigenvalues and eigenvectors of the given covariance matrix. `eigh` is specifically optimized for symmetric matrices (like a covariance matrix) and returns real-valued results.

**Q4: Look at the visual output of the program. Which plot usually shows better separation of the colors (classes)?**
*Answer:* The LDA plot almost always shows better separation of the colored classes. This is because LDA was explicitly designed to separate classes, while PCA was only designed to find the axes of maximum overall variance, which doesn't guarantee the classes won't overlap.

**Q5: Why is `StandardScaler` used before PCA?**
*Answer:* PCA seeks to maximize variance. If a feature is measured in thousands and another in decimals, the feature in thousands will have a massive variance simply due to its scale, and PCA will inappropriately skew the principal components towards it.

### General Theory Questions
**Q6: What is the "Curse of Dimensionality"?**
*Answer:* As the number of features (dimensions) in a dataset increases, the amount of data required to make statistically reliable models grows exponentially. High dimensions make distance calculations less meaningful and increase the risk of overfitting.

**Q7: Explain what a Principal Component is.**
*Answer:* A Principal Component is a new, artificially constructed variable (a linear combination of the original variables) that points in the direction of the highest variance in the data. They are orthogonal (perpendicular) to each other.

**Q8: What is the maximum number of components you can choose in LDA?**
*Answer:* The maximum number of components in LDA is `C - 1`, where `C` is the total number of classes. For the Iris dataset (3 classes), the maximum number of LDA components you can extract is 2.

**Q9: Can PCA be used for feature selection?**
*Answer:* No. PCA is used for **feature extraction**, not feature selection. Feature selection picks the best original features and drops the rest. PCA creates entirely *new* features that are mathematical mashups of the original features, making them hard to interpret.

**Q10: When should you prefer PCA over LDA?**
*Answer:* You should prefer PCA when you have an unlabeled dataset (unsupervised learning), or when your goal is purely image compression, noise reduction, or visualizing the overall structure of the data rather than classifying it.
