from functools import reduce
from fractions import gcd

N, K = map(int, input().split())
A = set(map(int, input().split()))

if K in A:
    print('POSSIBLE')
    exit()

if K > max(A):
    print('IMPOSSIBLE')
    exit()

g = reduce(gcd, A)

if g == 1:
    print('POSSIBLE')
    exit()

for a in A:
    if K > a:
        continue
    if (a - K) % g == 0:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')
