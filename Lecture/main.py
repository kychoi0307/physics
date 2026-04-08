import numpy as np


def givenf(x):
    return x - 2 + np.exp(-x)


def dfdx(f, x1, x0):
    df = f(x1) - f(x0)
    dx = x1 - x0
    return df / dx


x0 = 3.0
x1 = 3.5
tolerance = 1.0e-6
delta = 1.0

while delta > tolerance:
    delta = -givenf(x1) / dfdx(givenf, x1, x0)
    x2 = x1 + delta
    delta = np.abs(delta)
    x0, x1 = x1, x2

print("x=%f" % (x1))
