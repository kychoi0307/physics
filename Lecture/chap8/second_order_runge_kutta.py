import numpy as np


def f(x, t):
    return -x**3+np.sin(t)


t = np.linspace(0, 10, 10001)
h = t[1] - t[0]
x = np.zeros_like(t,float)

for i in range(len(t)-1):
    k1 = h*f(x[i],t[i])
    k2 = h*f(x[i]+k1/2,t[i]+h/2)
    x[i+1]=x[i]+k2

import matplotlib.pyplot as plt
plt.plot(t,x,'r-',lw=2)
plt.show()
