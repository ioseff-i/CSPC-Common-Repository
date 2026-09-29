"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     

# 1. Read decay_observed.csv into arrays t and observed
# Adjust skiprows=1 if your CSV has a single header line
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# 2. Set N0 to the first observed value and compute analytical values
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# 3. Create a 1x2 subplot with shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 5))

# Left plot: Observed data (scatter/points)
ax1.scatter(t, observed, color="blue", label="Observed")
ax1.set_title("Observed Data")
ax1.set_xlabel("Time (t)")
ax1.set_ylabel("Count (N)")
ax1.grid(True)

# Right plot: Analytical law (line)
ax2.plot(t, analytical, color="red", label="Analytical")
ax2.set_title("Analytical Law")
ax2.set_xlabel("Time (t)")
ax2.grid(True)

plt.tight_layout()

# 4. Save the figure
plt.savefig("figure.png")
plt.show()
