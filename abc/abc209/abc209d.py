from collections import deque
from sys import stdin

readline = stdin.readline

INF = 10 ** 15

N, Q = map(int, readline().split())

links = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, readline().split())
    links[a].append(b)
    links[b].append(a)

dp = [INF] * N
dp[0] = 0
q = deque([0])
while q:
    a = q.popleft()
    for b in links[a]:
        if dp[b] <= dp[a] + 1:
            continue
        dp[b] = dp[a] + 1
        q.append(b)

result = []
for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, readline().split())
    if (dp[c] + dp[d]) % 2 == 0:
        result.append('Town')
    else:
        result.append('Road')
print(*result, sep='\n')
