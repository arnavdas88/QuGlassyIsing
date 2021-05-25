from config import cellular_potts_list, no_of_cells
from collections import Counter
import itertools

cellular_potts_list = cellular_potts_list
cellular_potts_list_flattened = list(itertools.chain(*cellular_potts_list))
area_of_cell_dict = Counter(cellular_potts_list_flattened)
print(area_of_cell_dict)
