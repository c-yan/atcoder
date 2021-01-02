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
    if t == 1:
        if a == 0 or parent[b] == a:
            c[0] += x
            c[b] -= x
        else:
            c[a] += x
    elif t == 2:
        if b == 0 or parent[a] == b:
            c[0] += x
            c[a] -= x
        else:
            c[b] += x

q = deque([0])
while q:
    i = q.popleft()
    for j in links[i]:
        if j == parent[i]:
            continue
        c[j] += c[i]
        q.append(j)

print(*c, sep='\n')
