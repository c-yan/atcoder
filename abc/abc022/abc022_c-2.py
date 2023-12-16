from sys import stdin
from itertools import combinations
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

readline = stdin.readline
INF = float('inf')

N, M = map(int, readline().split())

g = [[0] * N for _ in range(N)]
from0 = {}
for _ in range(M):
    u, v, l = map(int, readline().split())
    u, v = u - 1, v - 1
    if u == 0:
        from0[v] = l
    elif v == 0:
        from0[u] = l
    else:
        g[u][v] = l
        g[v][u] = l
g = floyd_warshall(csgraph_from_dense(g))

result = INF
for i, j in combinations(from0, 2):
    if g[i][j] == INF:
        continue
    result = min(result, int(g[i][j]) + from0[i] + from0[j])
if result == INF:
    print(-1)
else:
    print(result)
