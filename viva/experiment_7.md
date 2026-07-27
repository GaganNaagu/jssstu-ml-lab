# Experiment 7: K-Nearest Neighbors (KNN)

This document covers the theoretical concepts (derived from our from-scratch implementation), the standard `sklearn` code explanation, and viva questions for the seventh lab experiment: `7.py` and `7o.py`.

---

## Theoretical Background (Based on `7o.py`)
K-Nearest Neighbors (KNN) is a simple, non-parametric, **lazy learning** algorithm used for classification and regression. 

It is called "lazy" because it does not actually "train" or build a model during the fitting phase. It simply memorizes the training dataset. All the heavy computational work is delayed until a prediction is requested.

**How it works step-by-step (as seen in `7o.py`):**
1. **Fit (Training phase)**:
   - Simply store `X_train` and `y_train` in memory.
2. **Predict (Testing phase)**: For a given unknown data point:
   - **Calculate Distances**: Compute the mathematical distance between the unknown point and *every single point* in the memorized training set.
   - **Find Nearest**: Sort the distances in ascending order and pick the top `K` training data points (the nearest neighbors).
   - **Majority Vote**: Look at the class labels of those `K` neighbors. The class that appears most frequently (the mode) is chosen as the final prediction for the unknown point.

**Distance Metrics used in the code:**
- **Euclidean Distance**: Straight-line distance. `sqrt(sum((x - y)^2))`
- **Manhattan Distance**: City-block distance (sum of absolute differences). `sum(|x - y|)`

---

## Code Walkthrough (`7.py` - Built-in Implementation)
1. **Data Loading**: 
   - `glass.csv` is read using pandas. The features are everything except the first (ID) and last (Class) columns: `X = glass_data.iloc[:, 1:-1]`. The target is the last column: `y = glass_data.iloc[:, -1]`.
2. **Scaling (Crucial for KNN)**:
   - `StandardScaler()` is applied. Because KNN relies entirely on distance calculations, features with large scales (like weight in thousands) will completely overpower features with small scales (like height in decimals). Scaling forces all features to contribute equally.
3. **Custom Distance Functions**:
   - The code defines two custom functions: `custom_euclidean` and `custom_manhattan`. `sklearn`'s KNN allows passing custom callable functions via the `metric` parameter.
4. **Model Training & Prediction**:
   - `knn = KNeighborsClassifier(n_neighbors=3, metric=metric_type)` initializes the model with `K=3` and the custom distance function.
   - It prints the accuracy using both Euclidean and Manhattan metrics to compare performance.

---

## Viva Questions

### Program-Specific Questions
**Q1: What does `iloc[:, 1:-1]` do?**
*Answer:* In pandas, `iloc` is integer-location based indexing. `:` means "select all rows". `1:-1` means "select columns starting from index 1 up to, but not including, the last column". This strips away the ID column (index 0) and the Target column (index -1) to give pure features.

**Q2: Why is `StandardScaler` absolutely required for KNN?**
*Answer:* KNN calculates distances between points. If one feature ranges from 1 to 1000 and another ranges from 0.1 to 0.9, the larger feature will dominate the distance calculation. Standard scaling ensures all features have a mean of 0 and standard deviation of 1, giving them equal weight.

**Q3: How does the algorithm choose the winner among the K neighbors?**
*Answer:* It uses a majority voting system. Whichever class label is most frequent among the K nearest neighbors becomes the prediction. In python, this is often implemented using `collections.Counter().most_common(1)`.

**Q4: In the from-scratch implementation (`7o.py`), what does `np.argsort(distances)[:self.k]` do?**
*Answer:* `np.argsort` returns the *indices* that would sort the array in ascending order. Slicing it with `[:self.k]` grabs the indices of the `K` smallest distances, pointing exactly to the nearest neighbors in the training array.

**Q5: What happens if there is a tie in the majority vote (e.g., K=4, two vote class A, two vote class B)?**
*Answer:* In standard implementations like `sklearn`, a tie is usually broken arbitrarily (e.g., picking the first class encountered). This is why it is highly recommended to choose an **odd number** for K in binary classification to prevent ties.

### General Theory Questions
**Q6: What is a "non-parametric" algorithm?**
*Answer:* A non-parametric algorithm does not make strong assumptions about the underlying mapping function or data distribution. It does not try to fit data into a fixed number of parameters (like a linear regression equation). KNN is non-parametric.

**Q7: Why is KNN called a "lazy learner"?**
*Answer:* Because it does practically no work during the training phase—it just stores the data. All the heavy computation (calculating distances to every point) is deferred until it actually needs to make a prediction.

**Q8: How does the value of K affect the model?**
*Answer:* A very small K (e.g., K=1) makes the model highly sensitive to noise, leading to **overfitting**. A very large K smooths out boundaries but might include points from other classes, leading to **underfitting**.

**Q9: What is the "Curse of Dimensionality" in the context of KNN?**
*Answer:* As the number of features (dimensions) increases, the volume of the space increases exponentially. In high dimensions, all points become almost equidistant from each other, making the concept of "nearest neighbor" meaningless and causing KNN to perform poorly.

**Q10: When would you prefer Manhattan distance over Euclidean distance?**
*Answer:* Manhattan distance is often preferred for high-dimensional data (as it is less affected by the curse of dimensionality) or when the data features are discrete or grid-like rather than continuous.
