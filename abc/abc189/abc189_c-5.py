from sys import setrecursionlimit
from operator import itemgetter


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

result = 0
parent = [-1] * (N + 1)
for i, _ in sorted(enumerate(A), reverse=True, key=itemgetter(1)):
    for j in [i - 1, i + 1]:
        if j < 0 or j >= N:
            continue
        if A[j] < A[i]:
            continue
        unite(parent, i, j)
    result = max(result, A[i] * -parent[find(parent, i)])
print(result)
