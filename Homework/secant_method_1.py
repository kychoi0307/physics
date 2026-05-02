import numpy as np


def f(x):
    y = np.exp(x) * np.log(x) - x ** 2  #주어진 함수
    return y

accuracy = 1e-12
delta = 1.0
x1 = 1.0
x2 = 2.0

while abs(delta) > accuracy:
    delta = f(x2) * (x2 - x1) / (f(x2) - f(x1))
    x = x2 - delta
    x1, x2 = x2, x

print("The root is x =", x)