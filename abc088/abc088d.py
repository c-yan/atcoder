H, W = map(int, input().split())
s = [input() for _ in range(H)]

dp = [[2501] * W for _ in range(H)]
dp[0][0] = 1

q = [(0, 0)]
while q:
    nq = []
    while q:
        y, x = q.pop()
        t = dp[y][x] + 1
        if y < H - 1:
            if s[y + 1][x] == '.' and dp[y + 1][x] > t:
                dp[y + 1][x] = t
                nq.append((y + 1, x))
        if y > 0:
            if s[y - 1][x] == '.' and dp[y - 1][x] > t:
                dp[y - 1][x] = t
                nq.append((y - 1, x))
        if x < W - 1:
            if s[y][x + 1] == '.' and dp[y][x + 1] > t:
                dp[y][x + 1] = t
                nq.append((y, x + 1))
        if x > 0:
            if s[y][x - 1] == '.' and dp[y][x - 1] > t:
                dp[y][x - 1] = t
                nq.append((y, x - 1))
    q = nq

if dp[H - 1][W - 1] == 2501:
    print(-1)
else:
    print(sum(s[y].count('.') for y in range(H)) - dp[H - 1][W - 1])
