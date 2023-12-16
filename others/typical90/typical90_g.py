from sys import stdin
from bisect import bisect_left

readline = stdin.readline

N = int(readline())
A = list(map(int, readline().split()))
Q = int(readline())

A.sort()

result = []
for _ in range(Q):
    B = int(readline())
    i = bisect_left(A, B)
    if i == 0:
        result.append(abs(A[0] - B))
    elif i == N:
        result.append(abs(A[N - 1] - B))
    else:
        result.append(min(abs(A[i] - B), abs(A[i - 1] - B)))
print(*result, sep='\n')
