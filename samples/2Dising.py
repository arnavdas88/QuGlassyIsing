from qiskit.providers.aer import QasmSimulator  
from qiskit.providers.aer import AerSimulator
from qiskit import Aer, transpile
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms import VQE
from qiskit.algorithms.optimizers import COBYLA 
from qiskit.circuit.library import EfficientSU2
from qiskit.visualization import plot_histogram

from qiskit_glassydynamics.helpers import ising

counts = []
values = []


def store_intermediate_result(eval_count, parameters, mean, std):
  counts.append(eval_count)
  values.append(mean)


J_hamiltonian = ising.Ising2DHamiltonian( (5, 5) )
Bz_hamiltonian = ising.FieldHamiltonian( (5, 5) , 'Z')
Bx_hamiltonian = ising.FieldHamiltonian( (5, 5) , 'X')


print("=== Z ===")
print(J_hamiltonian)
print()
print("=== Bz ===")
print(Bz_hamiltonian)
print()
print("=== Bx ===")
print(Bx_hamiltonian)

H = - 1. * J_hamiltonian + 1. * Bz_hamiltonian - 1. * Bx_hamiltonian

print()
print("=== H ===")
print(H)

# 2D Ising Simulation

# you can swap this for a real quantum device and keep the rest of the code the same!
backend = QasmSimulator() 

# COBYLA usually works well for small problems like this one
optimizer = COBYLA(maxiter=2000)

# EfficientSU2 is a standard heuristic chemistry ansatz from Qiskit's circuit library
ansatz = EfficientSU2(5, reps=1)

# set the algorithm
vqe = VQE(ansatz, optimizer, quantum_instance=backend, callback=store_intermediate_result)

# run it with the Hamiltonian we defined above
result = vqe.compute_minimum_eigenvalue(H)  

print(result)

plot_histogram(result.eigenstate)
