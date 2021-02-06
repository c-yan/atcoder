from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline
INF = 10 ** 16

N, M = map(int, readline().split())
links = [{} for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, readline().split())
    if B - 1 in links[A - 1]:
        links[A - 1][B - 1] = min(links[A - 1][B - 1], C)
    else:
        links[A - 1][B - 1] = C

dp = [[INF] * N for _ in range(N)]
for i in range(N):
    t = dp[i]
    q = [(0, i)]
    while q:
        c, j = heappop(q)
        link = links[j]
        if t[j] < c:
            continue
        for k in link:
            if t[k] > c + link[k]:
                t[k] = c + link[k]
                heappush(q, (c + link[k], k))

result = [dp[i][i] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        result[j] = min(result[j], dp[j][i] + dp[i][j])

for i in range(N):
    if result[i] == INF:
        result[i] = -1
print(*result, sep='\n')
