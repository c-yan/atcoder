# 幅優先探索
from sys import stdin
from collections import deque

readline = stdin.readline
INF = 10 ** 20

N = int(readline())
links = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, readline().split())
    links[a - 1].append((b - 1, c))
    links[b - 1].append((a - 1, c))

Q, K = map(int, readline().split())

d = [INF] * N
d[K - 1] = 0
q = deque([K - 1])
while q:
    i = q.popleft()
    for j, c in links[i]:
        if d[i] + c < d[j]:
            d[j] = d[i] + c
            q.append(j)

result = []
for _ in range(Q):
    x, y = map(int, readline().split())
    result.append(d[x - 1] + d[y - 1])
print(*result, sep='\n')
