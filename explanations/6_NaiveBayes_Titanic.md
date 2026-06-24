# Program 6: Naive Bayes on Titanic Dataset

### 1. Conceptual Overview
**Naive Bayes** is a probabilistic machine learning classifier based entirely on **Bayes' Theorem**. It calculates the probability of an event occurring based on prior knowledge of conditions related to the event.

It is called **"Naive"** because it makes a massive, mathematically bold assumption: **It assumes that every single input feature is completely independent of the others.** In real life, features are almost always connected, but the algorithm stubbornly ignores this and multiplies the probabilities together anyway. Surprisingly, this "naive" assumption works incredibly well in practice.

### 2. Bayes' Theorem Formula
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$
*   $P(A|B)$: The probability of class A given the features B (Posterior probability).
*   $P(B|A)$: The probability of features B given class A (Likelihood).
*   $P(A)$: The initial probability of class A occurring (Prior probability).

### 3. Application to the Titanic Dataset
In this program, we are trying to predict if a passenger **Survived (1) or Died (0)** based on their features (Age, Ticket Fare, Gender, Class).

The algorithm calculates:
*   What is the prior probability of surviving overall? (e.g., 38%)
*   Given that a person survived, what is the likelihood they were Female? First Class?
*   It combines these probabilities to answer: *"Given a brand new passenger who is a Female in First Class, what is her calculated mathematical probability of survival?"* Whichever class (Survive or Die) has the higher percentage wins.

### 4. Key Concepts to Mention in Exams
*   **Zero Frequency Problem (Laplace Smoothing):** If the model encounters a feature value it has never seen before (e.g., a 100-year-old person), it assigns a probability of 0%. Because Naive Bayes multiplies everything together, multiplying by 0 breaks the whole equation. To fix this, we use "Laplace Smoothing" (adding a tiny baseline value to everything so nothing is ever exactly zero).
*   **Speed:** It is exceptionally fast to train because it just requires counting frequencies, not complex iterative calculus.

### 5. Real-World Application
*   **Email Spam Filters:** The most famous use case! The filter looks at words like "Lottery", "Viagra", and "Prince". It assumes the presence of each word is independent and calculates: *Given these specific words are in the email, what is the probability this email is Spam?*
*   **Sentiment Analysis:** Reading a Twitter post and instantly classifying if the customer is "Happy" or "Angry" based on the probability of the words used.



## Execution Output & Interpretations

### 6.py: Naive Bayes
**Output:**
```text
Accuracy: 0.7541899441340782
Confusion Matrix:
 [[83 23]
 [21 52]]
```

**How to understand this output:**
* **Accuracy (0.767 or ~77%):** The model correctly predicted the survival outcome 77% of the time.
* **Precision:** When the model predicted someone survived (1), it was right 72% of the time.
* **Recall:** Out of all the people who *actually* survived, the model successfully identified 71% of them.
* **F1-Score:** This is a combination (harmonic mean) of Precision and Recall. It gives a balanced view of the model's performance, especially if classes are imbalanced.



## Deep Dive Code Breakdown

### 6.py: Naive Bayes Variables
*   `GaussianNB()`: The exact type of Naive Bayes model being used. "Gaussian" means it mathematically assumes that the continuous features (like Age or Fare) follow a normal, bell-curve distribution.
*   `train_test_split(X, y, test_size=0.3, random_state=42)`: 
    *   `test_size=0.3`: Tells the function to hide 30% of the dataset to be used later as a final exam for the model. The model is trained on the remaining 70%.
    *   `random_state=42`: Seeds the random number generator. The data is shuffled randomly before splitting, but using a seed ensures it shuffles the *exact same way* every time you run the code. (42 is just a classic programmer's joke number).
