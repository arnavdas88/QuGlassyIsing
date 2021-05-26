# This is the file containing the interaction method for the interacting cells
import sys
from config import *

INT_MIN = -sys.maxsize - 1


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
    return 0


class Point:
    """Defines a point
    """

    def __init__(self, x, y, parent=[[]]):
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
        if self.x == 0:
            return INT_MIN
        return self.parent[self.x - 1][self.y]

    @property
    def bottom(self, ):
        """Bottom point to the original

        Returns:
            Any: Point on the bottom
        """

        if self.x == len(self.parent) - 1:
            return INT_MIN
        return self.parent[self.x + 1][self.y]

    @property
    def left(self, ):
        """Left point to the original

        Returns:
            Any: Point on the left
        """

        if self.y == 0:
            return INT_MIN
        return self.parent[self.x][self.y - 1]

    @property
    def right(self, ):
        """Right point to the original

        Returns:
            Any: Point on the right
        """

        if self.y == len(self.parent[0]) - 1:
            return INT_MIN
        return self.parent[self.x][self.y + 1]

    def __str__(self, ):
        """Returns the point as string representation

        Returns:
            String
        """
        return f"Point({self.x}, {self.y})"

    @property
    def type(self, ):
        """Returns the type of the cess

        Returns:
            Any: Type/Value of the cell
        """
        return self.parent[self.x][self.y]


def get_1D_neighbour(mat, point):
    """Gets the 1D neighbour in respect to the specified point on the matrix  

    Args:
        mat (2D Array): The base matrix
        point (int, int): x, y point

    Returns:
        Tuple: Returns 4 neighbouring points 
    """
    point = Point(*point, mat)
    return (point.left, point.right, point.top, point.bottom)


def get_neighbour_mapping(mat):
    """Gets all the points from the 2D Matrix as point lists

    Usage:
        [x for x in get_neighbour_mapping(mat)]

    Args:
        mat (2D List): 2D Matrix

    Yields:
        Point: Point representing the points in the matrix
    """
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            yield Point(x, y, mat)


def get_interaction(mat):
    R = len(mat)
    C = len(mat[0])
    arr = [0, R, C]
    total_interaction = 0
    neighbour_mapping = get_neighbour_mapping(mat)
    for neighbour in neighbour_mapping:
        unique_neighbour = set([neighbour.left, neighbour.right, neighbour.top, neighbour.bottom, neighbour.type])
        for f_neighbour in unique_neighbour:
            total_interaction += reversed_kronecker(f_neighbour, neighbour.type)
    total_interaction = total_interaction - (R+C) # Subtracting the box sides
    return (total_interaction / 2 )
