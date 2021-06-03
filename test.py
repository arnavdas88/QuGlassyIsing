from qiskit import *
from qiskit.opflow import OperatorBase
from qiskit.opflow import Z, X, I  # Pauli Z, X matrices and identity

from qiskit_glassydynamics.helpers import ising

Z_hamiltonian = ising.hamiltonian_interaction((3, 3))
Bz_hamiltonian = ising.plain_hamiltonian( (3,3) , 'Z')
Bx_hamiltonian = ising.plain_hamiltonian( (3,3) , 'X')

print(3.0 * Z_hamiltonian)
print()
print(type(Bz_hamiltonian))
print()
print(Bx_hamiltonian)

