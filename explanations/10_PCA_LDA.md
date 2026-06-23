# Program 10: PCA and LDA

### 1. Conceptual Overview
Both PCA and LDA are **Dimensionality Reduction** algorithms. 
In the real world, datasets often have hundreds or thousands of columns (features or "dimensions"). This causes the **"Curse of Dimensionality"**—algorithms become painfully slow, overfit easily, and human beings cannot visualize anything beyond 3 dimensions. Dimensionality reduction squashes thousands of columns down to just 2 or 3 columns, saving the most important mathematical information while deleting the noise.

---

### 2. PCA (Principal Component Analysis)
*   **Type:** Unsupervised (It completely ignores the class labels/answers).
*   **Goal:** To find the directions (axes) where the data is most spread out (maximum variance).
*   **Logic:** Imagine shining a flashlight on a 3D cloud of data to project a 2D shadow on a wall. PCA calculates the absolute best angle to hold that flashlight so the 2D shadow captures the maximum possible spread of the data, ensuring no dots overlap unnecessarily. It creates new mathematical features called "Principal Components".
*   **Real-World Application:** **Image Compression.** A massive 4K image might have millions of pixels. PCA can reduce this to the top 100 "Principal Components" that capture 99% of the visual information, compressing the file size drastically without visibly ruining the image.

---

### 3. LDA (Linear Discriminant Analysis)
*   **Type:** Supervised (It relies entirely on knowing the class labels/answers).
*   **Goal:** To find the directions (axes) that maximize the separation *between* different classes, while simultaneously minimizing the spread *within* each class.
*   **Logic:** LDA doesn't just want the data to be spread out (like PCA). It actively wants all the "Class 1" dots to clump tightly together on the left, and all the "Class 2" dots to clump tightly together on the right. 
*   **Real-World Application:** **Facial Recognition (Fisherfaces).** The system knows which photos belong to "Person A" and which belong to "Person B" (supervised). LDA squashes the thousands of pixels down to a few components that specifically highlight the mathematical differences between Person A's face and Person B's face.

### 4. Key Exam Difference
If an examiner asks for the main difference: **PCA is unsupervised and maximizes overall data variance. LDA is supervised and maximizes class separation.**



## Execution Output & Interpretations

### 10.py: PCA & LDA Dimensionality Reduction
**Graph:**
![10.py](../outputs/10.png)

**How to understand these graphs:**
* **What it shows:** Both PCA and LDA are trying to squash a multi-dimensional dataset down to just 2 dimensions so we can visualize it on a flat screen.
* **PCA (Principal Component Analysis):** This is *unsupervised*. It doesn't care about the class labels; it simply looks for the angles where the data is spread out the most (maximum variance).
* **LDA (Linear Discriminant Analysis):** This is *supervised*. It actively uses the class labels and tries to find the angles that maximize the distance *between* different classes while minimizing the spread *within* each class.
* **Interpretation:** Look at the separation of colors. Usually, LDA (the right plot) will show much clearer boundaries between classes because it explicitly tries to separate them, whereas PCA (the left plot) just looks for raw data spread.



## Deep Dive Code Breakdown

### 10.py: PCA & LDA Variables
*   `PCA(n_components=2)`: The `n_components` parameter forces the algorithm to squish the 4-dimensional Iris data down to exactly 2 dimensions (components) so we can plot it on an X-Y graph.
*   `pca.fit_transform(X)`: A convenience function that does two steps at once. First, it `fit`s (does the heavy math to find the principal components of variance), and then it `transform`s (actually multiplies the data to project it onto the new 2D plane).
*   `lda.fit_transform(X, y)`: Notice LDA requires `y` (the answers/labels) as a parameter, while PCA only requires `X`. This is because PCA is blind (unsupervised), while LDA actively looks at the answers to figure out how to best pull the distinct classes apart (supervised).
