from sys import stdin
readline = stdin.readline

R, C, K = map(int, readline().split())

goods = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, readline().split())
    goods[r - 1][c - 1] = v

dp = [0] * (C + 1)
for i in range(R):
    cur = [0] * 4
    cur[0] = dp[0]
    for j in range(C):
        if goods[i][j] != 0:
            for k in range(2, -1, -1):
                cur[k + 1] = max(cur[k + 1], cur[k] + goods[i][j])
        dp[j] = max(cur)
        cur[0] = max(cur[0], dp[j + 1])

print(max(cur))
