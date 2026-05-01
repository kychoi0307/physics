import numpy as np


def f(x):
    y = np.exp(x) * np.log(x) - x ** 2 #주어진 함수
    return y


def df(x):
    y = np.exp(x) * np.log(x) + np.exp(x) / x - 2 * x #f(x)의 미분
    return y


accuracy = 1e-12
x = 1.5
error = 1.0

while abs(error) > accuracy:
    error = f(x) / df(x)
    x -= error

print(x)
print(f(x))
