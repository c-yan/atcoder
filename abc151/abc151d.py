# 幅優先探索
H, W = map(int, input().split())
S = [input() for _ in range(H)]


def f(i, j):
    t = [[-1] * W for _ in range(H)]
    t[i][j] = 0
    q = [(i, j)]
    while q:
        y, x = q.pop(0)
        if y - 1 >= 0 and S[y - 1][x] != '#' and t[y - 1][x] == -1:
            t[y - 1][x] = t[y][x] + 1
            q.append((y - 1, x))
        if y + 1 < H and S[y + 1][x] != '#' and t[y + 1][x] == -1:
            t[y + 1][x] = t[y][x] + 1
            q.append((y + 1, x))
        if x - 1 >= 0 and S[y][x - 1] != '#' and t[y][x - 1] == -1:
            t[y][x - 1] = t[y][x] + 1
            q.append((y, x - 1))
        if x + 1 < W and S[y][x + 1] != '#' and t[y][x + 1] == -1:
            t[y][x + 1] = t[y][x] + 1
            q.append((y, x + 1))
    return max(max(tt) for tt in t)


result = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            result = max(result, f(i, j))
print(result)
