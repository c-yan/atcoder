# PyPy なら通る
# DP(配るDP)
N, K, *h = map(int, open(0).read().split())

dp = [float('inf')] * N
dp[0] = 0
for i in range(N - 1):
    for j in range(1, K + 1):
        if i + j > N - 1:
            break
        dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))
print(dp[N - 1])
