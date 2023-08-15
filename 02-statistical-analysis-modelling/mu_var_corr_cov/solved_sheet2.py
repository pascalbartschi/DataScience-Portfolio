import numpy as np
import matplotlib.pyplot as plt


def mean(x):
    """Calculate the mean for an array-like object x.

    Parameters
    ----------
    x : array-like
        Array-like object containing the data.

    Returns
    -------
    mean : float
        The mean of the data.
    """
    # here goes your code
    summed = 0
    for i in range(len(x)):
        summed += x[i]

    return summed / len(x)


def variance(x):

    """Calculate the variance for an array-like object x."""
    mean_x = mean(x)
    varsum = 0
    for i in range(len(x)):
        varsum += (x[i] - mean_x) ** 2

    return varsum / len(x)


def std(x):
    """Calculate the standard deviation for an array-like object x."""

    return (variance(x)) ** 0.5  # replace this with your code


def mean_uncertainty(x):
    """Calculate the uncertainty in the mean for an array-like object x."""

    return std(x) / len(x) ** 0.5


def histogram(x, bins, title):
    """X is an array like object and bins are the asked number of bins"""

    bins = bins + 1                                              # number of bins + 1 because one is lost in process
    x_bins = np.arange(min(x), max(x), (max(x)-min(x)) / bins)   # bin edges for x
    x_binned = []
    x_freq = []
    x_unit = []

    for i in range(len(x_bins) - 1):

       x_binned.append(x[np.logical_and(x_bins[i] <= x, x_bins[i+1] > x)])
       x_freq.append(len(x_binned[i]))
       x_unit.append(str(round(x_bins[i],1)) + "-" + str(round(x_bins[i+1],1)))

    # x_binned = np.array(x_binned)
    x_freq = np.array(x_freq)

    sta_uncertainty = len(x) ** 0.5

    # histograms of
    plt.figure()
    plt.rcParams.update({'font.size': 7})
    title_ = "Histogram of " + str(title)
    plt.title(title_)
    plt.ylabel("Frequency")
    plt.xticks(rotation = 45)
    plt.bar(x = x_unit, height = x_freq, yerr = sta_uncertainty)
    plt.savefig(title_.replace(" ", "_") + ".pdf")

    return ()

def covariance(x1,x2):
    '''covariance of to random variables'''
    covsum = 0
    mean_x1 = mean(x1)
    mean_x2 = mean(x2)
    for i in range(len(x1)):
        covsum += (x1[i] - mean_x1) * (x2[i] - mean_x2)

    return (covsum / len(x1))        # sample formula: len(x1) - 1

def correlation_coefficient(x1, x2):
    '''pearson correlation coefficient of two random variables'''

    return covariance(x1, x2) / (std(x1) * std(x2))


def weighted_avg(data, error):
    '''data and error are two arrays of the same dimension to calculate weighted mean'''

    numerator, denominator = 0, 0
    for dat, err in zip(data, error):
        numerator += dat / (err ** 2)
        denominator += 1 / (err ** 2)

    weighted_average = numerator / denominator
    uncertainty = 1 / denominator ** 0.5

    return np.array([weighted_average, uncertainty])



