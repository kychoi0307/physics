import numpy as np


def f(x, t):
    return -x**3+np.sin(t)


t = np.linspace(0, 10, 10001)
h = t[1] - t[0]
x = np.zeros_like(t,float)
k = np.zeros_like(4,float)

for i in range(len(t)-1):
    k[0]=h*f(x[i],t[i])
    k[1]=h*f(x[i]+k[0]/2,t[i]+h/2)
    k[2]=h*f(x[i]+k[1]/2,t[i]+h/2)
    k[3]=h*f(x[i]+k[2],t[i]+h)

import matplotlib.pyplot as plt
plt.plot(t,x,'r-',lw=2)
plt.show()