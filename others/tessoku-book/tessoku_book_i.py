from sys import stdin

readline = stdin.readline

H, W, N = map(int, readline().split())

a = [[0] * (W + 1) for _ in range(H + 1)]
for _ in range(N):
    A, B, C, D = map(lambda x: int(x) - 1, readline().split())
    a[A][B] += 1
    a[C + 1][D + 1] -= 1
b = [[0] * W for _ in range(H)]
b[0][0] = a[0][0]
for i in range(1, W):
    b[0][i] = b[0][i - 1] + a[0][i]
for i in range(1, H):
    b[i][0] = b[i - 1][0] + a[i][0]
for i in range(1, H):
    for j in range(1, W):
        b[i][j] = b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1] + a[i][j]
for _ in range(H):
    print(*b[H])
