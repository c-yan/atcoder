from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

N, *a = map(int, open(0).read().split())

M = 301


def f(x, y, z):
    a = x * M * M + y * M + z
    if dp[a] != -1.0:
        return dp[a]
    if a == 0:
        return 0
    # dp[x, y, z] = 1 + (f(x - 1, y + 1, z) * x + f(x, y - 1, z + 1) * y + f(x, y, z - 1) * z + f(x, y, z) * (N - x - y - z)) / N
    # dp[x, y, z] = (N + (f(x - 1, y + 1, z) * x + f(x, y - 1, z + 1) * y + f(x, y, z - 1) * z)) / (x + y + z)
    t = N
    if x != 0:
        t += f(x - 1, y + 1, z) * x
    if y != 0:
        t += f(x, y - 1, z + 1) * y
    if z != 0:
        t += f(x, y, z - 1) * z
    dp[a] = t / (x + y + z)
    return dp[a]


c = [0] * 4
for x in a:
    c[x] += 1

dp = [-1.0] * (M * M * M)
print(f(c[3], c[2], c[1]))
