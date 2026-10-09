import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# Read data
t, y = np.loadtxt('freefall.csv', delimiter=',', skiprows=1, unpack=True)

# Compute derivatives
velocity = np.gradient(y, t)
acceleration = np.gradient(velocity, t)

# Print stats
print(f"Mean acceleration: {np.mean(acceleration):.2f} m/s^2")
print(f"Standard deviation: {np.std(acceleration):.2f} m/s^2")

# Integrate back
rec_vel = cumulative_trapezoid(acceleration, t, initial=0) + velocity[0]
rec_pos = cumulative_trapezoid(rec_vel, t, initial=0) + y[0]
print(f"Largest diff in recovered pos: {np.max(np.abs(rec_pos - y)):.4f} m")

# Part 5: Plotting three stacked panels
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

# Position Panel
ax1.plot(t, y, color='blue')
ax1.set_ylabel('Position (m)')
ax1.set_title('Position, Velocity, and Acceleration over Time')
ax1.grid(True)

# Velocity Panel
ax2.plot(t, velocity, color='orange')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)

# Acceleration Panel with dashed line
ax3.plot(t, acceleration, color='gray', alpha=0.7, label='Calculated')
ax3.axhline(-9.81, color='red', linestyle='--', label='-9.81 m/s^2')
ax3.set_ylabel('Acceleration (m/s^2)')
ax3.set_xlabel('Time (s)')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig('motion.png')
print("motion.png saved successfully.")
