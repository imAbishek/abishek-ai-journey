import time

import numpy as np

# py_list = list(range(1_000_000))
# np_arr = np.arange(1_000_000)
# # Time the Python way
# start = time.time()
# result_py = [x * 2 for x in py_list]
# end = time.time()
# print(f"Python list: {end - start:.4f} seconds")
#
# # Time the NumPy way
# start = time.time()
# result_np = np_arr * 2
# end = time.time()
# print(f"NumPy array: {end - start:.6f} seconds")


# properties = np.array([
#     [5000000, 2500, 3],
#     [7500000, 3500, 3],
#     [15000000, 5000, 5],
# ])
#
# column_max = np.max(properties, axis=0)
# print("Column Max:" ,column_max)
#
# norm = properties / column_max
# print("Normalized:\n" ,norm)

prices = np.array([5000000, 7500000, 15000000, 3000000, 9000000])
areas = np.array([1200, 1800, 2500, 800, 1500])

affordable = prices[(prices < 8000000) & (areas > 1000)]
print("Affordable:", affordable)
print("Total count:", len(affordable) )