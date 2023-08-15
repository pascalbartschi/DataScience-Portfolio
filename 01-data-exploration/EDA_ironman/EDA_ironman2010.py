# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt


## SCATTERPLOTS

# load data

ironman = np.loadtxt("ironman.txt") # times are given in minutes

# modifying 2nd column to age

ironman[:,1] = abs(ironman[:,1] - 2010)

# dictionary with columnindex as key

column_dict = {0: 'total rank [rank]' ,
               1: 'age [year]',
               2: 'total time [min]',
               3: 'swimming time [min]',
               4: 'swimming rank [min]',
               5: 'cycling time [min]',
               6: 'cycling rank [rank]',
               7: 'running time [min]',
               8: 'running rank [rank]'}

# asked combinations to plot

combos = [[0,2], [1,2], [7,3], [3,2], [5,2], [7,2]]

# Scatter plotting function setting title and labels

def scatter(lyst, dir): # multiple dimensioanl array
    plt.figure()
    # plot
    plt.scatter(ironman[:,lyst[0]], ironman[:,lyst[1]])
    # labs
    plt.xlabel(column_dict[lyst[0]])
    plt.ylabel(column_dict[lyst[1]])
    title = ("{a} vs. {b}").format(a = column_dict[lyst[0]],
                                      b = column_dict[lyst[1]])
    plt.title(title)
    plt.savefig(dir + "/" + "scatter_" + title.replace(" ", "_") + ".pdf")

# Hexbin plotting is advantegous when scatter has poor overview:

def hexbin(lyst, dir):
    plt.figure()
    # plot
    plt.hexbin(ironman[:,lyst[0]], ironman[:,lyst[1]], gridsize=20, cmap="binary")
    # cbar
    plt.colorbar(label='Count')
    # labs
    plt.xlabel(column_dict[lyst[0]])
    plt.ylabel(column_dict[lyst[1]])
    title = ("{a} vs. {b}").format(a = column_dict[lyst[0]],
                                      b = column_dict[lyst[1]])
    plt.title(title)
    plt.savefig(dir + "/" + "hexbin_" + title.replace(" ", "_") + ".pdf")


## HISTOGRAMS

# setting number of bins (bin width)

bins = 20

# implementing hist func, taking min/max of array as bounds/range

def histogram(key, bins, dir):
    lower = min(ironman[:,key])
    upper = max(ironman[:,key])
    plt.figure()
    plt.hist(ironman[:, key], bins = bins, range = (lower, upper))
    plt.ylabel("Frequency")
    plt.xlabel(column_dict[key])
    title = ("histogram of {}").format(column_dict[key])
    plt.title(title)
    plt.savefig(dir + "/" + title.replace(" ", "_") + ".pdf")


def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")


# function calls

if __name__ == "__main__":

    # dir
    dir = "figures"
    create_directory(dir)
    # all scatters
    for combo in combos:
        scatter(combo, dir)
        hexbin(combo, dir)

    # 2 exploratory histograms
    histogram(2, bins = bins, dir = dir)
    histogram(1, bins = bins, dir = dir)

# comment from DA-team: a vs. b means f(b) = a, thus a is on the y and b on the x axis

    
    
    




