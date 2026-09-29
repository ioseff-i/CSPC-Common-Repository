import time
import decay

N0 = 200000
rate = 0.4

# 1. Pure-Python simulate_loop icra müddəti
t0 = time.perf_counter()
decay.simulate_loop(N0, rate)
t1 = time.perf_counter()
loop_time = t1 - t0

# 2. NumPy simulate icra müddəti
t2 = time.perf_counter()
decay.simulate(N0, rate)
t3 = time.perf_counter()
numpy_time = t3 - t2

# 3. Sürətlənmə nisbəti (Speed-up factor)
speedup = loop_time / numpy_time

print(f"Pure-Python loop time: {loop_time:.4f} seconds")
print(f"NumPy simulate time:    {numpy_time:.4f} seconds")
print(f"NumPy is {speedup:.2f}x faster than pure-Python loop.")
