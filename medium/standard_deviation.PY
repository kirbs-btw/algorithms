import numpy as np
import math

def standardDeviation():
    arr = np.random.rand(100)
    med = np.sum(arr) / len(arr)

    subSqrtSum = 0
    for i in arr:
        subSqrtSum += (i - med) ** 2

    stdrdDvtn = math.sqrt(subSqrtSum * (1/len(arr)))

    return stdrdDvtn

if __name__ == '__main__':
    standardDeviation()