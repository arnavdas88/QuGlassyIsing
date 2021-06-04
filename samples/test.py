from qiskit_glassydynamics.helpers import ising

ising_1D_hamiltonian = ising.Ising1D(10)
ising_2D_hamiltonian = ising.Ising2D((5, 5))
plain_hamiltonian_Z = ising.plain_hamiltonian( (3,3) , 'Z')
plain_hamiltonian_X = ising.plain_hamiltonian( (3,3) , 'X')

print()
print(ising_1D_hamiltonian)
print()
print(type(plain_hamiltonian_Z))
print()
print(plain_hamiltonian_X)
print()
print(plain_hamiltonian_Z)
