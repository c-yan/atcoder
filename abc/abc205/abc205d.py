from sys import stdin

readline = stdin.readline

N, Q = map(int, readline().split())
A = list(map(int, readline().split()))

result = []
for _ in range(Q):
    K = int(readline())
    ok = 0
    ng = N + 1
    while ng - ok > 1:
        m = ok + (ng - ok) // 2
        if A[m - 1] - m < K:
            ok = m
        else:
            ng = m
    result.append(K + ok)
print(*result, sep='\n')
