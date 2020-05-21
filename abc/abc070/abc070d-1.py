# ダイクストラ法
from heapq import heappop, heappush

N = int(input())
links = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    links[a].append((b, c))
    links[b].append((a, c))

Q, K = map(int, input().split())

d = [float('inf')] * (N + 1)
d[K] = 0
#prev = [None] * (N + 1)
q = [(0, K)]
while q:
    _, u = heappop(q)
    for v, c in links[u]:
        alt = d[u] + c
        if d[v] > alt:
            d[v] = alt
            #prev[v] = u
            heappush(q, (alt, v))

result = []
for _ in range(Q):
    x, y = map(int, input().split())
    result.append(d[x] + d[y])
print('\n'.join(str(v) for v in result))
