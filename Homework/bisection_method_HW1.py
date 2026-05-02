import numpy as np


def f(x):
    y = np.exp(x) * np.log(x) - x ** 2 #주어진 함수
    return y


a = 1.0
b = 2.0
accuracy = 1e-6
error = 1.0

while error > accuracy:
    x0 = (a + b) / 2.0
    if f(a) * f(x0) < 0:
        b = x0
    else:
        a = x0
    error = abs(a - b)

x = (a + b) / 2.0

print("The root is x =", x)