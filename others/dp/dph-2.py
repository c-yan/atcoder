# 貰うDP
H, W = map(int, input().split())
a = [input() for _ in range(H)]

m = 1000000007

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for w in range(1, W):
    if a[0][w] != '#':
        dp[0][w] = dp[0][w - 1]

for h in range(1, H):
    if a[h][0] != '#':
        dp[h][0] = dp[h - 1][0]
    for w in range(1, W):
        if a[h][w] != '#':
            dp[h][w] = (dp[h][w - 1] + dp[h - 1][w]) % m

print(dp[H - 1][W - 1])
