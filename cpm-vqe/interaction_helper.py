# This is the file containing the interaction method for the interacting cells
from config import *


def reversed_kronecker(cell_1: int, cell_2: int):
    """
    This function determines the interaction between cell_1 and cell_2. Here were are going to implement a reversed
    Kronecker Delta function ie. if the two cells are the same, they will not interact (because we arent looking at
    intracellular interaction) and if they are different, then they will interact with an interaction strength of J that
    is defined in the config file

    ---
    :param cell_1: Type of cell in the lattice for which interaction is to be measured
    :param cell_2: Type of cell in the lattice for which the a cell interacts with
    :return: interaction_strength: The interaction strength if they were to interact
    """
    if cell_1 != cell_2:
        interaction_strength = j
        return interaction_strength

