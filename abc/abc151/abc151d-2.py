# ワーシャルフロイド
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

H, W = map(int, input().split())
S = [input() for _ in range(H)]

g = [[0] * (H * W) for _ in range(H * W)]
for y in range(H):
    for x in range(W):
        if S[y][x] == '#':
            continue
        if y - 1 >= 0 and S[y - 1][x] != '#':
            g[y * W + x][(y - 1) * W + x] = 1
        if y + 1 < H and S[y + 1][x] != '#':
            g[y * W + x][(y + 1) * W + x] = 1
        if x - 1 >= 0 and S[y][x - 1] != '#':
            g[y * W + x][y * W + x - 1] = 1
        if x + 1 < W and S[y][x + 1] != '#':
            g[y * W + x][y * W + x + 1] = 1
g = floyd_warshall(csgraph_from_dense(g))

result = 0
for i in range(H * W):
    for j in range(H * W):
        if g[i][j] == 0:
            continue
        result = max(result, g[i][j])
print(int(result))
