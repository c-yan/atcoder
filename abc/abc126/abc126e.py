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

parent = [-1] * N
for _ in range(M):
    X, Y, Z = map(int, input().split())
    unite(parent, X - 1, Y - 1)
print(len([x for x in parent if x < 0]))
