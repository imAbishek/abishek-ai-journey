"""
NumPy Benchmarking: Loops vs Vectorized Operations
===================================================
Comparing Python loops against NumPy vectorized operations
on 1 million elements across three common operations.

Context: PropFind property listing platform — real-world scenarios
where you'd process large datasets of property listings.
"""

import time
import numpy as np

# Generate shared test data — 1 million property listings
np.random.seed(42)  # reproducible results
arr = np.random.randint(1, 100, size=1_000_000)
prices = np.random.randint(500000, 10000000, size=1_000_000)
areas = np.random.randint(500, 5000, size=1_000_000)

results = {}

# ============================================================
# Benchmark 1: Sum of 1 million elements
# Use case: total revenue across all property listings
# ============================================================

# Loop
start = time.time()
memory = 0
for n in arr:
    memory = memory + n
loop_time = time.time() - start

# NumPy
start = time.time()
result = np.sum(arr)
numpy_time = time.time() - start

results["Sum"] = {"loop": loop_time, "numpy": numpy_time}
print(f"--- Benchmark 1: Sum ---")
print(f"Loop:  {loop_time:.6f}s")
print(f"NumPy: {numpy_time:.6f}s")
print(f"Speedup: {loop_time / numpy_time:.0f}x\n")

# ============================================================
# Benchmark 2: Element-wise division (price per sqft)
# Use case: calculating derived metrics for every listing
# ============================================================

# Loop
start = time.time()
price_per_sqft_loop = []
for i in range(len(prices)):
    price_per_sqft_loop.append(prices[i] / areas[i])
loop_time = time.time() - start

# NumPy
start = time.time()
price_per_sqft_np = prices / areas
numpy_time = time.time() - start

results["Division"] = {"loop": loop_time, "numpy": numpy_time}
print(f"--- Benchmark 2: Element-wise Division ---")
print(f"Loop:  {loop_time:.6f}s")
print(f"NumPy: {numpy_time:.6f}s")
print(f"Speedup: {loop_time / numpy_time:.0f}x\n")

# ============================================================
# Benchmark 3: Conditional filtering (properties above threshold)
# Use case: filtering premium listings where price/sqft > 3000
# ============================================================

price_per_sqft = prices / areas

# Loop
start = time.time()
filtered_loop = []
for sqft in price_per_sqft:
    if sqft > 3000:
        filtered_loop.append(sqft)
loop_time = time.time() - start

# NumPy
start = time.time()
filtered_np = price_per_sqft[price_per_sqft > 3000]
numpy_time = time.time() - start

results["Filtering"] = {"loop": loop_time, "numpy": numpy_time}
print(f"--- Benchmark 3: Conditional Filtering ---")
print(f"Loop:  {loop_time:.6f}s")
print(f"NumPy: {numpy_time:.6f}s")
print(f"Speedup: {loop_time / numpy_time:.0f}x\n")

# ============================================================
# Summary
# ============================================================
print("=" * 50)
print(f"{'Operation':<20} {'Loop':>10} {'NumPy':>10} {'Speedup':>10}")
print("-" * 50)
for op, times in results.items():
    speedup = times["loop"] / times["numpy"]
    print(f"{op:<20} {times['loop']:>9.4f}s {times['numpy']:>9.4f}s {speedup:>9.0f}x")
print("=" * 50)
print(f"\nDataset: {len(arr):,} elements")
print("Takeaway: NumPy vectorized operations are 20-150x faster than Python loops.")
print("For data-heavy apps like PropFind, this is the difference between")
print("seconds and milliseconds when processing large listing datasets.")