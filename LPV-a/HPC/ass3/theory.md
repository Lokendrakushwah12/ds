# Assignment 3: Parallel Reduction (Sum, Min, Max, Avg)

Problem:
Implement reduction operations (sum, min, max, average) both sequentially and using OpenMP reduction clauses, and compare performance on large arrays.

Expected Output:
- Correct results for sum, min, max and average (compared to sequential baseline)
- Timings for sequential vs parallel implementations
- Speedup and efficiency numbers and throughput

## Viva QnA
- What is an OpenMP reduction and how does it work?: Reduction creates private copies of a variable for each thread and combines them using the specified operator at the end of the parallel region.
- Why is reduction preferred over manual critical sections?: Reductions avoid high contention and critical-section bottlenecks and are implemented efficiently by the runtime.
- Give examples of reduction operators supported by OpenMP.: `+`, `-`, `*`, `min`, `max`, `&`, `|`, `^`, `&&`, `||`.
- How does thread count affect reduction performance?: More threads can reduce wall-clock time up to a point; overhead and memory bandwidth limit scaling.
- What numerical issues might affect parallel sum (floating point)?: Non-associativity causes different rounding/order-dependent results; use Kahan summation or higher precision to reduce error.
- How would you implement min/max reduction manually?: Use thread-local min/max then combine in a synchronized step (critical or atomic compare) or use a tree-based reduction.