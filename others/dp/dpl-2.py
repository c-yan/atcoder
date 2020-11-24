from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

N, *a = map(int, open(0).read().split())

M = 3001
INF = M * 10 ** 9


def f(l, r):
    i = l * M + r
    if dp[i] != INF:
        return dp[i]
    if l == r:
        dp[i] = a[l]
        return dp[i]
    dp[i] = max(a[l] - f(l + 1, r), a[r] - f(l, r - 1))
    return dp[i]


dp = [INF] * (M * M)
print(f(0, N - 1))
