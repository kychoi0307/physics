def f(x):
    y = x**5 - 3*x**4 - 5*x**3 + x**2 + x + 3 #주어진 함수
    return y

accuracy = 1e-12

#첫 번째 해가 있는 구간 [-2,0]
x1 = -2.0
x2 = -1.0
delta = 1.0

#첫 번째 구간에서 SM 적용
while abs(delta) > accuracy:
    delta = f(x2) * (x2 - x1) / (f(x2) - f(x1))
    x = x2 - delta
    x1, x2 = x2, x

print("root1: x =", x)


#두 번째 해가 있는 구간 [0,4]
x1 = 0.0
x2 = 1.0
delta = 1.0

#두 번째 구간에서 SM 적용
while abs(delta) > accuracy:
    delta = f(x2) * (x2 - x1) / (f(x2) - f(x1))
    x = x2 - delta
    x1, x2 = x2, x

print("root2: x =", x)