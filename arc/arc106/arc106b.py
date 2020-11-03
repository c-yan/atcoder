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
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))

parent = [-1] * N
for _ in range(M):
    c, d = map(lambda x: int(x) - 1, readline().split())
    unite(parent, c, d)

ca = {}
cb = {}
for i in range(N):
    j = find(parent, i)
    ca.setdefault(j ,0)
    ca[j] += a[i]
    cb.setdefault(j ,0)
    cb[j] += b[i]

for k in ca:
    if ca[k] == cb[k]:
        continue
    print('No')
    break
else:
    print('Yes')
