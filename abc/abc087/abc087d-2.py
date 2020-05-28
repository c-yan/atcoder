# Union Find 木
from sys import setrecursionlimit


def find(parent, i):
    t = parent[i]
    if t < 0:
        return i
    t = find(parent, t)
    parent[i] = t
    return t


def pos(x, i):
    j, k = x[i]
    if i == j:
        return i, 0
    l, m = pos(x, j)
    x[i] = (l, m + k)
    return x[i]


setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
LRD = [tuple(map(int, input().split())) for _ in range(M)]

parent = [-1] * (N + 1)
x = [(i, 0) for i in range(N + 1)]
for L, R, D in LRD:
    i = find(parent, L)
    j = find(parent, R)
    if i != j:
        x[j] = (i, D - pos(x, R)[1] + pos(x, L)[1])
        parent[i] += parent[j]
        parent[j] = i
    else:
        if pos(x, L)[1] + D != pos(x, R)[1]:
            print('No')
            exit()
print('Yes')
