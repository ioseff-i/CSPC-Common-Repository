"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png

import numpy as np

# Load data using NumPy (skipping the header row)
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

# Compute derivatives
v = np.gradient(y, t)
a = np.gradient(v, t)

# Print mean acceleration
print(f"Mean acceleration: {np.mean(a):.2f} m/s^2")




import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# --- Part 2: Load Data & Compute Derivatives ---
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {a.mean():.2f} m/s^2")

# --- Part 3: Noise Analysis ---
a_std = a.std()
print(f"Acceleration standard deviation: {a_std:.2f} m/s^2")

# --- Part 4: Integrating Back ---
# Integrate acceleration to recover velocity, adding initial velocity v[0]
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]

# Integrate velocity to recover position, adding initial position y[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

# Calculate and print the maximum difference between original and recovered position
max_diff = np.max(np.abs(y - y_rec))
print(f"Max difference in position: {max_diff:.4f} m")

# --- Part 5: Plotting ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Panel 1: Position
ax1.plot(t, y, label='Original Position', color='blue')
ax1.set_ylabel('Position (m)')
ax1.set_title('Motion Analysis')
ax1.grid(True)

# Panel 2: Velocity
ax2.plot(t, v, label='Velocity', color='orange')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)

# Panel 3: Acceleration
ax3.plot(t, a, label='Computed Acceleration', color='red')
ax3.axhline(-9.81, color='black', linestyle='--', label='Theoretical (-9.81 m/s²)')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig('motion.png')
plt.show()
