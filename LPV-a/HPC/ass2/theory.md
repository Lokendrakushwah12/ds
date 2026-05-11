# Assignment 2: Parallel Sorting (Bubble / Merge)

Problem:
Implement Bubble Sort (odd-even variant) and Merge Sort in sequential and parallel versions using OpenMP. Compare correctness and performance across algorithms.

Expected Output:
- Confirmation that arrays are sorted (isSorted checks)
- Execution times for sequential and parallel Bubble Sort
- Execution times for sequential and parallel Merge Sort
- Speedup, efficiency, and throughput measurements

## Viva QnA
- Explain odd-even (parallel) bubble sort and why pairs are independent.: Odd-even alternates comparing non-overlapping pairs (even indices then odd indices), so comparisons in each phase are independent and can be run in parallel.
- Why is merge sort better asymptotically than bubble sort?: Merge sort is O(n log n) due to divide-and-conquer; bubble sort is O(n²) from repeated adjacent swaps.
- How are OpenMP tasks used for parallel merge sort?: Create tasks for recursive halves (`#pragma omp task`) and `#pragma omp taskwait` before merging.
- When do you switch from parallel to sequential recursion (threshold)?: Use a size threshold (e.g., <1000) to avoid task overhead for small subarrays.
- How do you verify sort correctness efficiently?: Use a linear `isSorted` check or compare to std::sort result.
- What are practical limits of parallelizing sorting?: Memory contention, unstable hardware threads, and communication/merge overhead for very large thread counts.