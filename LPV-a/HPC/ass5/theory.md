# Assignment 5: Parallel K-Means Clustering

Problem:
Implement K-Means clustering for 2D points and parallelize the cluster assignment phase using OpenMP. Measure performance across different thread counts and report centroids/throughput.

Expected Output:
- Final centroid positions after fixed iterations
- Per-thread-count execution time and throughput (points/sec)
- Optional visualization or sample cluster assignments

## Viva QnA
- Explain K-Means algorithm (assignment and update steps).: Repeat assigning each point to nearest centroid, then recompute centroids as cluster means until convergence.
- Why is the assignment step embarrassingly parallel?: Each point's nearest-centroid computation is independent of others.
- How would you parallelize centroid updates (reductions)?: Use per-thread accumulators with `reduction` or atomic adds, or compute local sums then combine.
- What is K-Means++ and why use it?: K-Means++ smartly initializes centroids to improve convergence and final clustering quality.
- How do you choose k and number of iterations?: Use domain knowledge, elbow method, silhouette score; iterations until centroids stabilize or fixed max iterations.
- What are common failure modes (empty clusters, poor initialization)?: Empty clusters happen if no points assigned; reinitialize centroid or remove cluster; poor init can yield bad local minima.