from sys import stdin
from collections import deque

readline = stdin.readline

N = int(readline())
ab = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in range(N - 1)]

links = [[] for _ in range(N)]
for a, b in ab:
    links[a].append(b)
    links[b].append(a)

parent = [-1] * N
parent[0] = 0
q = deque([0])
while q:
    i = q.popleft()
    for j in links[i]:
        if parent[j] != -1:
            continue
        parent[j] = i
        q.append(j)

c = [0] * N
Q = int(readline())
for _ in range(Q):
    t, e, x = map(int, readline().split())
    a, b = ab[e - 1]
    if t == 2:
        a, b = b, a
    if a == parent[b]:
        c[0] += x
        c[b] -= x
    else:
        c[a] += x

q = deque([0])
while q:
    i = q.popleft()
    for j in links[i]:
        if j == parent[i]:
            continue
        c[j] += c[i]
        q.append(j)

print(*c, sep='\n')
