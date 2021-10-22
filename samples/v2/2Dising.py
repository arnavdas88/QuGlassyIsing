import numpy as np
import networkx as nx # networkx package, see https://networkx.github.io/documentation/stable/
import matplotlib.pyplot as plt # plotting library

from qiskit_glassydynamics.helpers import ising

# lattice graph parameters
m = 3  # number of rows of hexagons in the lattice
n = 3  # number of columns of hexagons in the lattice
isPBC = False # if True, use periodic boundary conditions

# build graph using networkx
square_graph = nx.generators.lattice.grid_2d_graph(m, n, periodic=isPBC)

# label graph nodes by consecutive integers
square_graph = nx.convert_node_labels_to_integers(square_graph)

# set number of lattice sites
N = square_graph.number_of_nodes()
print('constructed hexagonal lattice with {0:d} sites.\n'.format(N))

# visualise graph
pos = nx.spring_layout(square_graph, seed=42, iterations=100)
nx.draw(square_graph, pos=pos, with_labels=True)
plt.show(block=False)


# Building the Ising Model
model = ising.IsingModel(square_graph)

print(model.ising())
print(model.field())
