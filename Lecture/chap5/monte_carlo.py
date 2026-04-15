import numpy as np
import numpy.random as nr

N=10000
res=0.0
for i in range(N):
    x = nr.rand()*np.pi
    res += np.sin(x)
res /= N
res *= np.pi

print("res=%f", res)