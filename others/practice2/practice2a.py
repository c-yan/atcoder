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

N, Q = map(int, readline().split())

parent = [-1] * (N + 1)
result = []
for _ in range(Q):
    t, u, v = map(int, readline().split())
    if t == 0:
        unite(parent, u, v)
    elif t == 1:
        if find(parent, u) == find(parent, v):
            result.append(1)
        else:
            result.append(0)

print(*result, sep='\n')
