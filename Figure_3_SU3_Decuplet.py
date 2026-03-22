import matplotlib.pyplot as plt

# Isospin (x) and Strangeness (y) coordinates for the SU(3) Decuplet
particles = {
    r'$\Delta^-$': (-1.5, 0), r'$\Delta^0$': (-0.5, 0), r'$\Delta^+$': (0.5, 0), r'$\Delta^{++}$': (1.5, 0),
    r'$\Sigma^{*-}$': (-1.0, -1), r'$\Sigma^{*0}$': (0.0, -1), r'$\Sigma^{*+}$': (1.0, -1),
    r'$\Xi^{*-}$': (-0.5, -2), r'$\Xi^{*0}$': (0.5, -2),
    r'$\Omega^-$ (Predicted)': (0.0, -3) # The Empty Vessel
}

fig, ax = plt.subplots(figsize=(8, 6))

# Plot all particles
for name, coords in particles.items():
    if 'Omega' in name:
        # Highlight the predicted Empty Vessel in red
        ax.plot(coords[0], coords[1], 'ro', markersize=12, label='Predicted Empty Vessel')
        ax.text(coords[0], coords[1]-0.25, name, fontsize=12, ha='center', color='red', fontweight='bold')
    else:
        ax.plot(coords[0], coords[1], 'bo', markersize=10)
        ax.text(coords[0], coords[1]+0.15, name, fontsize=12, ha='center')

# Draw the connecting grid (the formal symmetry scaffolding)
lines = [
    [(-1.5, 0), (1.5, 0)], [(-1.0, -1), (1.0, -1)], [(-0.5, -2), (0.5, -2)],
    [(-1.5, 0), (0.0, -3)], [(-0.5, 0), (0.5, -2)],
    [(1.5, 0), (0.0, -3)], [(0.5, 0), (-0.5, -2)]
]
for line in lines:
    x_val = [line[0][0], line[1][0]]
    y_val = [line[0][1], line[1][1]]
    ax.plot(x_val, y_val, 'k--', alpha=0.5)

ax.set_title('Figure 3: SU(3) Baryon Decuplet & The Predictive Engine', fontsize=14, pad=20)
ax.set_xlabel('Isospin ($I_z$)', fontsize=12)
ax.set_ylabel('Strangeness ($S$)', fontsize=12)
ax.set_xlim(-2, 2)
ax.set_ylim(-3.8, 0.8)
ax.grid(False)
ax.legend(loc='upper right')

plt.tight_layout()

# --- EXPORT TO PDF ---
plt.savefig('Figure_3_SU3_Decuplet.pdf', format='pdf', bbox_inches='tight')
print("File successfully saved as 'Figure_3_SU3_Decuplet.pdf' in your current working directory.")

plt.show()