import numpy as np
import matplotlib.pyplot as plt

 # exercise 2, instead of calculator :P

def ex2(s_sys, s_stat1, s_stat2):
    tot1 = (s_sys ** 2 + s_stat1 ** 2) ** 0.5
    tot2 = (s_sys ** 2 + s_stat2 ** 2) ** 0.5

    p = s_sys ** 2 / (tot1 * tot2)

    return round(p, 2)

# s_sys = 0.1
#
# print("p1,2:", ex2(s_sys, 0.2, 0.04))
# print("p1,3:", ex2(s_sys, 0.2, 0.1))
# print("p2,3:", ex2(s_sys, 0.04, 0.1))

def plot_data(so):
    fig = plt.figure(figsize = (10, 6))

    plt.scatter()

    return

def ex4():
    sand = np.loadtxt("sand.txt")
    slope = sand[:,1]
    diameter = sand[:,0]
    uncertainties = sand[:,2]


    return