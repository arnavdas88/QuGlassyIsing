from config import cellular_potts_list, no_of_cells
from collections import Counter
from pprint import pprint 
import itertools


def perimeter(matrix):
    """Returns a dictionary mapping of each unique elements with the perimeter of their respective clusters.

    Args:
        matrix (2D Array): Base matrix

    Returns:
        dict: mapping of the perimeter
    """
    R = len(matrix)
    C = len(matrix[0])
    
    def numofneighbour(mat, i, j, p=1):
        count = 0
        if (i > 0 and mat[i - 1][j] == p):
            count+= 1
        if (j > 0 and mat[i][j - 1] == p):
            count+= 1
        if (i < R-1 and mat[i + 1][j] == p):
            count+= 1
        if (j < C-1 and mat[i][j + 1] == p):
            count+= 1
        return count
    
    def findperimeter(mat, p=1):
        perimeter = 0
        for i in range(0, R):
            for j in range(0, C):
                if (mat[i][j]) == p:
                    perimeter += (4 - numofneighbour(mat, i, j, p))
    
        return perimeter
    return {x:findperimeter(matrix, x) for x in range(1, 10)}


cellular_potts_list = cellular_potts_list
cellular_potts_list_flattened = list(itertools.chain(*cellular_potts_list))
area_of_cell_dict = Counter(cellular_potts_list_flattened)
perimeter_of_cell_dict = perimeter(cellular_potts_list)

print("\n"*2)
pprint(cellular_potts_list)
print("\n"*2)


print("Area: ", area_of_cell_dict)
print("Perimeter: ", perimeter_of_cell_dict)


print("\n"*4)
