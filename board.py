import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


def getboard():
    start = ['Blue', 'Red']
    first = random.choice(start)
    board = []
    for i in range(0, 8):
        board.append(-1)
    for i in range(0, 8):
        board.append(1)
    for i in range(0, 7):
        board.append(0)
    if (first == "Blue"):
        board.append(-1)
    else:
        board.append(1)
    board.append(2)
    random.shuffle(board)
    board = np.array(board).reshape((5, 5))

    vals = np.array(
        [[0, 0, 1, 1], [240/256, 230/256, 140/256, 1], [1, 0, 0, 1], [0, 0, 0, 1]])
    newcmap = ListedColormap(vals)
    fig = plt.figure()
    ax = plt.axes()
    psm = ax.pcolormesh(board, cmap=newcmap, rasterized=True, vmin=-1, vmax=2)
    for x in range(6):
        ax.axhline(x, lw=2, color='k', zorder=5)
        ax.axvline(x, lw=2, color='k', zorder=5)
    #fig.colorbar(psm, ax=ax)
    plt.title("{} team is starting".format(first))
    ax.axis('off')
    plt.savefig("board.png")
    return board
