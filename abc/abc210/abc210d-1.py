from sys import stdin

readline = stdin.readline

H, W, C = map(int, readline().split())
A = [list(map(int, readline().split())) for _ in range(H)]

result = 10 ** 15

dp = [A[i][:] for i in range(H)]
for i in range(H):
    for j in range(W):
        if i != 0:
            result = min(result, dp[i][j] + dp[i - 1][j] + C)
        if j != 0:
            result = min(result, dp[i][j] + dp[i][j - 1] + C)
        if i != 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + C)
        if j != 0:
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + C)

dp = [A[i][:] for i in range(H)]
for i in range(H):
    for j in range(W - 1, -1, -1):
        if i != 0:
            result = min(result, dp[i][j] + dp[i - 1][j] + C)
        if j != W - 1:
            result = min(result, dp[i][j] + dp[i][j + 1] + C)
        if i != 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + C)
        if j != W - 1:
            dp[i][j] = min(dp[i][j], dp[i][j + 1] + C)

print(result)
