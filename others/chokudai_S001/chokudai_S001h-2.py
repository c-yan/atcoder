from bisect import bisect_left

N, *a = map(int, open(0).read().split())

INF = 10 ** 12

dp = [INF] * (N + 1)

for x in a:
    dp[bisect_left(dp, x)] = x
print(bisect_left(dp, N + 1))
