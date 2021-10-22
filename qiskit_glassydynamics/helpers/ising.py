from qiskit.opflow.primitive_ops.pauli_sum_op import PauliSumOp
from .decoretors import str_to_hamiltonian
import networkx as nx # networkx package, see https://networkx.github.io/documentation/stable/
import numpy as np

class IsingModel():
    def __init__(self, graph):
        """Creates an Ising Object from a `NetworkX` Graph of Lattice

        Args:
            graph (networkx.classes.graph.Graph): NetworkX Graph of the Lattice
        """        
        self.name = "IsingModel"
        self.size = graph.number_of_nodes()
        self.graph = graph
        self.adjacency_matrix = nx.adjacency_matrix(self.graph).todense()
        self.list_of_neigh = {}
        for node in self.graph.nodes():
            self.list_of_neigh[node] = list(self.graph.neighbors(node))
        self.edges = list(self.graph.edges())
    
    def ising(self, basis='Z') -> PauliSumOp:
        """Generates the Ising Model of the Lattice

        Args:
            basis (str, optional): Basis over the Ising Hamiltonian. Defaults to 'Z'.

        Returns:
            PauliSumOp: Pauli Sum for the Ising Hamiltonian
        """        
        total_interaction = []
        for interaction in self.edges:
            A, B = interaction
            current_interction = self.interact(A, B, basis=basis)
            if current_interction not in total_interaction:
                total_interaction += [ current_interction ]
        return sum(total_interaction)
    
    @str_to_hamiltonian()
    def interact(self, node_A, node_B, basis = 'Z'):
        hamiltonian_element = [ 'I' ] * self.size
        hamiltonian_element[node_A] = basis
        hamiltonian_element[node_B] = basis
        return ''.join(hamiltonian_element)

    def field(self, basis='X') -> PauliSumOp:
        """Generates a Field Model to be superimposed over the Lattice

        Args:
            basis (str, optional): Basis over the Field Hamiltonian. Defaults to 'X'.

        Returns:
            PauliSumOp: Pauli Sum for the Field Hamiltonian
        """        
        total_field = []
        for diagonal in range(self.size):
            field_element = self.plain(diagonal, basis)
            if field_element not in total_field:
                total_field += [ field_element ]
        return sum(total_field)

    @str_to_hamiltonian()
    def plain(self, node, basis = 'Z'):
        hamiltonian_element = [ 'I' ] * self.size
        hamiltonian_element[node] = basis
        return ''.join(hamiltonian_element)
