import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from scipy.stats import binom, poisson, norm


def integrate(dist, lower, upper):
    """Integrate the pdf of a distribution between lower and upper.

    Parameters
    ----------
    dist : scipy.stats.rv_continuous
        A scipy.stats distribution object.
    lower : float
        Lower limit of the integration.
    upper : float
        Upper limit of the integration.

    Returns
    -------
    integral : float
        The integral of the pdf between lower and upper.
    """
    return dist.cdf(upper)-dist.cdf(lower)

def ex1():
    print(seperate)
    p = 0.85
    n_det = 4

    # pmf
    r = np.arange(n_det+1)
    P = binom.pmf(r, n_det, p)

    # plot
    plt.plot(r, P, '-x')
    plt.xlabel('Number of detections')
    plt.ylabel('Probability')
    plt.title('Probability distribution with four detectors')
    plt.savefig(fname='Ex1a_four_detectors.pdf')

    # cdf
    tries = np.arange(4, 20)
    for n in tries:

        detections = 1-binom.cdf(2, n, p)
        if detections > 0.99:
            print('Exercise 1:')
            print('B')
            print(n, 'detectors provide an efficiency of > 99%.')
            break

    # cdf
    n_tries = 1000
    r_tries = np.arange(750, n_tries+1)
    P_3 = 1-binom.cdf(2, n_det, p) ## probability for 3 | 4 detections
    det_part = binom.pmf(r_tries, n_tries, P_3)

    # plot
    plt.cla()
    plt.plot(r_tries, det_part, label='binomial')
    plt.plot(r_tries, poisson.pmf(r_tries, n_tries*P_3), label='poisson')
    plt.xlabel('Particles detected')
    plt.ylabel('Probability')
    plt.title('Binomial vs. Poisson')
    plt.legend()
    plt.savefig(fname='Ex1c_binomial_vs_poisson.pdf')
    print('C')
    print('The width of the poisson distribution is bigger, \n'
          'because the  binomial distribution includes \n'
          'the exact number of tries.')

def ex3():
    print(seperate)
    mu = 1.
    sigma = 0.01
    p_gauss = norm(mu, sigma)
    prob_a = np.zeros(4)
    prob_a[0]=integrate(p_gauss, 0.97, 1.03) # a
    prob_a[1] = integrate(p_gauss, 0.99, 1.) # b
    prob_a[2] = integrate(p_gauss, 0.95, 1.05) # c
    prob_a[3] = integrate(p_gauss, 0., 1.015) # d

    print('EXERCISE 3')
    print(('Probabilities for a)[0.97, 1.03]:{} \n,'
          '                   b)[0.99, 1.00]:{} \n,'
          '                   c)[0.95, 1.05]:{} \n,'
          '                   d)[0, 1.015]:{}.').format(np.round(prob_a, 3)[0],np.round(prob_a, 3)[1],
                                                     np.round(prob_a, 3)[2],np.round(prob_a, 3)[3]))

def ex4():
    print(seperate)
    p_charged = .82
    p_neut = .18
    n_bos = 500
    t = 125 #hours
    r_4 = np.arange(1, n_bos)
    p_binom = binom.pmf(r_4, n_bos, p_charged)
    p_binom_390 = 1-binom.cdf(389, n_bos, p_charged)
    print('EXERCISE 4')
    print('A')
    print('P(>390 bosons) detected using charged particles: ', np.round(p_binom_390, 5), '\n')
    # approximation
    mu_approx = n_bos*p_charged
    sigma_approx = np.sqrt(n_bos*p_charged*(1-p_charged))
    lam = n_bos*p_charged
    gauss = lambda x: 1/(np.sqrt(sigma_approx**2*2*np.pi))*np.exp(-0.5*((x-mu_approx)/sigma_approx)**2)
    # integrate
    x = np.arange(500)
    p_gauss_390 = scipy.integrate.quad(gauss, 390, 500)[0]
    n1 = 375
    n2 = 450
    plt.cla()
    plt.plot(r_4[n1:n2], p_binom[n1:n2], label='binomial')
    plt.plot(x[n1:n2], gauss(x)[n1:n2], label = 'gaussian')
    plt.legend()
    plt.xlabel('Detected particles ')
    plt.ylabel('Probability')
    plt.title('Binomial vs Gauss')
    plt.savefig(fname='Ex4b_binomial_vs_gauss.pdf')

    print('B')
    print('Gauss approximation result: ', np.round(p_gauss_390, 5))
    print('The approximation is quite good, as is relies up on a big number of trails \n'
          'However, small error is still seen. \n')

    p_poisson_390 = 1-poisson.cdf(389, lam)
    p_poisson = poisson.pmf(r_4, lam)

    plt.cla()
    plt.plot(r_4, p_binom, label='binomial')
    plt.plot(r_4, p_poisson, label = 'poisson')
    plt.xlabel('Particles detected')
    plt.ylabel('Probability')
    plt.title('Binomial vs Poisson')
    plt.savefig(fname='Ex4c_binomial_vs_poisson.pdf')
    plt.legend()

    print('C')
    print('Poisson approximation result: ', np.round(p_poisson_390, 2))
    print('Due to poisson, there is a big loss of information as before.')

    n_1h = n_bos/t
    expected = n_1h*p_charged

    r_charged = np.arange(n_1h + 1)
    p_bos_charged_bin = binom.pmf(r_charged, n_1h, p_charged)
    p_bos_charged_poiss = poisson.pmf(r_charged, expected)
    p_all_charged_bin = p_bos_charged_bin[-1]
    p_all_charged_poiss = p_bos_charged_poiss[-1]
    p_atleast1_neutr_bin = 1- p_all_charged_bin
    p_atleast1_neutr_poiss = 1- p_all_charged_poiss

    plt.cla()
    plt.plot(r_charged, p_bos_charged_bin, '-o', label ='Binomial')
    plt.plot(r_charged, p_bos_charged_poiss, '-o', label = 'Poisson')
    plt.xlabel('Number of decays')
    plt.ylabel('Probability')
    plt.legend()
    plt.title('Probability for boson to decay with n=' + str(n_1h))
    plt.savefig(fname='Ex4c_poisson_vs_binomial.pdf')

    print('\nD')
    print('P(>=1 bosons) decay into neutrinos in 1h: ')
    print('binomial: ', np.round(p_atleast1_neutr_bin, 2))
    print('poisson: ', np.round(p_atleast1_neutr_poiss, 2))

    print('Here, the poisson distribution is unrepresentative, \n'
          'as information of exact number of particles that \n'
          'will reach the detector is lost.')

seperate = '============================================================='

if __name__ == '__main__':
    ex1()
    ex3()
    ex4()
