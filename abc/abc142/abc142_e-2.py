# DP(配るDP)
def read_key():
    a, _ = map(int, input().split())
    m = 0
    for c in map(int, input().split()):
        m |= 1 << (c - 1)
    return (a, m)


INF = float('inf')

N, M = map(int, input().split())
keys = [read_key() for _ in range(M)]

dp = [INF] * (1 << N)

dp[0] = 0
for i in range(M):
    a, m = keys[i]
    for j in range((1 << N) - 1, -1, -1):
        if dp[j] == INF:
            continue
        if dp[j] + a < dp[j | m]:
            dp[j | m] = dp[j] + a

if dp[(1 << N) - 1] == INF:
    print(-1)
else:
    print(dp[(1 << N) - 1])
