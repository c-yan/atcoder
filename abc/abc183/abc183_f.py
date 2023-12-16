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


def merge(a, b):
    if len(a) < len(b):
        a, b = b, a
    for k in b:
        if k in a:
            a[k] += b[k]
        else:
            a[k] = b[k]
    return a


setrecursionlimit(10 ** 6)
readline = stdin.readline

N, Q = map(int, readline().split())
C = list(map(lambda x: int(x) - 1, readline().split()))

parent = [-1] * N
breakdown = [{C[i]: 1} for i in range(N)]
result = []
for _ in range(Q):
    Query = list(map(int, readline().split()))
    if Query[0] == 1:
        a, b = Query[1] - 1, Query[2] - 1
        i = find(parent, a)
        j = find(parent, b)
        if i == j:
            continue
        unite(parent, a, b)
        breakdown[find(parent, a)] = merge(breakdown[i], breakdown[j])
    elif Query[0] == 2:
        x, y = Query[1] - 1, Query[2] - 1
        b = breakdown[find(parent, x)]
        if y in b:
            result.append(b[y])
        else:
            result.append(0)
print(*result, sep='\n')
