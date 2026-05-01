def f(x):
    y = x**5 - 3*x**4 - 5*x**3 + x**2 + x + 3  #주어진 함수
    return y

accuracy = 1e-6

# 주어진 함수가 구간 안에서 두 개의 해를 가진다
# 첫 번째 구간: [-2, 0]
a = -2.0
b = 0.0
error = abs(a - b)

while error > accuracy:
    x0 = (a + b) / 2.0

    if f(a) * f(x0) < 0:
        b = x0
    else:
        a = x0

    error = abs(a - b)

x = (a + b) / 2.0
print("root1:", x)

# 두 번째 구간: [0, 4]
a = 0.0
b = 4.0
error = abs(a - b)

while error > accuracy:
    x0 = (a + b) / 2.0

    if f(a) * f(x0) < 0:
        b = x0
    else:
        a = x0

    error = abs(a - b)

x = (a + b) / 2.0
print("root2:", x)