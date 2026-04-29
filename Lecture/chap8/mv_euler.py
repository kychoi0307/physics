import numpy as np
import matplotlib.pyplot as plt


def f(r, t):
    omega = 1
    x = r[0]
    y = r[1]
    fx =x*y-x
    fy=y-x*y+np.sin(omega*t)**2
    return np.array([fx,fy])

t = np.linspace(0,10,1001)
h = t[1]-t[0]
x = np.ones_like(t,float)
y = np.ones_like(t,float)

for i in range(1,len(t)):
    r = np.array([x[i-1],y[i-1]])
    r += h*f(r,t[i-1])
    x[i], y[i] = r[0], r[1]

plt.xlim(0,10)
plt.xlabel(r'$t$',fontsize = 16)
plt.ylabel(r'$t$, $y(t)$', fontsize = 16)
plt.plot(t,x,'r-')
plt.plot(t,y,'b-')
plt.show()