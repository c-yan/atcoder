from sys import stdin
from collections import deque

readline = stdin.readline

N = int(readline())
ab = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in range(N - 1)]

links = [[] for _ in range(N)]
for a, b in ab:
    links[a].append(b)
    links[b].append(a)

depth = [-1] * N
depth[0] = 0
q = deque([0])
while q:
    i = q.popleft()
    for j in links[i]:
        if depth[j] != -1:
            continue
        depth[j] = depth[i] + 1
        q.append(j)

c = [0] * N
Q = int(readline())
for _ in range(Q):
    t, e, x = map(int, readline().split())
    a, b = ab[e - 1]
    if t == 2:
        a, b = b, a
    if depth[a] < depth[b]:
        c[0] += x
        c[b] -= x
    else:
        c[a] += x

q = deque([0])
while q:
    i = q.popleft()
    for j in links[i]:
        if depth[j] < depth[i]:
            continue
        c[j] += c[i]
        q.append(j)

print(*c, sep='\n')
