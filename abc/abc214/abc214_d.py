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

N = int(readline())
uvw = [tuple(map(int, readline().split())) for _ in range(N - 1)]

result = 0
parent = [-1] * (N + 1)
for u, v, w in sorted(uvw, key=lambda x: x[2]):
    x = -parent[find(parent, u)]
    y = -parent[find(parent, v)]
    result += x * y * w
    unite(parent, x, y)
print(result)
