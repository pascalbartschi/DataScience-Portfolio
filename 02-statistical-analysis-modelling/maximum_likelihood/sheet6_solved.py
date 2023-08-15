import numpy as np
import scipy.optimize as opt
from matplotlib import pyplot as plt


def nll(prob):
    """Calculate the negative log likelihood for a dataset and its predictions.

    Args:
        data (array): The data set.
        prob (array): Predicted probabilities for the data set.

    Returns:
        float: The negative log likelihood.
    """

    return -1 * np.sum(np.log(prob))

def two_nll(prob):
    """Calculate 2 times the negative log likelihood for a dataset and its probabilites.

    Args:
        data (array): The data set.
        prob (array): Predicted probabilities for the data set.

    Returns:
        float: 2 times the negative log likelihood.
    """
    return 2 * nll(prob)  # an easy way to re-use existing code.

def nll_alpha(alpha):
    """Calculate the negative log likelihood for exercise 1a.

    Args:
        alpha (float): The alpha parameter.

    Returns:
        float: The negative log likelihood.
    """
    # Here is your code for exercise 1a.
    mle = np.loadtxt("MLE.txt")
    prob_mle = 0.5 * (1 + alpha * mle)
    NLL = nll(prob = prob_mle)

    return NLL

def P_t(x, tau):
    return 1 / (tau * (1 - np.exp(-5 / tau)))\
                  * np.exp(-1 * x / tau)

def two_nll_tau(tau):

    ddecay = np.loadtxt("exponential_data.txt")
    prob_decay_times = 1 / (tau * (1 - np.exp(-5 / tau)))\
                  * np.exp(-1 * ddecay / tau)

    two_NLL = two_nll(prob = prob_decay_times)

    return two_NLL


def binned_2nll(tau, nbins, integrate=False):
    """Calculate 2 times the negative log likelihood for a dataset and its probabilites.

    Args:
        data (array): The data set.
        prob (array): Predicted probabilities for the data set.
        nbins (int): Number of bins to use.

    Returns:
        float: 2 times the binned negative log likelihood.
    """

    data = np.loadtxt("exponential_data.txt")
    counts, edges = np.histogram(data, bins=nbins, range = (0, 5))  # get the counts and bin edges. Not sure what they are? Check the documentation!
    # or use the debugger to inspect the variables.
    if integrate:
        pass # scipy intergate
    else:
        bincenter = 0.5 * (edges[1:] + edges[:-1])
        pred = P_t(bincenter, tau)
        bwidth = np.array([edges[i] - edges[i-1] for i in range(len(edges))])
        approx = pred * bwidth[1:]

    return -np.sum(counts * np.log(approx) - approx)


def chi2(tau, nbins):

    x = np.loadtxt("exponential_data.txt")
    counts, edges = np.histogram(x, bins=nbins, range=(0, 5))
    bincenter = 0.5 * (edges[1:] + edges[:-1])
    pred = P_t(bincenter, tau)
    bwidth = np.array([edges[i] - edges[i - 1] for i in range(len(edges))])
    y = pred * bwidth[1:]
    # c = np.cumsum(counts)
    x = counts  # (0.5 * (c[1:] + c[:-1])).astype(int)

    return np.sum((x - y) ** 2 / counts)

def chi2_2c(tau, nbins):

    """Calculate the chi2 statistic for a dataset and its predictions.

    Args:
        x (array): The first data set.
        y (array): Predicted values for the first data set.
        err (array): The error on the measurements of the first data set.

    Returns:
        float: The chi2 statistic.
    """
    x = np.loadtxt("exponential_data.txt")
    counts, edges = np.histogram(x, nbins, range=(0, 5))
    prob = lambda t: (1 / (tau * (1 - (np.exp(-5 / tau))))) * (np.exp(-t / tau))

    fi = []
    for i in range(0, len(counts)):
        binwith = (edges[i + 1] - edges[i]) / 2
        fi.append(x.shape[0] * prob(edges[i] + binwith) * (edges[i + 1] - edges[i]))

    vector = (counts - fi) ** 2 / counts
    chi_2 = np.sum(vector)

    return chi_2

