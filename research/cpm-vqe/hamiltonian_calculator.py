from interaction_helper import *
from config import *
from docplex.mp.model import Model
from qiskit.optimization.problems import QuadraticProgram
from qiskit.optimization.converters import QuadraticProgramToQubo
from area_perimeter_helper import *
import collections


def hamiltonian_calculator(cellular_potts_matrix, area_coeff, area_of_cell_dict, perimeter_coeff, perimeter_of_cell_dict):
    mdl = Model()
    A_0 = mdl.integer_var(lb=min(area_of_cell_dict) - 1, ub=max(area_of_cell_dict) + 1, name="A")
    P_0 = mdl.integer_var(lb=min(perimeter_of_cell_dict) - 1, ub=max(perimeter_of_cell_dict) + 1, name = "P")
    objective_1 = area_coeff * mdl.sum([value - A_0 for key, value in area_of_cell_dict.items()]) ** 2
    objective_2 = perimeter_coeff * mdl.sum([value - P_0 for key, value in perimeter_of_cell_dict.items()]) ** 2
    objective_3 = mdl.sum(get_interaction(cellular_potts_matrix))
    objective = objective_1 + objective_2 + objective_3
    mdl.minimize(objective)
    qp = QuadraticProgram()
    qp.from_docplex(mdl)
    # print(qp.export_as_lp_string())
    return qp

def hamiltonian_to_ising_formulation(mdl_quadratic_program):
    qp2Qubo = QuadraticProgramToQubo()
    QuboProblem = qp2Qubo.convert(mdl_quadratic_program)
    op, offset = QuboProblem.to_ising()
    # print('Offset: {}'.format(offset))
    # print(op)
    return op,offset


# hamiltonian_to_ising_formulation(hamiltonian_calculator(cellular_potts_list, 2, area_of_cell_dict=area_of_cell_dict,
#                                                         perimeter_coeff=1.9, perimeter_of_cell_dict=perimeter_of_cell_dict))