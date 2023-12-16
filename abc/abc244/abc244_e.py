from sys import stdin

readline = stdin.readline
m = 998244353

N, M, K, S, T, X = map(int, readline().split())
S, T, X = S - 1, T - 1, X - 1
UV = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in range(M)]

dp = [[0] * N for _ in range(2)]
dp[0][S] = 1
for _ in range(K):
    t = [[0] * N for _ in range(2)]
    for u, v in UV:
        if v == X:
            t[1][v] += dp[0][u]
            t[1][v] %= m
            t[0][v] += dp[1][u]
            t[0][v] %= m
        else:
            t[0][v] += dp[0][u]
            t[0][v] %= m
            t[1][v] += dp[1][u]
            t[1][v] %= m
        if u == X:
            t[1][u] += dp[0][v]
            t[1][u] %= m
            t[0][u] += dp[1][v]
            t[0][u] %= m
        else:
            t[0][u] += dp[0][v]
            t[0][u] %= m
            t[1][u] += dp[1][v]
            t[1][u] %= m
    dp = t
print(dp[0][T])
