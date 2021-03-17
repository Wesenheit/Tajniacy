import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


def getmap(dic, board):
    vals = np.array([[1, 1, 1, 1], [0, 0, 1, 1], [
                    240/256, 230/256, 140/256, 1], [1, 0, 0, 1], [0, 0, 0, 1]])
    newcmap = ListedColormap(vals)
    fig = plt.figure()
    ax = plt.axes()
    ax.axis([0, 5, 0, 5])
    psm = ax.pcolormesh(board, cmap=newcmap, rasterized=True, vmin=-2, vmax=2)
    for x in range(6):
        ax.axhline(x, lw=2, color='k', zorder=5)
        ax.axvline(x, lw=2, color='k', zorder=5)
    ax.axis('off')
    for key in dic:
        ax.text(dic[key][0]+0.5-len(key)/20, dic[key][1]+0.5, key)
    plt.savefig("game_board.png")
