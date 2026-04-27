import numpy as np


def f(x, t):
    return -x**3+np.sin(t)


t = np.linspace(0, 10, 10001)
h = t[1] - t[0]
x = np.zeros_like(t,float)

for i in range(1, len(t)):
    x[i] = x[i - 1]+h*f(x[i-1],t[i-1])

import matplotlib.pyplot as plt
plt.plot(t,x,'ro')
plt.show()
