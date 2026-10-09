import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# 1. Read kinetics.csv
t, C_meas = np.loadtxt('kinetics.csv', delimiter=',', skiprows=1, unpack=True)

# 2. Set C0 to the first concentration value
C0 = C_meas[0]

# 3. Write total_error(k) to minimise the squared error
def total_error(k_array):
    k = k_array[0] # minimize passes parameters as an array
    C_model = C0 * np.exp(-k * t)
    return np.sum((C_meas - C_model)**2)

# 4. Minimise the error using SLSQP
result = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = result.x[0]

# 5. Print the fitted k
print(f"Fitted k: {k_fit:.4f}")

# 6. Plot the data with the fitted curve
plt.figure(figsize=(8, 5))
plt.scatter(t, C_meas, label='Measured Data', color='blue', alpha=0.6, s=15)

t_smooth = np.linspace(t.min(), t.max(), 100)
C_fit = C0 * np.exp(-k_fit * t_smooth)
plt.plot(t_smooth, C_fit, label=f'Fitted Curve ($k \\approx {k_fit:.2f}$)', color='red')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('First-Order Reaction Kinetics Curve-Fitting')
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig('kinetics.png')
print("kinetics.png saved successfully.")
