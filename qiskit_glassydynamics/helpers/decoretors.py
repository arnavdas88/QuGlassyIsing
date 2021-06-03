from qiskit.opflow import OperatorBase
from qiskit.opflow import Z, X, I  # Pauli Z, X matrices and identity

def str_to_hamiltonian(func):
    def wrapper(*args, **kwargs):
        op = func(*args, **kwargs)
        return eval(op)
    return wrapper