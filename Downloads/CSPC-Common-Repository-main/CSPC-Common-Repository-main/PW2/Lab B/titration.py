import numpy as np
import matplotlib.pyplot as plt

# 1. Read titration.csv (volume_base, pH)
V, pH = np.loadtxt('titration.csv', delimiter=',', skiprows=1, unpack=True)

# 2. Compute the slope using np.gradient
slope = np.gradient(pH, V)

# 3. Find the volume where the slope is largest
max_idx = np.argmax(slope)
eq_volume = V[max_idx]

# 4. Print the equivalence point volume
print(f"Equivalence point found at: {eq_volume:.2f} mL")

# 5. Make two plots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: pH curve
ax1.plot(V, pH, marker='.', color='blue')
ax1.axvline(eq_volume, color='red', linestyle='--', alpha=0.6, label=f'Eq Point ({eq_volume:.1f} mL)')
ax1.set_title('Titration pH Curve')
ax1.set_xlabel('Volume of Base (mL)')
ax1.set_ylabel('pH')
ax1.legend()
ax1.grid(True)

# Right plot: Slope (Derivative)
ax2.plot(V, slope, marker='.', color='green')
ax2.axvline(eq_volume, color='red', linestyle='--', alpha=0.6, label=f'Max Slope ({eq_volume:.1f} mL)')
ax2.set_title('Slope of pH Curve')
ax2.set_xlabel('Volume of Base (mL)')
ax2.set_ylabel('dpH/dV')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('titration.png')
print("titration.png saved successfully.")
