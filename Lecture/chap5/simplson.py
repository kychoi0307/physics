import numpy as np


def f(x):
    return np.sin(x)


x = np.linspace(0, np.pi, 10001)
h=x[1]-x[0]
my_res = 0.0
for i in range(0, len(x) - 1, 2):
    my_res += (f(x[i + 2] + 4 * f(x[i + 1]) + f(x[i])))
my_res *= h
my_res /= 3

print("my_res=%.10f" %(my_res))