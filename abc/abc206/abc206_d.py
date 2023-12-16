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

N, *A = map(int, open(0).read().split())

ma = max(A)

parent = [-1] * (ma + 1)
for i in range(N // 2):
    unite(parent, A[i], A[N - 1 - i])

result = 0
for i in range(ma + 1):
    if parent[i] > 0:
        continue
    result += -parent[i] - 1
print(result)
