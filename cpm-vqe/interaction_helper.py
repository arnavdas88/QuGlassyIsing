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

class Point:
    """Defines a point
    """
    def __init__(self, x, y, parent = [[]]):
        """Creates a point instance on a parent

        Args:
            x (int): X coordinate of the point on a matrix
            y (int): Y coordinate of the point on a matrix
            parent (2D Array, optional): Parent matrix. Defaults to a blank matrix.
        """
        self.x = x
        self.y = y
        self.parent = parent
    
    @property
    def top(self, ):
        """Top point to the original

        Returns:
            Any: Point on the top
        """
        return self.parent[self.x-1][self.y]

    @property
    def bottom(self, ):
        """Bottom point to the original

        Returns:
            Any: Point on the bottom
        """
        return self.parent[self.x+1][self.y]

    @property
    def left(self, ):
        """Left point to the original

        Returns:
            Any: Point on the left
        """
        return self.parent[self.x][self.y-1]

    @property
    def right(self, ):
        """Right point to the original

        Returns:
            Any: Point on the right
        """
        return self.parent[self.x][self.y+1]

def get_1_neghibour(mat, point):
    """Gets the 1D neghibour in respect to the specified point on the matrix  

    Args:
        mat (2D Array): The base matrix
        point (int, int): x, y point

    Returns:
        Tuple: Returns 4 neghibouring points 
    """
    point = Point(*point, mat)
    return ( point.left, point.right, point.top, point.bottom)