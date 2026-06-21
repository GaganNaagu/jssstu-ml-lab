# Program 10: PCA and LDA

**Logic / Algorithm:** Both are Dimensionality Reduction techniques. They take data with 100s of columns (features) and squash it down to 2 or 3 columns so it can be plotted or processed faster.

1. **PCA (Principal Component Analysis):** Unsupervised. It doesn't care about the labels. It rotates the data to find the directions (components) where the data is most spread out (maximum variance).
2. **LDA (Linear Discriminant Analysis):** Supervised. It uses the labels! It tries to find the axis that maximizes the separation *between* different classes while minimizing the spread *within* each class.

**Real-World Example:** Facial Recognition. An image of a face might have 10,000 pixels (10,000 dimensions). PCA reduces this to the 50 most important "Eigenfaces" (features), allowing the computer to process the image in milliseconds instead of seconds.
