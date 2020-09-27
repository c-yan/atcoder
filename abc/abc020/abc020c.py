from collections import deque


def f(c):
    for i in range(H):
        for j in range(W):
            if s[i][j] == c:
                return i, j


def g(x, sy, sx, gy, gx):
    t = [[float('inf')] * W for _ in range(H)]

    q = deque([(sy, sx)])
    t[sy][sx] = 0
    while q:
        i, j = q.popleft()
        if i > 0:
            c = None
            if s[i - 1][j] in ['.', 'S', 'G']:
                c = 1
            elif s[i - 1][j] == '#':
                c = x
            if t[i - 1][j] > t[i][j] + c:
                t[i - 1][j] = t[i][j] + c
                q.append((i - 1, j))
        if i < H - 1:
            c = None
            if s[i + 1][j] in ['.', 'S', 'G']:
                c = 1
            elif s[i + 1][j] == '#':
                c = x
            if t[i + 1][j] > t[i][j] + c:
                t[i + 1][j] = t[i][j] + c
                q.append((i + 1, j))
        if j > 0:
            c = None
            if s[i][j - 1] in ['.', 'S', 'G']:
                c = 1
            elif s[i][j - 1] == '#':
                c = x
            if t[i][j - 1] > t[i][j] + c:
                t[i][j - 1] = t[i][j] + c
                q.append((i, j - 1))
        if j < W - 1:
            c = None
            if s[i][j + 1] in ['.', 'S', 'G']:
                c = 1
            elif s[i][j + 1] == '#':
                c = x
            if t[i][j + 1] > t[i][j] + c:
                t[i][j + 1] = t[i][j] + c
                q.append((i, j + 1))
    return t[gy][gx]


T_max = 10 ** 9

H, W, T = map(int, input().split())
s = [input() for _ in range(H)]

sy, sx = f('S')
gy, gx = f('G')

ok = 0
ng = T_max + 1
while ng - ok > 1:
    m = (ok + ng) // 2
    if g(m, sy, sx, gy, gx) <= T:
        ok = m
    else:
        ng = m
print(ok)
