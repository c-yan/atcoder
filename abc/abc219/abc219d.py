INF = 10 ** 18

N = int(input())
X, Y = map(int, input().split())


def conv(x, y):
    return x * 301 + y


def deconv(n):
    return n // 301, n % 301


dp = [INF] * 10 ** 5
dp[0] = 0
m = 0
for _ in range(N):
    A, B = map(int, input().split())
    for j in range(m, -1, -1):
        if dp[j] == INF:
            continue
        x, y = deconv(j)
        x = min(x + A, 300)
        y = min(y + B, 300)
        k = conv(x, y)
        if dp[k] > dp[j] + 1:
            dp[k] = dp[j] + 1
            m = max(m, k)

result = INF
for j in range(m, -1, -1):
    if dp[j] == INF:
        continue
    x, y = deconv(j)
    if x < X or y < Y:
        continue
    result = min(result, dp[j])

if result == INF:
    print(-1)
else:
    print(result)
