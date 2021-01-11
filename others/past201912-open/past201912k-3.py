from math import log
from collections import deque
from sys import stdin

readline = stdin.readline

N = int(readline())

root = -1
children = [[] for _ in range(N + 1)]
parent = [[-1] * (N + 1) for _ in range(18)]
for i in range(1, N + 1):
    p = int(readline())
    parent[0][i] = p
    if p == -1:
        root = i
    else:
        children[p].append(i)

for i in range(1, 18):
    parenti1 = parent[i - 1]
    parenti = parent[i]
    for j in range(1, N + 1):
        t = parenti1[j]
        if t == -1:
            parenti[j] = -1
        else:
            parenti[j] = parenti1[t]

depth = [-1] * (N + 1)
q = deque([(root, 0)])
while q:
    n, d = q.pop()
    depth[n] = d
    for c in children[n]:
        q.append((c, d + 1))

Q = int(input())
result = []
for _ in range(Q):
    a, b = map(int, readline().split())
    if depth[a] <= depth[b]:
        result.append('No')
        continue
    while depth[a] != depth[b]:
        t = int(log(depth[a] - depth[b], 2))
        a = parent[t][a]
    if a == b:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
