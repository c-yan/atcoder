m = 1000000007

N, L = map(int, input().split())

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
    dp[i + 1] += dp[i]
    dp[i + 1] %= m
    if i + L <= N:
        dp[i + L] += dp[i]
        dp[i + L] %= m
print(dp[N])
