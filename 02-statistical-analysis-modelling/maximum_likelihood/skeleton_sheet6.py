"""Skeleton for Data Analysis Fall 2022 sheet 6.

This sheet helps to structure the code for the exercises of sheet 6.
It shows idioms and best practices for writing code in Python.

You can directly use this sheet and modify it.

(It is not guaranteed to be bug free)
"""
import numpy as np
import scipy.optimize as opt
from matplotlib import pyplot as plt


def nll(data, prob):
    """Calculate the negative log likelihood for a dataset and its predictions.

    Args:
        data (array): The data set.
        prob (array): Predicted probabilities for the data set.

    Returns:
        float: The negative log likelihood.
    """
    pass  # TODO: implement the NLL function.

def two_nll(data, prob):
    """Calculate 2 times the negative log likelihood for a dataset and its probabilites.

    Args:
        data (array): The data set.
        prob (array): Predicted probabilities for the data set.

    Returns:
        float: 2 times the negative log likelihood.
    """
    return 2 * nll(data, prob)  # an easy way to re-use existing code.

def nll1a(alpha):
    """Calculate the negative log likelihood for exercise 1a.

    Args:
        alpha (float): The alpha parameter.

    Returns:
        float: The negative log likelihood.
    """
    # Here is your code for exercise 1a.
    pass

def binned_2nll(data, prob, nbins, integrate=False):
    """Calculate 2 times the negative log likelihood for a dataset and its probabilites.

    Args:
        data (array): The data set.
        prob (array): Predicted probabilities for the data set.
        nbins (int): Number of bins to use.

    Returns:
        float: 2 times the binned negative log likelihood.
    """
    counts, edges = np.histogram(data, bins=nbins)  # get the counts and bin edges. Not sure what they are? Check the documentation!
    # or use the debugger to inspect the variables.
    if integrate:
        ...
    else:
        bincenter = ...  # TODO: use array slicing to get the bin centers.

def ex_1a():
    """Run exercise 1a."""

    # Here is your code for exercise 1a.
    print("ex1a executed.")





if __name__ == '__main__':
    # You can uncomment the exercises that you don't want to run. Here we have just one,
    # but in general you can have more.
    ex_1a()
