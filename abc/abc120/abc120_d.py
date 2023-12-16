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


setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
AB = [[int(c) - 1 for c in input().split()] for _ in range(M)]

parent = [-1] * N
inconvenience = N * (N - 1) // 2
result = []
for a, b in AB[::-1]:
    result.append(inconvenience)
    pa, pb = find(parent, a), find(parent, b)
    if pa != pb:
        inconvenience -= parent[pa] * parent[pb]
    unite(parent, a, b)
print(*result[::-1])
