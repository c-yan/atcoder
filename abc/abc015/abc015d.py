W = int(input())
N, K = map(int, input().split())

dp = [{} for _ in range(K + 1)]
dp[0][0] = 0
for _ in range(N):
    A, B = map(int, input().split())
    for i in range(K - 1, -1, -1):
        for j in dp[i]:
            if j + A <= W:
                dp[i + 1].setdefault(j + A, 0)
                dp[i + 1][j + A] = max(dp[i + 1][j + A], dp[i][j] + B)
result = 0
for i in range(K + 1):
    if len(dp[i]) == 0:
        continue
    result = max(result, max(dp[i].values()))
print(result)
