from math import gcd
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

x = reduce(gcd, A)
result = 0
while True:
    if x % 2 == 1:
        break
    result += 1
    x //= 2
print(result)
