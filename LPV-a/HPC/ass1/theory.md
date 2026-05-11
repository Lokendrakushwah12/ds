# Assignment 1: Parallel BFS & DFS

Problem:
Implement BFS and DFS graph traversals in both sequential and OpenMP-parallel forms on an undirected graph. Demonstrate correct traversal order and measure performance.

Expected Output:
- Printed adjacency list of the graph
- Traversal order for Sequential BFS and Parallel BFS
- Traversal order for Sequential DFS and Parallel DFS
- Execution times for each run and computed speedup/efficiency

## Viva QnA
- What is the difference between BFS and DFS?: BFS visits nodes level-by-level using a `queue`; DFS visits by going deep first using a `stack` or recursion.
- Why is `queue` used for BFS and `stack` for DFS?: `queue` enforces FIFO (level order); `stack`/recursion enforces LIFO (depth-first order).
- How did you parallelize neighbor exploration with OpenMP?: By parallelizing the neighbor loop (e.g. `#pragma omp parallel for`) and protecting shared updates with critical sections or atomics.
- What race conditions can occur and how are they avoided?: Concurrent writes to `visited` or the queue can race; avoid using `#pragma omp critical`, atomic operations, or thread-local buffers with later merging.
- How do you calculate speedup and efficiency?: Speedup = T_seq / T_par; Efficiency = Speedup / num_threads.
- When would parallel traversal not give speedup?: For small graphs, high synchronization overhead, or highly irregular work distribution (load imbalance).