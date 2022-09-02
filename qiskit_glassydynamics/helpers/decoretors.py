from qiskit.opflow.primitive_ops.pauli_sum_op import PauliSumOp
from qiskit.opflow.list_ops import SummedOp
from qiskit.opflow import OperatorBase
from qiskit.opflow import Z, X, I  # Pauli Z, X matrices and identity


def str_to_hamiltonian(coeffs_i = 1):
    def wrapper(func):
        def action(*args, **kwargs):
            op = func(*args, **kwargs)
            return eval(op)
            # return PauliSumOp.from_list( [ (op, coeffs_i) ] )
        return action
    return wrapper
