# Union Find 木
from sys import setrecursionlimit, stdin


def find(parent, diff_weight, i):
    t = parent[i]
    if t < 0:
        return i
    t = find(parent, diff_weight, t)
    diff_weight[i] += diff_weight[parent[i]]
    parent[i] = t
    return t


def weight(parent, diff_weight, i):
    find(parent, diff_weight, i)
    return diff_weight[i]


def unite(parent, diff_weight, i, j, d):
    d -= weight(parent, diff_weight, j)
    d += weight(parent, diff_weight, i)
    i = find(parent, diff_weight, i)
    j = find(parent, diff_weight, j)
    if i == j:
        return
    diff_weight[j] = d
    parent[i] += parent[j]
    parent[j] = i


setrecursionlimit(10 ** 6)

N, M = map(int, stdin.readline().split())
LRD = [tuple(map(int, stdin.readline().split())) for _ in range(M)]

parent = [-1] * (N + 1)
diff_weight = [0] * (N + 1)
for L, R, D in LRD:
    i = find(parent, diff_weight, L)
    j = find(parent, diff_weight, R)
    if i != j:
        unite(parent, diff_weight, L, R, D)
    else:
        if weight(parent, diff_weight, L) + D != weight(parent, diff_weight, R):
            print('No')
            exit()
print('Yes')
