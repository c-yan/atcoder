from sys import setrecursionlimit, stdin


def find(parent, i):
    t = parent[i]
    if t < 0:
        return i
    t = find(parent, t)
    parent[i] = t
    return t


def unite(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
        return
    parent[j] += parent[i]
    parent[i] = j


readline = stdin.readline
setrecursionlimit(10 ** 6)


def intersect(c1, c2):
    (x1, y1, r1), (x2, y2, r2) = c1, c2
    d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    return d >= (r1 - r2) * (r1 - r2) and d <= (r1 + r2) * (r1 + r2)


def on_circle(x1, y1, c):
    x2, y2, r = c
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) == r * r


N = int(readline())
sx, sy, tx, ty = map(int, readline().split())
xyr = [list(map(int, readline().split())) for _ in range(N)]

parent = [-1] * (N + 1)

for i in range(N - 1):
    for j in range(i + 1, N):
        if intersect(xyr[i], xyr[j]):
            unite(parent, i, j)

for i in range(N):
    if on_circle(sx, sy, xyr[i]):
        a = i
    if on_circle(tx, ty, xyr[i]):
        b = i

if find(parent, a) == find(parent, b):
    print('Yes')
else:
    print('No')
