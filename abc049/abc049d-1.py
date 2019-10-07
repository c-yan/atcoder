# Union Find 木
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


N, K, L = map(int, input().split())

roads = [-1] * N
rails = [-1] * N

for i in range(K):
    p, q = map(int, input().split())
    unite(roads, p - 1, q - 1)

for i in range(L):
    r, s = map(int, input().split())
    unite(rails, r - 1, s - 1)

d = {}
for i in range(N):
    t = (find(roads, i), find(rails, i))
    if t in d:
        d[t] += 1
    else:
        d[t] = 1

print(*[d[(find(roads, i), find(rails, i))] for i in range(N)])
