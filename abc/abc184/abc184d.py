A, B, C = map(int, input().split())

M = 101


def despread(x, y, z):
    return x * M * M + y * M + z


dp = [0] * (despread(100, 100, 100) + 1)
dp[despread(A, B, C)] = 1.0

for i in range(A, 100):
    for j in range(B, 100):
        for k in range(C, 100):
            if i + j + k == A + B + C:
                continue
            t = 0
            if i != 0:
                t += dp[despread(i - 1, j, k)] * (i - 1)
            if j != 0:
                t += dp[despread(i, j - 1, k)] * (j - 1)
            if k != 0:
                t += dp[despread(i, j, k - 1)] * (k - 1)
            dp[despread(i, j, k)] = t / (i + j + k - 1)

result = 0
D = A + B + C
for i in range(100):
    for j in range(100):
        t = 0
        t += dp[despread(99, i, j)]
        t += dp[despread(i, 99, j)]
        t += dp[despread(i, j, 99)]
        result += ((100 + i + j) - D) * t * 99 / (99 + i + j)
print(result)
