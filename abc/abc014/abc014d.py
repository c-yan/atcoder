from sys import stdin

readline = stdin.readline

N = int(readline())
links = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(lambda x: int(x) - 1, readline().split())
    links[x].append(y)
    links[y].append(x)

depth = [None] * N
depth[0] = 0
q = [0]
while q:
    i = q.pop()
    d = depth[i]
    for j in links[i]:
        if depth[j] is not None:
            continue
        depth[j] = d + 1
        q.append(j)

a = [None] * N
a[0] = 0
for i in range(1, N):
    d = depth[i]
    for j in links[i]:
        if depth[j] < d:
            a[i] = j
            break


def do_doubling(a, n):
    l = len(a)
    result = {1: a}
    x = 2
    while x <= n:
        a = [a[a[i]] for i in range(l)]
        result[x] = a
        x *= 2
    return result


# get_nth_ancestor
def get_na(a, n):
    x = 1
    while n != 0:
        if n & x != 0:
            a = ansestor[x][a]
            n -= x
        x *= 2
    return a


# get_lowest_common_ancestor
def get_lca(a, b):
    if depth[b] > depth[a]:
        a, b = b, a
    a = get_na(a, depth[a] - depth[b])
    if a == b:
        return a
    ok = depth[a]
    ng = 0
    while ok - ng > 1:
        m = ng + (ok - ng) // 2
        if get_na(a, m) == get_na(b, m):
            ok = m
        else:
            ng = m
    return get_na(a, ok)


ansestor = do_doubling(a, max(depth))

result = []
Q = int(readline())
for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, readline().split())
    c = get_lca(a, b)
    result.append(depth[a] + depth[b] - 2 * depth[c] + 1)
print(*result, sep='\n')
