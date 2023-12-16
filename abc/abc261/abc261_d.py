from sys import stdin

readline = stdin.readline

N, M = map(int, readline().split())
X = list(map(int, readline().split()))

a = [0] * (N + 1)
for _ in range(M):
    C, Y = map(int, readline().split())
    a[C] = Y

dp = [0] * (N + 1)
for i in range(N):
    t = [0] * (N + 1)
    for j in range(i + 1):
        t[j + 1] = max(t[j + 1], dp[j] + X[i] + a[j + 1])
        t[0] = max(t[0], dp[j])
    dp = t
print(max(dp))
