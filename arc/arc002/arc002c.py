from itertools import product

N = int(input())
c = input()

result = N
for x in product('ABXY', repeat=4):
    L = x[0] + x[1]
    R = x[2] + x[3]
    dp = [N] * (N + 1)
    dp[0] = 0
    for i in range(N):
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        if c[i:i + 2] == L:
            dp[i + 2] = min(dp[i + 2], dp[i] + 1)
        if c[i:i + 2] == R:
            dp[i + 2] = min(dp[i + 2], dp[i] + 1)
    result = min(result, dp[N])
print(result)