def ex_1a():
    """Run exercise 1a."""

    # Here is your code for exercise 1a.
    alphas = np.linspace(0, 1, 10)
    nll_values = [nll_alpha(alpha) for alpha in alphas]

    fig, ax = plt.subplots(1, 1, figsize = (7, 7))

    ax.plot(alphas, nll_values, marker = "o", color = "purple")
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel("NLL")
    ax.set_title(r"Negative-Log-Likelihoods of $\alpha$ in [0, 1]")
    plt.savefig("1a_NLL_of_alphas.png")

def ex_1b():

    alphas = np.linspace(0, 1, 10)
    nll_values = [nll_alpha(alpha) for alpha in alphas]

    i = np.argwhere(nll_values == min(nll_values))[0][0]
    min_a = alphas[i]

    print(f"1B:\nThe alpha that shows the lowest NLL is alpha = {round(min_a, 2)}, as visible in plot 1a.")

def ex_2a():

    taus = np.linspace(1.81, 2.19, 10)
    two_nll_values = [two_nll_tau(tau) for tau in taus]
    two_nll_values -= min(two_nll_values) # shift of minimum to zero

    fig, ax = plt.subplots(1, 1, figsize = (7, 7))

    ax.plot(taus, two_nll_values, marker = "o", color = "purple")
    ax.set_xlabel("tau [müs]")
    ax.set_ylabel("NLL")
    ax.set_title("Negative-Log-Likelihoods of tau in (1.8, 2.2)")
    plt.savefig("2a_two_NLL_of_taus.png")

def ex_2b():

    data = np.loadtxt("exponential_data.txt")

    taus = np.linspace(1.81, 2.19, 10)

    two_nll_values_bin = [binned_2nll(tau, 40) for tau in taus] # implement integrate
    two_nll_values_bin -= min(two_nll_values_bin) # shift of minimum to zero

    # plot integrate and not integrate

    fig, ax = plt.subplots(1, 1, figsize = (7, 7))

    ax.plot(taus, two_nll_values_bin, marker = "o", color = "purple")
    ax.set_xlabel("tau [müs]")
    ax.set_ylabel("NLL")
    ax.set_title("Negative-Log-Likelihoods approximated with bincenter")
    plt.savefig("2b_two_NLL_of_taus_bins.png")

    print(f"\n2B:\n"
          f"The trajectory of the binned function seems to have lower NLL values overall. \n"
          f"Nevertheless, they both display their minimum at the same tau.")

def ex_2c():

    taus = np.linspace(1.81, 2.19, 10)

    # calculation from 2a)
    two_nll_values = [two_nll_tau(tau) for tau in taus]
    two_nll_values -= min(two_nll_values) # shift of minimum to zero

    nbins = 40
    # calculation from 2b)
    two_nll_values_bin = [binned_2nll(tau, nbins) for tau in taus]
    two_nll_values_bin -= min(two_nll_values_bin) # shift of minimum to zero

    # calculation of chi squared
    chi2_values = [chi2_2c(tau, nbins) for tau in taus]
    chi2_values -= min(chi2_values)

    # overlay the three plots

    fig, ax = plt.subplots(1, 1, figsize = (7, 7))

    ax.plot(taus, two_nll_values, marker = "o", color = "blue", label = "a) two nll")
    ax.plot(taus, two_nll_values_bin, marker = "o", color = "purple",label = "b) two nll binned")
    ax.plot(taus, chi2_values, marker = "o", color = "green", label = "c) chi2")
    ax.set_xlabel("tau [müs]")
    ax.set_ylabel("NLL resp. Chi2")
    ax.set_title("Compare Chi2 and NLL of tau in [1.8, 2.2], nbins = 40")
    ax.legend()
    plt.savefig("2c_comparison_40bins.png")

    print(f"\n2C:\n"
          f"The Chi2 function proposes a different optimal tau than the two NLL functions,\nas the Chi2-minumum"
          f"is slightly shifted to the left")

