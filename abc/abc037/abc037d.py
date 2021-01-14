from sys import setrecursionlimit


def f(i):
    if dp[i] != 0:
        return dp[i]
    y = i // W
    x = i % W
    result = 1
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if a[ny][nx] <= a[y][x]:
            continue
        result += f(ny * W + nx)
        result %= m
    dp[i] = result
    return result


setrecursionlimit(10 ** 6)
m = 1000000007

H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

dp = [0] * (H * W)

result = 0
for i in range(H * W):
    result += f(i)
    result %= m
print(result)
