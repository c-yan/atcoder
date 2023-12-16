# DP(貰うDP)
N, K, *h = map(int, open(0).read().split())

dp = [0] * N
for i in range(1, N):
    dp[i] = min(dp[j] + abs(h[i] - h[j]) for j in range(max(0, i - K), i))
print(dp[N - 1])
