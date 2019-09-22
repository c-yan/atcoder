# DP(配るDP)
N = int(input())
h = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0
for i in range(N - 2):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
    dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i + 2] - h[i]))
dp[N - 1] = min(dp[N - 1], dp[N - 2] + abs(h[N - 1] - h[N - 2]))
print(dp[N - 1])
