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


N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

parent = [-1] * N
friends = [[] for _ in range(N)]
for A, B in AB:
    unite(parent, A - 1, B - 1)
    friends[A-1].append(B-1)
    friends[B-1].append(A-1)
blocks = [[] for _ in range(N)]
for C, D in CD:
    blocks[C-1].append(D-1)
    blocks[D-1].append(C-1)

result = []
for i in range(N):
    p = find(parent, i)
    t = -parent[p] - 1
    t -= len(friends[i])
    for b in blocks[i]:
        if p == find(parent, b):
            t -= 1
    result.append(t)
print(*result)
