from config import *


def print_if_verbose(*args):
    """
    This function prints the background work to console

    ---
    :param args: Arguments to be printed to console
    """
    if VERBOSE:
        print(*args)


def check_config_validity():
    """
    This function prints the validity of the config file

    ---
    :rtype: None
    """
    assert(0 <= j <= 100)
    assert(0 <= lattice_length <= 20)
    assert(VERBOSE is True or VERBOSE is False)
    assert(0 <= lambda_a <= 5)
    assert(0 <= lambda_a <= 5)