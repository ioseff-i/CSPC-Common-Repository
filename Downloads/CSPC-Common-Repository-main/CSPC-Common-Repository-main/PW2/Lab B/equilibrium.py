import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

# Deduced K value based on the target x ~ 0.66
K = 16

# 1. Define the imbalance function (zero at equilibrium)
def k_imbalance(x):
    return ((2 * x)**2) / ((1 - x)**2) - K

# 2. Solve Method 1: Root-finding with Newton's method
# Starting guess x0 = 0.5 (must be between 0 and 1)
x_newton = newton(k_imbalance, 0.5)

# 3. Solve Method 2: Minimizing the squared imbalance with SLSQP
def objective(x_array):
    x = x_array[0]
    return k_imbalance(x)**2

result = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0, 0.99)])
x_slsqp = result.x[0]

# 4. Confirm both give the same x
print("--- Chemical Equilibrium ---")
print(f"Newton's method x : {x_newton:.4f}")
print(f"SLSQP minimizer x : {x_slsqp:.4f}")

# 5. Report the equilibrium amounts
x_eq = x_newton
n_H2 = 1 - x_eq
n_I2 = 1 - x_eq
n_HI = 2 * x_eq

print(f"\nEquilibrium Amounts:")
print(f"H2: {n_H2:.4f} mol")
print(f"I2: {n_I2:.4f} mol")
print(f"HI: {n_HI:.4f} mol")

# 6. Plot how H2, I2, and HI change with x
x_vals = np.linspace(0, 0.9, 100)
H2_vals = 1 - x_vals
HI_vals = 2 * x_vals

plt.figure(figsize=(8, 5))
# Reactants fall
plt.plot(x_vals, H2_vals, label='H2 & I2 (Reactants)', color='blue')
# Product rises
plt.plot(x_vals, HI_vals, label='HI (Product)', color='red')

# Mark the equilibrium point
plt.axvline(x_eq, color='gray', linestyle='--', label=f'Equilibrium (x $\\approx$ {x_eq:.2f})')
plt.scatter([x_eq, x_eq], [n_H2, n_HI], color='black', zorder=5)

plt.xlabel('Extent of reaction (x)')
plt.ylabel('Amount (mol)')
plt.title(r'Chemical Equilibrium: $H_2 + I_2 \rightleftharpoons 2HI$')
plt.legend()
plt.grid(True)

plt.savefig('equilibrium.png')
print("\nequilibrium.png saved successfully.")
