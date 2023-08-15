import numpy as np
import matplotlib.pyplot as plt

## 1

# a

particles = 100

# experiment
signals_array = np.zeros(4)

for i in range(particles):
    x = np.random.random(size=4)
    signals = 0
    for s in x:
        if s >= 0.15:
            signals += 1

    signals_array[signals-1] += 1

# plot

plt.stairs(values=signals_array / 100, edges=np.linspace(0.5, 4.5, 5))
plt.xticks([1, 2, 3, 4])
plt.title("4 detectors")
plt.xlabel("Number of signals")
plt.ylabel("Probability")
plt.show()

# b

efficiency = 0.99

particels = 100

signals_array = np.zeros(4)

for i in range(particles):
    x = np.random.random(size=4)
    signals = 0
    for s in x:
        if s >= 0.15:
            signals += 1

    signals_array[signals-1] += 1

# c

