# Program 7: KNN (Euclidean & Manhattan) on Glass Dataset

**Logic / Algorithm:** K-Nearest Neighbors (KNN) is an instance-based, "lazy learning" algorithm. To classify a new, unknown data point, it looks at the $K$ closest training data points. The new point is assigned to the class that is most common among its $K$ neighbors (like a democratic vote).

**Distance Metrics:**
1. **Euclidean Distance:** The straight-line distance between two points (like a bird flying). Uses the Pythagorean theorem.
2. **Manhattan Distance:** The distance if you could only travel along grid lines (like driving in a city with square blocks). 

**Glass Application:** Predicts the type of glass (window, car headlamp, tableware) based on its chemical elements (Sodium, Magnesium, Iron, etc.). 

**Real-World Example:** Netflix Recommendations. If your watch history is very "close" (in data space) to 5 other users, Netflix looks at what those 5 neighbors watched and recommends it to you.
