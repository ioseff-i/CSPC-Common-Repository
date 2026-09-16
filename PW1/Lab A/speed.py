"""
Speed comparison between pure Python loop and NumPy vectorized simulation.
Part 6.2
"""

import time
import numpy as np
from decay import simulate, simulate_loop


def measure_speed():
    N0 = 1_000_000  # Большое количество атомов для наглядности
    r = 0.01
    
    print(f"--- Starting performance test (N0 = {N0:,}) ---")
    
    # 1. Измерение скорости чистого Python (циклы)
    start_time = time.perf_counter()
    res_loop = simulate_loop(N0, r)
    loop_time = time.perf_counter() - start_time
    print(f"Pure Python loop execution time: {loop_time:.4f} seconds")
    
    # 2. Измерение скорости NumPy (векторизация)
    start_time = time.perf_counter()
    res_numpy = simulate(N0, r)
    numpy_time = time.perf_counter() - start_time
    print(f"NumPy vectorized execution time:  {numpy_time:.4f} seconds")
    
    # 3. Вычисление ускорения
    speedup = loop_time / numpy_time if numpy_time > 0 else 0
    print(f"\nSpeedup: NumPy is {speedup:.2f}x faster than pure Python!")


if __name__ == "__main__":
    measure_speed()
