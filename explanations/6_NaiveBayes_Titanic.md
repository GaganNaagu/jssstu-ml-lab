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
