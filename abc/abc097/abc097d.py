# Union Find 木
from sys import setrecursionlimit


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


setrecursionlimit(10 ** 5)


N, M = map(int, input().split())
p = list(map(int, input().split()))

parent = [-1] * N
for _ in range(M):
    x, y = map(int, input().split())
    unite(parent, x - 1, y - 1)

result = 0
for i in range(N):
    if find(parent, i) == find(parent, p[i] - 1):
        result += 1
print(result)
