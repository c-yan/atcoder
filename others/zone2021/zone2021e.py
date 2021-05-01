from heapq import heappop, heappush

R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
B = [list(map(int, input().split())) for _ in range(R - 1)]

dp = [[10 ** 15] * C for _ in range(R)]
dp[0][0] = 0
q = [(0, 0, 0, True)]
while q:
    cost, r, c, no_warp = heappop(q)
    if dp[r][c] < cost:
        continue
    # (r, c + 1)
    if c < C - 1:
        ncost = dp[r][c] + A[r][c]
        if dp[r][c + 1] > ncost:
            dp[r][c + 1] = ncost
            heappush(q, (ncost, r, c + 1, False))
    # (r, c - 1)
    if c > 0:
        ncost = dp[r][c] + A[r][c - 1]
        if dp[r][c - 1] > ncost:
            dp[r][c - 1] = ncost
            heappush(q, (ncost, r, c - 1, False))
    # (r + 1, c)
    if r < R - 1:
        ncost = dp[r][c] + B[r][c]
        if dp[r + 1][c] > ncost:
            dp[r + 1][c] = ncost
            heappush(q, (ncost, r + 1, c, True))
    if no_warp:
        continue
    # (r - i, c)
    for i in range(1, r + 1):
        ncost = dp[r][c] + (1 + i)
        if dp[r - i][c] > ncost:
            dp[r - i][c] = ncost
            heappush(q, (ncost, r - i, c, True))
print(dp[R - 1][C - 1])
