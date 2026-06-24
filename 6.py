import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load and prep data
titanic = sns.load_dataset('titanic')[['survived', 'pclass', 'sex', 'age', 'fare']].dropna()
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})

X = titanic.drop('survived', axis=1)
y = titanic['survived']

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Train Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# 4. Predict & Evaluate
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))