# Experiment 6: Gaussian Naive Bayes Classifier

This document covers the theoretical concepts (derived from our from-scratch implementation), the standard `sklearn` code explanation, and viva questions for the sixth lab experiment: `6.py` and `6o.py`.

---

## Theoretical Background (Based on `6o.py`)
Naive Bayes classifiers are a family of simple "probabilistic classifiers" based on applying **Bayes' Theorem** with strong (naive) independence assumptions between the features. 

**Bayes' Theorem:**
`P(A|B) = [P(B|A) * P(A)] / P(B)`
Where:
- `P(A|B)`: Posterior probability (Probability of class A given feature B).
- `P(B|A)`: Likelihood (Probability of feature B given class A).
- `P(A)`: Prior probability (Overall probability of class A).

**Gaussian Naive Bayes** assumes that the continuous values associated with each class are distributed according to a Gaussian (Normal) distribution.

**How it works step-by-step (as seen in `6o.py`):**
1. **Fit (Training phase)**:
   - Calculate the **Prior probability** for each class: `(Count of class elements) / (Total elements)`.
   - Calculate the **Mean** and **Variance** for every single feature, separated by class.
2. **Calculate Likelihood**:
   - To predict the probability of a new data point belonging to a class, plug the new point's feature values into the Gaussian Probability Density Function (PDF):
     `f(x) = (1 / sqrt(2 * pi * variance)) * e^(-((x - mean)^2) / (2 * variance))`
3. **Predict (Testing phase)**:
   - Multiply the Prior probability by the Likelihoods of all features (usually done by summing the *logarithms* to prevent underflow: `log(Prior) + log(Likelihoods)`).
   - The class with the highest resulting posterior probability wins.

---

## Code Walkthrough (`6.py` - Built-in Implementation)
1. **Data Preparation**: 
   - Loads the Titanic dataset from Seaborn.
   - Drops null values and maps the 'sex' categorical column to numerical values (`0` and `1`).
   - Separates the target column (`y = 'survived'`) from the features (`X`).
2. **Train/Test Split & Scaling**:
   - `train_test_split(X, y)` splits the data so the model can be evaluated on unseen data.
   - `StandardScaler()` scales the features to have a mean of 0 and a variance of 1. While Naive Bayes doesn't strictly *require* scaling like KNN does, it can sometimes improve numerical stability.
3. **Model Training**:
   - `model = GaussianNB()` initializes the built-in sklearn classifier.
   - `model.fit(X_train, y_train)` calculates and stores the means, variances, and priors automatically.
4. **Prediction and Evaluation**:
   - `model.predict(X_test)` generates survival predictions.
   - `accuracy_score` and `confusion_matrix` are printed to evaluate performance.

---

## Viva Questions

### Program-Specific Questions
**Q1: Why is it called "Naive"?**
*Answer:* It is called "naive" because it makes the strong, often unrealistic assumption that all features are completely independent of each other given the class. For example, it assumes a passenger's 'age' has absolutely no correlation with their 'fare' regarding their chance of survival.

**Q2: What is the purpose of `titanic.drop('survived', axis=1)`?**
*Answer:* It removes the target column from the feature matrix `X`. The `axis=1` parameter explicitly tells pandas to look for and drop a *column* named 'survived', rather than a row.

**Q3: How does the Gaussian Probability Density Function help in predicting continuous values?**
*Answer:* Instead of counting exact matches (like we do for discrete categorical features), the Gaussian PDF calculates the probability density of a specific continuous value occurring, assuming the data follows a normal bell-curve distribution defined by the training mean and variance.

**Q4: In our theory implementation (`6o.py`), why do we add `1e-9` to the variance?**
*Answer:* We add a very small number (epsilon, `1e-9`) to the variance to prevent "divide by zero" errors during the Likelihood calculation just in case a feature has zero variance (i.e., all values for that feature in a class are identical).

**Q5: Why do we use `np.log` (logarithms) when calculating the final posterior probability?**
*Answer:* Multiplying many very small probabilities (likelihoods) together can cause "numerical underflow" where computers round the result down to exactly zero. By taking the log, we can *add* the values instead of multiplying them, which preserves precision.

### General Theory Questions
**Q6: What is a Confusion Matrix?**
*Answer:* It is a table used to describe the performance of a classification model. It shows True Positives (correctly predicted positive), True Negatives (correctly predicted negative), False Positives (predicted positive but actually negative), and False Negatives (predicted negative but actually positive).

**Q7: Is Naive Bayes a generative or discriminative model?**
*Answer:* It is a **generative** model. It models the joint probability distribution `P(X, Y)` and uses Bayes theorem to calculate `P(Y|X)`, unlike discriminative models (like Logistic Regression) which model `P(Y|X)` directly.

**Q8: What happens if a categorical feature in the test set has a category that was never seen in the training set?**
*Answer:* This causes the "Zero Frequency Problem", resulting in a likelihood of 0, which zeroes out the entire posterior probability. Techniques like Laplace Smoothing (adding a small count to all frequencies) are used to fix this.

**Q9: When should you use Gaussian Naive Bayes over Multinomial Naive Bayes?**
*Answer:* Gaussian Naive Bayes is used when your features are continuous (real numbers like height, weight). Multinomial Naive Bayes is used for discrete counts (like word frequencies in text classification).

**Q10: What are the advantages of Naive Bayes?**
*Answer:* It is very fast, requires relatively little training data, scales well to high-dimensional data, and handles missing values reasonably well. It often serves as a highly effective baseline model.
