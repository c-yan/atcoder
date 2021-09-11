from sys import setrecursionlimit, stdin


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


readline = stdin.readline
setrecursionlimit(10 ** 6)

N, M = map(int, readline().split())
ABC = [list(map(int, readline().split())) for _ in range(M)]

parent = [-1] * (N + 1)

result = 0
for a, b, c in sorted(ABC, key=lambda x: x[2]):
    if c > 0 and find(parent, a) == find(parent, b):
        result += c
        continue
    unite(parent, a, b)
print(result)
