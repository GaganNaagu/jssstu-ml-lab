# Program 13: KNN Manhattan on Fruit Dataset

**Logic / Algorithm:** This is identical to the core concepts of Program 7, but focuses exclusively on the **Manhattan Distance** metric.
Manhattan distance (also known as L1 norm or taxicab geometry) calculates distance by summing the absolute differences of their coordinates. 

**Mathematical formula:** 
$d(p, q) = |p_1 - q_1| + |p_2 - q_2| ...$

**Why use Manhattan instead of Euclidean?** Manhattan distance is less affected by massive outliers. If one feature has an extremely high value, Euclidean distance squares it (making the distance explode), whereas Manhattan distance simply adds it. 

**Real-World Example:** If you are driving a taxi in New York City (Manhattan), you cannot drive straight through buildings. You must drive along the grid-like streets. Your driving distance is the Manhattan distance!
