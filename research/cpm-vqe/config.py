# This is the config file to be referenced by the rest of the software.


# GENERAL SETTINGS
# ----------------------
lattice_length = 8  # Length of the lattice on each side to run our CPM
no_of_cells = 7  # Number of cells that will be contained in lattice model
is_overlap = False  # No cells overlap each other
lattice_block_area = 1.  # Area of each individual cell block in the lattice

# HAMILTONIAN SETTINGS
# -----------------------
lambda_a = 1.0  # Area coefficient in expression lambda_a(A_0 - A_t)^2
lambda_p = 0.5  # Perimeter coefficient in expression lambda_p(P_0 - P_t)^2
interaction_method = "inverted_kronecker"  # Reference the type of interaction in interaction_helper
j = 1.
VERBOSE = True  # Logs to console
RANDOM_SEED = 108  # Defines the random seed

# CELLULAR POTTS POSITIONS
# -------------------------
cellular_potts_list = [[4, 4, 4, 4, 4, 7, 7, 7],
                       [4, 4, 4, 4, 7, 7, 7, 7],
                       [3, 3, 4, 3, 7, 7, 7, 7],
                       [3, 3, 3, 3, 3, 7, 6, 6],
                       [1, 3, 2, 2, 3, 5, 5, 6],
                       [1, 1, 1, 2, 2, 5, 5, 6],
                       [1, 1, 1, 2, 2, 5, 6, 6],
                       [1, 2, 2, 2, 5, 5, 6, 6]]
