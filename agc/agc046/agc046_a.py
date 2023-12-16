from math import gcd

X = int(input())


def lcm(x, y):
    return x // gcd(x, y) * y


print(lcm(X, 360) // X)
