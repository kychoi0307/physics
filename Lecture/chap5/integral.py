import numpy as np

def f(x):
    #return x**4-2*x+1
    return np.sin(x)

def Integrate_singv(g,x):
    h = x[1] - x[0]
    print("h=%f" % (h))
    Int_res = 0.0
    for i in range(len(x) - 1):
        Int_res += f((x[i+1]+x[i])/2)
    Int_res *= h
    return  Int_res

x = np.linspace(0, np.pi, 10001)

my_res = Integrate_singv(f,x)
print("Integration_results:%.10f"%(my_res))
