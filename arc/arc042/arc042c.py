N, P = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]

ab.sort()
dp = [0] * (P + 1)
dp[0] = ab[0][1]
for a, b in ab[1:]:
    for i in range(P, -1, -1):
        if dp[i] == 0:
            continue
        if i + a > P:
            continue
        dp[i + a] = max(dp[i + a], dp[i] + b)
    dp[0] = max(dp[0], b)
print(max(dp))