def ex_2d():
    data = np.loadtxt("exponential_data.txt")

    taus = np.linspace(1.81, 2.19, 10)

    # calculation from 2a)
    two_nll_values = [two_nll_tau(tau) for tau in taus]
    two_nll_values -= min(two_nll_values) # shift of minimum to zero

    nbins = 2
    # calculation from 2b)
    two_nll_values_bin = [binned_2nll(tau, nbins) for tau in taus]
    two_nll_values_bin -= min(two_nll_values_bin)  # shift of minimum to zero

    # calculation of chi squared
    chi2_values = [chi2_2c(tau, nbins) for tau in taus]
    chi2_values -= min(chi2_values)

    # overlay the three plots

    fig, ax = plt.subplots(1, 1, figsize=(7, 7))

    ax.plot(taus, two_nll_values, marker = "o", color = "blue", label = "a) two nll")
    ax.plot(taus, two_nll_values_bin, marker="o", color="purple", label="b) two nll binned")
    ax.plot(taus, chi2_values, marker="o", color="green", label="c) chi2")
    ax.set_xlabel("tau [müs]")
    ax.set_ylabel("NLL resp. Chi2")
    ax.set_title("Compare Chi2 and NLL of tau in [1.8, 2.2], nbins = 2")
    ax.legend()
    plt.savefig("2d_comparison_2bins.png")

    print(f"Plot 2d proposes that the binning of NLL function in two bins is less helpful. \n"
          f"The NLL trajectory doesn't agree with the one obtained in a). The Chi function, however,\n"
          f"displays the same minimum as the result obtained in a).")


def ex_3a():
    data = np.loadtxt("polynomial_data.txt")
    counts, edges = np.histogram(data, bins=20)
    bincenters = 0.5 * (edges[1:] + edges[:-1])
    binwidths = np.array([edges[i] - edges[i - 1] for i in range(len(edges))])

    # plot the histogram

    fig, ax = plt.subplots(1, 1, figsize=(7, 7))

    ax.bar(bincenters, counts, binwidths[1:], yerr = counts ** 0.5) # apply N square rule for poisson errors
    ax.set_title("Histogram and Poisson error")
    ax.set_ylim(1200, 1750)
    ax.set_xlabel("x")
    ax.set_ylabel("measurement")
    # ax.legend()

    plt.savefig("3a_histogram_with_poisson_error")



def polynomial(x, popt, order = None):

    if order == 1:
        a, b = popt
        return a * x + b

    elif order == 2:
        a, b, c = popt
        return a * x ** 2 + b * x + c

    elif order == 3:
        a, b, c, d = popt
        return a * x ** 3 + b * x ** 2 + c * x + d

    elif order == 4:
        a, b, c, d, e = popt
        return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e

    else:
        raise ValueError("Please specify order of polynomial.")



