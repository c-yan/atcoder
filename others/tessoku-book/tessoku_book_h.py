from sys import stdin

readline = stdin.readline

H, W = map(int, readline().split())
X = [list(map(int, readline().split())) for _ in range(H)]

a = [[0] * W for _ in range(H)]
a[0][0] = X[0][0]
for i in range(1, W):
    a[0][i] = a[0][i - 1] + X[0][i]
for i in range(1, H):
    a[i][0] = a[i - 1][0] + X[i][0]
for i in range(1, H):
    for j in range(1, W):
        a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + X[i][j]

Q = int(readline())
result = []
for _ in range(Q):
    A, B, C, D = map(lambda x: int(x) - 1, readline().split())
    t = a[C][D]
    if A != 0 and B != 0:
        t += a[A - 1][B - 1] - a[A - 1][D] - a[C][B - 1]
    elif A == 0 and B != 0:
        t -= a[C][B - 1]
    elif A != 0 and B == 0:
        t -= a[A - 1][D]
    result.append(t)
print(*result, sep='\n')
