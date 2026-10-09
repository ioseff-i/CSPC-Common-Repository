import numpy as np
import matplotlib.pyplot as plt

# Read trajectory.csv into arrays t, x, y
t, x, y = np.loadtxt('trajectory.csv', delimiter=',', skiprows=1, unpack=True)

# Compute velocity in each direction using np.gradient
vx = np.gradient(x, t)
vy = np.gradient(y, t)

# Compute overall speed
speed = np.sqrt(vx**2 + vy**2)

# Set up a 1x2 figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot the path (x vs y)
ax1.plot(x, y, color='blue')
ax1.set_title('2D Tracked Trajectory (Path)')
ax1.set_xlabel('x position')
ax1.set_ylabel('y position')
ax1.grid(True)
ax1.axis('equal')  # Keeps the spatial scale proportional

# Plot the speed over time
ax2.plot(t, speed, color='red')
ax2.set_title('Speed over Time')
ax2.set_xlabel('Time (t)')
ax2.set_ylabel('Speed')
ax2.grid(True)

plt.tight_layout()
plt.savefig('trajectory_plot.png')
print("trajectory_plot.png saved successfully.")
