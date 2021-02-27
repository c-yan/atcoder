N, X, *A = map(int, open(0).read().split())

result = 10 ** 19
for k in range(1, N + 1):
    dp = {}
    for i in range(k + 1):
        dp[i] = {}
    dp[0][0] = 0

    for i in range(N):
        a = A[i]
        for j in range(min(i, k - 1), -1, -1):
            for b in dp[j].values():
                c = (a + b) % k
                dp[j + 1].setdefault(c, 0)
                dp[j + 1][c] = max(dp[j + 1][c], a + b)

    for m in dp[k]:
        if (X - m) % k != 0:
            continue
        result = min(result, (X - dp[k][m]) // k)
print(result)
