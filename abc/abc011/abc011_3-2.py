N = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())

dp = [301] * 301
dp[N] = 0
dp[NG1] = -1
dp[NG2] = -1
dp[NG3] = -1
for i in range(N, 0, -1):
    if dp[i] == -1:
        continue
    if i - 3 >= 0:
        dp[i - 3] = min(dp[i - 3], dp[i] + 1)
    if i - 2 >= 0:
        dp[i - 2] = min(dp[i - 2], dp[i] + 1)
    dp[i - 1] = min(dp[i - 1], dp[i] + 1)

if 0 <= dp[0] <= 100:
    print('YES')
else:
    print('NO')
