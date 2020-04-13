INF = float('inf')


def cost_from(H, W, A, y0, x0):
    dp = [[INF] * W for _ in range(H)]
    dp[y0][x0] = 0
    q = [(y0, x0)]
    while q:
        y, x = q.pop(0)
        t = dp[y][x]
        if y - 1 >= 0:
            u = t + A[y - 1][x]
            if dp[y - 1][x] > u:
                dp[y - 1][x] = u
                q.append((y - 1, x))
        if y + 1 < H:
            u = t + A[y + 1][x]
            if dp[y + 1][x] > u:
                dp[y + 1][x] = t + A[y + 1][x]
                q.append((y + 1, x))
        if x - 1 >= 0:
            u = t + A[y][x - 1]
            if dp[y][x - 1] > u:
                dp[y][x - 1] = u
                q.append((y, x - 1))
        if x + 1 < W:
            u = t + A[y][x + 1]
            if dp[y][x + 1] > u:
                dp[y][x + 1] = u
                q.append((y, x + 1))
    return dp


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

result = INF
cost1 = cost_from(H, W, A, H - 1, 0)
cost2 = cost_from(H, W, A, H - 1, W - 1)
cost3 = cost_from(H, W, A, 0, W - 1)
for i in range(H):
    for j in range(W):
        t = cost1[i][j] + cost2[i][j] + cost3[i][j] - 2 * A[i][j]
        if t < result:
            result = t
print(result)
