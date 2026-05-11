# LPV-c HPC: Assignment Theory Overview

This folder contains the HPC assignment implementations (ass1..ass5). For each assignment, the theory is analogous to LPV-a HPC assignments:

- ass1: Parallel BFS & DFS — traversal orders, timings, speedup.
- ass2: Parallel Sorting — odd-even bubble and task-based merge sort, correctness and performance.
- ass3: Parallel Reduction — sum/min/max/avg with OpenMP reduction.
- ass4: CUDA Vector Add & Matrix Multiply — kernels, memory transfers, grid/block configuration.
- ass5: Parallel K-Means — assignment/update phases and thread-scaling measurements.

Expected outputs follow the same patterns as LPV-a HPC assignments (see LPV-a theory files for details).

## Viva QnA (summary)
- Parallel BFS/DFS: protect shared state (`visited`, frontier) or use thread-local queues and merge; speedup depends on graph size and synchronization costs.
- Parallel Sorting: odd-even parallelizes non-overlapping swaps; merge sort uses tasks and thresholding to balance overhead.
- Parallel Reduction: use OpenMP `reduction` to avoid critical sections; floating-point sums are not strictly associative.
- CUDA: kernels use `(blockIdx, threadIdx)` to compute global indices; use pinned memory for faster host↔device transfers and shared memory for tiling.
- K-Means: assignment is parallelizable per point; centroid updates require reduction or accumulation and careful handling of empty clusters.