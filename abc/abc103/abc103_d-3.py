# DP
from sys import stdin
readline = stdin.readline

N, M = map(int, readline().split())

ab = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, readline().split())
    ab[a].append(b)

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])
    for j in ab[i]:
        dp[j] = max(dp[j], dp[i] + 1)

print(dp[N])
