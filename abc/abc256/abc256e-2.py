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

N = int(input())
X = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))

parent = [-1] * N
result = 0
for c, i in sorted(zip(C, range(N)), reverse=True):
    if find(parent, i) != find(parent, X[i]):
        unite(parent, i, X[i])
    else:
        result += c
print(result)
