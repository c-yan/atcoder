from fractions import gcd
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

m = 1000000007

lcm = reduce(lambda a, b: a * b // gcd(a, b), A)
print(sum(lcm // a for a in A) % m)
