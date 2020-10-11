from math import gcd
from functools import reduce

N, *a = map(int, open(0).read().split())

print(reduce(gcd, a))
