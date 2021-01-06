# ダイクストラ法
from sys import stdin
from heapq import heappop, heappush

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
#prev = [None] * N
q = [(0, K - 1)]
while q:
    c, a = heappop(q)
    if d[a] != c:
        continue
    for b, c in links[a]:
        nc = d[a] + c
        if d[b] > nc:
            d[b] = nc
            #prev[b] = a
            heappush(q, (nc, b))

result = []
for _ in range(Q):
    x, y = map(int, readline().split())
    result.append(d[x - 1] + d[y - 1])
print(*result, sep='\n')
