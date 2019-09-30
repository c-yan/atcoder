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
ab = [[int(c) - 1 for c in input().split()] for _ in range(M)]

result = 0
for i in range(M):
    parent = [-1] * N
    for j in range(M):
        if j == i:
            continue
        unite(parent, ab[j][0], ab[j][1])
    if len([i for i in parent if i < 0]) != -1:
        result += 1
print(result)
