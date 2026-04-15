import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt


def f(x):
    return (1 - x ** 2) ** (0.5)

N_SAPLE = 10000
pi_avg = 0.0
n_iter = np.array(range(1, N_SAPLE+1))
pi_n_iter = np.zeros_like(n_iter,float)

for n in range(N_SAPLE):
    N = 1000
    px = np.zeros(N, float)
    py = np.zeros(N, float)
    N_sir = 0
    for i in range(N):
        x = nr.rand()
        y = nr.rand()
        if y <= f(x):
            N_sir += 1
        px[i] = x
        py[i] = y

    p = N_sir / N
    pi = 4 * p
    print("pi =%f" % (pi))
    pi_avg = (pi_avg*n+pi)/(n+1)
    print("pi_avg =%f" %(pi_avg))
    pi_n_iter[n]=pi_avg

plt.plot(n_iter,pi_n_iter,'ro',ms = 1.5)
plt.plot(n_iter, np.ones(N_SAPLE)*np.pi,'b-')
plt.show()