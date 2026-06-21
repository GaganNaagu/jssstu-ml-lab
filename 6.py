import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns

# Load Titanic dataset from seaborn
try:
    titanic = sns.load_dataset('titanic')
except Exception as e:
    print("Error loading dataset:", e)
    sys.exit(1)
    
# Preprocessing
titanic = titanic[['survived', 'pclass', 'sex', 'age', 'fare']].dropna()
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})

X = titanic.drop('survived', axis=1)
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

