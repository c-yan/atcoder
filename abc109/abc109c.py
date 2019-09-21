from sys import stdin
from fractions import gcd
from functools import reduce
n, x, *xs = map(int, stdin.read().split())
print(reduce(gcd, [abs(xs[i] - x) for i in range(n)]))
