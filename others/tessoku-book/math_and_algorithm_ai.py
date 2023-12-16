from sys import stdin
from itertools import accumulate

readline = stdin.readline

N, Q = map(int, readline().split())
A = list(map(int, readline().split()))

a = list(accumulate(A))
result = []
for _ in range(Q):
    L, R = map(int, readline().split())
    if L == 1:
        result.append(a[R - 1])
    else:
        result.append(a[R - 1] - a[L - 2])
print(*result, sep='\n')
