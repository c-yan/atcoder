from fractions import gcd
from functools import reduce

N, X = map(int, input().split())
x = list(map(int, input().split()))

print(reduce(gcd, [abs(x[i] - X) for i in range(N)]))
