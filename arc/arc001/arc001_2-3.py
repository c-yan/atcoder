# ワーシャルフロイド
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

A, B = map(int, input().split())

g = [[0] * (40 + 1) for _ in range(40 + 1)]
for i in range(40):
    for j in [1, 5, 10]:
        if 0 <= i + j <= 40:
            g[i][i + j] = 1
            g[i+j][i] = 1
        if 0 <= i - j <= 40:
            g[i][i - j] = 1
            g[i-j][i] = 1
print(floyd_warshall(csgraph_from_dense(g))[A][B])
