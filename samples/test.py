from qiskit_glassydynamics.helpers import ising

ising_1D_hamiltonian = ising.Ising1DHamiltonian(10)
ising_2D_hamiltonian = ising.Ising2DHamiltonian((5, 5))
FieldHamiltonian_Z = ising.FieldHamiltonian( (3,3) , 'Z')
FieldHamiltonian_X = ising.FieldHamiltonian( (3,3) , 'X')

print()
print(ising_1D_hamiltonian)
print()
print(type(FieldHamiltonian_Z))
print()
print(FieldHamiltonian_X)
print()
print(FieldHamiltonian_Z)
