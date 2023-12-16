N, *a = map(int, open(0).read().split())

M = 301


def despread(x, y, z):
    return x * M * M + y * M + z


c = [0] * 4
for x in a:
    c[x] += 1

dp = [0.0] * (M * M * M)
for x in range(c[3] + 1):
    for y in range(c[3] + c[2] + 1):
        for z in range(c[3] + c[2] + c[1] + 1):
            a = despread(x, y, z)
            if a == 0:
                continue
            t = N
            if x != 0:
                t += dp[despread(x - 1, y + 1, z)] * x
            if y != 0:
                t += dp[despread(x, y - 1, z + 1)] * y
            if z != 0:
                t += dp[despread(x, y, z - 1)] * z
            dp[a] = t / (x + y + z)
print(dp[despread(c[3], c[2], c[1])])
