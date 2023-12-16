# ワーシャルフロイド
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

N, M = map(int, input().split())

g = [[0] * N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A - 1][B - 1] = 1
    g[B - 1][A - 1] = 1
g = floyd_warshall(csgraph_from_dense(g))

for i in range(N):
    print(len([j for j in g[i] if j == 2]))
