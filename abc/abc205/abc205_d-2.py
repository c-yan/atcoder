from sys import stdin
from bisect import bisect_left

readline = stdin.readline

N, Q = map(int, readline().split())
A = list(map(int, readline().split()))

result = []
for _ in range(Q):
    K = int(readline())
    ok = K
    ng = K + N + 1
    while ng - ok > 1:
        m = ok + (ng - ok) // 2
        if m - bisect_left(A, m) <= K:
            ok = m
        else:
            ng = m
    result.append(ok)
print(*result, sep='\n')
