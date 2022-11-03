# %%
from turtle import color
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import math
import random


def marche1(n):
    pos = 0
    x = [k for k in range(n+1)]
    axeabsisse = [0 for k in range(n+1)]
    result = []
    result.append(pos)
    for i in range(0, n):
        rdm = random.uniform(0, 1)
        if rdm < 0.5:
            pos += 1
        else:
            pos += -1
        result.append(pos)
    plt.title("Simulation marche aléatoire 1D avec n = " + str(n))
    plt.plot(x, result, label="Position à l'instant k")
    plt.plot(x, axeabsisse, label="position x=0")
    plt.legend()
    plt.grid()


marche1(4)


# %%
