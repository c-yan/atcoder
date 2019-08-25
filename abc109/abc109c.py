from sys import stdin
from fractions import gcd
n, x, *xs = map(int, stdin.read().split())
result = abs(xs[0] - x)
for i in range(1, n):
  result = gcd(result, abs(xs[i] - x))
print(result)
