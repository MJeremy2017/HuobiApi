import numpy as np


def get_ma(close, size=None):
    if not size:
        return np.mean(close)
    else:
        return np.mean(close[:size])
