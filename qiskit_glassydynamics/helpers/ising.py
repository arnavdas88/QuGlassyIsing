from .decoretors import str_to_hamiltonian
import numpy as np
from qiskit.opflow.primitive_ops.pauli_sum_op import PauliSumOp

def get_interaction(element_1, element_2, matrix_dimension):
    """Gets singular interaction between 2 elements of an ising matrix and returns the hamiltonion

    Args:
        element_1 ([int, int]): x, y coordinate of element 1 on the ising matrix
        element_2 ([int, int]): x, y coordinate of element 2 on the ising matrix
        matrix_dimension ([int, int]): Tuple representing the height, width of the ising matrix
    
    Example:
        element_1 : [1, 0]
        element_2 : [2, 0]
        matrix_dimension : 3, 3

        output : ( I^I^I ^ Z^I^I ^ Z^I^I )
        ___________________^_______^
        [1, 0] + [2, 0]

    Returns:
        str: Hamiltonian representing the singular interaction
    """
    output = []
    (tR, tC) = matrix_dimension
    (R1, C1) = element_1
    (R2, C2) = element_2
    if (-1 in element_1) or (-1 in element_2) or (tR in [R1, R2]) or (tC in [C1, C2]):
        # Return empty, for outside bounds in edge cases  
        return ""

    for _ in range(tR):
        R = []
        for _ in range(tC):
            R += [ "I" ]
        output += [R]
    R,C = element_1
    output[R][C] = "Z"
    R,C = element_2
    output[R][C] = "Z" 
    output = "^".join([ "^".join([ R for R in C ]) for C in output ])
    return f"({output})"

def array2hamiltonian(arr, op = 'Z'):
    result = []
    for i in arr:
        result += [op if i == 1 else 'I']
    return f"({'^'.join(result)})"

@str_to_hamiltonian
def Ising2D(matrix_dimension = None) -> PauliSumOp:
    """Gets total interaction over the ising matrix and returns the hamiltonian

    Args:
        matrix_dimension ([int, int], optional): A tuple representing the height and width of the ising matrix . Defaults to (3, 3).

    Returns:
        PauliSumOp: PauliSumOp representation of the total hamiltonian.
    """
    if not matrix_dimension:
        matrix_dimension = (3 , 3)
    (tR, tC) = matrix_dimension
    output = ""
    for R in range(tR):
        for C in range(tC):
            Oi = (R, C)
            Li = (R-1, C)
            Ri = (R+1, C)
            Ti = (R, C-1)
            Bi = (R, C+1)
            I = []
            I += [get_interaction(Li, Oi, matrix_dimension)]
            I += [get_interaction(Ri, Oi, matrix_dimension)]
            I += [get_interaction(Ti, Oi, matrix_dimension)]
            I += [get_interaction(Bi, Oi, matrix_dimension)]
            I = "+".join(I)
            # print(I)
            output += I + "+"
    output = output.replace("++", "+").replace("++", "+").strip('+')
    return output

@str_to_hamiltonian
def Ising1D(matrix_length = None) -> PauliSumOp:
    if not matrix_length:
        matrix_length = 7
    arr = [0 for i in range(matrix_length)]
    arr[0], arr[1] = 1, 1
    arr = np.asarray(arr)
    opmap = []
    for i in range(matrix_length):
        opmap += [ array2hamiltonian(arr) ]
        arr = np.roll(arr, 1)
    opmap = "+".join(opmap)
    return opmap

@str_to_hamiltonian
def plain_hamiltonian(matrix_dimension = None, constructor = 'Z')->PauliSumOp:
    if not matrix_dimension:
        matrix_dimension = (3 , 3)
    if type(matrix_dimension) == type(()):
        (tR, tC) = matrix_dimension
        (tR, tC) = (tR*tC, tR*tC)
    if type(matrix_dimension) == int:
        (tR, tC) = (matrix_dimension, matrix_dimension)
    output = []
    for R in range(tR):
        r = []
        for C in range(tC):
            r += [constructor if R==C else "I"]
        output += [f"({'^'.join(r)})"]
    return "+".join(output)