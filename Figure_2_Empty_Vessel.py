import matplotlib.pyplot as plt
import networkx as nx

fig, ax = plt.subplots(figsize=(8, 6))
G = nx.DiGraph()

# Add the "Empty Vessel" and surrounding Category objects
G.add_node("V", pos=(0, 0))
G.add_node("A", pos=(-2, 1.5))
G.add_node("B", pos=(2, 1.5))
G.add_node("C", pos=(-2, -1.5))
G.add_node("D", pos=(2, -1.5))

# Add Morphisms (Arrows) defining V from the outside
G.add_edge("A", "V", label="$f$")
G.add_edge("B", "V", label="$g$")
G.add_edge("V", "C", label="$h$")
G.add_edge("V", "D", label="$k$")

pos = nx.get_node_attributes(G, 'pos')

# Draw nodes: V is an 'Empty' circle, others are solid
nx.draw_networkx_nodes(G, pos, nodelist=["A", "B", "C", "D"], node_size=1500, node_color='lightgray', edgecolors='black')
nx.draw_networkx_nodes(G, pos, nodelist=["V"], node_size=2000, node_color='white', edgecolors='blue', linewidths=3)

# Draw edges and labels
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='black', connectionstyle="arc3,rad=0.1")
nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif", font_weight='bold')

edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=14)

# Titles and Captions
ax.set_title(r'Figure 2: The Empty Vessel ($V$) Exhausted by $\operatorname{Hom}(-, V)$', fontsize=14)
ax.text(0, -2.5, 'Object $V$ possesses no internal elements.\nIdentity is structurally mapped via the Yoneda Lemma.', ha='center', fontsize=12, style='italic')

plt.axis('off')
plt.tight_layout()

# --- EXPORT TO PDF ---
# The bbox_inches='tight' argument ensures no white space is cut off.
plt.savefig('Figure_2_Empty_Vessel.pdf', format='pdf', bbox_inches='tight')
print("File successfully saved as 'Figure_2_Empty_Vessel.pdf' in your current working directory.")

# Display the plot in your editor as well
plt.show()