def f(x):
    y = x**5 - 3*x**4 - 5*x**3 + x**2 + x + 3 #주어진 함수
    return y


def df(x):
    y = 5*x**4 - 12*x**3 - 15*x**2 + 2*x + 1 #f(x)의 미분
    return y


accuracy = 1e-12

# 주어진 함수가 구간 안에서 두 개의 해를 가진다
# 첫 번째 초기값 [-2, 0]
x = -2.0
error = 1.0

while abs(error) > accuracy:
    error = f(x) / df(x)
    x -= error

print("root1:", x)

# 두 번째 구간 [0, 4] 근처
x = 1.0
error = 1.0

while abs(error) > accuracy:
    error = f(x) / df(x)
    x -= error

print("root2:", x)