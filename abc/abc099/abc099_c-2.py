# DP(貰うDP)
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

dp = [0] * (N + 1)
for i in range(1, N + 1):
    t = INF
    for j in c:
        if i - j >= 0 and t > dp[i - j] + 1:
            t = dp[i - j] + 1
    dp[i] = t
print(dp[N])
