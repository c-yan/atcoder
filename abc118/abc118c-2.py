from functools import reduce
from fractions import gcd

N = int(input())
A = list(map(int, input().split()))

print(reduce(gcd, A))