def ex1():
    data = np.loadtxt("ironman.txt")
    age = 2010 - data[:, 1]
    tot_time = data[:,2]
    tot_rank = data[:,0]
    swim_time = data[:, 3]
    cyc_time = data[:, 5]
    run_time = data[:, 7]


    # a1)
    print("1 Ai")
    mean_age = mean(age)
    mean_age_uncertainty = mean_uncertainty(age)
    # .2f means that the number is printed with two decimals. Check if that makes sense
    print(f"The mean age of the participants is {mean_age:.2f} +/- {mean_age_uncertainty:.2f} years.")
    var_age = variance(age)
    std_age = std(age)
    print(f"The variance of age of the participants is {var_age:.2f} and the standard deviation {std_age:.2f} years.")


    #a2)
    print("\n 1 Aii")
    mean_tt = mean(tot_time)
    mean_tt_uncertainty = mean_uncertainty(tot_time)
    # .2f means that the number is printed with two decimals. Check if that makes sense
    print(f"The mean total time of the participants is {mean_tt:.2f} +/- {mean_tt_uncertainty:.2f} minutes.")
    var_tt = variance(tot_time)
    std_tt = std(tot_time)
    print(f"The variance of total time of the participants is {var_tt:.2f} and the standard deviation {std_tt:.2f} minutes.")


    #b)
    print("\n 1 B")
    data_copy = np.copy(data)
    data_copy[:,1] = 2010 - data_copy[:,1]

    young = data_copy[data_copy[:,1] < 35][:,2]
    old = data_copy[data_copy[:,1] > 35][:,2]
    mean_young = mean(young)
    mean_young_uncertainty = mean_uncertainty(young)
    mean_old = mean(old)
    mean_old_uncertainty = mean_uncertainty(old)
    print(f"The mean total time of the young participants is {mean_young:.2f} +/- {mean_young_uncertainty:.2f} \n"
          f"The mean total time of the old participants is {mean_old:.2f} +/- {mean_old_uncertainty:.2f}")
    print("Yes, one can conclude that the younger ones were faster because the upper uncertainty bound of \n"
          f"the younger peoble (= {mean_young + mean_young_uncertainty:.2f}) doesn't lie within the uncertainty "
          f"interval of the old ones (check above) ")


    #c)
    print("\n 1 C \n -> see saved files")

    histogram(x = age, bins = 10, title = "age")
    histogram(x = tot_time, bins = 10, title = "total time")


    #d)
    print("\n 1 D")

    binwidths_tt = [5, 10, 15, 20, 30, 50]
    binwidths_age = [2, 3, 4, 5, 6, 7]
    means_tt = {}
    means_age = {}

    for binwidth1,binwidth2 in zip(enumerate(binwidths_tt), enumerate(binwidths_age)):
        i, j , bw_tt, bw_age = binwidth1[0], binwidth2[0],  binwidth1[1], binwidth2[1]

        hist_tt = np.histogram(a=tot_time, bins=int((max(tot_time) - min(tot_time)) / bw_tt), range = (min(tot_time), max(tot_time)))[1]
        hist_age = np.histogram(a=age, bins=int((max(age) - min(age)) / bw_age), range = (min(age), max(age)))[1]
        hist_age = list(hist_age)
        hist_tt = list(hist_tt)

        if i != 0:
          tt = [tot_time[int(hist_tt[i - 1]):int(hist_tt[i])]]
        else: tt = [tot_time[:int(hist_tt[i])]]
        means_tt[str(bw1)] = [mean(tt), variance(tt), std(tt)]

        if j != 0:
          a = [age[int(hist_age[j - 1]): int(hist_age[j])]]
        else: a = [age[:int(hist_age[j])]]
        means_age[str(bw2)] = [mean(a), variance(a), std(a)]

    print(means_tt)
    print(means_age)
    print("Conclusion: The higher the binwidth is set the higher the variance and standard deviation become, this means" \
          "that the mean precision is higher at lower binwidths")


    #e)
    print("\n 1 E")

    # total rank and total time
    cov1 = covariance(tot_rank, tot_time)
    cor1 = correlation_coefficient(tot_rank, tot_time)
    print(("The total rank and the total time have a covariance of {:.2f} with a correlation coefficient of {:.2f}.") \
          .format(cov1, cor1))
    # print(np.cov(tot_time, tot_rank))

    # age and total time
    cov2 = covariance(age, tot_time)
    cor2 = correlation_coefficient(age, tot_time)
    print(("The age in 2010 and the total time have a covariance of {:.2f} with a correlation coefficient of {:.2f}.") \
        .format(cov2, cor2))

    # total time and swimming and time
    cov3 = covariance(tot_time, swim_time)
    cor3 = correlation_coefficient(tot_time, swim_time)
    print(("The total time and the swimming time have a covariance of {:.2f} with a correlation coefficient of {:.2f}.") \
          .format(cov3, cor3))

    # cycling time and running time
    cov4 = covariance(cyc_time, run_time)
    cor4 = correlation_coefficient(cyc_time, run_time)
    print(("The cycling time and the runnning time have a covariance of {:.2f} with a correlation coefficient of {:.2f}.") \
          .format(cov4, cor4))

    print("Conclusion: The impression from the scatter plots coincides with the calculated values above. The total time \n"
          "leads directly to the total rank, thus we see high correlation and covariance and low scatter. From eye also the \n"
          "extent of scatter of the other plots coincides with the related correlation values of this weeks exercise.")

    # the total time in seconds
    tot_time_sec = tot_time * 60

    # age and total time in seconds
    cov5 = covariance(age, tot_time_sec)
    cor5 = correlation_coefficient(age, tot_time_sec)
    print(("The age in 2010 and the total time in seconds have a covariance of {:.2f} with a correlation coefficient of {:.2f} \n" \
          "compared to {:.2f} and {:.2f} when time was measured in minutes.Fortunately, the normalization did its job and the \n" \
           "correlation coefficient stays the same whereas the covariance changes").format(cov5, cor5, cov2, cor2))



def ex2():
    radiation = np.loadtxt("radiation.txt")
    measurements = radiation[:,0]
    uncertainties = radiation[:,1]

    #a)
    avg = weighted_avg(measurements, uncertainties)

    print("\n 2 A")
    print(("The weighted average is {:.3e} +/- {:.1e}").format(avg[0], avg[1]))

    # b)
    # conversion to mSv/y: 1 common year = 365 days = (365 days) * (24 hours/day) = 8760 hours

    avg_y = avg * 8760

    print("\n 2 B")
    print(("No, the backgound radiation of 2.4 mSv/y doesn't lie within the uncertainty of my measured {:.2f} +/- {:.2f} mSv/y ") \
    .format(avg_y[0], avg_y[1]))
    print("Thus, the radiation containers have proved effect on the radiation level!")







if __name__ == '__main__':
    ex1()
    ex2()


## what I learned:
# np.logical_and/or is used for logical combos in masking arrays, use of AND/OR not possible.
# np.cov output(cov(a,a), cov(a,b), cov(a,b), cov(b, b)) # attention calculates sample variance(set bias = True) for /N
# np.corrcoef: works similar, normalized as in lecture
# use of zip in looping through multiple arrays