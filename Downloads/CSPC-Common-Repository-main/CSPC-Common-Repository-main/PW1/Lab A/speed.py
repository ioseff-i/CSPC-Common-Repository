import time
import decay

N = 200000
rate = 0.4

t0 = time.perf_counter()
decay.simulate_loop(N, rate)
t_loop = time.perf_counter() - t0

t1 = time.perf_counter()
decay.simulate(N, rate)
t_numpy = time.perf_counter() - t1

speedup = t_loop / t_numpy if t_numpy > 0 else 1.0

print(f"Loop execution time: {t_loop:.6f} seconds")
print(f"NumPy execution time: {t_numpy:.6f} seconds")
print(f"NumPy is {speedup:.2f}x faster than loop")
