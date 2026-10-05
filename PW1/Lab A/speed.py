import time
import numpy as np
from decay import simulate, simulate_loop

NO = 200000
lam = 0.4
dt = 0.05
steps = 200

def timed(func):
    #Run func once and return (result, elapsed seconds)
    start = time.perf_counter()
    result = func(NO, lam, dt=dt, steps=steps, seed=0)
    elapsed = time.perf_counter() - start
    return result, elapsed
 
 
if __name__ == "__main__":
    print(f"Run: N0 = {NO}, lam = {lam}, dt = {dt}, steps = {steps}\n")
 
    _, t_loop = timed(simulate_loop)
    print(f"Pure-Python loop : {t_loop:.4f} s")
 
    _, t_numpy = timed(simulate)
    print(f"NumPy version    : {t_numpy:.6f} s")
 
    print(f"\nNumPy is about {t_loop / t_numpy:,.0f} times faster.")
 