from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from itertools import permutations

N, M, R = map(int, input().split())
r = list(map(int, input().split()))

g = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    g[A][B] = C
    g[B][A] = C
g = floyd_warshall(csgraph_from_dense(g))

result = 1000000000
for p in permutations(r):
    t = 0
    for i in range(R - 1):
        t += g[p[i]][p[i + 1]]
    result = min(result, t)
print(int(result))
