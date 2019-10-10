# DP
N, W = map(int, input().split())

M = 100000
dp = [-1] * (M + 1)
dp[0] = W
for _ in range(N):
    w, v = map(int, input().split())
    for i in range(M + 1, -1, -1):
        if dp[i] == -1:
            continue
        if dp[i + v] < dp[i] - w:
            dp[i + v] = dp[i] - w

for i in range(M + 1, -1, -1):
    if dp[i] != -1:
        print(i)
        break
