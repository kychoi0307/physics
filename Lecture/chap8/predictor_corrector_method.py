import numpy as np


def f(x, t):
    return -x**3+np.sin(t)


t = np.linspace(0, 10, 10001)
h = t[1] - t[0]
x = np.zeros_like(t,float)

for i in range(len(t)-1):
    p = x[i]+h*f(x[i],t[i])
    x[i+1] = x[i]+h*(f(x[i], t[i])+f(p, t[i+1]))/2

import matplotlib.pyplot as plt
plt.plot(t,x,'ro')
plt.show()