from functools import reduce
from fractions import gcd

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K > max(A):
    print('IMPOSSIBLE')
    exit()

if A.count(K) != 0:
    print('POSSIBLE')
    exit()

g = reduce(gcd, A)
for a in A:
    if K > a:
        continue
    if (a - K) % g == 0:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')
