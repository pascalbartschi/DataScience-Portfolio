"""Skeleton for sheet4.

This contains a fit, you don't need to fit, just use the covariance matrix and best fit from the sheet.

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# define function for the fit
def linear(x, m, q):
    """Linear function

    Returns the linear function of x with slope m and intercept q.

    .. math::
        f(x) = m x + q

    Args:
        x (float): x value
        m (float): slope
        q (float): y-intercept
    """
    return m * x + q

def fit_linear(x, y):
    """Fit linear function

    Fits the linear function to the data (x, y).

    Args:
        x (array): x values
        y (array): y values
    """
    popt, pcov = curve_fit(linear, x, y)
    return popt, pcov

def linear_uncertainty(dev1, dev2, cov, dependence = False):
    tot_uncertainty = (dev1 ** 2 * cov[0][0]) + (dev2 ** 2 * cov[1][1]) # without dependence of variables

    if dependence == True:
        tot_uncertainty = tot_uncertainty + (2 * dev1 * dev2 * cov[0][1]) # with dependence of variables

    tot_uncertainty = (tot_uncertainty) ** 0.5

    return tot_uncertainty


def ex4():
    # loading data
    data = np.loadtxt('sand.txt')

    diameter = data[:, 0]
    slope = data[:, 1]
    slope_err = data[:, 2]

    # covariance matrix pcov and best fit terms from exercise sheet
    pcov = np.array([[1.068, -0.302], [-0.302, 0.118]])
    m , q  = 16.1, -2.61


    # plot the data
    plt.figure(figsize = (10, 6))
    plt.errorbar(diameter, slope, yerr = slope_err, fmt='b.')
    plt.scatter(diameter, slope, color = "k")# plat the data with errorbars
    plt.plot(diameter, linear(diameter, m, q), 'r-')  # plot the fit
    # add labels, titel etc.
    plt.xlabel('diameter [mm]')
    plt.ylabel('slope [%]')
    plt.title('linear "prediction" of slope')
    plt.savefig('slope_diameter_linear.pdf')
    # plt.show()
    plt.clf()

    print("EXERCISE 4")
    print("\nB")

    x = 1.5 # diameter given in exercise
    central_value = linear(x, m, q) # function call
    dev_q = 1 # derivative of mx+q derived for q
    dev_m = x # derviative of mx+q derived for m
    uncertainty_without = linear_uncertainty(dev_m, dev_q, pcov, dependence = False)
    uncertainty_with = linear_uncertainty(dev_m, dev_q, pcov, dependence=True)
    print("The slope disregarding the correlation is {} +/- {}".format(round(central_value, 2), round(uncertainty_without, 1)))
    print("\nC")
    print("The slope including the correlation is {} +/- {}".format(round(central_value, 2), round(uncertainty_with, 1)))

    print("\nConclusion: It makes sense that the uncertainty decreases when one includes the \n"
          "correlation term, because this way we include more information on uncertainty of \n"
          "the data. Including more information means narrower error/ higher precision.")
    # excluding values with including correlation, higher precision more terms, correlation

if __name__ == '__main__':
    ex4()
