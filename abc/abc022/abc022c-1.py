from sys import stdin
from itertools import combinations

readline = stdin.readline
INF = 10 ** 18


def warshall_floyd(n, d):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])


N, M = map(int, readline().split())

d = [[INF] * N for _ in range(N)]
for k in range(N):
    d[k][k] = 0
from0 = {}
for _ in range(M):
    u, v, l = map(int, readline().split())
    u, v = u - 1, v - 1
    if u == 0:
        from0[v] = l
    elif v == 0:
        from0[u] = l
    else:
        d[u][v] = l
        d[v][u] = l
warshall_floyd(N, d)

result = INF
for i, j in combinations(from0, 2):
    if d[i][j] == INF:
        continue
    result = min(result, d[i][j] + from0[i] + from0[j])
if result == INF:
    print(-1)
else:
    print(result)
