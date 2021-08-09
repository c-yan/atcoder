from collections import deque

INF = 10 ** 15

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dp = [[INF] * W for _ in range(H)]
dp[0][0] = 0
q1 = deque([(0, 0)])
q2 = deque([])
while q1:
    while q1:
        y, x = q1.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if S[ny][nx] == '.':
                if dp[ny][nx] <= dp[y][x]:
                    continue
                dp[ny][nx] = dp[y][x]
                q1.append((ny, nx))
            elif S[ny][nx] == '#':
                if dp[ny][nx] <= dp[y][x] + 1:
                    continue
                dp[ny][nx] = dp[y][x] + 1
                q2.append((ny, nx))
    while q2:
        y, x = q2.popleft()
        for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if dp[ny][nx] <= dp[y][x]:
                continue
            dp[ny][nx] = dp[y][x]
            q1.append((ny, nx))
print(dp[H - 1][W - 1])
