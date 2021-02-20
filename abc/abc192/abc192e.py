from sys import stdin
from heapq import heappop, heappush

readline = stdin.readline
INF = 10 ** 18

N, M, X, Y = map(int, readline().split())

links = [{} for _ in range(N)]
for _ in range(M):
    A, B, T, K = map(int, readline().split())
    links[A - 1].setdefault(B - 1, [])
    links[B - 1].setdefault(A - 1, [])
    links[A - 1][B - 1].append((T, K))
    links[B - 1][A - 1].append((T, K))

dp = [INF] * N
dp[X - 1] = 0
q = [(0, X - 1)]
while len(q) != 0:
    n, i = heappop(q)
    link = links[i]
    for j in link:
        for t, k in link[j]:
            d = (n + k - 1) // k * k
            if d + t >= dp[j]:
                continue
            dp[j] = d + t
            heappush(q, (d + t, j))

if dp[Y - 1] == INF:
    print(-1)
else:
    print(dp[Y - 1])
