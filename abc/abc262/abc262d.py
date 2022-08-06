m = 998244353

N, *a = map(int, open(0).read().split())

result = 0
for i in range(1, N + 1):
    dp = [[0] * i for _ in range(i + 1)]
    dp[0][0] = 1
    for j in range(N):
        for k in range(i - 1, -1, -1):
            for l in range(i):
                if dp[k][l] == 0:
                    continue
                dp[k + 1][(l + a[j]) % i] += dp[k][l]
                dp[k + 1][(l + a[j]) % i] %= m
    result += dp[i][0]
    result %= m
print(result)
