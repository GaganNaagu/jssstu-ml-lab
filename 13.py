import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

"""
GUIDE: Using Your Own Dataset
-----------------------------
If you are using a custom dataset file:
1. File Format: Text or CSV files may use different separators (e.g., commas vs tabs). 
   Use `pd.read_csv()` for commas and `pd.read_table()` for tabs.
2. Column Names: Be aware of your dataset's columns. If it doesn't have a header, 
   pass `header=None` and provide a `names` list.
3. Feature & Target Splitting: Modify the slicing below to select the appropriate 
   features (X) and target class (y).

Example:
    If your dataset is 'my_data.csv' with headers: Weight, Height, Age, Class
    You would change the loading code to:
    
    my_data = pd.read_csv('my_data.csv')      # Use read_csv for comma separated
    X = my_data[['Weight', 'Height', 'Age']]  # Select Feature columns
    y = my_data['Class']                      # Select Target column
"""

try:
    fruit_data = pd.read_table('fruit_data_with_colors.txt')
    X = fruit_data[['mass', 'width', 'height', 'color_score']]
    y = fruit_data['fruit_name']
except FileNotFoundError:
    print("Error: 'fruit_data_with_colors.txt' not found.")
    sys.exit(1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5, metric='manhattan')
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

