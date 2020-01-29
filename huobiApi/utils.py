import numpy as np


def get_ma(price, size=None):
    if not size:
        return np.mean(price)
    else:
        return np.mean(price[:size])
