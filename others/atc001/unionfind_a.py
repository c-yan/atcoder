# Union Find 木
def find(parent, i):
    t = parent[i]
    if t == -1:
        return i
    t = find(parent, t)
    parent[i] = t
    return t

def unite(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
        return
    parent[i] = j

N, Q = map(int, input().split())
parent = [-1] * N

for _ in range(Q):
    P, A, B = map(int, input().split())
    if P == 0:
        unite(parent, A, B)
    else:
        if find(parent, A) == find(parent, B):
            print('Yes')
        else:
            print('No')
