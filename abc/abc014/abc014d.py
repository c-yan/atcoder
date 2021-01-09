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
max_depth = max(depth)

p = [None] * N
p[0] = 0
for i in range(1, N):
    d = depth[i]
    for j in links[i]:
        if depth[j] < d:
            p[i] = j
            break
parent = {}
parent[1] = p
i = 2
while i <= max_depth:
    p = parent[i // 2]
    t = [None] * N
    for j in range(N):
        t[j] = p[p[j]]
    parent[i] = t
    i *= 2

result = []
Q = int(readline())
for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, readline().split())
    t = 1
    if depth[b] > depth[a]:
        a, b = b, a
    x = depth[a] - depth[b]
    t += x
    i = 1
    while x != 0:
        if x & i != 0:
            a = parent[i][a]
            x -= i
        i *= 2
    ok = depth[a]
    ng = -1
    while ok - ng > 1:
        m = ng + (ok - ng) // 2
        n = m
        x, y = a, b
        i = 1
        while n != 0:
            if n & i != 0:
                x = parent[i][x]
                y = parent[i][y]
                n -= i
            i *= 2
        if x == y:
            ok = m
        else:
            ng = m
    t += ok * 2
    result.append(t)
print(*result, sep='\n')
