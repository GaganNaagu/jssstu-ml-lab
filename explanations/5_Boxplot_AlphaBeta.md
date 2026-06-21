# Program 5: Box-plots & Alpha-Beta Pruning

## 5(a): Box-plot (Whisker Plot)
**What it does:** Displays the distribution of data based on a five-number summary: minimum, first quartile (Q1), median, third quartile (Q3), and maximum.
**What to look for:** **Outliers!** Dots that fall outside the "whiskers" are anomalies. Also, look at the median line inside the box to see where the "average" data sits.
**Real-World Example:** Analyzing the salaries of a company. The box shows where 50% of the employees sit, while the outliers instantly highlight the CEO's massive salary.

## 5(b): Alpha-Beta Pruning
**Logic / Algorithm:** An optimization technique for the Min-Max algorithm. It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. 
- **Alpha:** Best already explored option for Maximizer.
- **Beta:** Best already explored option for Minimizer.
**Real-World Example:** IBM's Deep Blue chess computer. By ignoring branch moves that are obviously terrible (pruning), the computer can look 10 moves ahead instead of just 5 in the same amount of time.
