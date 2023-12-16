N, A = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
x = [v - A for v in x]

dp = [0] * 5001
for v in x:
    for i in range(2501) if v < 0 else range(5000, -1, -1):
        if dp[i] == 0:
            continue
        dp[i + v] += dp[i]
    dp[2500 + v] += 1
print(dp[2500])
