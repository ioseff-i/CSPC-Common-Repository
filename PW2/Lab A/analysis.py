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
t, y = np.loadtxt(r"/home/aydan/Desktop/CSPC/PW2/Lab A/freefall.csv", delimiter=',', skiprows=1, unpack=True)
# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)
print(f'Mean acceleration: {np.mean(a):.2f} m/s^2')
deviation = a.std()
print(f'Standard deviation of acceleration: {deviation:.2f} m/s^2')
#The acceleration is -8.58 m/ s^2, standard deviation is 28.72 m/s^2. For v, we get the first derivative of y, but for a, we get the second derivative of y. That is why the acceleration is more noisy than the velocity. 
# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
recovered_v = cumulative_trapezoid(a, t, initial = 0) + v[0]
recovered_y = cumulative_trapezoid(recovered_v, t, initial = 0) + y[0]
# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.plot(t, y, label='Position')
plt.ylabel('Position (m)')
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(t, v, label='Velocity')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.subplot(3, 1, 3)
plt.plot(t, a, label='Acceleration')
plt.axhline(y=-9.81, color='r', linestyle='--', label='True Acceleration')
plt.ylabel('Acceleration (m/s^2)')
plt.xlabel('Time (s)')
plt.legend()
plt.savefig('/home/aydan/Desktop/CSPC/PW2/Lab A/motion.png')
