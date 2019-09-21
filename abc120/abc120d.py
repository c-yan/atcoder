# Union Find 木
import sys
sys.setrecursionlimit(10 ** 5)


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


n, m = map(int, input().split())
parent = [-1] * n
inconvenience = n * (n - 1) // 2
result = []
for a, b in reversed([[int(c) - 1 for c in input().split()] for _ in range(m)]):
    result.append(inconvenience)
    pa, pb = find(parent, a), find(parent, b)
    if pa != pb:
        inconvenience -= parent[pa] * parent[pb]
    unite(parent, a, b)
for i in reversed(result):
    print(i)
