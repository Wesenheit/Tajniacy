import numpy as np
import random


def getwords():
    A = np.loadtxt('words.txt', dtype=str)
    random.shuffle(A)
    pairs = []
    for i in range(0, 5):
        for j in range(0, 5):
            pairs.append([i, j])
    dic = dict(zip(A[0:25], pairs))
    return dic
