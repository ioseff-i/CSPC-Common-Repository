"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: read decay_observed.csv (columns: time, count; skip the header row)
#         and split it into two arrays: t and observed.
t, observed = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1, unpack=True)
# TODO 2: set N0 to the FIRST observed value, then build the analytical curve
#         analytical = N0 * exp(-LAMBDA * t)
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: make a 1x2 subplot with SHARED x and y axes.
#         left panel : scatter of the observed data, titled "Observed data"
#         right panel: line plot of the analytical curve, titled "Analytical"
#         label the axes.
fig, axes = plt.subplots(1, 2, sharex=True, sharey=True)

axes[0].scatter(t, observed)
axes[0].set_title("Observed data")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Count")

axes[1].plot(t, analytical)
axes[1].set_title("Analytical")
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Count")

fig.tight_layout()
# TODO 4: save the figure as figure.png
fig.savefig('figure.png')