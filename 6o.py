import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split

class GaussianNaiveBayesScratch:
    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        self.classes = np.unique(y)
        self.means = {}
        self.vars = {}
        self.priors = {}

        for c in self.classes:
            X_c = X[y == c]
            self.means[c] = np.mean(X_c, axis=0)
            self.vars[c] = np.var(X_c, axis=0) + 1e-9
            self.priors[c] = X_c.shape[0] / X.shape[0]

    def _calculate_likelihood(self, class_val, x):
        mean = self.means[class_val]
        var = self.vars[class_val]
        numerator = np.exp(-((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator

    def predict(self, X):
        X = np.array(X)
        y_pred = [self._predict_one(x) for x in X]
        return np.array(y_pred)

    def _predict_one(self, x):
        posteriors = []
        for c in self.classes:
            prior = np.log(self.priors[c])
            conditional = np.sum(np.log(self._calculate_likelihood(c, x)))
            posterior = prior + conditional
            posteriors.append((posterior, c))
        return max(posteriors, key=lambda item: item[0])[1]

def confusion_matrix_scratch(y_true, y_pred):
    classes = np.unique(np.concatenate([y_true, y_pred]))
    cm = np.zeros((len(classes), len(classes)), dtype=int)
    for i, c_true in enumerate(classes):
        for j, c_pred in enumerate(classes):
            cm[i, j] = np.sum((y_true == c_true) & (y_pred == c_pred))
    return cm

def accuracy_score_scratch(y_true, y_pred):
    return np.mean(y_true == y_pred)

titanic = sns.load_dataset('titanic')[['survived', 'pclass', 'sex', 'age', 'fare']].dropna()
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})

X = titanic.drop('survived', axis=1)
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = GaussianNaiveBayesScratch()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Gaussian Naive Bayes (From Scratch)")
print("Accuracy:", accuracy_score_scratch(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix_scratch(y_test, y_pred))
