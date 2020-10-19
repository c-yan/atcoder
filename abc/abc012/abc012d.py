from sys import stdin
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

readline = stdin.readline

N, M = map(int, readline().split())
g = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, readline().split())
    g[a - 1][b - 1] = t
    g[b - 1][a - 1] = t
g = floyd_warshall(csgraph_from_dense(g))
print(int(min(max(x) for x in g)))
