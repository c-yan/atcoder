H, W = map(int, input().split())
s = [input() for _ in range(H)]

dp = [[0] * W for _ in range(H)]
if s[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for x in range(1, W):
    if s[0][x - 1] == '.' != s[0][x] == '#':
        dp[0][x] = dp[0][x - 1] + 1
    else:
        dp[0][x] = dp[0][x - 1]

for y in range(1, H):
    for x in range(W):
        if s[y - 1][x] == '.' != s[y][x] == '#':
            dp[y][x] = dp[y - 1][x] + 1
        else:
            dp[y][x] = dp[y - 1][x]
        if x == 0:
            continue
        if s[y][x - 1] == '.' != s[y][x] == '#':
            dp[y][x] = min(dp[y][x], dp[y][x - 1] + 1)
        else:
            dp[y][x] = min(dp[y][x], dp[y][x - 1])
print(dp[H - 1][W - 1])
