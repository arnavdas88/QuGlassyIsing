# This file is meant to build the original CPM that is to be implemented via Quantum processes
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from config import *
from interaction_helper import reversed_kronecker
from validator import *

import numpy as np
import seaborn as sns
from matplotlib.figure import Figure
from numpy.random import RandomState

cellular_potts_list = cellular_potts_list

# fig, ax = plt.subplots()
# i = ax.imshow(cellular_potts_list, interpolation='nearest')
# plt.show()

