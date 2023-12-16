# 配るDP
H, W = map(int, input().split())
a = [input() for _ in range(H)]

m = 1000000007

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for h in range(H - 1):
    for w in range(W - 1):
        if a[h][w] == '#':
            continue
        if a[h][w + 1] != '#':
            dp[h][w + 1] = (dp[h][w + 1] + dp[h][w]) % m
        if a[h + 1][w] != '#':
            dp[h + 1][w] = (dp[h + 1][w] + dp[h][w]) % m
    if a[h][W - 1] == '#':
        continue
    if a[h + 1][W - 1] != '#':
        dp[h + 1][W - 1] = (dp[h + 1][W - 1] + dp[h][W - 1]) % m
for w in range(W - 1):
    if a[H - 1][w] == '#':
        continue
    if a[H - 1][w + 1] != '#':
        dp[H - 1][w + 1] = (dp[H - 1][w + 1] + dp[H - 1][w]) % m

print(dp[H - 1][W - 1])
