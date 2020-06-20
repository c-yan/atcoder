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
roads = []
for _ in range(M):
    a, b, y = map(int, input().split())
    roads.append((y, a - 1, b - 1))
Q = int(input())
citizen = []
for i in range(Q):
    v, w = map(int, input().split())
    citizen.append((w, v - 1, i))

parent = [-1] * N

roads.sort(reverse=True)

results = [None] * Q
t = 0
for c in sorted(citizen, reverse=True):
    while t < M and roads[t][0] > c[0]:
        unite(parent, find(parent, roads[t][1]), find(parent, roads[t][2]))
        t += 1
    results[c[2]] = -parent[find(parent, c[1])]
print(*results, sep='\n')
