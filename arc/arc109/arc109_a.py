from collections import deque

a, b, x, y = map(int, input().split())

INF = 10 ** 12

dp = [[INF] * 101 for _ in range(2)]
dp[0][a] = 0

q = deque([(0, a)])
while q:
    m, n = q.popleft()
    if dp[m ^ 1][n] > dp[m][n] + x:
        dp[m ^ 1][n] = dp[m][n] + x
        q.append((m ^ 1, n))
    if m == 0 and n != 1 and dp[m ^ 1][n - 1] > dp[m][n] + x:
        dp[m ^ 1][n - 1] = dp[m][n] + x
        q.append((m ^ 1, n - 1))
    if m == 1 and n != 100 and dp[m ^ 1][n + 1] > dp[m][n] + x:
        dp[m ^ 1][n + 1] = dp[m][n] + x
        q.append((m ^ 1, n + 1))
    if n != 1 and dp[m][n - 1] > dp[m][n] + y:
            dp[m][n - 1] = dp[m][n] + y
            q.append((m, n - 1))
    if n != 100 and dp[m][n + 1] > dp[m][n] + y:
            dp[m][n + 1] = dp[m][n] + y
            q.append((m, n + 1))
print(dp[1][b])
