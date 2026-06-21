# Program 6: Naive Bayes on Titanic Dataset

**Logic / Algorithm:** Naive Bayes is a probabilistic classification algorithm based on Bayes' Theorem. It calculates the probability of an event occurring based on prior knowledge of conditions related to the event.
- It is called **"Naive"** because it assumes that all input features are completely independent of each other (which is rarely true in real life, but the math still works surprisingly well).

**Titanic Application:** We use passenger data (Age, Fare, Gender, Class) to predict whether they Survived (1) or Died (0). The model calculates probabilities: e.g., "Given this person is Female and First Class, what is the probability they survived?"

**Real-World Example:** Email Spam Filters! The filter looks at words like "Lottery", "Viagra", and "Prince". It calculates: *Given these words are in the email, what is the probability this email is Spam?*

**Exam Tip:** Naive Bayes is incredibly fast and works exceptionally well on text classification and natural language processing (NLP).