def ex_3b(plot = True, return_opt = False):
    data = np.loadtxt("polynomial_data.txt")
    counts, edges = np.histogram(data, bins=20)
    x = 0.5 * (edges[1:] + edges[:-1])
    y = counts

    # first order
    popt1, pcov1 = opt.curve_fit(f = (lambda x, a, b: a * x + b), xdata = x, ydata = y)
    popt2, pcov2 = opt.curve_fit((lambda x, a, b, c: a * x ** 2 + b * x + c), x, y)
    popt3, pcov3 = opt.curve_fit((lambda x, a, b, c, d: a * x ** 3 + b * x ** 2 + c * x + d), x, y)
    popt4, pcov4 = opt.curve_fit((lambda x, a, b, c, d, e: a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e), x, y)

    if return_opt == True:
        return popt1, popt2, popt3, popt3, popt4

    if plot == True:

        xs = np.linspace(-1, 1, 30000)
        binwidths = np.array([edges[i] - edges[i - 1] for i in range(len(edges))])
        bincenters = x

        fig, ax = plt.subplots(1, 1, figsize=(7, 7))

        ax.bar(bincenters, counts, binwidths[1:], yerr=counts ** 0.5)  # apply N square rule for poisson errors
        ax.plot(xs, polynomial(x = xs, popt = popt1, order = 1), label = "1st order", color = "purple")
        ax.plot(xs, polynomial(x=xs, popt=popt2, order=2), label="2nd order", color = "red")
        ax.plot(xs, polynomial(x=xs, popt=popt3, order=3), label="3rd order", color = "green")
        ax.plot(xs, polynomial(x=xs, popt=popt4, order=4), label="4th order", color = "orange")

        ax.set_title("Polynomial fit to binned data")
        ax.set_ylim(1200, 1750)
        ax.set_xlabel("x")
        ax.set_ylabel("measurement")
        ax.legend()

        plt.savefig("3b_histogram_with_polynomial_fits")

    else:
        return pcov1, pcov2, pcov3, pcov4


def extract_sigma(pcov):
    return round(pcov[0][1] ** 0.5, 2)


def ex_3c():
    pcov1, pcov2, pcov3, pcov4 = ex_3b(plot = False)

    print(f"\n3C\nThe uncertainties are as follows: \n"
          f"1st order: {extract_sigma(pcov1)}\n"
          f"2nd order: {extract_sigma(pcov2)}\n"
          f"3rd order: {extract_sigma(pcov3)}\n"
          f"4th order: {extract_sigma(pcov4)}")

def chi2_3d(x, y):
    return np.sum((x - y) ** 2)

def ex_3d():
    popt1, popt2, popt3, popt3, popt4 = ex_3b(return_opt = True)

    data = np.loadtxt("polynomial_data.txt")
    counts, edges = np.histogram(data, bins=20)
    x = 0.5 * (edges[1:] + edges[:-1])
    y = counts

    df_inital = 30000

    fit1 = chi2_3d(y, polynomial(x=x, popt=popt1, order=1)) / (30000 - len(popt1))  # chi2 / ndf
    fit2 = chi2_3d(y, polynomial(x=x, popt=popt2, order=2)) / (30000 - len(popt2))  # chi2 / ndf
    fit3 = chi2_3d(y, polynomial(x=x, popt=popt3, order=3)) / (30000 - len(popt3))  # chi2 / ndf
    fit4 = chi2_3d(y, polynomial(x=x, popt=popt4, order=4)) / (30000 - len(popt4))  # chi2 / ndf

    plot_x = [1, 2, 3, 4]
    plot_y = [fit1, fit2, fit3, fit4]
    line_y = [1, 1, 1, 1]

    fig, ax = plt.subplots()

    ax.scatter(plot_x, plot_y, color = "purple")
    ax.plot(plot_x, line_y, color = "red", label = "optimal: 1")
    ax.set_title("Chi2/ndf for different degrees")
    ax.set_xlabel("Polynomial degrees")
    ax.set_ylabel("Chi2 / ndf")
    ax.set_xticks([1, 2, 3, 4])
    ax.legend()

    plt.savefig("3d_compare_different degrees")


def ex_3e():
    print("\n3E:\nAccording to the lecture it is optimal to have ratio of one. Below one it means to have overfitted"
          "our polynomial fit. \nGenerally we want to avoid that, but in our case we do not want to predict anything. \n"
          "Therefore, it was generated with third or fourth order as the fits of these is almost identical. (see all plot 3d)")







if __name__ == '__main__':
    # You can uncomment the exercises that you don't want to run. Here we have just one,
    # # but in general you can have more.
    ex_1a()
    ex_1b()
    ex_2a()
    ex_2b()
    ex_2c()
    ex_2d()
    ex_3a()
    ex_3b()
    ex_3c()
    ex_3d()
    ex_3e()