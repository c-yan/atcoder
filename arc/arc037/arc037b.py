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

N, M = map(int, readline().split())

parent = [-1] * N
cycle = set()
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, readline().split())
    a = find(parent, u)
    b = find(parent, v)
    if a == b:
        cycle.add(a)
    unite(parent, u, v)
c = {i for i in range(N) if parent[i] < 0}
d = {find(parent, i) for i in cycle}
print(len(c - d))
