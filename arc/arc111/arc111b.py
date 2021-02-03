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

parent = [-1] * 400000
edges = [0] * 400000
for _ in range(N):
    a, b = map(lambda x: int(x) - 1, readline().split())
    i, j = find(parent, a), find(parent, b)
    if i == j:
        edges[i] += 1
        continue
    unite(parent, a, b)
    k = find(parent, a)
    if k == i:
        edges[i] += edges[j] + 1
    elif k == j:
        edges[j] += edges[i] + 1

result = 0
for i in [i for i in range(400000) if parent[i] < 0]:
    if edges[i] >= -parent[i]:
        result += -parent[i]
    else:
        result += -(parent[i] + 1)
print(result)
