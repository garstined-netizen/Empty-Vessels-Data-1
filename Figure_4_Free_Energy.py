import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate a complex non-Euclidean manifold (Free Energy Landscape)
X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(X, Y)
# A function representing thermodynamic surprise/free energy
Z = np.sin(np.sqrt(X**2 + Y**2)) + 0.1 * (X**2 + Y**2)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the Free Energy surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')

# Simulate a gradient descent trajectory (Active Inference)
t = np.linspace(0, 1, 20)
path_x = 4 * (1 - t) * np.cos(t * np.pi)
path_y = 4 * (1 - t) * np.sin(t * np.pi)
path_z = np.sin(np.sqrt(path_x**2 + path_y**2)) + 0.1 * (path_x**2 + path_y**2)

# Plot the trajectory of the cognitive state
ax.plot(path_x, path_y, path_z, color='red', marker='o', markersize=4, linewidth=2, label='Active Inference (Gradient Descent)')

ax.set_title('Figure 4: Variational Free Energy ($F$) Minimization', fontsize=14, pad=20)
ax.set_xlabel(r'Internal State ($\mu$)')
ax.set_ylabel(r'External State ($\eta$)')
ax.set_zlabel('Surprise / Free Energy')
ax.legend()

plt.tight_layout()

# --- EXPORT TO PDF ---
plt.savefig('Figure_4_Free_Energy.pdf', format='pdf', bbox_inches='tight')
print("File successfully saved as 'Figure_4_Free_Energy.pdf' in your current working directory.")

plt.show()