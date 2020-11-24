from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

N, *a = map(int, open(0).read().split())

M = 3001
INF = M * 10 ** 9


def f(l, r, t):
    if l > r:
        return 0
    i = l * M + r
    if dp[i] != INF:
        return dp[i]

    if t == 0:
        x = f(l + 1, r, t ^ 1) + a[l]
        y = f(l, r - 1, t ^ 1) + a[r]
        if x >= y:
            dp[i] = x
        else:
            dp[i] = y
    else:
        x = f(l + 1, r, t ^ 1) - a[l]
        y = f(l, r - 1, t ^ 1) - a[r]
        if x <= y:
            dp[i] = x
        else:
            dp[i] = y
    return dp[i]


dp = [INF] * (M * M)
print(f(0, N - 1, 0))
