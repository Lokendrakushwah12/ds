# Assignment 4: CUDA Programming — Vector Add & Matrix Multiply

Problem:
Implement GPU kernels for vector addition and matrix multiplication using CUDA, demonstrate correct memory transfers and kernel configuration, and validate results against CPU reference.

Expected Output:
- Successful allocation of host (pinned) and device memory
- Kernel launches for vector add and matrix multiply
- Sample printed results (first 10 vector sums / result matrix) and correctness checks
- Notes on block/grid configuration and performance observations

## Viva QnA
- Explain CUDA memory hierarchy (host, device, pinned, pageable).: Host memory is CPU RAM; device memory is GPU global memory; pinned (page-locked) host memory allows faster DMA transfers; pageable is regular host memory that may be paged.
- How are thread and block indices computed for 1D and 2D kernels?: 1D: `i = blockIdx.x * blockDim.x + threadIdx.x`; 2D: `row = blockIdx.y*blockDim.y + threadIdx.y`, `col = blockIdx.x*blockDim.x + threadIdx.x`.
- Why is boundary checking (if index < n) necessary?: Because grid can contain extra threads beyond problem size; checking prevents out-of-bounds memory access.
- What is coalesced memory access and why does it matter?: Coalescing groups adjacent threads accessing adjacent memory for efficient memory transactions, improving throughput.
- How would you optimize matrix multiply (shared memory, tiling)?: Use tiled multiplication with shared memory to reuse elements in blocks, reduce global memory accesses, and increase arithmetic intensity.
- How do you measure kernel vs transfer time?: Use CUDA events (`cudaEventRecord`, `cudaEventElapsedTime`) to time kernel execution and `cudaMemcpy` durations separately.