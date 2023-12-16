# ワーシャルフロイド
# PyPy なら通る
def warshall_floyd(n, d):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])


INF = float('inf')

H, W = map(int, input().split())
S = [input() for _ in range(H)]

N = H * W
d = [[INF] * N for _ in range(N)]
for k in range(N):
    d[k][k] = 0

for y in range(H):
    for x in range(W):
        if S[y][x] == '#':
            continue
        if y - 1 >= 0 and S[y - 1][x] != '#':
            d[y * W + x][(y - 1) * W + x] = 1
        if y + 1 < H and S[y + 1][x] != '#':
            d[y * W + x][(y + 1) * W + x] = 1
        if x - 1 >= 0 and S[y][x - 1] != '#':
            d[y * W + x][y * W + x - 1] = 1
        if x + 1 < W and S[y][x + 1] != '#':
            d[y * W + x][y * W + x + 1] = 1

warshall_floyd(N, d)

result = 0
for i in range(N):
    for j in range(N):
        if d[i][j] != INF and d[i][j] > result:
            result = d[i][j]
print(result)
