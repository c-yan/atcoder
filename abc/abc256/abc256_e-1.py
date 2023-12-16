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
for i in range(N):
    unite(parent, i, X[i])
roots = [i for i in range(N) if parent[i] < 0]

result = 0
for r in roots:
    used = {r}
    i = X[r]
    while i not in used:
        used.add(i)
        i = X[i]

    t = [C[i]]
    used = {i}
    i = X[i]
    while i not in used:
        t.append(C[i])
        used.add(i)
        i = X[i]
    result += min(t)
print(result)
