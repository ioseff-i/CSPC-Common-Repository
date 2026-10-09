import numpy as np
from scipy.optimize import newton, minimize

# ==========================================
# 2A. An easy convex function
# f(x) = (x-3)^2 + 1
# f'(x) = 2(x-3)
# f''(x) = 2
# ==========================================
def f(x): return (x - 3)**2 + 1
def df(x): return 2 * (x - 3)
def d2f(x): return 2

x0_A = 0.0

# 1. Gradient Descent by hand
x_gd = x0_A
for _ in range(100): x_gd -= 0.1 * df(x_gd)

# 2. Newton's Method (finding root of derivative)
x_newton = newton(df, x0_A, fprime=d2f)

# 3. SLSQP
x_slsqp = minimize(f, x0_A, method="SLSQP").x[0]

print("--- 2A: Easy Convex Function f(x) ---")
print(f"Gradient descent : x = {x_gd:.4f}")
print(f"Newton's method  : x = {x_newton:.4f}")
print(f"SLSQP minimizer  : x = {x_slsqp:.4f}\n")

# ==========================================
# 2B. A harder landscape
# g(x) = x^4 - 3x^2 + x + 5
# g'(x) = 4x^3 - 6x + 1
# g''(x) = 12x^2 - 6
# ==========================================
def g(x): return x**4 - 3*x**2 + x + 5
def dg(x): return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

def test_harder_landscape(x0):
    # 1. Gradient Descent (using smaller step size to prevent divergence)
    x_gd = x0
    for _ in range(100): x_gd -= 0.05 * dg(x_gd)
    
    # 2. Newton's Method
    x_newton = newton(dg, x0, fprime=d2g)
    curvature = d2g(x_newton)
    point_type = "minimum" if curvature > 0 else "maximum"
    
    # 3. SLSQP
    x_slsqp = minimize(g, x0, method="SLSQP").x[0]
    
    print(f"--- 2B: Harder Landscape g(x) starting at x0 = {x0} ---")
    print(f"Gradient descent : x = {x_gd:.4f}")
    print(f"Newton's method  : x = {x_newton:.4f} (g'' = {curvature:.2f} -> {point_type})")
    print(f"SLSQP minimizer  : x = {x_slsqp:.4f}\n")

test_harder_landscape(0.0)
test_harder_landscape(2.0)
