import numpy as np
import matplotlib.pyplot as plt
import integral as inte

def f(x):
    return np.sin(x)


x = np.linspace(0, 2 * np.pi, 101)
y = f(x)
ddy = np.zeros_like(x,float)
h = 1.0e-2

for i in range(len(x)):
    ddf = f(x[i] + h) -2*f(x[i]) + f(x[i]-h)
    ddf /= (h**2)
    ddy[i] = ddf

anal_dydx = np.cos(x)

plt.xlim(0,2*np.pi)
plt.ylim(-1,1)
plt.plot(x, y, 'k-', lw=2)
plt.plot(x, ddy, 'ro', mfc='None', mew=2)
plt.plot(x, np.sin(x), 'b-', lw=2)
plt.show()
