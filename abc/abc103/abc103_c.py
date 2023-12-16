from fractions import gcd
from functools import reduce


def lcm(x, y):
    return x // gcd(x, y) * y


N = int(input())
a = list(map(int, input().split()))

t = reduce(lcm, a, 1) - 1
print(sum(t % a[i] for i in range(N)))
