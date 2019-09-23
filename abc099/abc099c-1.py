# DP(配るDP)
INF = float('inf')

N = int(input())

c = [1]
t = 6
while t <= N:
    c.append(t)
    t *= 6
t = 9
while t <= N:
    c.append(t)
    t *= 9

dp = [INF] * (N + 1)
dp[0] = 0
for i in range(N):
    for j in c:
        if i + j <= N and dp[i + j] > dp[i] + 1:
            dp[i + j] = dp[i] + 1
print(dp[N])
