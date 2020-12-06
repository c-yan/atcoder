from math import gcd
from functools import reduce


def lcm(x, y):
    return x // gcd(x, y) * y


N = int(input())

print(reduce(lcm, range(1, N + 1)) + 1)
