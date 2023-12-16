N = int(input())
p = list(map(float, input().split()))

dp = [1]
for i in range(N):
    t = [0] * (len(dp) + 1)
    for j in range(len(dp)):
        t[j + 1] += dp[j] * p[i]
        t[j] += dp[j] * (1 - p[i])
    dp = t

result = 0
for i in range((N + 2) // 2, N + 1):
    result += dp[i]
print(result)
