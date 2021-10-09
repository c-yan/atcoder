from itertools import accumulate

m = 998244353

N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * 3002
for i in range(a[0], b[0] + 1):
    dp[i] = 1

for i in range(1, N):
    t = [0] * 3002
    for j in range(a[i - 1], b[i - 1] + 1):
        t[max(j, a[i])] += dp[j]
        t[b[i] + 1] -= dp[j]
    dp = list(accumulate(x % m for x in t))
print(sum(dp) % m)
