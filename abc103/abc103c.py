from fractions import gcd
from functools import reduce
def lcm(x, y):
  return (x * y) // gcd(x, y)
n = int(input())
a = list(map(int, input().split()))
t = reduce(lcm, a, 1) - 1
print(sum(t % a[i] for i in range(n)))
