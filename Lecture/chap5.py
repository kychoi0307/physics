import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


x = np.linspace(0, 2 * np.pi, 101)
y = f(x)
dydx_f = np.zeros_like(x, float)
dydx_b = np.zeros_like(x, float)
h = 1.0e-2

for i in range(len(x)):
    dfdx = f(x[i] + h) - f(x[i])
    dfdx /= h
    dydx_f[i] = dfdx
    dfdx = f(x[i]) - f(x[i] - h)
    dfdx /= h
    dydx_b[i] = dfdx

anal_dydx = np.cos(x)

plt.xlim(0,2*np.pi)
plt.ylim(-1,1)
plt.plot(x, y, 'k-', lw=2)
plt.plot(x, dydx_f, 'ro', mfc='None', mew=2)
plt.plot(x, anal_dydx, 'b-', lw=2)
plt.plot(x, dydx_b, 'go', lw=2)
plt.show()
