import numpy as np

def Integrate_singv_Sm38(f,x):
    h = x[1] - x[0]
    my_res = 0.0
    for i in range(0, len(x) - 1, 3):
        my_res += (f(x[i]) + 3 * f(x[i + 1]) + 3 * f(x[i + 2]) + f(x[i + 3]))
    my_res *= h
    my_res *= 3 / 8

    return my_res